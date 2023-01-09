import { BoardEventName, Stroke, Whiteboard } from "./whiteboard";

type EventHandler = (event: RevealEvent) => void;

interface RevealDeck {
  addKeyBinding(keyCode: number, callback: EventHandler): void;
  down(): void;
  getConfig(): { admin: boolean };
  getIndices(): { h: number; v: number };
  left(): void;
  on(eventName: string, eventHandler: EventHandler): void;
  right(): void;
  slide(indexh: number, indexv: number, fragment: number): void;
  sync(): void;
  up(): void;
}

interface RevealEvent {
  indexh: number;
  indexv: number;
}

interface BoardEvent {
  i: number;
  j: number;
  url?: string;
  eventName: BoardEventName;
  data: any;
}

export default class WhiteboardPlugin {
  public id: string = "RevealWhiteboard";
  public board: Whiteboard;
  public boards: Whiteboard[][];
  private deck: RevealDeck;
  private parentNode: HTMLElement;
  private slides: HTMLElement[] = [];

  /**
   * Add a board
   * @ param i horizontal index
   * @ param j vertical index
   */
  addVerticalSlide(i?: number, j?: number): void {
    const pos = this.deck.getIndices();
    if (i === undefined || j === undefined) {
      i = this.deck.getIndices().h;
      j = this.deck.getIndices().v + 1;
    }
    this.broadcast({ i, j, eventName: "addBoard", data: true });
    const parent = document.querySelector(
      `.slides > section:nth-child(${i + 1})`
    )!;
    this.boards[i].splice(j, 0, this.newBoard(i, j));

    // Add vertical slide
    if (j === this.boards[i].length) {
      parent.appendChild(this.slides[i].cloneNode(true));
    } else {
      parent.insertBefore(this.slides[i].cloneNode(true), this.getSlide(i, j));
    }

    // Adding the canvas
    this.getSlide(i, j).appendChild(this.boards[i][j].canvas);

    this.deck.sync();
    this.deck.slide(pos.h, pos.v, 0);
    this.save();
  }

  /**
   * Send data to socketio route for broadcasting
   * @param data
   */
  async broadcast(boardEvent: BoardEvent) {
    if (!this.deck.getConfig().admin) {
      return;
    }
    const requestOptions: RequestInit = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(boardEvent),
    };
    return fetch("/socketio" + window.location.pathname, requestOptions);
  }

  /**
   * Get the HTML element associated with a vertical slide
   *
   * @param i horizontal index (starts from 0)
   * @param j vertical index (starts from 0)
   */
  getSlide(i: number, j: number): HTMLElement {
    let selector = `section:nth-child(${i + 1}) > section:nth-child(${j + 1})`;
    return document.querySelector(`.reveal .slides > ${selector}`)!;
  }

  /**
   * Set up event listeners
   * @param deck Reveal.js object
   */
  init(deck: RevealDeck) {
    this.deck = deck;
    this.deck.on("slidechanged", this.onSlideChanged.bind(this));
    this.deck.on("ready", this.onReady.bind(this));
    this.deck.addKeyBinding(38, this.onUpArrow.bind(this));
    this.deck.addKeyBinding(40, this.onDownArrow.bind(this));
    this.parentNode = document.querySelector(".reveal .slides")!;
    this.parentNode.oncontextmenu = () => false;
    this.parentNode.onselectstart = () => false;
  }

  /**
   * Create a new whiteboard with predefined strokes
   * @param i horizontal index
   * @param j vertical index
   * @param strokes Strokes to add on the whiteboard
   * @return Created whiteboard
   */
  newBoard(i: number, j: number, strokes: Stroke[] = []): Whiteboard {
    const board = new Whiteboard(1920, 1080, this.parentNode, strokes);
    if (!this.deck.getConfig().admin) {
      setTimeout(() => {
        board.mode = "readonly";
      }, 0);
    }
    board.canvas.addEventListener("change", async (event: any) => {
      const eventName: BoardEventName = event.detail.eventName;
      const data: any = event.detail.data;
      this.broadcast({ i, j, eventName, data });
    });
    return board;
  }

  /**
   * When receiving a change via SocketIO, apply it to all non-admin clients
   * @param change Change received from the backend
   */
  onBoardChangeReceived(change: BoardEvent) {
    const { i, j, url, eventName, data } = change;
    if (this.deck.getConfig().admin || url !== window.location.pathname) {
      return;
    }
    switch (eventName) {
      case "addStroke":
        this.boards[i][j].strokes.push(data);
        this.boards[i][j].redraw();
        break;
      case "removeStroke":
        this.boards[i][j].eraseStroke(data);
        break;
      case "clearBoard":
        this.boards[i][j].clearBoard(true);
        break;
      case "removeBoard":
        this.removeVerticalSlide(i, j);
        break;
      case "addBoard":
        this.addVerticalSlide(i, j);
        break;
      case "slideChange":
        this.deck.slide(i, j, 0);
        break;
    }
  }

  /**
   * Actions to perform when pressing the down arrow
   */
  onDownArrow() {
    const { h, v } = this.deck.getIndices();
    if (v === this.boards[h].length - 1) {
      if (this.board.strokes.length <= 1) {
        return;
      }
      this.addVerticalSlide();
    }
    this.deck.down();
  }

  /**
   * Create the canvas and draw them
   * @param event Reveal.js event
   */
  async onReady() {
    let data: Stroke[][][] = [[[]]];
    this.boards = [[]];
    await fetch(window.location.pathname + ".json")
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error("No board file");
      })
      .then((jsonData) => {
        data = jsonData;
      })
      .catch(() => {});

    const slides = document.querySelectorAll(".slides > section");
    for (let i = 0; i < slides.length; i++) {
      const slide = slides[i];

      // Complete missing data
      if (i >= data.length) {
        data.push([[]]);
      }
      this.boards.push([]);

      // Keep a copy of the slide without transitions
      const slideCopy = slide.cloneNode(true) as HTMLElement;
      const classAttr = slideCopy.getAttribute("class") || "";
      slideCopy.removeAttribute("id");
      slideCopy.setAttribute("class", classAttr.replace("present", "future"));
      const slideCopyFragments = slideCopy.querySelectorAll(".fragment");
      [].forEach.call(slideCopyFragments, function (el: HTMLElement) {
        el.classList.remove("fragment");
      });
      this.slides.push(slideCopy);

      // Wrap slide into a container
      const wrapper = document.createElement("section");
      slide.parentNode!.insertBefore(wrapper, slide);
      wrapper.appendChild(slide);

      for (let j = 0; j < data[i].length; j++) {
        // Create the vertical slide
        if (j > 0) {
          wrapper.appendChild(slideCopy.cloneNode(true));
        }
        // Create the canvas and add it to the DOM
        const strokes = j < data[i].length ? data[i][j] : [];
        this.boards[i][j] = this.newBoard(i, j, strokes);
        this.getSlide(i, j).appendChild(this.boards[i][j].canvas);
      }
    }
    const indices = this.deck.getIndices();
    this.board = this.boards[indices.h][indices.v];

    // Fix missing arrow issue on slideshow
    this.deck.sync();
    this.deck.right();
    this.deck.left();
  }

  /**
   * Deal with slide transitions, save if necessary
   * @param event Reveal.js event
   */
  async onSlideChanged(event: RevealEvent) {
    this.broadcast({
      i: event.indexh,
      j: event.indexv,
      eventName: "slideChange",
      data: true,
    });
    if (this.board !== undefined && this.board.hasUnsavedChanges) {
      await this.save();
      this.board.hasUnsavedChanges = false;
    }
    if (this.boards !== undefined) {
      this.board = this.boards[event.indexh][event.indexv];
    }
  }

  /**
   * Actions to perform when pressing the up arrow
   */
  onUpArrow() {
    const { h, v } = this.deck.getIndices();
    if (this.board.strokes.length <= 1) {
      this.removeVerticalSlide();
    }
    this.deck.slide(h, Math.max(v - 1, 0), 0);
  }

  /**
   * Remove current board
   * @param i horizontal index of board to be removed
   * @param j vertical index of board to be removed
   */
  removeVerticalSlide(i?: number, j?: number): void {
    const currentPos = this.deck.getIndices();
    if (i === undefined || j === undefined) {
      i = currentPos.h;
      j = currentPos.v;
    }
    if (this.boards[i].length === 1) {
      this.board[i][0].clearBoard(true);
    } else {
      this.boards[i][j].emit("removeBoard", true);
      this.boards[i].splice(j, 1);
      this.getSlide(i, j).remove();
      this.deck.sync();
      this.deck.slide(currentPos.h, currentPos.v, 0);
    }
    this.save();
  }

  /**
   * Send all boards to the backend
   */
  async save() {
    if (!this.deck.getConfig().admin) {
      return;
    }
    const requestOptions: RequestInit = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(this.boards),
    };
    return fetch("/boards" + window.location.pathname, requestOptions);
  }
}

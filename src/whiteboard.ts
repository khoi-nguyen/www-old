type Point = [number, number];

type RGB = `rgb(${number}, ${number}, ${number})`;
type RGBA = `rgba(${number}, ${number}, ${number}, ${number})`;
type HEX = `#${string}`;
type Color = RGB | RGBA | HEX | string;

type BoardMode = "draw" | "erase";

interface Stroke {
  color: string;
  lineWidth: number;
  points: Point[];
}

class Whiteboard {

  private context: CanvasRenderingContext2D;
  private height: number;
  private isActive: boolean = false;
  private parentNode: HTMLElement;
  private strokes: Stroke[];
  private width: number;

  public canvas: HTMLCanvasElement;
  public color: Color = "#255994";
  public hasUnsavedChanges: boolean = false;
  public lineWidth: number = 2;
  public mode: BoardMode = "draw";

  /**
   * Add a point to the last stroke
   * @param point Point to add
   */
  addPoint(point: Point): void {
    const stroke = this.strokes[this.strokes.length - 1];
    stroke.points.push(point);
    this.drawStroke(stroke);
    this.hasUnsavedChanges = true;
  }

  changeBrush(color: Color, lineWidth: number) {
    const stroke = this.strokes[this.strokes.length - 1];
    stroke.color = color;
    stroke.lineWidth = lineWidth;
    this.color = color;
    this.lineWidth = lineWidth;
  }

  /**
   * Clear the whiteboard
   * @param removeStrokes Whether to remove the stored strokes
   */
  clearBoard(removeStrokes: boolean = false): void {
    if (removeStrokes) {
      this.strokes.splice(0, this.strokes.length);
      this.hasUnsavedChanges = true;
    }
    this.context.clearRect(0, 0, this.width, this.height)
  }

  /**
   * Create a canvas with its 2D context
   * @param width Width of the canvas
   * @param height Height of the canvas
   * @param parentNode Parent node (useful to calculate offset)
   * @param strokes Strokes to draw
   */
  constructor(width: number, height: number, parentNode: HTMLElement, strokes: Stroke[] = []) {
    this.canvas = document.createElement("canvas");
    this.context = this.canvas.getContext("2d")!;
    this.canvas.addEventListener("mousedown", this.onMouseDown.bind(this));
    this.canvas.addEventListener("mousemove", this.onMouseMove.bind(this));
    this.canvas.addEventListener("mouseup", this.onMouseUp.bind(this));
    this.canvas.width = width;
    this.canvas.height = height;
    this.canvas.classList.add("whiteboard");
    this.parentNode = parentNode;
    this.width = width;
    this.height = height;
    this.strokes = strokes;
    this.redraw();
  }

  /**
   * Draw a stroke on the canvas
   * @param stroke Stroke to draw on the canvas
   */
  drawStroke(stroke: Stroke): void {
    this.context.beginPath();
    this.context.fillStyle = stroke.color;
    this.context.strokeStyle = stroke.color;
    this.context.lineCap = "round";
    this.context.lineWidth = stroke.lineWidth;
    for(const point of stroke.points) {
      this.context.lineTo(...point);
    }
    this.context.stroke();
    this.context.closePath();
  }

  /**
   * Erase all strokes that contain a certain point
   * @param point Point
   */
  eraseStroke(point: Point): void {
    for (let i = 0; i < this.strokes.length; i++) {
      const stroke = this.strokes[i];
      for (const p of stroke.points) {
        const dist = (p[0] - point[0]) ** 2 + (p[1] - point[1]) ** 2
        if (dist <= 5) {
          this.strokes.splice(i, 1);
          this.hasUnsavedChanges = true;
          this.redraw();
          return;
        }
      }
    }
  }
  
  /**
   * Mouse down event listener
   * @param event Mouse event
   */
  onMouseDown(event: MouseEvent): void {
    const leftClick = event.button === 0 || event.button === 1;
    const rightClick = event.button === 2;
    if (leftClick || rightClick) {
      this.isActive = true;
      if (rightClick) {
        this.mode = "erase";
      }
    }
  }
  
  /**
   * Mouse move event listener
   * @param event Mouse event
   */
  onMouseMove(event: MouseEvent): void {
    if (!this.isActive) {
      return;
    }
    const scaleX = this.canvas.offsetWidth / this.canvas.getBoundingClientRect().width;
    const scaleY = this.canvas.offsetHeight / this.canvas.getBoundingClientRect().height;
    const container = this.parentNode.getBoundingClientRect();
    const x = Math.round((event.clientX - container.left) * scaleX)
    const y = Math.round((event.clientY - container.top) * scaleY)
    if (this.mode === "draw") {
      this.addPoint([x, y]);
    } else if (this.mode === "erase") {
      this.eraseStroke([x, y]);
    }
  }
  
  /**
   * Mouse up event listener
   * @param event Mouse event
   */
  onMouseUp(event: MouseEvent): void {
    this.isActive = false;
    if (this.mode === "draw") {
      this.redraw();
    }
    if (event.button === 2) {
      this.mode = "draw";
    }
  }

  /**
   * Redraw all the strokes on the canvas
   */
  redraw(): void {
    this.clearBoard();
    for(const stroke of this.strokes) {
      this.drawStroke(stroke);
    }
    this.startStroke();
  }

  /**
   * Start a new stroke
   */
  startStroke(): void {
    if (this.strokes.length) {
      const lastStroke = this.strokes[this.strokes.length - 1];
      if (lastStroke.points.length === 0) {
        this.strokes.splice(this.strokes.length - 1, 1);
      }
    }
    this.strokes.push({
      color: this.color,
      lineWidth: this.lineWidth,
      points: [],
    });
  }
  
  /**
   * Describe how JSON serialization should happen
   * @returns List of all the strokes on the whiteboard
   */
  toJSON(): Stroke[] {
    return this.strokes;
  }
}

type EventHandler = (event: RevealEvent) => void;

interface RevealDeck {
  down(): void;
  getConfig(): {admin: boolean};
  getIndices(): {h: number, v: number};
  left(): void;
  on(eventName: string, eventHandler: EventHandler): void;
  right(): void;
  slide(indexh: number, indexv: number, fragment: number): void;
  sync(): void;
  up(): void;
}

interface RevealEvent {
  indexh: number,
  indexv: number,
}

class WhiteboardPlugin {
  public id: string = "RevealWhiteboard";
  public board: Whiteboard;
  public boards: Whiteboard[][];
  private deck: RevealDeck;
  private parentNode: HTMLElement;
  private slides: HTMLElement[] = [];

  /**
   * Add a board
   */
  addVerticalSlide(): void {
    const indexh = this.deck.getIndices().h;
    const indexv = this.deck.getIndices().v + 1;
    const parent = document.querySelector(`.slides > section:nth-child(${indexh + 1})`);
    this.boards[indexh].splice(indexv, 0, new Whiteboard(1920, 1080, this.parentNode, []));
    const board = this.boards[indexh][indexv];

    // Add vertical slide
    if (indexv === this.boards[indexh].length) {
      parent!.appendChild(this.slides[indexh].cloneNode(true));
    } else {
      const next = document.querySelector(`.slides > section:nth-child(${indexh + 1}) > section:nth-child(${indexv + 1})`)
      parent!.insertBefore(this.slides[indexh].cloneNode(true), next)
    }

    // Adding the canvas
    const slide = document.querySelector(`.slides > section:nth-child(${indexh + 1}) > section:nth-child(${indexv + 1})`);
    slide!.appendChild(board.canvas);

    this.deck.sync();
    this.deck.slide(indexh, indexv, 0);
    this.save();
  }

  /**
   * Set up event listeners
   * @param deck Reveal.js object
   */
  init(deck: RevealDeck) {
    this.deck = deck;
    this.deck.on("slidechanged", this.onSlideChanged.bind(this));
    this.deck.on("ready", this.onReady.bind(this));
    this.parentNode = document.querySelector(".reveal .slides")!;
    document.oncontextmenu = () => false;
    document.onselectstart = () => false;
  }

  /**
   * Create the canvas and draw them
   * @param event Reveal.js event
   */
  async onReady() {
    let data: Stroke[][][] = [[]];
    this.boards = [[]];
    await fetch("/boards" + window.location.pathname).then(response => {
      if (response.ok) {
        return response.json();
      }
      throw new Error("No board file");
    }).then((jsonData) => { data = jsonData; }).catch(() => {});

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
      const classAttr = slideCopy.getAttribute("class") || ""
      slideCopy.removeAttribute("id");
      slideCopy.setAttribute("class", classAttr.replace("present", "future"));
      const slideCopyFragments = slideCopy.querySelectorAll(".fragment");
      [].forEach.call(slideCopyFragments, function(el: HTMLElement) {
        el.classList.remove("fragment");
      });
      this.slides.push(slideCopy);

      // Wrap slide into a container
      const wrapper = document.createElement("section");
      slide.parentNode!.insertBefore(wrapper, slide);
      wrapper.appendChild(slide)

      for (let j = 0; j < data[i].length; j++) {
        // Create the vertical slide
        if (j > 0) {
          wrapper.appendChild(slideCopy.cloneNode(true))
        }
        // Create the canvas and add it to the DOM
        let strokes: Stroke[] = [];
        if (j < data[i].length) {
          strokes = data[i][j];
        }
        this.boards[i][j] = new Whiteboard(1920, 1080, this.parentNode, strokes);
        const canvas = this.boards[i][j].canvas;
        const selector = `.reveal .slides > section:nth-child(${i + 1}) > section:nth-child(${j + 1})`;
        document.querySelector(selector)!.appendChild(canvas);
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
    if (this.board !== undefined && this.board.hasUnsavedChanges) {
      await this.save();
      this.board.hasUnsavedChanges = false;
    }
    if (this.boards !== undefined) {
      this.board = this.boards[event.indexh][event.indexv];
    }
  }

  /**
   * Remove current board
   */
  removeVerticalSlide(): void {
    const pos = this.deck.getIndices();
    if (this.boards[pos.h].length === 1) {
      this.board.clearBoard(true);
      return;
    }
    if (pos.v === 0) {
      this.deck.down();
    } else {
      this.deck.up();
    }
    this.boards[pos.h].splice(pos.v, 1);
    document.querySelector(`.slides > section:nth-child(${pos.h + 1}) > section:nth-child(${pos.v + 1}`)!.remove();
    this.deck.sync();
    if (pos.v === 0) {
      this.deck.up();
    } else {
      this.deck.down();
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

(<any>window).RevealWhiteboard = new WhiteboardPlugin();

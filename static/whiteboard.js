window.RevealWhiteboard = window.RevealWhiteboard || {
  id: "RevealWhiteboard",
  hasUnsavedChanges: false,
  isAdmin: false,
  isDeleting: false,
  isDrawing: false,
  currentBoard: {},
  canvas: false,
  context: false,
  deck: {},
  paths: [],
  color: "#255994",
  mode: "drawing",
  lineWidth: 2,
  boards: [[{}]],
  slides: [],
  init: function (deck) {
    this.isAdmin = deck.getConfig().admin
    this.deck = deck;
    deck.on("slidechanged", (event) => {
      if (Object.keys(this.boards).length) {
        if (this.hasUnsavedChanges) {
          this.save();
        }
        this.removeListeners();
      }
      this.clear();
      this.loadBoard(event);
    });
    deck.on("ready", (event) => {
      fetch("/boards" + window.location.pathname)
        .then(response => {
          if (response.ok) {
            return response.json();
          }
          throw new Error("No board file");
        }).then((data) => {
          this.boards = data;
          this.prepareSlides();
          this.loadBoard(event);
        }).catch((error) => {
          this.prepareSlides();
          this.loadBoard(event);
        });
    });
  },
  createCanvas: function (indexh = 0, indexv = 0) {
    const canvas = (() => {
      const node = document.createElement("canvas");
      document.querySelector(`.slides > section:nth-child(${indexh + 1}) > section:nth-child(${indexv + 1}`).appendChild(node);
      node.classList.add("whiteboard")
      return node;
    })();
    const context = canvas.getContext("2d");
    context.canvas.height = this.deck.getConfig().height
    context.canvas.width = this.deck.getConfig().width
    context.imageSmoothingEnabled = true;
    return {canvas, context}
  },
  loadBoard: function (event) {
    this.currentBoard = this.boards[parseInt(event.indexh)][parseInt(event.indexv)]
    this.canvas = this.currentBoard.canvas
    this.context = this.currentBoard.context
    this.paths = this.currentBoard.paths
    for (const path of this.paths) {
      if(!("path" in path) || Object.keys(path.path).length === 0) {
        path.path = new Path2D();
        for (const point of path.points) {
          path.path.lineTo(point[0], point[1]);
        }
      }
    }
    this.addPath();
    this.redraw();
    this.addListeners();
  },
  addPath: function() {
    this.paths.push({
      color: this.color,
      lineWidth: this.lineWidth,
      points: [],
      path: new Path2D(),
    });
  },
  addListeners: function () {
    if (!this.isAdmin) {
      return false;
    }
    this.canvas.addEventListener("mousedown", this.mousedown.bind(this));
    this.canvas.addEventListener("mouseup", this.mouseup.bind(this));
    this.canvas.addEventListener("mousemove", this.mousemove.bind(this));
    document.addEventListener("keydown", this.undo.bind(this));
    document.oncontextmenu = (event) => false;
    document.onselectstart = (event) => false;
  },
  removeListeners: function () {
    if (this.canvas) {
      this.canvas.removeEventListener("mousedown", this.mousedown.bind(this));
      this.canvas.removeEventListener("mouseup", this.mouseup.bind(this));
      this.canvas.removeEventListener("mousemove", this.mousemove.bind(this));
      document.removeEventListener("keydown", this.undo.bind(this));
    }
  },
  mousedown: function (event) {
    const leftClick = event.button === 0 || event.button === 1;
    const rightClick = event.button === 2;
    if (leftClick && this.mode === "drawing" && !this.isDeleting) {
      this.isDrawing = true;
    } else if ((rightClick || (leftClick && this.mode === "eraser")) && !this.isDrawing) {
      this.isDeleting = true
    }
  },
  mouseup: function (event) {
    if (this.isDrawing) {
      this.isDrawing = false;
      this.addPath();
      this.redraw();
    } else if (this.isDeleting) {
      this.isDeleting = false;
    }
  },
  mousemove: function (event) {
    const scaleX = this.canvas.offsetWidth / this.canvas.getBoundingClientRect().width;
    const scaleY = this.canvas.offsetHeight / this.canvas.getBoundingClientRect().height;
    const slides = document.querySelector(".reveal .slides")
    const offsetX = slides.getBoundingClientRect().left
    const offsetY = slides.getBoundingClientRect().top
    const x = parseInt((event.clientX - offsetX) * scaleX)
    const y = parseInt((event.clientY - offsetY) * scaleY)
    if (this.isDeleting) {
      for (var index in this.paths) {
        if (this.context.isPointInPath(this.paths[index].path, x, y)) {
          this.paths.splice(index, 1);
          this.redraw();
          this.hasUnsavedChanges = true;
          break;
        }
      }
    }
    if (this.isDrawing) {
      this.paths[this.paths.length - 1].points.push([x, y]);
      this.paths[this.paths.length - 1].path.lineTo(x, y);
      this.hasUnsavedChanges = true;
      this.draw();
    }
  },
  clear: function (removePaths = false) {
    if (removePaths) {
      this.paths.splice(0, this.paths.length);
      this.redraw();
      this.addPath();
      this.hasUnsavedChanges = true;
    } else if(this.context) {
      this.context.clearRect(0, 0, this.deck.getConfig().width, this.deck.getConfig().height);
    }
  },
  drawPath: function(path) {
    this.context.fillStyle = path.color;
    this.context.strokeStyle = path.color;
    this.context.lineCap = "round";
    this.context.lineWidth = path.lineWidth;
    this.context.stroke(path.path)
  },
  draw: function () {
    this.drawPath(this.paths[this.paths.length - 1]);
  },
  redraw: function () {
    this.clear();
    for (const path of this.paths) {
      this.drawPath(path);
    }
  },
  undo: function (event, force = false) {
    if ((event.ctrlKey && event.key === "z") || force) {
      const current = this.paths.pop();
      this.paths.pop();
      this.addPath();
      this.redraw();
      this.hasUnsavedChanges = true;
    }
  },
  setColor: function (color, lineWidth = 2) {
    this.mode = "drawing";
    this.color = color;
    this.lineWidth = lineWidth;
    if (this.paths.length) {
      this.paths[this.paths.length - 1].color = color;
      this.paths[this.paths.length - 1].lineWidth = lineWidth;
    }
  },
  startErasing: function () {
    this.mode = "eraser";
  },
  save: function () {
    if (!this.isAdmin) {
      return false;
    }
    const boards = []
    for (var i = 0; i < this.boards.length; i++) {
      boards.push([])
      for (var j = 0; j < this.boards[i].length; j++) {
        boards[i].push([])
        boards[i][j] = {paths: JSON.parse(JSON.stringify(this.boards[i][j].paths))}
      }
    }
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(boards)
    };
    fetch("/boards" + window.location.pathname, requestOptions)
    this.hasUnsavedChanges = false;
  },
  prepareSlides: function (deck) {
    // Wrap slides and keep a copy
    const slides = document.querySelectorAll(".reveal .slides > section");
    slides.forEach((slide, indexh) => {
      while (indexh >= this.boards.length) {
        this.boards.push([[]])
      }
      // Keep a copy of the slide
      const slideCopy = slide.cloneNode(true);
      slideCopy.removeAttribute("id");
      slideCopy.setAttribute("class", slideCopy.getAttribute("class").replace("present", "future"));
      const slideCopyFragments = slideCopy.querySelectorAll(".fragment");
      [].forEach.call(slideCopyFragments, function(el) {
        el.classList.remove("fragment");
      });
      this.slides.push(slideCopy);
      // Wrap into a higher level one
      const wrapper = document.createElement("section");
      slide.parentNode.insertBefore(wrapper, slide);
      wrapper.appendChild(slide)
      // Create vertical slides and their canvases
      for (var indexv = 0; indexv < this.boards[indexh].length; indexv++) {
        const board = this.boards[indexh][indexv];
        if (!("paths" in board)) {
          board.paths = [{points: [], color: this.color, lineWidth: this.lineWidth}]
        }
        if (indexv > 0) {
          wrapper.appendChild(slideCopy.cloneNode(true))
        }
        Object.assign(board, this.createCanvas(indexh, indexv));
      }
    })
    this.deck.sync();
    this.deck.right();
    this.deck.left();
  },
  addVerticalSlide: function () {
    const indexh = this.deck.getIndices().h;
    const indexv = this.deck.getIndices().v + 1;
    const parent = document.querySelector(`.slides > section:nth-child(${indexh + 1})`)
    this.boards[indexh].splice(indexv, 0, [{}]);
    const board = this.boards[indexh][indexv];
    if (!("paths" in board)) {
      board.paths = [{points: [], color: this.color, lineWidth: this.lineWidth}]
    }
    if (indexv === this.boards[indexh].length) {
      parent.appendChild(this.slides[indexh].cloneNode(true));
    } else {
      const next = document.querySelector(`.slides > section:nth-child(${indexh + 1}) > section:nth-child(${indexv + 1})`)
      parent.insertBefore(this.slides[indexh].cloneNode(true), next)
    }
    Object.assign(board, this.createCanvas(indexh, indexv));
    this.deck.sync();
    this.deck.slide(indexh, indexv, 0);
    this.save();
  },
  removeVerticalSlide: function () {
    const pos = this.deck.getIndices();
    if (this.boards[pos.h].length === 1) {
      this.clear(true);
      return false;
    }
    if (pos.v === 0) {
      this.deck.down();
    } else {
      this.deck.up();
    }
    this.boards[pos.h].splice(pos.v, 1);
    document.querySelector(`.slides > section:nth-child(${pos.h + 1}) > section:nth-child(${pos.v + 1}`).remove();
    this.deck.sync();
    if (pos.v === 0) {
      this.deck.up();
    } else {
      this.deck.down();
    }
    this.save();
  }
}

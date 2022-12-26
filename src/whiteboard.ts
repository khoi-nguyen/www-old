type Point = [number, number];

type RGB = `rgb(${number}, ${number}, ${number})`;
type RGBA = `rgba(${number}, ${number}, ${number}, ${number})`;
type HEX = `#${string}`;
type Color = RGB | RGBA | HEX;

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
   * @param strokes Strokes to draw
   */
  constructor(width: number, height: number, strokes: Stroke[] = []) {
    this.canvas = document.createElement("canvas");
    this.context = this.canvas.getContext("2d")!;
    this.canvas.addEventListener("mousedown", this.onMouseDown.bind(this));
    this.canvas.addEventListener("mousemove", this.onMouseMove.bind(this));
    this.canvas.addEventListener("mouseup", this.onMouseUp.bind(this));
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
        if (dist <= 1) {
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
    const point: Point = [event.clientX, event.clientY];
    if (this.mode === "draw") {
      this.addPoint(point);
    } else if (this.mode === "erase") {
      this.eraseStroke(point);
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
      this.startStroke();
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
  }

  /**
   * Start a new stroke
   */
  startStroke(): void {
    this.strokes.push({
      color: this.color,
      lineWidth: this.lineWidth,
      points: [],
    });
  }
  
  toJSON(): Stroke[] {
    return this.strokes;
  }
}
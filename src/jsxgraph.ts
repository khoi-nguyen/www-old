import { Board } from "jsxgraph";

type RealFunction = (x: number) => number;

type plotOptions = {
  strokecolor?: string;
};

export default class JSXBoard {
  axis: boolean = true;
  board: Board;
  boundingbox: number[] = [-5, 5, 5, -5];
  height: number = 500;
  keepAspectRatio: boolean = true;
  showCopyright: boolean = false;
  width: number = 500;
  colors: string[] = ["#255994", "darkred", "darkgreen", "black"];

  get options() {
    return {
      boundingbox: this.boundingbox,
      keepAspectRatio: this.keepAspectRatio,
      axis: this.axis,
      showCopyright: this.showCopyright,
    };
  }

  plot(func: RealFunction) {
    let options: plotOptions = {};
    if (this.colors.length) {
      options.strokecolor = this.colors.shift()!;
      this.colors.push(options.strokecolor);
    }
    return this.board.create("functiongraph", [func], options);
  }
}

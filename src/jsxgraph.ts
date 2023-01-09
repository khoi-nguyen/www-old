import { Board } from "jsxgraph";

type RealFunction = (x: number) => number;

export default class JSXBoard {
  axis: boolean = true;
  board: Board;
  boundingbox: number[] = [-5, 5, 5, -5];
  height: number = 500;
  keepAspectRatio: boolean = true;
  showCopyright: boolean = false;
  width: number = 500;

  get options() {
    return {
      boundingbox: this.boundingbox,
      keepAspectRatio: this.keepAspectRatio,
      axis: this.axis,
      showCopyright: this.showCopyright,
    };
  }

  plot(func: RealFunction) {
    return this.board.create("functiongraph", [func], {});
  }
}

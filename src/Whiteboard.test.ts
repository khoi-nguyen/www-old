import { describe, expect, it } from "vitest";
import { Whiteboard } from "./Whiteboard";

describe("whiteboard class", () => {
  const parentNode = document.createElement("div");
  const whiteboard = new Whiteboard(parentNode);
  parentNode.appendChild(whiteboard.canvas);

  it("should create a canvas node", () => {
    expect(whiteboard.canvas).toBeDefined();
    expect(parentNode.children.length).toBe(1);
    expect(parentNode.style.position).toBe("relative");
    expect(whiteboard.canvas.style.position).toBe("absolute");
  });

  it("contains an empty stroke", () => {
    expect(whiteboard.strokes.length).toBe(1);
    expect(whiteboard.strokes[0].points.length).toBe(0);
  });
});

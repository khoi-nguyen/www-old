import { defineCustomElement } from "vue";
import Clock from "./elements/Clock.ce.vue";
import PdfReader from "./elements/PdfReader.ce.vue";
import WhiteboardPlugin from "./WhiteboardPlugin";
import JSXBoard from "./jsxgraph";

const ClockElement = defineCustomElement(Clock);
customElements.define("ticking-clock", ClockElement);

const PdfReaderElement = defineCustomElement(PdfReader);
customElements.define("pdf-reader", PdfReaderElement);

import katex from "katex";
import renderMathInElement from "katex/dist/contrib/auto-render.mjs";

(<any>window).RevealWhiteboard = new WhiteboardPlugin();
(<any>window).JSXBoard = JSXBoard;
(<any>window).renderMathInElement = renderMathInElement;

document.addEventListener("DOMContentLoaded", function () {
  var mathElements = document.getElementsByClassName("math");
  var macros = [];
  for (var i = 0; i < mathElements.length; i++) {
    var texText = mathElements[i].firstChild;
    if (mathElements[i].tagName == "SPAN") {
      katex.render(texText.data, mathElements[i], {
        displayMode: mathElements[i].classList.contains("display"),
        throwOnError: false,
        macros: macros,
        fleqn: false,
      });
    }
  }
});

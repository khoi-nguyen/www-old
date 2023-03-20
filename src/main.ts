import { defineCustomElement } from "vue";
import Clock from "./elements/Clock.ce.vue";
import PdfReader from "./elements/PdfReader.ce.vue";
import WhiteboardPlugin from "./WhiteboardPlugin";
import katex from "katex";
import renderMathInElement from "katex/dist/contrib/auto-render.mjs";

const ClockElement = defineCustomElement(Clock);
customElements.define("ticking-clock", ClockElement);

const PdfReaderElement = defineCustomElement(PdfReader);
customElements.define("pdf-reader", PdfReaderElement);

(<any>window).RevealWhiteboard = new WhiteboardPlugin();
(<any>window).JSXBoard = JSXBoard;
(<any>window).renderMathInElement = renderMathInElement;

document.addEventListener("DOMContentLoaded", function () {
  const mathElements = document.getElementsByClassName("math");
  const macros = [];
  for (let i = 0; i < mathElements.length; i++) {
    const texText = mathElements[i].firstChild;
    if (mathElements[i].tagName == "SPAN" && texText && "data" in texText) {
      katex.render(texText.data, mathElements[i], {
        displayMode: mathElements[i].classList.contains("display"),
        throwOnError: false,
        macros: macros,
        fleqn: false,
      });
    }
  }
});

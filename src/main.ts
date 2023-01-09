import { defineCustomElement } from "vue";
import Clock from "./elements/Clock.vue";
import PdfReader from "./elements/PDFReader";
import WhiteboardPlugin from "./whiteboard";

const ClockElement = defineCustomElement(Clock);
customElements.define("ticking-clock", ClockElement);

customElements.define("pdf-reader", PdfReader);

(<any>window).RevealWhiteboard = new WhiteboardPlugin();

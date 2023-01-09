import { defineCustomElement } from "vue";
import Clock from "./elements/Clock.ce.vue";
import PdfReader from "./elements/PdfReader.ce.vue";
import WhiteboardPlugin from "./WhiteboardPlugin";

const ClockElement = defineCustomElement(Clock);
customElements.define("ticking-clock", ClockElement);

const PdfReaderElement = defineCustomElement(PdfReader);
customElements.define("pdf-reader", PdfReaderElement);

(<any>window).RevealWhiteboard = new WhiteboardPlugin();

import { defineCustomElement } from "vue";
import Clock from "./elements/Clock.vue";
import PdfReader from "./elements/PdfReader.vue";
import WhiteboardPlugin from "./whiteboard";

const ClockElement = defineCustomElement(Clock);
customElements.define("ticking-clock", ClockElement);

const PdfReaderElement = defineCustomElement(PdfReader);
customElements.define("pdf-reader", PdfReaderElement);

(<any>window).RevealWhiteboard = new WhiteboardPlugin();

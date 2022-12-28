class PdfReader extends HTMLElement {

  public shadowRoot: ShadowRoot;

  constructor() {
    super();
  }

  connectedCallback() {
    this.attachShadow({ mode: "open" });

    const object = document.createElement("object");
    const embed = document.createElement("embed");
    object.append(embed);

    object.setAttribute("type", "application/pdf");
    object.setAttribute("width", this.getAttribute("width") || "100%");
    object.setAttribute("height", this.getAttribute("height") || "900");

    let src = this.getAttribute("src") || "";
    if (this.getAttribute("mode") === "A4") {
      const page = this.getAttribute("page") || "1";
      src += `#view=FitH&toolbar=0&page=${page}`
      const resizeObserver = new ResizeObserver(() => {
        object.setAttribute("height", String(1.414 * object.offsetWidth));
      })
      resizeObserver.observe(object);
    }
    object.setAttribute("data", src);
    embed.setAttribute("src", src);

    this.shadowRoot.append(object);
  }
}

customElements.define("pdf-reader", PdfReader);

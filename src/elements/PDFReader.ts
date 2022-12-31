class PdfReader extends HTMLElement {
  public count: number = 0;
  public shadowRoot: ShadowRoot;

  constructor() {
    super();
    this.attachShadow({ mode: "open" });
  }

  connectedCallback() {
    if (this.count) {
      return;
    }
    this.count++;
    const object = document.createElement("object");
    const embed = document.createElement("embed");
    object.append(embed);

    object.setAttribute("type", "application/pdf");
    object.setAttribute("width", this.getAttribute("width") || "100%");
    object.setAttribute("height", this.getAttribute("height") || "900");

    let src = this.getAttribute("src") || "";
    if (this.getAttribute("mode") === "A4") {
      const page = this.getAttribute("page") || "1";
      src += `#view=FitH&toolbar=0&page=${page}`;
      const resizeObserver = new ResizeObserver(() => {
        object.setAttribute("height", String(1.414 * object.offsetWidth));
      });
      resizeObserver.observe(object);
    }
    if (/(android)/i.test(navigator.userAgent)) {
      src = "https://docs.google.com/gview?embedded=true&url=" + src;
    }

    object.setAttribute("data", src);
    embed.setAttribute("src", src);

    this.shadowRoot.append(object);
  }
}

customElements.define("pdf-reader", PdfReader);

class Clock extends HTMLElement {
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
    const clock = document.createElement("span");
    clock.setAttribute("class", this.getAttribute("class") || "");
    clock.innerHTML = this.currentTime();
    setInterval((): void => {
      clock.innerHTML = this.currentTime();
    }, 1000);
    this.shadowRoot.append(clock);
  }

  currentTime() {
    const now = new Date();
    const hh = now.getHours();
    const mm = now.getMinutes();
    const addZero = (n: number): String => (n < 10 ? "0" : "") + String(n);
    return `${now.toDateString()} ${addZero(hh)}:${addZero(mm)}`;
  }
}

customElements.define("ticking-clock", Clock);

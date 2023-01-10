import { afterAll, beforeAll, describe, expect, it } from "vitest";
import puppeteer from "puppeteer";

const browser = await puppeteer.launch({ headless: true });
const page = await browser.newPage();

async function click(identifier: string): Promise<void> {
  await page.waitForSelector(identifier);
  await page.click(identifier);
}

async function type(identifier: string, value: string): Promise<void> {
  await page.waitForSelector(identifier);
  await page.type(identifier, value);
}

describe("whiteboard class", () => {
  beforeAll(async () => {
    await page.goto("http://localhost:5000/login");
    await type("input#password", "admin");
    await click('button[type="submit"]');
    await page.goto("http://localhost:5000/test");
    await page.waitForSelector(".reveal");
  });

  it("creates the vertical slides", async () => {
    const count = (elements: HTMLElement[]): number => elements.length;
    const horizontalSlidesCount = await page.$$eval(".slides > section", count);
    const verticalSlidesCount = await page.$$eval(
      ".slides > section > section",
      count
    );
    expect(verticalSlidesCount).toBe(horizontalSlidesCount);
  });

  it("creates the canvases", async () => {
    const count = (elements: HTMLElement[]): number => elements.length;
    const slidesCount = await page.$$eval(".slides > section > section", count);
    const canvasCount = await page.$$eval("canvas", count);
    expect(canvasCount).toBe(slidesCount);
  });

  afterAll(async () => {
    await browser.close();
  });
});

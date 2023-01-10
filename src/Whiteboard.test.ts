import { afterAll, beforeAll, describe } from "vitest";
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
  });

  afterAll(async () => {
    await browser.close();
  });
});

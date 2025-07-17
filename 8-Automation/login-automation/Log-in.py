import asyncio
import time
from playwright.async_api import async_playwright

async def type_with_animation(page, selector, text, delay=0.1):
    for char in text:
        await page.type(selector, char)
        await asyncio.sleep(delay)

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
        executable_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
        headless=False
        )
        page = await browser.new_page()

        await page.goto("https://practicetestautomation.com/practice-test-login/", wait_until="domcontentloaded", timeout=60000)

        await type_with_animation(page, "#username", "student", delay=0.2)
        await asyncio.sleep(1)  

        await type_with_animation(page, "#password", "Password123", delay=0.2)
        await asyncio.sleep(1)

        await page.click("button.btn")

        print("Logged in. Browser will stay open for manual inspection.")

        await asyncio.sleep(3600)  
        
asyncio.run(run())
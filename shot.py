"""Screenshot index.html to entry.png at exactly 1024x1024 using Playwright."""
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1024, "height": 1024}, device_scale_factor=1)
    page.goto("file://" + os.path.join(HERE, "index.html"))
    page.wait_for_timeout(400)
    page.screenshot(path=os.path.join(HERE, "entry.png"))
    browser.close()
print("entry.png written")

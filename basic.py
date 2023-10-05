from playwright.sync_api import sync_playwright
import argparse

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.display)
        page = browser.new_page()
        page.goto("https://www.yahoo.com")
        # page.screenshot(path="yahoo.png")
        browser.close()


def youtube_likes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.display)
        page = browser.new_page()
        page.goto("https://www.youtube.com")
        page.get_by_placeholder("Search").fill("Seatin man of legends")
        page.get_by_role("search-icon-legacy").click()
        page.get_by_title("October Paragon Gauntlet 100% - Morbius & Werewolf Boss Fights - Marvel Contest of Champions").click()
        page.pause()
        # page.locator("#title").locator("USE THESE BUFFS TO CHEESE!").click()
        # page.screenshot(path="yahoo.png")
        # browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("simple playwright script")
    parser.add_argument('-d', '--display', action='store_false', help='launch the browser when executing the script')
    
    args = parser.parse_args()
    # main()
    youtube_likes()


from playwright.sync_api import sync_playwright
import argparse

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.display)
        page = browser.new_page()
        page.goto("https://www.yahoo.com")
        # page.screenshot(path="yahoo.png")
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser("simple playwright script")
    parser.add_argument('-d', '--display', action='store_false', help='launch the browser when executing the script')
    
    args = parser.parse_args()
    main()

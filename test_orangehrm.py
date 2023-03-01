from playwright.sync_api import Page, expect
import pathlib, os, re

url = os.environ['orangehrm_baseurl']
username = os.environ['orangehrm_user_name']
psw = os.environ['orangehrm_user_password']

def orange_hrm_e2e_test(page: Page):
    page.goto(url)
    expect(page.title()).to_have_title("OrangeHRM")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(psw)
    page.get_by_role("button", name="Login").click()
    expect(page.url).to_have_text("http://65.21.1.10:9099/web/index.php/dashboard/index")
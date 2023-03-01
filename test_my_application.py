import re
from playwright.sync_api import Page, expect
import logging
from logging import getLogger
import sys

logger = getLogger('test_my_application')
logging.basicConfig(
    stream=sys.stdout,
    format="%(message)s",
    level=logging.INFO,
)


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    # page.goto("http://65.21.1.10:9099")
    # Expect a title "to contain" a substring.
    # expect(page).to_have_title(re.compile("OrangeHRM"))
    # page.get_by_placeholder('username').fill('zubbyik')
    # page.get_by_placeholder('password').fill('!1Winner75')
    # page.get_by_role('button', name='Login')
    # client_banner = page.get_by_role('img', name="client brand banner")
    # expect(client_banner).to_be_visible()
    # logging.info('This is just info')
    # logging.warning('dont try this')
    # create a locator
    # get_started = page.get_by_role("link", name="Get started")
    # Expect an attribute "to be strictly equal" to the value.
    # expect(get_started).to_have_attribute("href", "/docs/intro")

    # Code Generated from the Playwight CodeGen
    from playwright.sync_api import Page, expect

    page.goto("http://65.21.1.10:9099/web/index.php/auth/login")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("zubbyik")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("!1Winner75")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="client brand banner").click()
    page.goto("http://65.21.1.10:9099/web/index.php/dashboard/index")
    page.get_by_role("link", name="Admin").click()
    page.goto("http://65.21.1.10:9099/web/index.php/dashboard/index")
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("link", name="Leave").click()
    page.get_by_role("link", name="Time").click()
    page.get_by_role("link", name="Recruitment").click()
    page.get_by_role("link", name="My Info").click()
    page.get_by_role("link", name="Performance").click()
    page.get_by_role("link", name="Dashboard").click()
    page.get_by_role("link", name="Directory").click()
    page.get_by_role("link", name="Maintenance").click()
    # Expect a security pop up to ensure the user have the permission to edit or update the maintenance page

    expect(page.get_by_role("heading", name="Administrator Access")).to_be_visible()
    expect(page.get_by_role("heading", name="Administrator Access")).to_have_text('Administrator Access')

    expect(page.locator("form div").filter(has_text="You have requested to access a critical Administrator function in OrangeHRM and ")).to_be_visible()
    expect(page.locator("form div").filter(has_text="You have requested to access a critical Administrator function in OrangeHRM and ")).to_have_text('You have requested to access a critical Administrator function in OrangeHRM and are required to validate your credentials below')
    content = page.locator("form div").filter(has_text="You have requested to access a critical Administrator function in OrangeHRM and ").text_content()
    print("\n Hello Ikem "+content)
    with open('result.txt', "w") as result:
        result.write(content)
        result.close()
    expect(page.get_by_label('username')).not_to_be_visible()
    expect(page.get_by_label('username')).not_to_be_visible()
    page.goto("http://65.21.1.10:9099/web/index.php/directory/viewDirectory")
    page.close()
from playwright.async_api import Page, expect
import re
import pathlib

url = 'https://petstore.octoperf.com/actions/Catalog.action'

def test_pest_store_octoperf(page: Page):
    page.goto(url)
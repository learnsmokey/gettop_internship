from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@given("Open Gettop page")
def open_gettop(context):
    context.app.main_page.open_gettop_website()


@when("Click the heart icon")
def click_product(context):
    context.app.main_page.add_product_to_wishlist()


@then("Click on the browse wishlist")
def click_wishlist(context):
    context.app.main_page.wishlist_button()


@then("Verify correct product is there")
def correct_product(context):
    context.app.wishlist_page.wishlist_verify()

#    context.app.main_page.verify_product()

@when("Click on Remove this product button")
def click_remove_product(context):
    context.app.wishlist_page.remove_product()


@then("User see confirmation message")
def confirmation_message(context):
    context.app.wishlist_page.confirmation_message()


@then("Click on wishlist item")
def click_item(context):
    context.app.wishlist_page.wishlist_item()


@then("Confirm,taken to correct product page")
def correct_page(context):
    context.app.product_page.correct_product_page()


@then("User can see social logo to share")
def social_logo(context):
    context.app.wishlist_page.logo_to_share()
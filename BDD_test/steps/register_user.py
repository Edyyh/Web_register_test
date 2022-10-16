# coding = utf-8
from behave import *
from BDD_test.register_page import RegisterPage

use_step_matcher('re')


@when('I open the register website "([^"]*)"')
def step_register(context, url):
    RegisterPage(context).get_url(url)


@then('I expect that the title is "([^"]*)"')
def step_register(context, title_name):
    title = RegisterPage(context).get_title()
    assert title_name in title


@when('I input user email "([^"]*)"')
def step_register(context, useremail):
    RegisterPage(context).send_useremail(useremail)


@when('I input username "([^"]*)"')
def step_register(context, username):
    RegisterPage(context).send_useremail(username)


@when('I input password "([^"]*)"')
def step_register(context, password):
    RegisterPage(context).send_useremail(password)


@when('I input text code "([^"]*)"')
def step_register(context, code):
    RegisterPage(context).send_useremail(code)


@when('I click register button')
def step_register(context):
    RegisterPage(context).click_register_button()


@then('I expect that text "([^"]*)"')
def step_register(context, code_error_msg):
    text = RegisterPage(context).get_code_text_error_msg()
    assert code_error_msg in text

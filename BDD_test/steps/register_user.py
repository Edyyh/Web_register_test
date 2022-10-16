# coding = utf-8
from behave import *


@when('open register website')
def step_register(context):
    context.driver.get('http://www.5itest.cn/register')


@then('I expect that the title is "([^"]*)"')
def step_register(context, title_name):
    title = context.driver.title
    assert title_name in title

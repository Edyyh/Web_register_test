#coding = utf-8
Feature: Register User
  A Behavior Driven Development test

  Scenario: open register website
    When I open the register website 'http://www.5itest.cn/register'
    Then I expect that the title is '注册'

  Scenario: input username
    When I input user email 'abcdefg@outlook.com'
    And I input username 'abcdefg'
    And I input password 'aabbcc'
    And I input text code 'defg'
    And I click register button
    Then I expect that text '验证码错误'






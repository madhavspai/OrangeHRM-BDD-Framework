
@smoke
Feature: Login Functionality 

@smoke 
Scenario: Successful login 
Given user is on the login page  
When user enters valid credentials 
Then user should be directed to homepage 

Scenario: Unsuccessful Login 
Given user is on the login page
When user enters invalid credentials 
Then user must see error message on login page 


@regression
Scenario: Login with empty username
    Given user is on the login page
    When the user submits the login form with username empty and valid password
    Then a validation message "Required" should be displayed for the username field
    And the user should not be logged in


@regression
Scenario: Login with empty password
    Given user is on the login page
    When the user submits the login form with valid username and password empty
    Then a validation message "Required" should be displayed for the password field
    And the user should not be logged in


@regression
Scenario: Login with empty credentials
    Given user is on the login page
    When the user submits the login form with both username and password empty
    Then a validation message "Required" should be displayed for the username field
    And a validation message "Required" should be displayed for the password field
    And the user should not be logged in
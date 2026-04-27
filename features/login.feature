
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




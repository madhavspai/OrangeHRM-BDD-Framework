
@smoke
Feature: Add employee Functionality 

@smoke 
Scenario: Add employee details 
Given user is on the add employee page   
When user enters valid firstname and lastname
And user saves the details
Then user should see successfully saved message  

@regression
Scenario: Add only first name
Given user is on the add employee page   
When user submits the form without last name
Then user should see last name "required" message  

@regression
Scenario: Add only last name
Given user is on the add employee page   
When user submits the form without first name
Then user should see first name "required" message  

@regression
Scenario: add blank first and last name
Given user is on the add employee page   
When user submits the form without firstname and lastname
Then user should see first name last name "required" message  

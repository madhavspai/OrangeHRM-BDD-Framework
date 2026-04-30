@smoke
Feature: My Info functionality

@smoke 
Scenario: Add employee details 
  Given user is on the personal details page   
  When user updates valid firstname and lastname
  And user saves personal details
  Then user should see personal details saved message  

@regression
Scenario: Add only firstname
  Given user is on the personal details page   
  When user updates firstname only
  And user saves personal details
  Then user should see error message as required lastname  

@regression
Scenario: Add only lastname
  Given user is on the personal details page   
  When user updates lastname only  
  And user saves personal details
  Then user should see error message as required firstname

@regression
Scenario: add blank first and last name
  Given user is on the personal details page
  When user submits personal details form without firstname and lastname
  Then user should see myinfo first name last name "required" message
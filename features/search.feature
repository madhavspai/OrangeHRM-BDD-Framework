Feature: Employee Search Functionality
  @smoke
  Scenario: Search with a valid employee name
    Given user is on the employee search page
    When the user searches using a valid employee name
    Then the system should return the correct employee details
  @smoke
  Scenario: Search with a valid employee ID
    Given user is on the employee search page
    When the user searches using a valid employee ID
    Then the system should return the correct employee details
  @regression
  Scenario: Search with an invalid employee name
    Given user is on the employee search page
    When the user searches using an invalid employee name
    Then the system should display a "No records found" message
  @regression
  Scenario: Search with empty fields
    Given user is on the employee search page
    When the user submits the search with all fields empty
    Then the system should update and display the default table of employee records
    
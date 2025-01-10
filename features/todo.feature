Feature: Todo List Management
  As a user
  I want to manage my todo list
  So that I can organize my tasks

  Scenario: Add a new task
    Given I have an empty todo list
    When I add a task with the description "Buy milk"
    Then the todo list should contain 1 task
    And the task description should be "Buy milk"

  Scenario: List all tasks
    Given I have a todo list with the tasks "Buy milk" and "Walk the dog"
    When I list all tasks
    Then I should see the tasks "Buy milk" and "Walk the dog"

  Scenario: Mark a task as completed
    Given I have a todo list with the task "Buy milk"
    When I mark the task "Buy milk" as completed
    Then the task "Buy milk" should be marked as completed

  Scenario: Delete a task
    Given I have a todo list with the task "Buy milk"
    When I delete the task "Buy milk"
    Then the todo list should be empty

  Scenario: Get the creation date of the todo list
    Given I have a new todo list
    When I check the creation date of the todo list
    Then I should see the current date

  Scenario: Prevent adding duplicate tasks
    Given I have a todo list with the task "Buy milk"
    When I add a task with the description "Buy milk"
    Then I should see an error saying "Task already exists"

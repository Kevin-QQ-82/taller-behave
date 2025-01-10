from datetime import datetime
from behave import given, when, then
from app import TodoList

@given('I have an empty todo list')
def step_empty_todo_list(context):
    context.todo_list = TodoList()

@when('I add a task with the description "{description}"')
def step_add_task(context, description):
    context.result = context.todo_list.add_task(description)

@then('the todo list should contain {count} task')
def step_check_task_count(context, count):
    assert len(context.todo_list.tasks) == int(count)

@then('the task description should be "{description}"')
def step_check_task_description(context, description):
    assert context.todo_list.tasks[0]['description'] == description

@given('I have a todo list with the tasks {tasks}')
def step_setup_tasks(context, tasks):
    task_list = [task.strip() for task in tasks.split('and')]
    context.todo_list = TodoList()
    for task in task_list:
        context.todo_list.add_task(task)

@when('I list all tasks')
def step_list_tasks(context):
    context.result = context.todo_list.list_tasks()

@then('I should see the tasks {tasks}')
def step_see_tasks(context, tasks):
    expected_tasks = [task.strip() for task in tasks.split('and')]
    assert context.result == expected_tasks

@given('I have a todo list with the task "{description}"')
def step_single_task(context, description):
    context.todo_list = TodoList()
    context.todo_list.add_task(description)

@when('I mark the task "{description}" as completed')
def step_mark_completed(context, description):
    context.todo_list.mark_completed(description)

@then('the task "{description}" should be marked as completed')
def step_check_completed(context, description):
    for task in context.todo_list.tasks:
        if task['description'] == description:
            assert task['completed'] is True

@when('I delete the task "{description}"')
def step_delete_task(context, description):
    context.todo_list.delete_task(description)

@then('the todo list should be empty')
def step_check_empty(context):
    assert len(context.todo_list.tasks) == 0

@given('I have a new todo list')
def step_new_todo_list(context):
    context.todo_list = TodoList()

@when('I check the creation date of the todo list')
def step_check_creation_date(context):
    context.creation_date = context.todo_list.creation_date

@then('I should see the current date')
def step_verify_current_date(context):
    current_date = datetime.now().strftime('%Y-%m-%d')
    assert context.creation_date == current_date, f"Expected {current_date}, but got {context.creation_date}"

@then('I should see an error saying "{error_message}"')
def step_check_error(context, error_message):
    assert context.result == error_message

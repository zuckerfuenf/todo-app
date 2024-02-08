# from functions import get_todos, write_todos
import functions
import time


while True:
    # Get user input and strip space characters from it
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos =  [item.strip('\n') for items in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, "files/todos.txt")

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, "files/todos.txt")

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("Number missing")
        continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print("Bye")
class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, task):
        self.todos.append(task)

    def list(self):
        for index, task in enumerate(self.todos, 1):
            print(f"{index}. {task}")

    def remove(self, index):
        try:
            self.todos.pop(index - 1)
        except IndexError:
            print("Task not found.")
    

class CLI:
    def __init__(self):
        self.todo_list = TodoList()

    def run(self):
        while True:
            command = input("Enter command (add, list, remove, exit): ")
            if command == "exit":
                break
            elif command == "add":
                task = input("Enter the task: ")
                self.todo_list.add(task)
            elif command == "list":
                self.todo_list.list()
            elif command == "remove":
                index = int(input("Enter task number to remove: "))
                self.todo_list.remove(index)
            else:
                print("Unknown command!")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
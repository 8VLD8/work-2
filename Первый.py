# Простой список дел
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        task = input("Введите новую задачу: ")
        self.tasks.append(task)
        print(f"Задача '{task}' добавлена!")
    
    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст!")
        else:
            print("\nВаши задачи:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
    
    def remove_task(self):
        self.show_tasks()
        if self.tasks:
            try:
                task_num = int(input("Введите номер задачи для удаления: ")) - 1
                if 0 <= task_num < len(self.tasks):
                    removed = self.tasks.pop(task_num)
                    print(f"Задача '{removed}' удалена!")
                else:
                    print("Неверный номер задачи!")
            except ValueError:
                print("Введите номер задачи!")

def main():
    todo = TodoList()
    
    while True:
        print("\n=== Меню Списка дел ===")
        print("1. Показать все задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            todo.add_task()
        elif choice == "3":
            todo.remove_task()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

if __name__ == "__main__":
    main()
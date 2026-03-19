class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None


class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_node = Node(val)
        new_node.pref = self.end
        self.end = new_node

    def print(self):
        current = self.end
        while current is not None:
            print(current.data, end=" ")
            current = current.pref
        print()


# Тестирование
stack = Stack()

while True:
    cmd = input("Введите команду (push X, pop, print, exit): ")

    if cmd == "exit":
        break
    elif cmd == "pop":
        val = stack.pop()
        if val is None:
            print("Стек пуст")
        else:
            print("Извлечено:", val)
    elif cmd == "print":
        stack.print()
    elif cmd.startswith("push"):
        try:
            val = int(cmd.split()[1])
            stack.push(val)
            print("Добавлено:", val)
        except:
            print("Ошибка: нужно указать число, например: push 5")
    else:
        print("Неизвестная команда")
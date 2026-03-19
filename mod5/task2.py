class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start is not None:
            self.start.pref = None
        else:
            self.end = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        if n == 0:
            new_node = Node(val)
            new_node.nref = self.start
            if self.start is not None:
                self.start.pref = new_node
            self.start = new_node
            if self.end is None:
                self.end = new_node
            return

        current = self.start
        index = 0
        while current is not None and index < n:
            current = current.nref
            index += 1

        if current is None and index == n:
            self.push(val)
            return

        if current is not None:
            new_node = Node(val)
            prev_node = current.pref
            new_node.pref = prev_node
            new_node.nref = current
            if prev_node is not None:
                prev_node.nref = new_node
            current.pref = new_node

    def print(self):
        current = self.start
        while current is not None:
            print(current.data, end=" ")
            current = current.nref
        print()


# Тестирование
queue = Queue()

while True:
    cmd = input("Введите команду (push X, pop, insert N X, print, exit): ")

    if cmd == "exit":
        break

    elif cmd == "pop":
        val = queue.pop()
        if val is None:
            print("Очередь пуста")
        else:
            print("Извлечено:", val)

    elif cmd == "print":
        queue.print()

    elif cmd.startswith("push"):
        try:
            val = int(cmd.split()[1])
            queue.push(val)
            print("Добавлено в конец:", val)
        except:
            print("Ошибка: нужно указать число, например: push 5")

    elif cmd.startswith("insert"):
        try:
            parts = cmd.split()
            n = int(parts[1])
            val = int(parts[2])
            queue.insert(n, val)
            print(f"Вставлено {val} на позицию {n}")
        except:
            print("Ошибка: нужно указать позицию и число, например: insert 2 7")

    else:
        print("Неизвестная команда")
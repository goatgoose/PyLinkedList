from typing import Any, Optional


class Node:
    def __init__(self):
        self._head: Node = None
        self._tail: Node = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self._tail = value


class DataNode(Node):
    def __init__(self, data: Any):
        super().__init__()
        self.data = data

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None

        self.length = 0
        self.connected = False

    def insert(self, index: int, node: Node) -> None:
        to_insert = node
        if index < 0:
            index = self.length + index + 1
        if index == 0:
            if self.first:
                to_insert.head = self.first
                self.first.tail = to_insert
            else:
                self.last = to_insert
            self.first = to_insert
        elif index < self.length:
            before = self.get(index - 1)
            after = before.head
            before.head = to_insert
            after.tail = to_insert
            to_insert.tail = before
            to_insert.head = after
        elif index == self.length:
            self.last.head = to_insert
            to_insert.tail = self.last
            self.last = to_insert
        else:
            raise IndexError()
        self.length += 1

    def remove(self, index: int) -> Node:
        to_remove = self.get(index)

        if to_remove == self.last:
            if to_remove.tail:
                self.last = to_remove.tail
            else:
                self.first = None
                self.last = None
        elif to_remove == self.first:
            if to_remove.head:
                self.first = to_remove.head
            else:
                self.first = None
                self.last = None
        else:
            to_remove.head.tail = to_remove.tail
            to_remove.tail.head = to_remove.head

        self.length -= 1
        return to_remove

    def pop(self, index: int =-1) -> Node:
        return self.remove(index)

    def append(self, node: Node) -> None:
        self.insert(self.length, node)

    def prepend(self, node: Node) -> None:
        self.insert(0, node)

    def get(self, index: int) -> Node:
        if index < 0:
            index = self.length + index + 1

        if index < self.length / 2:
            node = self.first
            for i in range(index):
                node = node.head
            return node
        else:
            node = self.last
            for i in range(self.length - index - 1):
                node = node.tail
            return node

    def set(self, index: int, node: Node) -> None:
        self.remove(index)
        self.insert(index, node)

    def find(self, func) -> Optional[Node]:
        for node in self:
            if func(node):
                return node
        return None

    def index_of(self, node: Node) -> Optional[int]:
        for i, _node in enumerate(self):
            if _node == node:
                return i
        return None

    def __iter__(self):
        node = self.first
        while node != self.last:
            yield node
            node = node.head
        if node:
            yield node  # yield the head

    def __getitem__(self, index: int) -> Node:
        return self.get(index)

    def __setitem__(self, index: int, node: Node) -> None:
        self.set(index, node)

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        string = ""
        for i, data in enumerate(self):
            string += str(data)
            if i < len(self) - 1:
                string += ", "
        return string


class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

        self._connected = False

    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, value: bool):
        if value:
            self._connected = True
            if self.last:
                self.last.head = self.first
                self.first.tail = self.last
        else:
            self._connected = False
            if self.first:
                self.last.tail = None
                self.first.head = None

    def to_modular_index(self, index: int) -> int:
        if self.connected:
            return index % (self.__len__() + 1)
        return index

    def insert(self, index: int, node: Node) -> None:
        super().insert(self.to_modular_index(index), node)
        if self.connected:
            self.last.head = self.first
            self.first.tail = self.last

    def remove(self, index: int) -> Node:
        removed = super().remove(self.to_modular_index(index))
        if self.connected:
            self.last.head = self.first
            self.first.tail = self.last
        return removed

    def pop(self, index: int =-1) -> Node:
        return super(CircularLinkedList, self).pop(self.to_modular_index(index))

    def get(self, index: int) -> Node:
        if self.connected:
            index = index % self.length
        else:
            if index >= self.length:
                raise IndexError()
        return super(CircularLinkedList, self).get(self.to_modular_index(index))

    def set(self, index: int, node: Node) -> None:
        super(CircularLinkedList, self).set(self.to_modular_index(index), node)


if __name__ == "__main__":

    class MyNode(Node):
        def __init__(self, my_data):
            super().__init__()
            self.my_data = my_data

        def __str__(self):
            return str(self.my_data)

    linked_list = LinkedList()

    print("adding to list:")
    node_1 = MyNode("test1")
    linked_list.append(node_1)
    linked_list.prepend(MyNode("test0"))
    linked_list.insert(-1, MyNode("test3"))
    linked_list.insert(2, MyNode("test2"))
    print(linked_list)

    print()
    print("retrieving from list:")
    print(linked_list[1])
    print(linked_list.index_of(node_1))
    print(linked_list.find(lambda node: node.my_data == "test3"))

    print()
    print("removing from list:")
    print(linked_list.remove(0))
    print(linked_list.pop())


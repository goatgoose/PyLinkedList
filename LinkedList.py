

class Node(object):
    def __init__(self):
        self._head = None
        self._tail = None

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
    def __init__(self, data):
        super(DataNode, self).__init__()
        self.data = data

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

        self.length = 0
        self.connected = False

    def insert(self, index, node):
        to_insert = node
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

    def remove(self, index):
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

    def pop(self, index=-1):
        return self.remove(index)

    def append(self, data):
        self.insert(self.length, data)

    def prepend(self, data):
        self.insert(0, data)

    def get(self, index):
        if index < 0:
            index = self.length + index
        if self.connected:
            index = index % self.length
        else:
            if index >= self.length:
                raise IndexError()

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

    def set(self, index, node):
        self.remove(index)
        self.insert(index, node)

    def find(self, func):
        for node in self:
            if func(node):
                return node

    def index_of(self, node):
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
        raise StopIteration

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, data):
        self.set(index, data)

    def __len__(self):
        return self.length

    def __str__(self):
        string = ""
        for i, data in enumerate(self):
            string += str(data)
            if i < len(self) - 1:
                string += ", "
        return string


class CircularLinkedList(LinkedList):
    def __init__(self):
        super(CircularLinkedList, self).__init__()

        self._connected = False

    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, value):
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

    def to_modular_index(self, index):
        if self.connected:
            return index % (self.__len__() + 1)
        return index

    def insert(self, index, node):
        super(CircularLinkedList, self).insert(self.to_modular_index(index), node)
        if self.connected:
            self.last.head = self.first
            self.first.tail = self.last

    def remove(self, index):
        removed = super(CircularLinkedList, self).remove(self.to_modular_index(index))
        if self.connected:
            self.last.head = self.first
            self.first.tail = self.last
        return removed

    def pop(self, index=-1):
        return super(CircularLinkedList, self).pop(self.to_modular_index(index))

    def get(self, index):
        return super(CircularLinkedList, self).get(self.to_modular_index(index))

    def set(self, index, node):
        super(CircularLinkedList, self).set(self.to_modular_index(index), node)


if __name__ == "__main__":
    linked_list = CircularLinkedList()
    linked_list.append(DataNode(0))
    linked_list.append(DataNode(1))
    linked_list.append(DataNode(2))
    linked_list.append(DataNode(3))
    linked_list.append(DataNode(4))
    linked_list.append(DataNode(5))
    linked_list.append(DataNode(6))

    linked_list.insert(2, DataNode(1.5))
    linked_list.append(DataNode(10))
    linked_list.prepend(DataNode(-1))

    linked_list.connected = True

    linked_list.insert(11, DataNode(11))

    print(linked_list)

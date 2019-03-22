# PyLinkedList

## Usage

```
from PyLinkedList import LinkedList, Node

class MyNode(Node):
    def __init__(self, my_data):
        super().__init__()
        self.my_data = my_data

    def __str__(self):
        return str(self.my_data)

linked_list = LinkedList()
```

Adding to the list:

```
linked_list.append(MyNode("test2"))
linked_list.prepend(MyNode("test1"))
linked_list.insert(-1, MyNode("test4"))
linked_list.insert(2, MyNode("test3"))
print(linked_list)
```
```
test1, test2, test3, test4
```

Retrieving from list:

```
print(linked_list[1])
print(linked_list.index_of(node_1))
print(linked_list.find(lambda node: node.my_data == "test3"))
```
```
test1
1
test3
```

Removing from list:

```
print(linked_list.remove(0))
print(linked_list.pop())
```
```
test0
test3
```

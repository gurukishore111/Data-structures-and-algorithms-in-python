# Stack Lifo method
"""
# First Method

stack = []


def checked_empty():
    if len(stack) == 0:
        print("Your Stack is Empty now")
    else:
        print("Yours Stack contains some elements",stack)


val1 = 1
val2 = 2
val3 = 3
stack.append(val1)
stack.append(val2)
stack.append(val3)
checked_empty()
a = stack.pop()
b = stack.pop()
c = stack.pop()

print("Elements get popped are", a, b, c,'\n')

checked_empty()

"""


# Second Class method

class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()

while True:
    print("1.Push")
    print("2.Pop")
    print("3.Exit")
    do = int(input("Enter the option:"))
    if do == 1:
        val = input("Enter the element:")
        s.push(val)
    elif do == 2:
        if s.is_empty():
            print("Enter the elements")
        else:
            print("Popped elements", s.pop())
    elif do == 3:
        break
    else:
        print("Invalid option")

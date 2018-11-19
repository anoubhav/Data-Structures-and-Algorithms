class Stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
    
# s = Stack()
# print(s.is_empty())
# s.push('a')
# s.push('b')
# s.push('c')
# print(s.get_stack())
# print(s.peek())
# print(s.is_empty())
# s.pop()
# s.pop()
# s.pop()
# print(s.is_empty())
# print(s.peek())
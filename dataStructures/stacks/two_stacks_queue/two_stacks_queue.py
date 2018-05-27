class StackQueue(object):
    def __init__(self):
        self.tail_stack = []
        self.head_stack = []

    def refresh_head(self):
        if not self.head_stack:
            while self.tail_stack:
                self.head_stack.append(self.tail_stack.pop())

    def peek(self):
        self.refresh_head()
        if self.head_stack:
            return self.head_stack[-1]

    def pop(self):
        self.refresh_head()
        if self.head_stack:
            return self.head_stack.pop()

    def put(self, value):
        self.tail_stack.append(value)

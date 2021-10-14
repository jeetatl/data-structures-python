
class RecursiveQueue:

    def __init__(self):
        self.enqueue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack) == 0:
            return None
        else:
            return self._dequeue_helper(self.enqueue_stack)

    def _dequeue_helper(self, source_stack):
        if len(source_stack) == 1:
            return source_stack.pop()
        else:
            popped_value = source_stack.pop()
            dequeue_value = self._dequeue_helper(source_stack)
            source_stack.append(popped_value)
            return dequeue_value

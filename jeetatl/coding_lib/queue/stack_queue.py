class StackQueue:
    def __init__(self):
        self._enqueue_stack = []
        self._dequeue_stack = []

    def enqueue(self, data):
        self._enqueue_stack.append(data)

    def dequeue(self):
        if len(self._dequeue_stack) == 0:
            if len(self._enqueue_stack) == 0:
                return None
            else:
                while len(self._enqueue_stack) > 0:
                    self._dequeue_stack.append(self._enqueue_stack.pop())

        return self._dequeue_stack.pop()

    def print_enqueue(self):
        print("Current enqueue state: %s" % self._enqueue_stack)

    def print_dequeue(self):
        print("Current dequeue state: %s" % self._dequeue_stack)

    def print_state(self):
        print("---------------")
        print("Current queue state: %s %s", self._dequeue_stack[:].reverse(), self._enqueue_stack)


if __name__ == "__main__":
    sq = StackQueue()
    sq.enqueue(10)
    sq.print_state()

    sq.enqueue(20)
    sq.print_state()

    sq.enqueue(45)
    sq.print_state()

    sq.enqueue(39)
    sq.print_state()

    sq.enqueue(25)
    sq.print_state()

    sq.dequeue()
    sq.print_state()

    sq.enqueue(200)
    sq.print_state()

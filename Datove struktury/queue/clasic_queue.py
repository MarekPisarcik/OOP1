


class SimpleQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        self.__queue.append(item)

    def enqueue(self):
        return self.__queue.pop(0)

    def peek(self):
        if self.is_empty():
            return
        return self.__queue[0]

    def is_empty(self):
        return not self.__queue

"""
A queue is similar to a line at a cash register. People queue up, and the person who
came first is served first, known in computer science as FIFO for First In, First Out.
    1. enqueue(element) adds an element to the end of the queue.
    2. dequeue() takes a look at the element at the beginning of
    the queue.
    3. peek() takes a look at the element at the beginning of the queue.
    4. is_empty() checks if the queue is empty.
"""


class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, element):
        self.values.append(element)

    def dequeue(self):
        if self.is_empty():
            raise QueueIsEmptyException()
        return self.values.pop(0)

    def peek(self):
        if self.is_empty():
            raise QueueIsEmptyException()
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0


class QueueIsEmptyException(Exception):
    pass


def main():
    waiting_persons = Queue()
    waiting_persons.enqueue("Julito")
    waiting_persons.enqueue("Michele")
    waiting_persons.enqueue("Jemima")
    while not waiting_persons.is_empty():
        if waiting_persons.peek() == "Michele":
            # reprocess at the end
            waiting_persons.enqueue("Michele again")
        next_person = waiting_persons.dequeue()
        print("Processing " + next_person)


if __name__ == "__main__":
    main()

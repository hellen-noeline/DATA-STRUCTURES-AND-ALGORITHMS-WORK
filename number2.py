class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)
        print(f"{student} has joined the queue.")

    def dequeue(self):
        if not self.is_empty():
            served_student = self.queue.pop(0)
            print(f"{served_student} is being served.")
            return served_student
        else:
            print("Queue is empty. No students to dequeue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def queue_size(self):
        return len(self.queue)


# Example Usage:
queue_manager = StudentQueue()

queue_manager.enqueue("Student A")
queue_manager.enqueue("Student B")
queue_manager.enqueue("Student C")

print("Queue Size:", queue_manager.queue_size())

served_student = queue_manager.dequeue()
if served_student:
    print(f"{served_student} has been served.")

print("Queue Size:", queue_manager.queue_size())

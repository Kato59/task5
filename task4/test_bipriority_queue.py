from bipriority_queue import BiPriorityQueue

q = BiPriorityQueue()

q.enqueue("task1", priority=3)
q.enqueue("task2", priority=5)
q.enqueue("task3", priority=1)

print("Peek highest:", q.peek("highest"))   # Очікується: task2
print("Peek lowest:", q.peek("lowest"))     # Очікується: task3
print("Peek oldest:", q.peek("oldest"))     # Очікується: task1
print("Peek newest:", q.peek("newest"))     # Очікується: task3

print("Dequeue highest:", q.dequeue("highest"))  # Очікується: task2
print("Dequeue oldest:", q.dequeue("oldest"))    # Очікується: task1
print("Dequeue lowest:", q.dequeue("lowest"))    # Очікується: task3

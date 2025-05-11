class BiPriorityQueue:
    def __init__(self):
        self._queue = []
        self._counter = 0  # Для відстеження порядку вставки

    def enqueue(self, item, priority):
        entry = (priority, self._counter, item)
        self._queue.append(entry)
        self._counter += 1

    def peek(self, mode='highest'):
        if not self._queue:
            return None

        if mode == 'highest':
            return max(self._queue)[2]
        elif mode == 'lowest':
            return min(self._queue)[2]
        elif mode == 'oldest':
            return min(self._queue, key=lambda x: x[1])[2]
        elif mode == 'newest':
            return max(self._queue, key=lambda x: x[1])[2]
        else:
            raise ValueError("Mode must be one of: 'highest', 'lowest', 'oldest', 'newest'")

    def dequeue(self, mode='highest'):
        if not self._queue:
            return None

        if mode == 'highest':
            target = max(self._queue)
        elif mode == 'lowest':
            target = min(self._queue)
        elif mode == 'oldest':
            target = min(self._queue, key=lambda x: x[1])
        elif mode == 'newest':
            target = max(self._queue, key=lambda x: x[1])
        else:
            raise ValueError("Mode must be one of: 'highest', 'lowest', 'oldest', 'newest'")

        self._queue.remove(target)
        return target[2]


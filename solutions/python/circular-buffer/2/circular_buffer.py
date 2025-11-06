class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class CircularBuffer:
    "Included some extra methods just because ¯\_(ツ)_/¯"
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.ind = 0
    
    def cycle(self):
        if self.buffer:
            if self.ind < self.capacity:
                self.ind += 1
                return self.buffer[self.ind-1]
            else:
                self.ind = 1
                return self.buffer[self.ind-1]
        else:
            raise BufferEmptyException("Circular buffer is empty")

    def read(self):
        if self.buffer:
            return self.buffer.pop(0)
        else:
            raise BufferEmptyException("Circular buffer is empty")

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if self.buffer and len(self.buffer) == self.capacity:
            self.buffer.pop(0)
            self.buffer.append(data)
        elif self.buffer and len(self.buffer) < self.capacity:
            self.buffer.append(data)

    def clear(self):
        self.buffer.clear()

    def see_buffer(self):
        full_buffer = '->'.join([str(i) for i in self.buffer])
        oldest = full_buffer[0]
        newest = full_buffer[-1]
        return f'full_buffer: ->{full_buffer}->, oldest: {oldest}, newest: {newest}'



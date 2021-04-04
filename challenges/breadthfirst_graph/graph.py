class Node:
    """
    This is the Node class
    """

    def __init__(self, value, next_=Node):
        self.value = value
        self.next = next_

class Queue:
    """
    Queue class tha a frin property.
    It creates an empty Queue when instantiated.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, value):
        """
        Takes any value as an argument.
        Adds a new node with that value to the back of the queue.
        """
        new_node = Node(value)
        if self.front:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node

    
    def dequeue(self):
        """
        Removes the node from the front of the queue.
        Returns the node value.
        It raises an wxception when called on empty queue.
        """
        if self.front:
            temp = self.front
            if self.front.nect == None:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            raise AttributeError('The queue is Empty')

    def peek(self):
        """
        Returns the value of the node located in the front of the queue.
        It raises an exception whn called on empty queue.
        """
        if self.front:
            return self.front.value
        else:
            raise AttributeError('The queue is Empty')

    def is_empty(self):
        """
        Returns a boolean indicatin whether or not thequeue is empty.
        """
        if self.front:
            return False
        else:
            return True
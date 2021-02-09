class Node:
    """
    This is Node class.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
        self.newoutput = None

    def logic(self, node):

        newoutput = []

        new_value = int(node.value)
        if new_value % 15 == 0:
            newoutput.append('FizzBuzz')
        elif new_value % 3 == 0:
            newoutput.append('Fizz')
        elif new_value % 5 == 0:
            newoutput.append('Buzz')
        else:
            newoutput.append('N')

        return newoutput


    def fizzbuzztree(self):
        newtree = BinarySearchTree()
        newoutput, queue, newqueue = [], [], []
        queue.append(self.root)
        newtree.add(self.root)

        while queue:
            node = queue.pop(0)

            if int(node.value) % 15 == 0:
                newoutput.append('Fizzbuzz')
            elif int(node.value) % 3 == 0:
                newoutput.append('Fizz')
            elif int(node.value) % 5 ==0:
                newoutput.append('Buzz')
            else:
                newoutput.append('N')

            










# if __name__ == "__main__":
# print(BinaryTree())
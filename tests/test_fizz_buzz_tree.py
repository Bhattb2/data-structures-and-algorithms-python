from challenges.fizz_buzz_tree import __version__
from challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinarySearchTree, BinaryTree


def test_version():
    assert __version__ == '0.1.0'


def test_imports():
    assert BinarySearchTree
    assert BinaryTree
    assert Node


def test_newtree():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(5)
    tree.add(3)
    tree.add(1)
    tree.add(35)
    tree.add(30)
    tree.add(9)
    tree.add(6)
    tree.add(41)
    tree.add(3)
    expected = ['FizzBuzz', 'Buzz', 'Buzz', 'Fizz', 'Fizz', 'FizzBuzz', 'N', 'N', 'Fizz', 'Fizz']
    assert expected == tree.fizzbuzztree() 
     
import pytest
from data_structures.tree.tree import Node, BinaryTree, BinarySearchTree


def test_node_exists():
    assert Node

def test_BinaryTree_exists():
    BinaryTree

def test_BinarySearchTree():
    BinarySearchTree


#Can successfully instantiate an empty tree
def test_instantiate_empty_tree():
    bst = BinarySearchTree()
    assert bst




# Can successfully instantiate a tree with a single root node
# Can successfully add a left child and right child to a single root node
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal
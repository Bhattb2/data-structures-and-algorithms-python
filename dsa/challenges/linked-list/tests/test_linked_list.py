from linked_list import Node, __version__
# from linked_list import Node, LinkedList
# import linked_list

def test_version():
    assert __version__ == '0.1.0'


def test_node_exist():
    node = Node()
    assert node.version == 1

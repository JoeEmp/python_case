'''
@Author: your name
@Date: 2020-03-06 15:27:35
@LastEditTime: 2020-03-07 00:18:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /learn_case/DataStructure/tree.py
'''
import os


class TreeNode():
    def __init__(self, data=None, parent=None):
        super().__init__()
        self.data = data
        self.parent = None
        self.children = list()
        self.indexs = list()
        self.set_parent(parent)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def add_child(self, child, index=-1):
        if child.data not in self.indexs:
            if -1 == index or index >= len(self.children):
                self.children.append(child)
            else:
                self.children.insert(index, child)
            self.indexs.append(child.get_data())
        return child

    def remove_child(self, child):
        try:
            child.set_parent(None)
            self.children.remove(child)
        except Exception as e:
            return None
        return child

    def set_parent(self, parent):
        if self.parent:
            self.parent.remove_child(self)
        self.parent = parent
        if parent:
            self.parent.add_child(self)


def walk_tree(root):
    """ 遍历 """
    print(root.data)
    for node in root.children:
        walk_tree(node)


def pre_walk_tree(root):
    """ 先序遍历 """
    for node in root.children:
        walk_tree(node)
    print(root.data)


def add_node(path: str, root):
    nodes = path.split(os.sep)
    for node in nodes:
        if node and '.' != node:
            node = TreeNode(node, root)
            print(node,node.data)
            root = node


if __name__ == "__main__":
    root = TreeNode('.')
    nodes = [
        '/computer/dev/c',
        '/computer/dev/cpp',
        '/book/dev/',
    ]
    for node in nodes:
        add_node(node, root)
    walk_tree(root)

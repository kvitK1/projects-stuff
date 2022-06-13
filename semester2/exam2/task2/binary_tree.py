"""
File: linkedbst.py
Author: Ken Lambert
"""

from abstractcollection import AbstractCollection
from bstnode import BSTNode
from linkedstack import LinkedStack
# from linkedqueue import LinkedQueue


class BinaryTree(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            string = ""
            if node is not None:
                string += recurse(node.right, level + 1)
                string += "| " * level
                string += str(node.data) + "\n"
                string += recurse(node.left, level + 1)
            return string

        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        if not self.isEmpty():
            stack = LinkedStack()
            stack.push(self._root)
            while not stack.isEmpty():
                node = stack.pop()
                yield node.data
                if node.right is not None:
                    stack.push(node.right)
                if node.left is not None:
                    stack.push(node.left)

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        lyst = []

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def add_left(self, node):
        """Add node to the left."""
        def recurse(nod):
            # New item is less, go left until spot is found
            if node < nod.data:
                if nod.left is None:
                    node.left = BSTNode(node)
                else:
                    recurse(nod.left)
                # Tree is empty, so new item goes at the root

        if self.isEmpty():
            self._root = BSTNode(node)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def add_right(self, node):
        """Add node to the right."""
        def recurse(nod):
            # New item is less, go left until spot is found
            if node > nod.data:
                if nod.right is None:
                    node.right = BSTNode(node)
                else:
                    recurse(nod.right)
                # Tree is empty, so new item goes at the root

        if self.isEmpty():
            self._root = BSTNode(node)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1

    def get_left(self):
        """Get all left nodes."""
        if self._root is None:
            return
        q = []
        q.append(self._root)
        lefts = []
        while len(q) != 0:
            n = len(q)
            for i in range(1, n+1):
                temp=q[0]
                q.pop(0)
                if i == 1:
                    lefts.append(temp.data)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
        return lefts

    def get_right(self):
        """Get all right nodes."""
        if self._root is None:
            return
        q = []
        q.append(self._root)
        rights = []

        while q:
            n = len(q)
            while n > 0:
                n -= 1
                temp = q.pop(0)
                if n == 0:
                    rights.append(temp.data)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
        return rights

    def set_root(self, node):
        """Set new root if old one is None."""
        if self._root is None:
            self._root = BSTNode(node)

    def get_root(self):
        """Return root."""
        return self._root.data if self._root else None

    def rightmost(self):
        """Not implemented, yet."""

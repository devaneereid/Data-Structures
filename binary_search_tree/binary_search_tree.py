from doubly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if not self.storage.head:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if not self.storage.head:
            return None

        self.size -= 1
        return self.storage.remove_head()

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
        # forget about the left subtree
        # iterate through the nodes using a loop construct
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

        # Example how Matt showed us in lecture
        # if not self:
        #     return None
        # max_value = self.value
        # current = self
        # while current:
        #     if current.value > max_value:
        #         max_value = current.value
        #     current = current.right
        # return max_value

    # Call the function `fn` on the value of each node
        # recursive solution
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return 
        if self is None:
            return

        #check if we can "move left"
        if self.left is not None:
            self.left.in_order_print()   

        # visit the node by printing it's value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an `iterative` breadth first traversal - not recursive
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while len(queue) > 0:
            x = queue.dequeue()

            print(x.value)

            if x.left:
                queue.enqueue(x.left)
            if x.right:
                queue.enqueue(x.right)

        # Use a queue to form a "line"
        # need a while loop to iterate
        # for the nodes to "get in"
        # start by placing the root in the queue
        # what are we checking in the while statement
        # while length of queue is greater than 0
        #     # dequeue item from front of queue
        #     # print that item
        #     print(self.value)
            # place current items in left node in queue if not None
            # place current items in right node in queue if not None

        # queue = Queue()
        # bft_nodes = node

        # while bft_nodes:
        #     print(bft_nodes.value)
        # if bft_nodes.left:
        #     queue.enqueue(bft_nodes.left)
        
        # if bft_nodes.right:
        #     queue.enqueue(bft_nodes.right)
        # bft_nodes = queue.dequeue() #??

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        all_nodes = node

        while all_nodes:
            print(all_nodes.value)

            if all_nodes.left:
                stack.push(all_nodes.left)
            if all_nodes.right:
                stack.push(all_nodes.right)
            
        # initialize an empty stack 
        # push the root node onto the stack
            # need a while loop to manager our iteration
            # what do we check in our while statement
        # if stack is not empty enter the while loop
            # pop top item off the stack
            # print that items value
            # if there is a left subtree
                # push left item onto the stack
            # if there is a right subtree
                # push right item onto the stack   
 
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
        


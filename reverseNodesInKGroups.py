# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverse(headNode, tailNode):
    currentNode = headNode
    newTail = tailNode.next
    previousNode = None
    nextNode = None
    while previousNode is not tailNode:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    headNode.next = newTail

    return previousNode


def reverseHelper(head, node, k, constK):
    print(k)
    if(node.next is None):
        return
    if k == 0:
        temp = reverse(head, node)
        reverseHelper(node.next, node.next.next, constK, constK)
        return temp
    else:
        return reverseHelper(head, node.next, k - 1, constK)


def reverseNodesInKGroups(l, k):
    if k == 1:
        return l
    if l is None:
        return None

    return reverseHelper(l, l.next, k - 2, k - 2)

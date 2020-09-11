#!/usr/bin/env python3

def insert(self, head, data):
    node = Node(data)
    if head is None:
        head = node
    else:
        current = head
        while(current.next is not None):
            current = current.next
        current.next = node
    return head

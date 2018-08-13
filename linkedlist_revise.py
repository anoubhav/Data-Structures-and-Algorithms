

print('\n'*30)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr = self.head
        string = ''
        while curr:
            string += str(curr.data) + ' -> '
            curr = curr.next
        print(string[:-3])

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        curr = self.head
        if curr == None:
            self.head = new_node
        else:
            while curr.next:
                curr = curr.next
            curr.next = new_node
    
    def insert_after_node(self, prev_node, data):
        curr = self.head
        new_node = Node(data)
        while curr and curr.data != prev_node:
            curr = curr.next
        if not curr:
            print('Node not found')
            return
        new_node.next = curr.next
        curr.next = new_node
    
    def delete_node(self, key):
        prev = None
        curr = self.head
        if key == curr.data:
            self.head = curr.next
            curr = None
            return
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if not curr:
            print('Node not found')
            return
        prev.next = curr.next
        curr = None

    def delete_node_at_pos(self, pos):
        curr = self.head
        prev = None
        if pos == 1:
            self.head = curr.next
            curr = None
            return
        while curr and pos != 1:
            prev = curr
            curr = curr.next
            pos -= 1
        if not curr:
            print('Key not found')
            return
        prev.next = curr.next
        curr = None
    
    def len_iterative(self):
        curr = self.head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        print(length)
    
    def len_recursive(self, node):
        if not node:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap_nodes(self, node1, node2):
        if node1 == node2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != node1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != node2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            print('Node not found')
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(prev, curr):
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return _reverse_recursive(prev, curr)
                
        self.head = _reverse_recursive(None, self.head)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head

        if not p:
            return q
        if not q:
            return p
        
        if p.data<=q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s
        while p and q:
            if p.data<=q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head



llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

# llist_1.print_list()
# llist_2.print_list()

llist_1.merge_sorted(llist_2)
llist_1.print_list()

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()
# llist = LinkedList()
# llist.append('A')
# llist.append('B')
# llist.append('C')
# llist.append('D')
# llist.print_list()
# llist.swap_nodes('A', 'D')
# llist.print_list()
# llist.reverse_iterative()
# llist.print_list()
# llist.reverse_recursive()
# llist.print_list()

print('\n'*30)

            
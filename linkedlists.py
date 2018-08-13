print('\n'*50)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        string = ''
        while current:
            string = string + str(current.data) + '-> '
            current = current.next
        print(string[:-3])

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == prev_node:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        if current == None:
            print('Node not found')

    def delete_node(self, key):
        current = self.head
        if current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print('Key not found')
            return
        prev.next = current.next
        current = None
    
    def delete_node_at_pos(self, pos):
        current = self.head
        if pos == 0:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and pos!=0:
            prev = current
            current = current.next
            pos -= 1
        if current is None:
            print('Key not found')
            return
        prev.next = current.next 
        current = None
    
    def len_iterative(self):
        currrent = self.head
        count = 0
        while currrent:
            currrent = currrent.next
            count += 1
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, node1, node2):

        if node1 == node2:
            return

        prev_1 = None
        current_1 = self.head
        while current_1 and current_1.data != node1:
            prev_1 = current_1
            current_1 = current_1.next

        prev_2 = None
        current_2 = self.head
        while current_2 and current_2.data != node2:
            prev_2 = current_2
            current_2 = current_2.next

        # print(prev_1.data, current_1.data, prev_2.data, current_2.data)
        if not current_1 or not current_2:
            return
        
        if prev_1:
            prev_1.next = current_2
        else:
            self.head = current_2
        if prev_2:
            prev_2.next = current_1
        else:
            self.head = current_1

        current_1.next, current_2.next = current_2.next, current_1.next

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

        def _reverse_recursive(curr, prev):
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            return _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr = self.head, prev = None)

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
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
    
    def remove_duplicates(self):
        prev = None
        curr = self.head
        counts = dict()
        while curr:
            if curr.data in counts.keys():
                prev.next = curr.next
                curr = None

            else:
                counts[curr.data] = 1
                prev = curr
            curr = prev.next
    
    def print_nth_to_last(self, n):
        
        # Method 1
        total_len = self.len_iterative()

        curr = self.head
        while curr:
            if total_len == n:
                print(curr.data)
                return curr
            total_len -= 1
            curr = curr.next
        
        if not curr:
            print('Invalid position')
        
        ## Method 2
        # p = self.head
        # q = self.head
        # count = 0
        # tot_len = self.len_iterative()
        # if n == tot_len:
        #     print(self.head.data)
        #     return
        # while q and count<n:
        #     q = q.next
        #     count += 1
        # if not q:
        #     print('Invalid position')
        #     return
        # # print(q.data)
        # while p and q:
        #     p = p.next
        #     q = q.next
        # print(p.data)

    def count_occurences_iterative(self, data):
        curr = self.head
        count = 0
        while curr:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count

    def count_occurences_recursive(self, data, node):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(data, node.next)
        else:
            return self.count_occurences_recursive(data, node.next)

    def rotate(self, data):

        curr = self.head
        while curr and curr.data!=data:
            curr = curr.next
        if not curr:
            print('Invalid node')
        
        temp_head = curr.next
        temp = curr.next
        curr.next = None
        
        if temp == None:
            return

        while temp.next:
            temp = temp.next
        temp.next = self.head
        self.head = temp_head
    
    def is_palindrome(self):
        # Method 1
        s = ''
        curr = self.head
        while curr:
            s += str(curr.data)
            curr = curr.next
        return s == s[::-1]

        # Method 2
        # curr = self.head
        # s = []
        # while curr:
        #     s.append(curr.data)
        #     curr = curr.next
        # curr = self.head        
        # while curr:
        #     data = s.pop()
        #     if curr.data != data:
        #         return False
        #     curr = curr.next
        # return True

        # Method 3
        # p = self.head
        # q = self.head
        # prev = []

        # i = 0
        # while q:
        #     prev.append(q)
        #     q = q.next
        #     i += 1
        # q = prev[i-1]

        # count = 1
        # while count < i//2 + 1:
        #     if prev[-count].data != p.data:
        #         return False
        #     p = p.next
        #     count += 1
        # return True
    
    def move_tail_to_head(self):
        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        curr.next = self.head
        self.head = curr
    
    def sum_two_lists(self, llist):
        """ The least significant digit
        is appended first into the linked list aka read from right to leftz """
        p = self.head
        q = llist.head

        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s>=10:
                carry = 1
                remainder = s % 10
                if not p.next and not q.next:
                    sum_list.append(s)
                else:
                    sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        # sum_list.print_list()
        # sum_list.reverse_iterative()
        sum_list.print_list()
    








# Testing

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)
print(751+457)
llist_2.append(7)
# llist_2.append(5)
# llist_2.append(4)
# llist_1.append(9)
# llist_1.append(10)

llist_1.print_list()
# llist_1.remove_duplicates()
# llist_1.print_list()
llist_2.print_list()
llist_1.sum_two_lists(llist_2)

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()
llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
# llist.append(1)
# llist.append(6)
# print(llist.count_occurences_iterative(9))
# print(llist.count_occurences_recursive(1, llist.head))

# llist.print_list()
# llist.move_tail_to_head()
# llist.print_list()
# print(llist.is_palindrome())
# llist.rotate(2)
# llist.print_list()
# llist.print_nth_to_last(1)

# llist.swap_nodes('B', 'A')
# llist.print_list()
# llist.reverse_iterative()
# llist.print_list()
# llist.reverse_recursive()
# llist.print_list()

print('\n'*30)


# """ Default argument values are evaluated at function define-time, but self is an argument only available at function call time. Thus arguments in the argument list cannot refer each other.

# It's a common pattern to default an argument to None and add a test for that in code:
# def p(self, b=None):
# if b is None:
#     b = self.a
# print b 
# """

class node (object):
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_node (prev,curr):
    prev.next = curr.next

def remove_dups (ll):
    mask = set()
    temp = ll
    prev = None
    while (temp):
        if (temp.val in mask):
            prev.next = temp.next
        else:
            mask.add (temp.val)
            prev = temp
        temp = temp.next
    return ll

# with out using a temporary buffer, I can either sort the linked list [O(nlogn)],
# or use two pointers (O(n ^ 2)) and check every element in each iteration and remove it.

def kth_elem_from_last(ll, k):
    temp = ll
    runner = ll
    for i in xrange(k):
        runner = runner.next

    while (runner):
        temp = temp.next
        runner = runner.next

    return temp.val

def delete_middle_node(node):
    node.val = node.next.val
    node.next = node.next.next

def sum_lists_reverse_order(l1, l2):
    carry = 0
    result = None
    sol = None
    if (l1 and l2):
        while (l1 and l2):
            val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) / 10
            if (result):
                result.next = node(val)
                result = result.next
            else:
                result = node(val)
                sol = result
            l1 = l1.next
            l2 = l2.next
        if (l1):
            while (l1):
                val = (l1.val + carry) % 10
                carry = (l1.val + carry) / 10
                result.next = node(val)
                result = result.next
                l1 = l1.next
            if (carry > 0):
                result.next = node(carry)
        elif (l2):
            while (l2):
                val = (l2.val + carry) % 10
                carry = (l2.val + carry) / 10
                result.next = node(val)
                result = result.next
                l2 = l2.next
            if (carry > 0):
                result.next = node(carry)
        else:
            if (carry > 0):
                result.next = node(carry)
        return sol
    else:
        return l1 if not l2 else l2

def sum_lists_straight_order(l1, l2):
    n1 = 0
    n2 = 0
    if (l1 and l2):
        while (l1 and l2):
            n1 = (n1 * 10) + l1.val
            n2 = (n2 * 10) + l2.val
            l1 = l1.next
            l2 = l2.next
        if (l1):
            while (l1):
                n1 = (n1 * 10) + l1.val
                l1 = l1.next
        if (l2):
            while (l2):
                n2 = (n2 * 10) + l2.val
                l2 = l2.next
    else:
        if (l1):
            while (l1):
                n1 = (n1 * 10) + l1.val
                l1 = l1.next
        if (l2):
            while (l2):
                n2 = (n2 * 10) + l2.val
                l2 = l2.next
    print n1, n2
    if ((n1 + n2) > 0):
        result = None
        sol = None
        for i in str(n1 + n2):
            if (result):
                result.next = node(i)
                result = result.next
            else:
                result = node(i)
                sol = result
        return sol
    else:
        return None

def is_palindrome(ll):
    next = None
    mid = ll
    run = ll
    prev = None
    second_half = None
    odd_len = True
    if (run.next and run.next.next):
        while (run):
            run = run.next
            if (run):
                if (run.next):
                    run = run.next
                    if (next):
                        prev = mid
                        mid = next
                        next = next.next
                        mid.next = prev
                    else:
                        next = run
                        prev = mid
                        mid = mid.next
                        mid.next = prev
                        prev.next = None
                else:
                    odd_len = False
    else:
        if (run.next):
            return True if mid.val == run.next.val else False
        else:
            return True

    second_half = next
    if (odd_len):
        temp = mid.next
        mid.next = next
        second_half = mid
        mid = temp

    while (mid and next):
        if (next.val == mid.val):
            temp = mid.next
            mid.next = second_half
            second_half = mid
            next = next.next
            mid = temp
        else:
            while (mid):
                temp = mid.next
                mid.next = second_half
                second_half = mid
                mid = temp
            ll = second_half
            return False
    ll = second_half
    return True

def intersection(l1,l2):
    l1_len = 0
    l2_len = 0
    temp_l1_ptr = l1
    temp_l2_ptr = l2
    if l1 is None or l2 is None:
        return None

    while (temp_l1_ptr and temp_l2_ptr):
        l1_len += 1
        l2_len += 1
        temp_l1_ptr = temp_l1_ptr.next
        temp_l2_ptr = temp_l2_ptr.next
    while (temp_l1_ptr):
        l1_len += 1
        temp_l1_ptr = temp_l1_ptr.next
    while (temp_l2_ptr):
        l2_len += 1
        temp_l2_ptr = temp_l2_ptr.next

    if (l1_len > l2_len):
        temp_l1_ptr = l1
        while (l1_len - l2_len > 0):
            temp_l1_ptr = temp_l1_ptr.next
            l1_len -= 1
    else:
        temp_l2_ptr = l2
        while (l2_len - l1_len > 0):
            temp_l2_ptr = temp_l2_ptr.next
            l2_len -= 1

    if(temp_l1_ptr):
        temp_l2_ptr = l2
    else:
        temp_l1_ptr = l1

    while (temp_l1_ptr):
        if(id(temp_l1_ptr) == id(temp_l2_ptr)):
            return temp_l1_ptr
        else:
            temp_l1_ptr = temp_l1_ptr.next
            temp_l2_ptr = temp_l2_ptr.next
    return None

def is_looped(ll):
    ptr = ll
    addresses = set()
    while (ptr):
        if (id(ptr) in addresses):
            return True
        else:
            addresses.add(id(ptr))
        ptr = ptr.next
    return False



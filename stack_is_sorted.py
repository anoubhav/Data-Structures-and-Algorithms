def is_sorted(stack):
    storage_stack = []
    for i in range(len(stack)):
        if len(stack) == 0:
            break
        first_val = stack.pop()
        if len(stack) == 0:
            break
        second_val = stack.pop()
        if first_val < second_val:
            return False
        storage_stack.append(first_val)
        stack.append(second_val)
    print('hi')
    # Backup stack
    for i in range(len(storage_stack)):
        stack.append(storage_stack.pop())

    return True

print(is_sorted([9,2,3,4,5,6]))
print(is_sorted([1,2,3,4,5,6]))
print(is_sorted([1,2,7,8,5,6]))
print(is_sorted([1]))
print(is_sorted([]))
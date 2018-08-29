class Vector:
    def __init__(self, nums):
        self.nums = nums

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector([a + b for a,b in zip(self.nums, other.nums)])

    def __str__(self):
        return ', '.join(map(str, self.nums))
    
    def __mul__(self, other):
        if not isinstance(other,(int, float)):
            return NotImplemented

        return Vector([a * other for a in self.nums])
    
    def __rmul__(self, other):
        return self * other


a = Vector([1, 2, 3])
b = Vector([9, 10, 11])

print(a + b)
print(a*2)
# print(a + 2)
print(2*a)



    
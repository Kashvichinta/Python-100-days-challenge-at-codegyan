# Relational operators

a = 10
b = 20

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical operators
print("a > 5 and b > 15 :", a > 5 and b > 15)
print("a > 15 or b > 15 :", a > 15 or b > 15)
print("not(a > 5) :", not(a > 5))

# Assignment operators

a = 10
print("Initial value:", a)

a += 5
print("After a += 5 :", a)

a -= 3
print("After a -= 3 :", a)

a *= 2
print("After a *= 2 :", a)

a //= 4
print("After a //= 4 :", a)

# Bitwise operators

a = 5   # 0101
b = 3   # 0011

print("Bitwise AND :", a & b)
print("Bitwise OR  :", a | b)
print("Bitwise XOR :", a ^ b)
print("Bitwise NOT :", ~a)
print("Left shift  :", a << 1)
print("Right shift :", a >> 1)

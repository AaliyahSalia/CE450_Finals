def verify_add(m, ls):
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j and ls[i] + ls[j] == m:
                return True
    return False



print(verify_add(100, [1, 2, 3, 4, 5]))
print(verify_add(7, [1, 2, 3, 4, 2]))
print(verify_add(10, [5, 5]))
print(verify_add(151, range(0, 200000, 3)))
print(verify_add(50004, range(0, 200000, 4)))

# Output:
# False
# True
# False
# False
# True

def sets(rar):
    for _ in range(0, 99999999999999999999999999999999999999999999999999):
        yield rar


rar = int(input("Enter the number: "))
obj = sets(rar)
print(obj)

listing = [23, 23, 21, 23, 436, 45, 6567, 876765, 343232, 32]
part = listing.__iter__()
print(part.__next__())

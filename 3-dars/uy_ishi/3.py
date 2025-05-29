list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']

TEXT = []
OTHER = []

for i in list1:
    if type(i) == str:
        TEXT.append(i)
    else:
        OTHER.append(i)

TEXT.sort()
OTHER.sort(reverse=True)

print("TEXT =", TEXT)
print("OTHER =", OTHER)

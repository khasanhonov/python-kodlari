nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

sonlar1 = set()
for son in nums:
    if son % 2 == 0:
        sonlar1.add(son)
print(sonlar1)
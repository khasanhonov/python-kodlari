son = 45893 

while son >= 10:
    yigindi = 0
    while son > 0:
        raqam = son % 10
        yigindi = yigindi + raqam
        son = son // 10
    son = yigindi

print(son)  

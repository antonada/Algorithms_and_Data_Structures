st = ['(', '(', '(', ')', '(', '(', ')', ')']
index = 0
normalny_stos =[]
j = 0

for i in st :
    if i == '(':
        normal_stos.append(i)
    elif i == ')':
        print(False)
    else:
        stos.pop(j)
    j += 1

if stos == 0:
    print(True)
else:
    print(False)
    print(normal_stos)
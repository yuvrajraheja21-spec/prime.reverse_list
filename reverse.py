a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
#printing prime number between a and b
for i in range(a, b):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)

#creating reverse list between a and b
reverse_list = []
for i in range(b-1, a-1, -1):
    reverse_list.append(i)

print("Reverse list between", a, "and", b, "is:", reverse_list)

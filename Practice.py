num = input("Enter a number")
i = 0
len = len(num)
j = len -1
sum = 0
while i <= j:
    if num[i] == num[j]:
        sum = sum + int(num[i])
        break
    else:
        num1 = str(num[i]) + str(num[j])
        num2 = int(num1)
        sum = sum+num2
        i = i+1
        j = j-1
print(sum)
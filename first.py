# print numbers from 0 to n and print even and odd numbers in them seperately:
my_list = []
my_list1 = []
my_list2 = []
n = int(input("Please enter a number : "))
for i in range(0,n):
    # Even numbers
    my_list.append(i)
    if (i%2 == 0):
        my_list1.append(i)
    else:
        #odd numbers
        my_list2.append(i)
    
print(my_list)
print("Even : ",my_list1)
print("Odd : ",my_list2)
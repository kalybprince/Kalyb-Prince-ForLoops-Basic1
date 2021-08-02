# 1
for each_item in range(151):
    print(each_item)
# 2
for each_item in range(5, 1000, 5):
    print(each_item)
# 3
for each_item in range(1, 101):
    if each_item % 10 == 0:
        print("Coding Dojo")
    elif each_item % 5 == 0:
        print("Coding")
    else:
        continue
# 4
my_sum = 0

for each_item in range(500001):
    my_sum += each_item

print(my_sum)
# 5
for each_item in range(2018, 0, -4):
    print(each_item)
# 6
lowNum = 2
highNum = 9
mult = 3

for each_item in range(lowNum+1, highNum+1, mult):
    print(each_item)
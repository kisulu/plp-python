## Create an empty list
my_list=[]

## Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

## Insert an element
my_list.insert(1, 15)
print(my_list)

## Extend the list
new_list = [50, 60, 70]
my_list.extend(new_list)
print(my_list)

## Remove the last element
del my_list[-1]
## my_list.remove(70)
print(my_list)

## Sort my_list in ascending order
my_list.sort()
## OR new_sorted_list = sorted(my_list)
print("Sorted List:", my_list)

## Find and print index of value 30

index_of_30 = my_list.index(30)

print("Final List:", my_list)
print("Index of 30:", index_of_30)

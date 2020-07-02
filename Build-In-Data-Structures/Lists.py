# Creating List
# List =[] is mutable
list1 = [1, 2, 3, 4, 5, 'developer']

# Inserting an element:append(),insert(),extend()
# append() is insert the element as list(or)tuples in list
list1.append('android')
list1.append((6, 7, 8))
print("Appended list:", list1)
# extends() is insert the element in list
list1.extend((10, 12, 13, 14))
print("Extended list:", list1)
# insert() is insert the element in defined index
list1.insert(4, 'web')
print("Inserted list:", list1)
# deleting a elements:del(),remove(),pop()
# del() is del the index element which specified
del list1[5]
print("Deleted list:", list1)
# pop() it show the deleted element
a = list1.pop(7)
print("Deleted element:", a)
# remove() is remove the element directly from list
list1.remove(2)
print("Removed list", list1)

# indexing
print(list1[0:4])
# [starting,ending,skipping value]
print(list1[0:4:2])
# reversing elements
print(list1[::-1])

# Sorting the elements
num = [1, 2, 3, 5, 6, 7, 8, 90]
print(sorted(num))

# Sorting in the reverse manner
num.sort(reverse=True)
print(num)
# To find the index of element
print(num.index(6))
# count is used to find the count of element
print(num.count(90))

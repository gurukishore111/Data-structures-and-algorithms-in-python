# Set={'value'} #set is not taken the duplicated value
set1 = {1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8}
print(set1)

set1.add(9)
print(set1)

# union(),intersection(),difference,symmetric_difference()
set2 = {10, 11, 12, 13, 14, 15, 16, 17, 1}
# union
print(set1.union(set2))
# intersection
print(set1.intersection(set2))
# symmetric_difference
print(set1.symmetric_difference(set2))

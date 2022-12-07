def union(s1, s2):
    union_set = set()
    
    for i in s1:
        union_set.add(i)
    for i in s2:
        union_set.add(i)
    return union_set

set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {6, 7, 8, 9, 10, 11, 12}
print(union(set1, set2))
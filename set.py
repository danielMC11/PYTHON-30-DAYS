"""
#set guide
mySet = {1, 2, 3, 4, 5, 6, 7}      # Unordered/Un-Indexed, changeable, No duplicates
mySet.add(6)  # {1, 2, 3, 4, 5, 6, 7}
mySet.update([7, 8])  # {1, 2, 3, 4, 5, 6, 7, 8}

otherSet = {8, 9, 10}
r_NewSet = mySet.union(otherSet) # Returns a Set of Two Sets United {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(r_NewSet)

otherSet2 = {1, 10, 2, 20, 3, 30}
r_InterSet = mySet.intersection(otherSet2)  # Returns a Set of Two Sets Intersected {1, 2, 3}
print(r_InterSet)

otherSet3 = {2, 3, 4, 5, 6, 7}
r_DifSet = mySet.difference(otherSet3) # Returns a Set of Difference of mySet regarding otherSet3 {1, 8}
print(r_DifSet)

otherSet4 = {1, 2, 3, 4, 5, 6, 10, 12}
r_SymDifSet = mySet.symmetric_difference(otherSet4) # Returns a set of elements not in common {7, 8, 10, 12}
print(r_SymDifSet)


otherSet5 = {9, 10, 11, 12}
print(mySet.isdisjoint(otherSet5)) #Returns boolean whether there are not items in common True or not False


Asup = {'a', 'b', 'c', 'd'}
Bsub = {'b','d'}
print('A contains B / A superset B ->', Asup.issuperset(Bsub), 'B contained in A / B subset A ->', Bsub.issubset(Asup))


mySet.remove(8)  # {1, 2, 3, 4, 5, 6, 7}
r_Random_DelValue = mySet.pop()  # Deletes and Returns a Random Value
mySet.discard(15)  # Discards an elements with no error even if it is not present
print(mySet)

message = 'I am a teacher and I love to inspire and teach people.'
listedWords = message.split(' ')
setWords = set(listedWords)
print('Unique Words in "I am a teacher and I love to inspire and teach people.": ', len(setWords))
"""
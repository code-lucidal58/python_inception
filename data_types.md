### List
Lists are similar to arrays. The following operations can be performed on a list.
```Python
l = []
l.insert(1,3) # (index, value)
l.append(8) #add to the end of list
l.remove(6) #removes the first instance of the data in the list
l.pop() # removes last element 
print(l) #prints list
l.sort() # sorts list in ascending order
l.reverse() #this does not change the origib]nal list. Used to reverse order of elements
```
Sorting a nested list based on say nth element of the list elements in list:
```l.sort(key = lambda x: x[3])``` where n is 3 here. Soring is done based on 4th element

### Map

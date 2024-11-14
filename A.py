# Q.1 Write a Python program to implement list operations (any 5).

# Initialize a sample list
sample_list = [10, 20, 30, 40, 50]

# 1. Append an element to the list
sample_list.append(60)
print("After append: ", sample_list)

# 2. Insert an element at a specific index
sample_list.insert(2, 25)
print("After insert: ", sample_list)

# 3. Remove an element by value
sample_list.remove(40)
print("After remove 40: ", sample_list)

# 4. Pop an element from the list
popped_element = sample_list.pop()
print("After pop (popped element: ", popped_element, "):", sample_list)

# 5. Count the occurrence of an element
count_20 = sample_list.count(20)
print("Count of 20: ", count_20)

# 6. Find the index of an element
index_30 = sample_list.index(30)
print("Index of 30: ", index_30)

# 7. Reverse the list
sample_list.reverse()
print("After reverse: ", sample_list)


Output:
After append:  [10, 20, 30, 40, 50, 60]
After insert:  [10, 20, 25, 30, 40, 50, 60]
After remove 40:  [10, 20, 25, 30, 50, 60]
After pop (popped element:  60 ): [10, 20, 25, 30, 50]
Count of 20:  1
Index of 30:  3
After reverse:  [50, 30, 25, 20, 10]
# The course provides a pre determined variable 's' which is a string
s = 'wpvrpxwxtqnarmmwtix'
# Creating an array of ASCII numbers
numbers = []
for char in s:
    temp = ord(char)
    numbers.append(temp)
# Initializing variables to parse
temp_index = 0
t_max = 0
index = 0
count = 0
# Parsing through the number list 
try:
    while temp_index < len(numbers):
        if numbers[temp_index] <= numbers[temp_index+1]:
            # Checking if the numbers are on sequence
            count += 1
            if t_max < count:
                # Storing the max values
                t_max = count
                index = temp_index
        else:
            count = 0
        temp_index += 1
except: IndexError
# Initializing new variables for output
if t_max > 0:
    # Checking if there is at least one element in 'alphabetical order'
    indexF = index + 1
    indexI = indexF - t_max
else:
    indexF = index
    indexI = index
# Starting list to store output in char 
text = []
for i in range(t_max + 1):
    # Transposing the number list to type char, then adding into text[] 
    a = chr(numbers[indexI + i])
    text.append(a)
# Transforming the list in a string
resposta = ''.join(text)
# Printing output
print("Longest substring in alphabetical order is: " + resposta)
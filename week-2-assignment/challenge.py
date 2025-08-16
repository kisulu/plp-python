""" weekly challenge
list_of_numbers = []
numbers=input("Enter all your marks separated by spaces: ")
for number in numbers.split():
    list_of_numbers.append(int(number))
print("Your marks are: ", list_of_numbers)"""

"""## tuple
favorite_books = ("Think Big", "The Power of Now", "Atomic Habits", "Little Heroes", "The Samaritan")
for book in favorite_books:
  print("One of my favorite books is: ", book)"""


## Attempt
"""person = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_color = input("Enter your favorite color: ")

person = {
    "name": name,
    "age": age,
    "favorite_color": favorite_color
}

print("Your profile information:", person)"""

# Create an empty dictionary
## Solution and Attempt
"""person = {}

# Ask user for input
person["name"] = input("Enter your name: ")
person["age"] = int(input("Enter your age: "))
person["favorite_color"] = input("Enter your favorite color: ")

# Print the dictionary
print("\nPerson Information Dictionary:")
print(person)"""

## Write a program that accepts user input to 
## create two sets of integers. Then, create a new 
## set that contains only the elements that are common to both sets

"""jane_marks = set()
john_marks = set()

# Get marks for Jane
jane_input = input("Enter Jane's marks separated by spaces: ")
for mark in jane_input.split():
    jane_marks.add(int(mark))
print("Jane's marks:", jane_marks)

# Get marks for John
john_input = input("Enter John's marks separated by spaces: ")
for mark in john_input.split():
    john_marks.add(int(mark))
print("John's marks:", john_marks)

# Find common marks
common_marks = jane_marks.intersection(john_marks)
print("Common marks:", common_marks)"""

"""# Accept user input for two sets of integers
# map(function, iterable/collection)
jane_marks = set(map(int, input("Enter numbers for the first set (separated by spaces): ").split()))
john_marks = set(map(int, input("Enter numbers for the second set (separated by spaces): ").split()))

# Find common elements using intersection
common_marks = jane_marks.intersection(john_marks)

# Display the result
print("\nJane's Marks:", jane_marks)
print("John's Marks:", john_marks)
print("Common Marks:", common_marks)"""

""" Create a program that stores a list of words. Then, 
use list comprehension to create a new list that 
contains only the words that have an odd number of characters."""

words = ["apple", "banana", "cherry", "date", "fig", "grape"]
odd_length_words = [word for word in words if len(word) % 2 == 1]
print("Original List of Words:", words)
print("Words with Odd Number of Characters:", odd_length_words)


## ChatGPT Solution
# Store a list of words
words = ["apple", "banana", "cherry", "date", "fig", "grape"]

# Use list comprehension to filter words with odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print results
print("Original List of Words:", words)
print("Words with Odd Number of Characters:", odd_length_words)



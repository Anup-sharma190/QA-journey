#Create a tuple named person with the following values:

#"Rahul" (string)

#25 (integer)

#5.9 (float)

#Print the second element of the tuple (the age).

#Try to change the first element (the name) to "John" using person[0] = "John".

#Catch the exception that occurs using a try-except block.

#Print the error message exactly as the Python error
Person = ("Rahul", 25, 5.9)

# Print the second element of the tuple
print(f"Age: {Person[1]}")

# Attempt to change the name in the tuple (this will raise an error)
try:
    person[0] = "John"
except Exception as e:
    print(f"Error: {e}-tuple are immutable")


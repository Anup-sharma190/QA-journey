#Use the attached text file "file1.txt"

#Write a Python script that opens the file, reads through it line by line, counts how many lines it has, and prints the total count.

with open("file.txt", "r") as file:
     lines= file.readlines()

len_count= len(lines)
print(f"total number of line:, {len_count}")
# Student B - Append

file = open("diary.txt", "a")

entry = input("Add another diary entry: ")
file.write(entry + "\n")

file.close()

print("Entry appended!")

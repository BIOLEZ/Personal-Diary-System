# Student A - Create and Write

try:
    file = open("diary.txt", "x")
    file.close()
except:
    print("File already exists")

file = open("diary.txt", "w")
entry = input("Enter your first diary entry: ")
file.write(entry + "\n")
file.close()

print("Entry saved!")

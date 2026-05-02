# Student C - Read and Count

file = open("diary.txt", "r")
lines = file.readlines()

print("\n--- Diary Entries ---")
for line in lines:
    print(line.strip())

print("\nTotal entries:", len(lines))

file.close()
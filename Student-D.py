FILE_NAME = "diary.txt"

def update_entry():
    try:
        with open(FILE_NAME, "r") as file:
            entries = file.readlines()

    except FileNotFoundError:
        print("Diary file not found. Creating one...")
        open(FILE_NAME, "w").close()
        return

    if not entries:
        print("Diary is empty.")
        return

    print("\nYour Diary Entries:")
    for i, entry in enumerate(entries, start=1):
        print(f"{i}. {entry.strip()}")

    try:
        entry_num = int(input("\nEnter entry number to update: "))
    except ValueError:
        print("Invalid input.")
        return

    if 1 <= entry_num <= len(entries):
        new_content = input("Enter new content: ").strip()
        entries[entry_num - 1] = new_content + "\n"

        with open(FILE_NAME, "w") as file:
            file.writelines(entries)

        print("Entry updated successfully.")
    else:
        print("Invalid entry number.")

update_entry()


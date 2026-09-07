text = []
undo_stack = []

while True:

    print("\n=== SIMPLE TEXT EDITOR ===")
    print("1. Add Line")
    print("2. View Text")
    print("3. Delete Line")
    print("4. Undo")
    print("5. Save to File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        undo_stack.append(text.copy())
        line = input("Enter the line: ")
        text.append(line)
        print("Line added successfully.")

    elif choice == "2":
        if len(text) == 0:
            print("No text available")
        else:
            print("\n----- DOCUMENT -----")
            for i in range(len(text)):
                print(i + 1, ".", text[i])

    elif choice == "3":
        if len(text) == 0:
            print("No lines to delete.")
        else:
            line_number = int(input("Enter line number to delete: "))

            if 1 <= line_number <= len(text):
                undo_stack.append(text.copy())
                deleted = text.pop(line_number - 1)
                print("Deleted:", deleted)
            else:
                print("Invalid line number.")

    elif choice == "4":
        if len(undo_stack) == 0:
            print("Nothing to undo.")
        else:
            text = undo_stack.pop()
            print("Undo successful.")

    elif choice == "5":
        with open("document.txt", "w") as file:
            for line in text:
                file.write(line + "\n")

        print("Document saved to document.txt")

    elif choice == "6":
        print("Thank you for using the text editor.")
        break

    else:
        print("Invalid choice.")

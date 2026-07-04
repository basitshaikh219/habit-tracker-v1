habits = []

def show_menu():
    print("\n========== Habit Tracker ==========")
    print("1. Add Habit")
    print("2. Track Habits")
    print("3. Delete Habit")
    print("4. Exit")
    print("===================================")

def add_habit():
    habit = input("Enter habit name: ")
    habits.append([habit, False])
    print(habit, "added successfully!")

def track_habits():
    if len(habits) == 0:
        print("No habits added yet.")
        return

    number = 1

    for habit in habits:
        if habit[1]:
            print(number, ".", habit[0], "✔")
        else:
            print(number, ".", habit[0], "❌")
        number = number + 1

    choice = int(input("Choose a habit to mark as completed: "))
    choice = choice - 1

    if 0 <= choice < len(habits):
        habits[choice][1] = True
        print("Habit marked as completed!")
    else:
        print("Invalid habit number!")

def delete_habit():
    if len(habits) == 0:
        print("No habits to delete.")
        return

    number = 1

    for habit in habits:
        print(number, ".", habit[0])
        number = number + 1

    choice = int(input("Choose a habit to delete: "))
    choice = choice - 1

    if 0 <= choice < len(habits):
        deleted = habits.pop(choice)
        print(deleted[0], "deleted successfully!")
    else:
        print("Invalid habit number!")

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        add_habit()

    elif choice == "2":
        track_habits()

    elif choice == "3":
        delete_habit()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
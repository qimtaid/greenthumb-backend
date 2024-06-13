from helpers import (
    exit_program,
    list_members,
    find_member_by_name,
    find_member_by_id,
    create_member,
    update_member,
    delete_member,
    list_trainers,
    find_trainer_by_name,
    find_trainer_by_id,
    create_trainer,
    update_trainer,
    delete_trainer,
    list_attendance_records,
    add_attendance_record,
    list_fitness_classes,
    add_fitness_class,
    list_payments,
    add_payment
)

def main():
    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. List all members")
        print("2. Find member by name")
        print("3. Find member by id")
        print("4. Create member")
        print("5. Update member")
        print("6. Delete member")
        print("7. List all trainers")
        print("8. Find trainer by name")
        print("9. Find trainer by id")
        print("10. Create trainer")
        print("11. Update trainer")
        print("12. Delete trainer")
        print("13. List all attendance records")
        print("14. Add attendance record")
        print("15. List all fitness classes")
        print("16. Add fitness class")
        print("17. List all payments")
        print("18. Add payment")

        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "1":
            list_members()
        elif choice == "2":
            find_member_by_name()
        elif choice == "3":
            find_member_by_id()
        elif choice == "4":
            create_member()
        elif choice == "5":
            update_member()
        elif choice == "6":
            delete_member()
        elif choice == "7":
            list_trainers()
        elif choice == "8":
            find_trainer_by_name()
        elif choice == "9":
            find_trainer_by_id()
        elif choice == "10":
            create_trainer()
        elif choice == "11":
            update_trainer()
        elif choice == "12":
            delete_trainer()
        elif choice == "13":
            list_attendance_records()
        elif choice == "14":
            add_attendance_record()
        elif choice == "15":
            list_fitness_classes()
        elif choice == "16":
            add_fitness_class()
        elif choice == "17":
            list_payments()
        elif choice == "18":
            add_payment()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

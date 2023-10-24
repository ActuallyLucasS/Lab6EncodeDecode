if __name__ == "__main__":
    while True:
        print("Menu\n" + "-------------\n" + "1. Encode\n" + "2. Decode\n" + "3. Quit")
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = ""
            for i in password:
                encoded_digit = str((int(i) + 3) % 10) # mod by 10 so it doesnt go over 10 (EX: 7 + 3 = 10, remainder will be 0)
                encoded_pass += encoded_digit # add to encode
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            pass
        elif option == 3:
            break
        else:
            print("Invalid choice. Please input 1, 2, or 3.\n")

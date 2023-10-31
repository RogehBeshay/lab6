# Rogeh Beshay's Code

def encode(password):
    new_password = ""
    for i in password:
        x = int(i) + 3
        if x > 9:
            x -= 10
        new_password += str(x)
    return new_password

def main():
    menu = True

    while menu:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {password}.\n')
        else:
            menu = False

if __name__ == "__main__":
    main()
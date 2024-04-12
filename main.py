def encode(num):
    diction = {"0": "3", "1": "4", "2": "5", "3": "8", "4": "7", "5": "8", "6": "9", "7": "0", "8": "1", "9": "2"}
    newpass = ""
    for letter in num:
        newpass += diction[letter]
    return newpass

def decode(num):
    diction = {"3": "0", "4": "1", "5": "2", "8": "3", "7": "4", "8": "5", "9": "6", "0": "7", "1": "8", "2": "9"}
    newpass = ""
    for letter in num:
        newpass += diction[letter]
    return newpass


def main():
    password = ""
    run = 1
    while run == 1:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = input("Please Enter an option: ")
        if choice == "1":
            ans = input("Please enter your password to encode: ")
            password = encode(ans)  # Fix here
            print("Your password has been encoded and stored!")
        elif choice == "2":
            decoded = decode(password)  # Fix here
            print(f"The encoded password is {password}, and the original password is {decoded}")  # Fix here
        elif choice == "3":
            run = 0

if __name__ == "__main__":
    main()

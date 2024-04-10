

def encode(num):
    newpass = ""
    for letter in num:
        newnum = (int(letter)+3)%10
        newdig = str(newnum)
        newpass += newdig
    return newpass




if __name__ == "__main__":
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        break
choice = input("Please Enter an option: ")
if(choice == "1"):
    password = input("Please enter your password to encode: ")
    print(encode(password))


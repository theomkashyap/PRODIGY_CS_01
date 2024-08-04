def caesar_cipher(message, shift, user_input):
    result = ""
    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            if user_input == 'e':
                result_char = chr((ord(char) - start + shift) % 26 + start)
            elif user_input == 'd':
                result_char = chr((ord(char) - start - shift) % 26 + start)
            result += result_char
        else:
            result += char
    return result

def get_user_input():
    while True:
        user_input = input("Do you want to (E)ncrypt or (D)ecrypt a message?").lower()
        if user_input in ['e', 'd', 'q']:
            return user_input
        else:
            print("Invalid action! (Q) for quit.")

def main():
    print("CAESAR CIPHER PROGRAM")

    user_input = get_user_input()
    if user_input == 'q':
        print("Session killed!")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-26): "))

    if user_input == 'e':
        result = caesar_cipher(message, shift, 'e')
        print("\nEncrypted Message:", result)
    elif user_input == 'd':
        result = caesar_cipher(message, shift, 'd')
        print("\nDecrypted Message:", result)

if __name__ == "__main__":
    main()

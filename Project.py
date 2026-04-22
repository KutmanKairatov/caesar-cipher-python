def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def get_shift():
    while True:
        try:
            shift = int(input("🔢 Введите сдвиг (например 3): "))
            return shift
        except:
            print("❌ Ошибка! Введите только число.")


def menu():
    print("\n===== CAESAR CIPHER =====")
    print("1. Шифрование (Encrypt)")
    print("2. Дешифрование (Decrypt)")
    print("0. Выход")


while True:
    menu()
    choice = input("Сделайте выбор: ")

    if choice == '1':
        text = input("Введите текст: ")
        shift = get_shift()
        result = caesar_encrypt(text, shift)
        print("🔐 Результат:", result)

    elif choice == '2':
        text = input("Введите текст: ")
        shift = get_shift()
        result = caesar_decrypt(text, shift)
        print("🔓 Результат:", result)

    elif choice == '0':
        print("Программа завершена.")
        break

    else:
        print("❌ Неверный выбор!")

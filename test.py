
width = int(input("Введите ширину торта: "))
length = int(input("Введите длину торта: "))

total_pieces = width * length
pieces_left = total_pieces

while pieces_left > 0:
    command = input("Введите количество кусочков, которые берут гости (или 'STOP' для завершения): ")

    if command.upper() == "STOP":
        print(f"{pieces_left} pieces are left.")
        break

    try:
        pieces_taken = int(command)
        pieces_left -= pieces_taken

        if pieces_left < 0:
            print(f"No more cake left! You need {-pieces_left} pieces more.")
            break

    except ValueError:
        print("Пожалуйста, введите корректное число или 'STOP'.")



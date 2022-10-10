class Player():
    def __init__(self, name, score = 0) -> None:
        self.name = name
        self.score = score

    def __str__(self) -> str:
        rep = f'{self.name}:\t {str(self.score)}'
        return rep


def ask_yes_no(question):
    response = None
    while response not in ('y','n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == '__main__':
    print('Запущено без импорта')
    input('Нажмите Enter, чтобы выйти')

PASSWORD = input("Введите пароль: ")


def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(word.isdigit() for word in password)


def has_upper_letters(password):
    return any(word.isupper() for word in password)


def has_lower_letters(password):
    return any(word.islower() for word in password)


def has_symbols(password):
    return any(not word.isdigit() and not word.isalpha() for word in password)


def main():
    score_conditions = [
        is_very_long(PASSWORD),
        has_digit(PASSWORD),
        has_upper_letters(PASSWORD),
        has_lower_letters(PASSWORD),
        has_symbols(PASSWORD),
    ]
    new_score = [score for score in score_conditions if score]

    summ_score = len(new_score) * 2

    return f"Рейтинг пароля: {summ_score}"


if __name__ == "__main__":
    print(main())

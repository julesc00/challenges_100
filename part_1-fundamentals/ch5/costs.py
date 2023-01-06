
def get_costs():
    money1, money2 = 25000, 12000
    bonus = get_bonus_amount()
    saved_prev = 95800 - money2
    money_now = 95800
    return f"Total juntado después de 1 quincena: ${money_now + money1 + bonus}"


def get_bonus_amount():
    bonus = (50000 / 12) * 4.3
    print(f"Aguinaldo: ${bonus}")
    return bonus


if __name__ == "__main__":
    print(get_costs())
    print(get_bonus_amount())

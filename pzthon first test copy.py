import random

hp = 100
xp = 0
money = 0


def add_hp(amount):
    global hp
    hp += amount
    if hp > 100:
        hp = 100


def stats():
    global hp, xp, money
    print(f"### HP {hp} ### XP {xp} ### PENÍZE {money} ###")


def safe_input():
    try:
        return int(input("Vyber: "))
    except:
        return None


def welcome_screen():
    print("########################")
    print("     Vítej v RPG hře    ")
    print("########################")
    print("1 - Start")
    print("Cokoliv jiného - Konec")


def tavern():
    global hp, money

    print("\n--- KRČMA ---")
    stats()

    print("1 - Pivo (20)")
    print("2 - Polévka (35)")
    print("3 - Velké jídlo (80)")

    choice = safe_input()

    if choice == 1:
        if money >= 20:
            money -= 20
            add_hp(5)
            print("🍺 Pivo")
        else:
            print("Nemáš peníze")

    elif choice == 2:
        if money >= 35:
            money -= 35
            add_hp(10)
            print("🥣 Polévka")
        else:
            print("Nemáš peníze")

    elif choice == 3:
        if money >= 80:
            money -= 80
            add_hp(50)
            print("🍖 Hostina")
        else:
            print("Nemáš peníze")


def fight(chance):
    return random.randint(1, 100) < chance


def training_course():
    global xp

    print("\n--- TRÉNINK ---")
    print("1 - Útok")
    print("2 - Obrana")

    choice = safe_input()

    if choice == 1:
        if fight(50):
            xp += 1
            print("Vyhrál jsi")
        else:
            print("Prohrál jsi")

    elif choice == 2:
        if fight(65):
            xp += 1
            print("Vyhrál jsi")
        else:
            print("Prohrál jsi")


def real_fight():
    global xp, hp, money

    print("\n--- SOUBOJ ---")
    print("1 - Útok")
    print("2 - Obrana")

    choice = safe_input()

    if choice == 1:
        chance = random.randint(40, 60)
    elif choice == 2:
        chance = random.randint(55, 75)
    else:
        return

    if fight(chance):
        xp_gain = random.randint(5, 30)
        money_gain = random.randint(10, 40)

        xp += xp_gain
        money += money_gain

        print(f"Vyhrál jsi +{xp_gain} XP +{money_gain} 💰")
    else:
        dmg = random.randint(5, 20)
        hp -= dmg
        print(f"Prohrál jsi -{dmg} HP")

    if hp <= 0:
        print("Zemřel jsi 💀")
        exit()


def forest():
    global hp, xp, money  # 🔥 DŮLEŽITÉ!

    print("\n--- LES 🌲 ---")
    print("1 - Prozkoumat")
    print("2 - Zpět")

    choice = safe_input()

    if choice == 1:
        event = random.randint(1, 3)

        if event == 1:
            found = random.randint(10, 50)
            money += found
            print(f"💰 Našel jsi {found} peněz")

        elif event == 2:
            print("🐺 Zvíře!")

            if fight(50):
                gain = random.randint(10, 25)
                xp += gain
                print(f"+{gain} XP")
            else:
                dmg = random.randint(10, 25)
                hp -= dmg
                print(f"-{dmg} HP")

        elif event == 3:
            heal = random.randint(10, 30)
            add_hp(heal)
            print(f"+{heal} HP")

    if hp <= 0:
        print("Zemřel jsi 💀")
        exit()


def crossroad():
    print("\n--- KŘIŽOVATKA ---")
    stats()

    print("1 - Trénink")
    print("2 - Krčma")
    print("3 - Souboj")
    print("4 - Les 🌲")
    print("5 - Konec")

    choice = safe_input()

    if choice == 1:
        training_course()
    elif choice == 2:
        tavern()
    elif choice == 3:
        real_fight()
    elif choice == 4:
        forest()
    elif choice == 5:
        print("Konec hry")
        stats()
        exit()


def main():
    welcome_screen()

    if safe_input() != 1:
        return

    while True:
        crossroad()


main()
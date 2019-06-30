class Game:

    def __init__(self):
        self.proc = 0
        self.crit = 100

    def normal(self):
        self.proc += 1

    def balance(self):
        return (self.proc + self.crit) / 2

    def bad_1(self):
        self.crit -= 1

    def good_1(self):
        self.proc += 1

    def good_2(self):
        self.proc += 1
        self.crit -= 1


game = Game()


while game.balance() > 0 or game.balance() < 70:
    print("\n")
    try:
        chos = int(input("1)Хорошо,2)Плохо или 3)Очень хорошо?:"))

    except ValueError as e:
        print("Error")
        continue
    game.normal()
    if chos == 1:
        game.good_1()
        print(game.proc)
        print(game.crit)
        print(game.balance())
    elif chos == 2:
        game.bad_1()
        print(game.proc)
        print(game.crit)
        print(game.balance())
    elif chos == 3:
        game.good_2()
        print(game.proc)
        print(game.crit)
        print(game.balance())
    if game.proc >= 100:
        print("Win")
        break
    elif game.balance() <= 30 or game.balance() >= 70:
        print("Lose")
        break
print("Hello Aziz 3")
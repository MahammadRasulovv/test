import math
import time


class DeveloperBrain:
    def __init__(self, coffee_cups: int):
        self.coffee_cups = coffee_cups
        self.energy = coffee_cups * 25

    def think_about_bugs(self):
        print(f"☕ {self.coffee_cups} fincan qəhvə qəbul edildi. Enerji səviyyəsi: {self.energy}%")
        time.sleep(0.5)

        if self.energy > 50:
            print("🚀 Beyin rejimdədir: Bütün xətalar tapılacaq və refactor olunacaq!")
        else:
            print("😴 DİQQƏT: Aşağı enerji! Koda toxunmayın, `print('test')` yazın və dincəlin.")


def calculate_programmer_logic(a, b):
    # PyCharm-da Reformat Code (Alt + Shift + F) yoxlamaq üçün bilərəkdən korlanmış girintilər:
    res = math.sqrt(a ** 2 + b ** 2)
    return res


if __name__ == "__main__":
    dev = DeveloperBrain(coffee_cups=3)
    dev.think_about_bugs()

    print(f"\n📐 Məntiqi hesablamanın nəticəsi: {calculate_programmer_logic(3, 4)}")


import random
import time

facts = [
    "PyCharm-da `Shift + Shift` sıxanda hər şey tapılır, amma itən corablar yox.",
    "Bütün proqramçılar `print('Bura gəldi')` yazaraq debug etməyə başlayır.",
    "Koddakı xəta 10 saat axtarılır, səbəb isə səhv yazılmış bircə hərf çıxır.",
    "İki növ insan var: Kodu formatlayanlar və `Alt + Shift + F` sıxanlar."
]


def generate_programmer_mood():
    status_list = [
        "Code compiled on first try (Mümkünsüz həzz)",
        "Fixing 1 bug -> Creating 5 new bugs",
        "Stack Overflow is down (Panika!)",
        "Git merge conflict (Dərin sükut)"
    ]
    return random.choice(status_list)


if __name__ == "__main__":
    print("🤖 PyCharm Test Tool v2.0 İşə Düşür...\n")
    time.sleep(0.5)

    print(f"💡 Günün Proqramçı Həqiqəti:\n -> {random.choice(facts)}\n")
    print(f"📊 Hazırkı Əhval-Ruhiyyə Statusu:\n -> {generate_programmer_mood()}")
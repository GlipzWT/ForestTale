"""
ForestTale
"""

import time
import sys
import os

# Цвета
C = {
    "reset": "\033[0m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "bold": "\033[1m",
    "dim": "\033[2m",
}


def col(text, color="white"):
    return f"{C.get(color, '')}{text}{C['reset']}"


def slow_print(text, delay=0.025, color=None, end=True):
    if color:
        text = col(text, color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if end:
        print()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(sec=1.0):
    time.sleep(sec)


def frame(text, color="yellow", width=52):
    """Рисует текст в красивой рамке."""
    clear()
    line = col("═" * width, color)
    print(line)
    # центрируем текст
    if len(text) < width:
        text = " " * ((width - len(text)) // 2) + text
    print(col(text, color))
    print(line)
    print()


def title_art():
    """ASCII-заставка с названием."""
    clear()
    art = [
        "     ╔═══════════════════════════════════════╗",
        "     ║                                       ║",
        "     ║   🌲  FORESTTALE  🌲                 ║",
        "     ║   ────  выбор меняет лес  ────       ║",
        "     ║                                       ║",
        "     ╚═══════════════════════════════════════╝",
        "",
        col("         нажми Enter, чтобы войти", "dim")
    ]
    for line in art:
        slow_print(col(line, "green"), delay=0.01)
    input()


# ------------- ИНВЕНТАРЬ -------------
class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        if len(self.items) < 3:
            self.items.append(item)
            return True
        return False

    def has(self, item):
        return item in self.items

    def use(self, item):
        if self.has(item):
            self.items.remove(item)
            return True
        return False

    def show(self):
        if not self.items:
            return "пусто"
        return ", ".join(self.items)


# ------------- ИГРОВЫЕ СЦЕНЫ -------------
def intro():
    title_art()
    frame("ДОБРО ПОЖАЛОВАТЬ В ЛЕС", "yellow")
    slow_print("Ты просыпаешься на мягком мху. Солнце пробивается сквозь листву.", color="white")
    pause(1)
    slow_print("Голос, похожий на шелест ветра:", color="magenta")
    slow_print("«Ты здесь... Давно никто не приходил. Будь внимателен к мелочам.»", color="magenta")
    pause(1)
    slow_print("\nПеред тобой появляется маленький светлячок по имени Эффи.", color="cyan")
    pause(0.5)


def meet_effie(inv):
    frame("ВСТРЕЧА С ЭФФИ", "cyan")
    slow_print("Эффи:", color="magenta")
    slow_print("«Привет! Я покажу тебе дорогу. Но лес проверяет сердце каждого.»", color="magenta")
    slow_print("«Вот возьми это на первое время.»", color="magenta")
    inv.add("Светлячок в банке")
    slow_print(col(f"[В инвентарь добавлен: Светлячок в банке]", "green"))
    pause(0.8)
    slow_print("\nТы благодаришь Эффи.", color="white")
    slow_print("Куда пойдёшь?", color="white")
    print(col("  1. На звук ручья", "cyan"))
    print(col("  2. К старому дубу", "green"))
    while True:
        ch = input("\n> ").strip()
        if ch == "1":
            return "stream"
        elif ch == "2":
            return "oak"
        # без сообщения об ошибке


def stream_scene(kindness, inv):
    frame("У РУЧЬЯ", "blue")
    slow_print("Ты видишь маленького ёжика, который не может перебраться через ручей.", color="white")
    slow_print("Ёжик:", color="yellow")
    slow_print("«Фыр... Помоги, добрый путник! Мои лапки коротки.»", color="yellow")
    print(col("  1. Построить мостик из веток (помочь)", "green"))
    print(col("  2. Пройти мимо", "red"))
    while True:
        ch = input("\n> ").strip()
        if ch == "1":
            slow_print("\nТы накидал веток — ёжик перебрался и подарил тебе лесную ягоду.", color="white")
            inv.add("Лесная ягода")
            slow_print(col("[Ягода добавлена в инвентарь]", "green"))
            kindness += 1
            break
        elif ch == "2":
            slow_print("\nТы уходишь, ёжик грустно вздыхает.", color="white")
            break
    return kindness


def oak_scene(kindness, inv):
    frame("У СТАРОГО ДУБА", "green")
    slow_print("Дуб шепчет скрипучим голосом:", color="yellow")
    slow_print("«Тот, кто разделит со мной печаль, получит дар.»", color="yellow")
    slow_print("Что ты ответишь?", color="white")
    print(col("  1. «Расскажи, я слушаю.»", "green"))
    print(col("  2. «Мне некогда.»", "red"))
    while True:
        ch = input("\n> ").strip()
        if ch == "1":
            slow_print("\nДуб рассказал историю о потерянном семечке.", color="yellow")
            slow_print("Ты посочувствовал, и дуб дал тебе светящийся лист.", color="white")
            inv.add("Светящийся лист")
            slow_print(col("[Лист добавлен в инвентарь]", "green"))
            kindness += 1
            break
        elif ch == "2":
            slow_print("\nДуб замолк, и ветер стал холоднее.", color="white")
            break
    return kindness


def lost_shadow(kindness, inv):
    frame("ПОТЕРЯННАЯ ТЕНЬ", "blue")
    slow_print("Из-за кустов выглядывает дрожащий комочек тьмы.", color="white")
    slow_print("Тень:", color="cyan")
    slow_print("«Я потерял свою звезду... Без неё я исчезну. Помоги!»", color="cyan")
    print(col("  1. Помочь найти звезду", "green"))
    print(col("  2. Игнорировать", "red"))
    while True:
        ch = input("\n> ").strip()
        if ch == "1":
            slow_print("\nТы нашёл звезду под листом. Тень радостно засиял и подарил тебе тёплый свет.", color="white")
            inv.add("Тёплый свет")
            slow_print(col("[Тёплый свет добавлен в инвентарь]", "green"))
            kindness += 1
            break
        elif ch == "2":
            slow_print("\nТень исчез, оставив после себя холод.", color="white")
            break
    return kindness


def final_judgment(kindness, inv):
    frame("ФИНАЛ", "magenta")
    slow_print("Ты выходишь на поляну. Перед тобой Дух Леса.", color="white")
    pause(0.5)
    slow_print("Дух:", color="magenta")
    slow_print("«Я видел твои поступки. А теперь покажи, что ты нёс в пути.»", color="magenta")

    # Возможность использовать предметы
    if inv.has("Тёплый свет"):
        slow_print("\nТы достаёшь Тёплый свет. Дух улыбается.", color="cyan")
        kindness += 1
    if inv.has("Лесная ягода"):
        slow_print("Ты предлагаешь Лесную ягоду. Дух благодарит.", color="green")
        kindness += 1

    pause(1)
    # Финальная речь
    if kindness >= 3:
        slow_print("\nДух сияет:", color="magenta")
        slow_print("«Твоё сердце полно света. Лес будет помнить тебя как Хранителя.»", color="magenta")
        frame("★ КОНЦОВКА: ХРАНИТЕЛЬ ЛЕСА ★", "yellow")
        slow_print("Ты чувствуешь, как силы леса текут сквозь тебя.", color="white")
    elif kindness == 2:
        slow_print("\nДух:", color="magenta")
        slow_print("«Ты был добр, но иногда сомневался. Этого достаточно.»", color="magenta")
        frame("✦ КОНЦОВКА: ДРУГ ЛЕСА ✦", "cyan")
        slow_print("Ты покидаешь лес с лёгким сердцем.", color="white")
    else:
        slow_print("\nДух грустит:", color="magenta")
        slow_print("«Ты прошёл мимо чужой боли. Лес не закроет врата, но даст тебе урок.»", color="magenta")
        frame("❀ КОНЦОВКА: ПЕРВЫЙ ШАГ ❀", "green")
        slow_print("Ты уходишь, обещая себе быть внимательнее.", color="white")

    slow_print(f"\nТвой инвентарь: {inv.show()}", color="dim")
    input(col("\n[Нажми Enter, чтобы завершить]", "dim"))


def play_again():
    print("\n")
    slow_print("Начать новое приключение?", color="white")
    print(col("  1. Да", "green"))
    print(col("  2. Выход", "yellow"))
    while True:
        ch = input("\n> ").strip()
        if ch == "1":
            return True
        elif ch == "2":
            return False


def main():
    while True:
        kindness = 0
        inv = Inventory()
        intro()
        # Первая развилка
        path = meet_effie(inv)
        if path == "stream":
            kindness = stream_scene(kindness, inv)
            # после ручья идём к дубу
            kindness = oak_scene(kindness, inv)
        else:
            kindness = oak_scene(kindness, inv)
            kindness = stream_scene(kindness, inv)
        # Встреча с тенью
        kindness = lost_shadow(kindness, inv)
        # Финальный суд
        final_judgment(kindness, inv)

        if not play_again():
            slow_print("\nСпасибо за игру! Пусть лес хранит тебя.", color="cyan")
            break
        clear()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        slow_print("\n\nДо встречи!", color="green")
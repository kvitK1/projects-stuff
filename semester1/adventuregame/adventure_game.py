#This Python file uses the following encoding: utf-8
import random
def main():
    """This function makes a game run"""
    ##### Player Setup #####
    print("Вибери свого гравця:")
    print("Сільванна: нащадок лісової феї,",
           "тому зберегла можливість літати за нагальної потреби.")
    print("Гендальф: практикувався у друїда,"
           " має деякі магічні штучки в запасі",
           " (камені для телепортації предметів).")
    player = ""
    while player != "Сільванна" or "Гендальф":
        print('Будь ласка, введіть обраного гравця :')
        player = input(">>> ")
        if player == "Сільванна":
            print("Сільванна, вперед!")
            break
        elif player == "Гендальф":
            print("Гендальф, вперед!")
            break
        elif player == "вийти":
            quit()

    def gendalf_attack():
        """Функція, що визначає можливість Гендальфа атакувати"""
        print("Ось що {} може зробити в цій ситуації: ".format(player))
        print("> вдарити")
        print("> кинути магічний камінь")
        gendalf_attack = ""
        while gendalf_attack != "вдарити" or "кинути магічний камінь":
            print("Будь ласка, обери, що будеш робити.")
            print("- у завданнях пиши з малої букви, де потрібно - число -")
            print("(введи: вдарити / кинути магічний камінь)")
            gendalf_attack = input(">>> ")
            if gendalf_attack == "вдарити":
                print("даремно, такого ворога кулаком не перемогти")
                quit()
            elif gendalf_attack == "кинути магічний камінь":
                print("Вийшло! Він зник, хоча у мене були сумніви,",
                      " що це спрацює.. Ну, гайда далі!")
                break
            elif gendalf_attack == "вийти":
                quit()

    def gendalf_run():
        """Функція, що визначає можливість Гендальфа втекти"""
        print("＼(º □ º l|l)/")
        print("Біжімо!")
        print(" ...")
        print("Напевно, варто піти іншою дорогою...")

    def silvanna_attack():
        """Функція, що визначає можливість Сільванни атакувати"""
        print("Ось що {} може зробити в цій ситуації: ".format(player))
        print("> вдарити")
        print("> взяти палку, що недалеко, й завдати турбо-удар")
        print("-- у завданнях пиши з маленької букви, де потрібно - число --")
        print("(щоб обрати, введи: вдарити / турбо-удар)")
        silvanna_attack = ""
        while silvanna_attack != "вдарити" or "турбо-удар":
            print("")
            silvanna_attack = input(">>> ")
            if silvanna_attack == "":
                continue
            elif silvanna_attack == "вдарити":
                print("даремно, такого ворога кулаком не перемогти")
                quit()
            elif silvanna_attack == "турбо-удар":
                print("Вийшло! Дивовижно, але вийшло. Час рухатися далі...")
                break
            elif silvanna_attack == "вийти":
                quit()

    def silvanna_magic():
        """Функція, що визначає можливість
        Сільванни використовувати свою силу"""
        print("Нагадаю, що {} вміє літати, тому,".format(player),
                " якщо знадобиться, можна спробувати")
        silvanna_choice = ""
        while silvanna_choice != "втекти" or "перелетіти":
            print("Що обереш, втекти звідси, поки не пізно,",
                  " чи спробувати дійти цим шляхом?")
            print("- у завданнях пиши з малої букви, де потрібно - число -")
            print("(щоб обрати, введи: втекти / перелетіти)")
            silvanna_choice = input(">>> ")
            if silvanna_choice == "":
                continue
            elif silvanna_choice == "втекти":
                print("＼(º □ º l|l)/")
                print("Біжімо!")
                print(" ...")
                print("Напевно, варто піти іншою дорогою...")
                break
            elif silvanna_choice == "перелетіти":
                print("Супер! У тебе вийшло, не зупиняйся!")
                break
            elif silvanna_choice  == "вийти":
                quit()

    ##### a stage of fight with evil goblin on the left road#####
    def second_left_stage():
        action = ""
        while action != "втекти" or action != "спробувати атакувати":
            print("Ти вже довго йдеш цією вузькою стежкою. Чим глибше в ліс,",
                  " тим страшніше й небезпечніше стає,",
                  " варто бути на поготові...")
            print("......")
            action = input(">>> натисни на enter...")
            print("Попереду! Здається, там лісовий гоблін...",
                  " Не з тих, кого хочеться зустрічати кожного дня...")
            print("GOBLIN")
            print("(‡▼益▼)")
            print("........")
            print("- у завданнях пиши з малої букви, де потрібно - число -")
            print("Що будеш робити? (введи: втекти / спробувати атакувати)")
            action = input(">>> ")
            if action == "":
                continue
            elif action == "втекти":
                if player == "Гендальф":
                    gendalf_run()
                if player == "Сільванна":
                    silvanna_magic()
                break
            elif action == "спробувати атакувати":
                print("Гаразд, сміливцю_вице")
                if player == "Гендальф":
                    gendalf_attack()
                elif player == "Сільванна":
                    silvanna_attack()
                elif player == "вийти":
                    quit()
                break
            elif action == "вийти":
                quit()

    questions_left = ["На дереві сиділо 6 горобців. Стрілець, " +
                      "вистріливши, влучив у двох з них. Скільки горобців" +
                      " залишилося на дереві?(ввести число)",
                      "Від якої тварини походить назва Канарських островів?",
                      "Із гнізда вилетіло 3 ластівки. Яка ймовірність того," +
                      " що через 15 секунд вони будуть в одній площині?" +
                      " (відповідь писати із знаком %)"]
    answers_left = ["0", "тюлень", "100%"]

    def left_path(count=1):
        for i in range(0, count):
            guesses = 3
            player_answer = ""
            questtion = random.choice(questions_left)
            num_of_questtion = questions_left.index(questtion)
            while player_answer != answers_left[num_of_questtion]:
                print(questions_left[num_of_questtion])
                print("Будь ласка, введи свою відповідь: ")
                player_answer = input(">>> ")
                if player_answer == answers_left[num_of_questtion]:
                    print("Так тримати, {}".format(player))
                    questions_left.pop(num_of_questtion)
                    answers_left.pop(num_of_questtion)
                    break
                if player_answer == "вийти":
                    quit()
                guesses -= 1
                if guesses == 0:
                    print("Вибач, не цього разу. Спробуй ще!")
                    quit()

    questions_right = ["Чим більше з неї береш, тим більша вона стає?",
                    "На вікні сидить кішка. І вуса, і шерсть, як у кішки," +
                    " але не кішка. Що це?",
                    "Що не може збільшити лупа у трикутнику?",
                    "У декількох столів 12 ніжок. Скільки столів у кімнаті?",
                    "Скільки разів можна від 100 відняти 10?"]
    answers_right = ["яма", "кіт", "кути", "декілька", "1"]

    def right_path(count=1):
        for i in range(0, count):
            guesses = 3
            player_answer = ""
            question = random.choice(questions_right)
            num_of_question = questions_right.index(question)
            while player_answer != answers_right[num_of_question]:
                print(questions_right[num_of_question])
                print("- у завданнях пиши з малої букви, де потрібно - число -")
                print("Будь ласка, введи свою відповідь: ")
                player_answer = input(">>> ")
                if player_answer == answers_right[num_of_question]:
                    print("Так тримати! Давай далі...")
                    questions_right.pop(num_of_question)
                    answers_right.pop(num_of_question)
                    break
                if player_answer == "вийти":
                    quit()
                guesses -= 1
                if guesses == 0:
                    print("Вибач, не цього разу. Спробуй ще!")
                    quit()

    treasure_list = ["Путівка у Глухів", "Посібник 'Python для чайників'",
                     "Творожні батончики з Сільпо", "Картка Local на -75%"]
    def treasure():
        treasure_choice = input(">>> натисни на enter...")
        print("....")
        print("Нарешті! Давай подивимося що ж у цій скрині...")
        treasure_choice = input(">>> натисни на enter...")
        print("{}, ось твоя нагорода (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧".format(player),
              "{}".format(random.choice(treasure_list)))
        print("Юхууу! Це кінець, заходь пограти ще...")
        if treasure_choice == "вийти":
            quit()

    def last_stage():
        player_act = ""
        while player_act != "1" or "2":
            print("Будь ласка, обери дерево, під яким доведеться копати?")
            print("введи: 1 / 2")
            player_act = input(">>> ")
            if player_act == "вийти":
                quit()
            elif player_act == "1":
                print(".....digging.....")
                player_act = input(">>> натисни на enter...")
                print(".....digging.....")
                player_act = input(">>> натисни на enter...")
                print("Я бачу скриню, ти знайшов_ла її! Нумо,",
                      " швидше діставай!")
                treasure()
                break
            elif player_act == "2":
                print(".....digging.....")
                player_act = input(">>> натисни на enter...")
                print("Я бачу скриню, ти знайшов_ла її! Нумо,",
                      " швидше діставай!")
                treasure()
                break

    def choose_your_road():
        road_choice = ""
        while road_choice != "наліво" or "направо":
            print("- у завданнях пиши з малої букви, де потрібно - число -")
            print("Будь ласка, обери, куди йдеш: (введи: наліво / направо)")
            road_choice = input(">>> ")
            if road_choice == "наліво":
                left_path()
                print("Молодець, ти вдало пройшов_ла цей етап!",
                      " Потрібно рухатися далі...")
                second_choice = input(">>> натисни на enter...")
                print("Ти вже доволі довго йдеш, навколо багато чого",
                      " цікавого й неможливо не відволікатися на щось ще...")
                print("......")
                print("Обережно! Звідки ж тут ця каменюка? "
                      "Прямо пройти не вийде...")
                second_choice = ""
                while True:
                    print("У тебе є вибір, обійти, проте витратити більше ",
                          "часу, чи спробувати перелізти?")
                    print("-- у завданнях пиши з маленької букви," 
                          " де потрібно - число --")
                    print("(введи: обійти / перелізти)")
                    second_choice = input(">>> ")
                    if second_choice == "обійти":
                        print("Тут ще глибші чагарники, але, потрібно ",
                              "йти вперед!")
                        print("Пам'ятай, що чим ближче до ночі, тим більша",
                              " ймовірність зустріти когось на своєму шляху!")
                        second_left_stage()
                        left_path(1)
                        print("Швидше проходь наступне завдання!Вже ",
                              "видніється потрібне дерево...")
                        left_path(1)
                        print("Здається, за довгий час тут виросло ще одне ",
                              "таке дерево. Доведеться знову обирати...")
                        last_stage()
                        break
                    elif second_choice == "перелізти":
                        print("О ні, здається ти зламав_ла ногу й не ",
                              "зможеш продовжити свої пошуки. ",
                              "Спробуй ще пізніше... ")
                        quit()
                    elif second_choice == "вийти":
                        quit()
                break

            if road_choice == "направо":
                right_path(4)
                print("Ще трохи, ти майже на фініші! Вже видніється",
                      " потрібне дерево...")
                right_path(1)
                print("Здається, за довгий час тут виросло ще ",
                      "одне таке дерево. Доведеться знову обирати...")
                last_stage()
                break
            if road_choice == "вийти":
                quit()

    ##### start your game #####
    starter_game = ""
    while starter_game != "так" or "ні":
        print("Ти не дуже славетний_а мандрівник_ця, але твої пригоди ",
              "не менш цікаві, ніж пригоди тореадорів з Васюківки.")
        print("Ось і зараз ти завітав_ла до незнайомого селища під",
              " темним лісом, що так і відштовхує, але шляху назад немає…")
        print("Люди тут відчужені й неприязні, а кава бридка й холодна.")
        print("Розглядаючи книги в місцевій бібліотеці, ти натрапляєш",
              " на дивне повідомлення, записане на форзаці однієї ",
              "з тих книг, яка чомусь не мала назви. ")
        print(".......")
        starter_game = input(">>> натисни на enter...")
        print("«Старий давно сундук сховав цей,")
        print("Та нікому не вдалось знайти.")
        print("Чи будеш ти першим, чи будеш як всі?")
        print("Не знаю, сходи перевір!")
        print("Де шлях на два розходиться, там все і починається,")
        print("Тож не марнуй ти часу i збирайся")
        print("На пошуки того, про що ще не здогадуєшся…»")
        print("Твоя ціль: йти вперд і тільки вперед, аж поки не знайдеш ",
              "високе переплетене дерево..")
        print("Під ним зможеш знайти скарб!")
        print("Можливо, це не якийсь жарт, і варто спробувати? Для такого_ї ",
              "мандрівника_ці це виклик, чи не так?")
        print("--- щоб вийти з гри, введи: вийти ---")
        print("-- у завданнях пиши з маленької букви, де потрібно - число --")
        print("--- пам'ятай: щоб вирішити завдання, ти маєш 3 спроби ---")
        print("Хочеш почати гру? (введи: так / ні)")
        starter_game = input(">>> ")
        if starter_game == "так":
            print("Вперед на пошуки, {}".format(player))
            print("Отже, перед тобою дороговказ. Потрібно обрати одну ",
                  "з двох доріг, якою піти... ")
            choose_your_road()
            break
        elif starter_game == "ні":
            quit()
        elif starter_game == "вийти":
            quit()
if __name__ == "__main__":
    main()

input_your_name = input("What is your name? ")
print("Hey", input_your_name,"!")


while True:
    try:
        age_request = float(input("What is your age? ")) ### ДОПИШИ КОД, ЧТОБЫ ЕСЛИ ЮЗЕР ВВЕДЕТ НЕ ЧИСЛО А БУКВЫ, ТО ПУСТЬ ВСЕ ВОЗВРАЩАЕТСЯ НАЗАД       (ВЫПОЛНЕНО)
        if age_request > 8:
            print("Good")
            break
        else:
            quit("You're too young")
    except ValueError: ###ЕСЛИ ЮЗЕР НАПИШЕТ ВМЕСТО ЧИСЕЛ БУКВЫ, ТО КОД ПОПРОСИТ ЕГО ВВЕСТИ ЧИСЛА
            print("Please use numbers")


def jumphere(): 
    print("Please choose and enter one of the following topics to start the test:")
    topics = ['Space', 'Computer science', 'Anatomy']
    for i in range(len(topics)):
        print(f"{i+1}. {topics[i]}")
    while True:
        choose_the_topic = input()
        if choose_the_topic.lower() in [topic.lower() for topic in topics]: #Если пользователь ответил с большими буквами, то оно преобразуется полностью в маленькие буквы и выдаст результат без ошибок
            break 
        else:
            print("Invalid topic selected. Please choose again.")

    print("Please select the dificulty:")
    difficulties = ['Easy', 'Medium', 'Hard']
    for i in range(len(difficulties)):
        print(f"{i+1}. {difficulties[i]}")
    while True:
        choose_the_difficulty = input()
        if choose_the_difficulty.lower() in [diffic.lower() for diffic in difficulties]:
            starting_the_test = print("Your selected topic is", choose_the_topic, "and difficulty", choose_the_difficulty + ".")
            print("If you want to abort the test, just type 'abort' at any time")
            break
        else:
            print("Invalid difficulty selected. Please choose again.")


    if choose_the_topic.lower() == ('space') and choose_the_difficulty.lower() == ('easy'):

        score = 0

        input('You\'ll be given 10 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')

        print("1. What planet is closest to the Sun?")
        question_1 = ['a) Venus', 'b) Mars', 'c) Jupiter', 'd) Mercury']
        for i in range(len(question_1)):
            print(question_1[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == ('d'):
                score +=1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("2. What is the only natural satellite of our planet?")
        question_2 = ['a) Moon', 'b) Phobos', 'c) Ganymede', 'd) Deimos']
        for i in range(len(question_2)):
            print(question_2[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score +=1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("3. Which planet is known as the red planet?")
        question_3 = ['a) Mars', 'b) Jupiter', 'c) Venus', 'd) Saturn']
        for i in range(len(question_3)):
            print(question_3[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == ('a'):
                score +=1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("4. What are asteroids?")
        question_4 = ['a) Small planets orbiting the Sun', 'b) Planets with rocky composition', 'c) Small, rocky objects that orbit the Sun', 'd) Chunks of ice moving in space']
        for i in range(len(question_4)):
            print(question_4[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == ('c'):
                score =+1 
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("5. What is the name of the closest star to Earth?")
        question_5 = ['a) Proxima Centauri', 'b) Alpha Centauri A', 'c) Alpha Centauri B', 'd) Sirius']
        for i in range(len(question_5)):
            print(question_5[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("6. What is the term used to describe a group of stars that form a recognizable pattern in the sky?")
        question_6 = ['a) Asterism', 'b) Constellation', 'c) Galaxy', 'd) Nebula']
        for i in range(len(question_6)):
            print(question_6[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("7. Do other planets have volcanos?")
        question_7 = ['a) Yes ', 'b) No']
        for i in range(len(question_7)):
            print(question_7[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b']:
                print("Please enter only one of the options (a or b).")
            else:
                break
            
        print("8. What is the name of the galaxy that contains our solar system?")
        question_8 = ['a) Whirlpool Galaxy', 'b) Andromeda Galaxy', 'c) Triangulum Galaxy', 'd) Milky Way Galaxy']
        for i in range(len(question_8)):
            print(question_8[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("9. What is the name of the spacecraft that carried the first humans to the moon?")
        question_9 = ['a) Voyager', 'b) Discovery', 'c) Apollo 11', 'd) Challenger']
        for i in range(len(question_9)):
            print(question_9[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("10. Who was the first human to walk on the moon?")
        question_10 = ['a) Louis Armstrong', 'b) Neil Armstrong', 'c) Buzz Aldrin', 'd) Yuri Gagarin']
        for i in range(len(question_10)):
            print(question_10[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please one letter only")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("Your total score is ", score, "out of 10")
        while True:
            yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
            if yes_or_no.lower() == 'y':
                jumphere() 
            elif yes_or_no.lower() == 'n':
                print("Thank you for taking the test. Goodbye!")
                quit()
            else:
                print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('space') and choose_the_difficulty.lower() == ('medium'):
            score = 0

            input('You\'ll be given 20 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')

            print("1. Which of the following stars is furthest from Earth?")
            question_1 = ['a) Sirius A', 'b) Alpha Centauri A', 'c) Betelgeuse', 'd) Proxima Centauri']
            for i in range(len(question_1)):
                print(question_1[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score +=1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please one letter only")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("2. What is the term for the theoretical boundary marking the edge of a black hole from which no light or radiation can escape?")
            question_2 = ['a) Singularity', 'b) Event horizon', 'c) Ergosphere', 'd) Photon sphere']
            for i in range(len(question_2)):
                print(question_2[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score +=1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please one letter only")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("3. Which spacecraft holds the record for the farthest distance from Earth?")
            question_3 = ['a) Juno', 'b) New Horizons', 'c) Cassini', 'd) Voyager 1']
            for i in range(len(question_3)):
                print(question_3[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'd':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("4. What is the approximate age of the universe, according to current scientific estimates?")
            question_4 = ['a) 10 billion years', 'b) 4.5 billion years', 'c) 13.8 billion years', 'd) 20 billion years']
            for i in range(len(question_4)):
                print(question_4[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("5. What is the name of the most massive known star in the universe?")
            question_5 = ['a) VY Canis Majoris', 'b) UY Scuti', 'c) Betelgeuse', 'd) Rigel']
            for i in range(len(question_5)):
                print(question_5[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("6. Which planet has the highest surface temperature in our solar system?")
            question_6 = ['a) Venus', 'b) Mercury', 'c) Mars', 'd) Jupiter']
            for i in range(len(question_6)):
                print(question_6[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("7. What is the name of the phenomenon where light from a distant object is bent by the gravitational field of a massive object between it and the observer?")
            question_7 = ['a) Gravitational lensing', 'b) Stellar occultation', 'c) Redshift', 'd) Dark matter']
            for i in range(len(question_7)):
                print(question_7[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("8. What is the name of the mission that provided evidence for the existence of water ice on the surface of the Moon?")
            question_8 = ['a) Chandrayaan-1', 'b) Luna 2', 'c) Apollo 11', 'd) Artemis']
            for i in range(len(question_8)):
                print(question_8[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("9. Which celestial object was the first to be visited by a spacecraft from Earth?")
            question_9 = ['a) Venus', 'b) Mars', 'c) Mercury', 'd) Moon']
            for i in range(len(question_9)):
                print(question_9[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'd':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("10. What is the term for a star that has collapsed under its own gravity and has a gravitational pull so strong that not even light can escape from it?")
            question_10 = ['a) Black hole', 'b) Neutron star', 'c) White dwarf', 'd) Red giant']
            for i in range(len(question_10)):
                print(question_10[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("11. What is the name of the spacecraft that observed the first evidence of liquid water on Mars?")
            question_11 = ['a) Mars Reconnaissance Orbiter', 'b) Viking 1', 'c) MAVEN', 'd) Mars Odyssey']
            for i in range(len(question_11)):
                print(question_11[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("12. What is the name of the first exoplanet ever discovered orbiting a main-sequence star similar to the Sun?")
            question_12 = ['a) 51 Pegasi b', 'b) HD 209458 b', 'c) Proxima Centauri b', 'd) Kepler-186f']
            for i in range(len(question_12)):
                print(question_12[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("13. What is the name of the phenomenon where a massive star collapses and explodes, releasing an immense amount of energy?")
            question_13 = ['a) Supernova', 'b) Hypernova', 'c) Nova', 'd) Pulsar']
            for i in range(len(question_13)):
                print(question_13[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("14. Which moon of Jupiter is considered to be the most likely candidate for hosting extraterrestrial life?")
            question_14 = ['a) Europa', 'b) Ganymede', 'c) Callisto', 'd) Io']
            for i in range(len(question_14)):
                print(question_14[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("15. What is the term for the boundary that separates the Earth's atmosphere from outer space?")
            question_15 = ['a) Kármán line', 'b) Tropopause', 'c) Thermosphere', 'd) Mesopause']
            for i in range(len(question_15)):
                print(question_15[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("16. Which spacecraft discovered the first evidence of organic molecules on Saturn's moon Titan?")
            question_16 = ['a) Cassini-Huygens', 'b) Voyager 1', 'c) Galileo', 'd) New Horizons']
            for i in range(len(question_16)):
                print(question_16[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("17. What is the name of the phenomenon where a small astronomical object passes in front of a larger one, causing the larger object to partially or fully disappear from view?")
            question_17 = ['a) Transit', 'b) Occultation', 'c) Eclipse', 'd) Conjunction']
            for i in range(len(question_17)):
                print(question_17[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("18. What is the name of the spacecraft that successfully landed on the surface of a comet in 2014?")
            question_18 = ['a) Philae', 'b) Stardust', 'c) Rosetta', 'd) Deep Impact']
            for i in range(len(question_18)):
                print(question_18[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("19. Which galaxy is the closest to the Milky Way?")
            question_19 = ['a) Andromeda', 'b) Triangulum', 'c) Sculptor', 'd) Large Magellanic Cloud']
            for i in range(len(question_19)):
                print(question_19[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("20. What is the name of the mission that successfully landed the Perseverance rover on Mars in 2021?")
            question_20 = ['a) InSight', 'b) ExoMars', 'c) Tianwen-1', 'd) Mars 2020 Mission']
            for i in range(len(question_20)):
                print(question_20[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'd':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("Your total score is ", score, "out of 20")

            while True:
                yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
                if yes_or_no.lower() == 'y':
                    jumphere() 
                elif yes_or_no.lower() == 'n':
                    print("Thank you for taking the test. Goodbye!")
                    quit()
                else:
                    print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('space') and choose_the_difficulty.lower() == ('hard'):
        score = 0

        input('You\'ll be given 30 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')

        print("1. What is the approximate distance between the Earth and the edge of the observable universe?")
        question_1 = ['a) 4.5 billion light-years', 'b) 1 trillion light-years', 'c) 13.8 billion light-years', 'd) 93 million light-years']
        for i in range(len(question_1)):
            print(question_1[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n2. Which of Jupiter's moons is known for its subsurface ocean that could potentially harbor life?")
        question_2 = ['a) Ganymede', 'b) Europa', 'c) Callisto', 'd) Io']
        for i in range(len(question_2)):
            print(question_2[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n3. What is the name of the phenomenon where a massive star collapses under its gravity, forming a neutron star or black hole?")
        question_3 = ['a) Hypernova', 'b) Supernova', 'c) Quasar', 'd) Nova']
        for i in range(len(question_3)):
            print(question_3[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n4. Which planet in our solar system experiences the strongest winds, reaching speeds of up to 1,500 miles per hour (2,400 kilometers per hour)?")
        question_4 = ['a) Saturn', 'b) Jupiter', 'c) Neptune', 'd) Uranus']
        for i in range(len(question_4)):
            print(question_4[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n5. What is the term for the process by which a black hole emits radiation due to quantum effects near its event horizon?")
        question_5 = ['a) Hawking radiation', 'b) Gamma-ray burst', 'c) X-ray emission', 'd) Gravitational lensing']
        for i in range(len(question_5)):
            print(question_5[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n6. Which space mission discovered the first exoplanet orbiting a Sun-like star?")
        question_6 = ['a) Spitzer Space Telescope', 'b) Gaia Space Telescope', 'c) Kepler Space Telescope', 'd) Hubble Space Telescope']
        for i in range(len(question_6)):
            print(question_6[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n7. What is the name of the space probe launched by NASA in 1977 that has now entered interstellar space?")
        question_7 = ['a) Voyager 2', 'b) Pioneer 11', 'c) Voyager 1', 'd) Pioneer 10']
        for i in range(len(question_7)):
            print(question_7[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n8. Which type of galaxy has a distinct, flattened disk, and a prominent central bulge surrounded by a halo of stars?")
        question_8 = ['a) Lenticular galaxy', 'b) Spiral galaxy', 'c) Irregular galaxy', 'd) Elliptical galaxy']
        for i in range(len(question_8)):
            print(question_8[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n9. What is the name of the region around a black hole where the gravitational pull is so strong that not even light can escape?")
        question_9 = ['a) Singularity', 'b) Event horizon', 'c) Ergosphere', 'd) Accretion disk']
        for i in range(len(question_9)):
            print(question_9[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n10. Which planet's atmosphere consists mainly of methane, giving it a bluish-green color?")
        question_10 = ['a) Neptune', 'b) Jupiter', 'c) Saturn', 'd) Uranus']
        for i in range(len(question_10)):
            print(question_10[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n11. What is the term for the process by which two neutron stars merge, releasing a tremendous amount of energy?")
        question_11 = ['a) Hypernova', 'b) Kilonova', 'c) Supernova', 'd) Quasar']
        for i in range(len(question_11)):
            print(question_11[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n12. What is the name of the most massive known black hole in the universe, located in the center of the galaxy M87?")
        question_12 = ['a) V404 Cygni', 'b) Cygnus X-1', 'c) Sagittarius A*', 'd) Messier 87*']
        for i in range(len(question_12)):
            print(question_12[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n13. Which of Saturn's moons has a thick atmosphere composed mainly of nitrogen and methane?")
        question_13 = ['a) Enceladus', 'b) Titan', 'c) Mimas', 'd) Dione']
        for i in range(len(question_13)):
            print(question_13[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n14. What is the name of the boundary in space beyond which the Sun's influence diminishes and interstellar space begins?")
        question_14 = ['a) Termination shock', 'b) Heliopause', 'c) Bow shock', 'd) Magnetopause']
        for i in range(len(question_14)):
            print(question_14[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n15. Which spacecraft conducted the first-ever flyby of Pluto and its moons in 2015?")
        question_15 = ['a) Rosetta', 'b) Dawn', 'c) Cassini', 'd) New Horizons']
        for i in range(len(question_15)):
            print(question_15[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n16. What is the name of the process by which a star's core collapses and rebounds, expelling its outer layers into space?")
        question_16 = ['a) Red giant phase', 'b) Planetary nebula formation', 'c) Core collapse supernova', 'd) Stellar accretion']
        for i in range(len(question_16)):
            print(question_16[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n17. What is the name of the mission that discovered evidence of water molecules on the Moon's surface in 2009?")
        question_17 = ['a) Luna 2', 'b) Clementine', 'c) Artemis', 'd) Chandrayaan-1']
        for i in range(len(question_17)):
            print(question_17[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n18. Which type of galaxy has an irregular shape and lacks a distinct structure?")
        question_18 = ['a) Spiral galaxy', 'b) Lenticular galaxy', 'c) Elliptical galaxy', 'd) Irregular galaxy']
        for i in range(len(question_18)):
            print(question_18[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n19. What is the name of the spacecraft that successfully landed on Mars in 2012 and discovered evidence of past water activity?")
        question_19 = ['a) Curiosity', 'b) Opportunity', 'c) Spirit', 'd) Perseverance']
        for i in range(len(question_19)):
            print(question_19[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n20. Which of the following objects is not considered a dwarf planet?")
        question_20 = ['a) Haumea', 'b) Sedna', 'c) Ceres', 'd) Eris']
        for i in range(len(question_20)):
            print(question_20[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n21. What is the name of the process by which two stars orbit around a common center of mass?")
        question_21 = ['a) White dwarf cooling', 'b) Binary star system', 'c) Neutron star formation', 'd) Stellar accretion']
        for i in range(len(question_21)):
            print(question_21[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n22. Which planet has the highest mountain in the Solar System, Olympus Mons?")
        question_22 = ['a) Earth', 'b) Mercury', 'c) Venus', 'd) Mars']
        for i in range(len(question_22)):
            print(question_22[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n23. What is the name of the region in space where the solar wind interacts with the interstellar medium?")
        question_23 = ['a) Termination shock', 'b) Magnetopause', 'c) Heliopause', 'd) Bow shock']
        for i in range(len(question_23)):
            print(question_23[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n24. What is the name of the process by which a massive star collapses directly into a black hole without a supernova explosion?")
        question_24 = ['a) Gamma-ray burst', 'b) Quasar ignition', 'c) Direct collapse', 'd) Black hole formation']
        for i in range(len(question_24)):
            print(question_24[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n25. Which of Jupiter's moons is the most volcanically active object in the Solar System?")
        question_25 = ['a) Ganymede', 'b) Europa', 'c) Callisto', 'd) Io']
        for i in range(len(question_25)):
            print(question_25[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n26. What is the name of the spacecraft that collected samples from the asteroid Ryugu and returned them to Earth in 2020?")
        question_26 = ['a) OSIRIS-REx', 'b) Hayabusa', 'c) Dawn', 'd) Rosetta']
        for i in range(len(question_26)):
            print(question_26[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n27. What is the name of the theory that suggests the universe underwent a rapid expansion just after the Big Bang?")
        question_27 = ['a) Steady-state theory', 'b) Multiverse theory', 'c) Oscillating universe theory', 'd) Inflation theory']
        for i in range(len(question_27)):
            print(question_27[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n28. Which planet has the most eccentric orbit, meaning its distance from the Sun varies significantly during its orbit?")
        question_28 = ['a) Mars', 'b) Venus', 'c) Pluto', 'd) Mercury']
        for i in range(len(question_28)):
            print(question_28[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n29. What is the name of the mission that successfully landed the first humans on the Moon in 1969?")
        question_29 = ['a) Vostok 1', 'b) Gemini 4', 'c) Mercury-Redstone 3', 'd) Apollo 11']
        for i in range(len(question_29)):
            print(question_29[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("\n30. What is the name of the process by which a star's core collapses under gravity, causing its outer layers to be expelled into space in a violent explosion?")
        question_30 = ['a) Kilonova', 'b) Hypernova', 'c) Supernova', 'd) Nova']
        for i in range(len(question_30)):
            print(question_30[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("Your total score is ", score, "out of 30")

        while True:
            yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
            if yes_or_no.lower() == 'y':
                jumphere() 
            elif yes_or_no.lower() == 'n':
                print("Thank you for taking the test. Goodbye!")
                quit()
            else:
                print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('Computer science') and choose_the_difficulty.lower() == ('easy'):
        input('You\'ll be given 10 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')
        score = 0

        print("1. What does HTML stand for?")
        question_1 = ['a) High Tech Machine Learning', 'b) Hyper Text Markup Language', 'c) Home Tool Management Logic', 'd) Halt Transmission Master List']
        for i in range(len(question_1)):
            print(question_1[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n2. Which programming language is often used for web development?")
        question_2 = ['a) ruby', 'b) python', 'c) java', 'd) javascript']
        for i in range(len(question_2)):
            print(question_2[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n3. What is the purpose of a loop in programming?")
        question_3 = ['a) To repeat a block of code', 'b) To stop the program', 'c) To create graphics', 'd) To display errors']
        for i in range(len(question_3)):
            print(question_3[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n4. What does CPU stand for?")
        question_4 = ['a) Central Processing Unit', 'b) Central Programmatic Unit', 'c) Control Panel Utility', 'd) Computer Power Unit']
        for i in range(len(question_4)):
            print(question_4[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n5. What is the file extension for a Python source code file?")
        question_5 = ['a) .txt', 'b) .exe', 'c) .py', 'd) .doc']
        for i in range(len(question_5)):
            print(question_5[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n6. Which data type is used to store a single character in Python?")
        question_6 = ['a) string', 'b) bool', 'c) int', 'd) char']
        for i in range(len(question_6)):
            print(question_6[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n7. What does CSS stand for in web development?")
        question_7 = ['a) Computer Style Sheets', 'b) Code Style System', 'c) Creative Scripting Styles', 'd) Cascading Style Sheets']
        for i in range(len(question_7)):
            print(question_7[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n8. Which of the following is not a type of computer memory?")
        question_8 = ['a) RAM', 'b) CPU', 'c) Cache', 'd) ROM']
        for i in range(len(question_8)):
            print(question_8[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n9. What does GUI stand for?")
        question_9 = ['a) Gaming Unit Integration', 'b) Graphical User Interface', 'c) Global User Integration', 'd) General Utility Interface']
        for i in range(len(question_9)):
            print(question_9[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n10. Which of the following is a relational database management system?")
        question_10 = ['a) Redis', 'b) Memcached', 'c) SQLite', 'd) MongoDB']
        for i in range(len(question_10)):
            print(question_10[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\nYour score is:", score, "out of 10")

        while True:
            yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
            if yes_or_no.lower() == 'y':
                jumphere() 
            elif yes_or_no.lower() == 'n':
                print("Thank you for taking the test. Goodbye!")
                quit()
            else:
                print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('Computer science') and choose_the_difficulty.lower() == ('medium'):
        input('You\'ll be given 20 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')
        score = 0

        print("1. Which of the following is a feature of functional programming?")
        question_1 = ['a) Mutable state', 'b) Side effects', 'c) Immutable data', 'd) Tight coupling']
        for i in range(len(question_1)):
            print(question_1[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n2. What is the purpose of a virtual function in C++?")
        question_2 = ['a) It allows a class to have multiple constructors', 'b) It allows a derived class to override a function in the base class', 'c) It enables dynamic memory allocation', 'd) It allows for operator overloading']
        for i in range(len(question_2)):
            print(question_2[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n3. Which of the following is NOT a valid HTTP request method?")
        question_3 = ['a) POST', 'b) PUT', 'c) DELETE', 'd) READ']
        for i in range(len(question_3)):
            print(question_3[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n4. What is the purpose of the 'finally' block in a try-except statement in Python?")
        question_4 = ['a) It must always execute regardless of whether an exception occurs', 'b) It only executes if an exception occurs', 'c) It only executes if no exception occurs', 'd) It is used to raise a specific exception']
        for i in range(len(question_4)):
            print(question_4[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n5. In relational database terminology, what is a foreign key?")
        question_5 = ['a) A key that uniquely identifies each row in a table', 'b) A key that is used for indexing', 'c) A key that references the primary key in another table', 'd) A key that ensures data integrity within a single table']
        for i in range(len(question_5)):
            print(question_5[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n6. Which of the following is NOT a valid method of handling concurrency in Python?")
        question_6 = ['a) Threading', 'b) Multiprocessing', 'c) Asynchronous programming', 'd) Coroutines']
        for i in range(len(question_6)):
            print(question_6[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n7. What is the primary purpose of an index in a database?")
        question_7 = ['a) To sort the data in a table', 'b) To encrypt sensitive information', 'c) To optimize query performance', 'd) To enforce data integrity constraints']
        for i in range(len(question_7)):
            print(question_7[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n8. Which of the following is true about Big O notation?")
        question_8 = ['a) It describes the exact running time of an algorithm', 'b) It provides an upper bound on the growth rate of an algorithm', 'c) It is only applicable to sorting algorithms', 'd) It measures the memory usage of an algorithm']
        for i in range(len(question_8)):
            print(question_8[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n9. What is the purpose of a destructor in C++?")
        question_9 = ['a) To create a new instance of a class', 'b) To free up resources allocated by an object before it is destroyed', 'c) To initialize the attributes of an object', 'd) To perform type conversion']
        for i in range(len(question_9)):
            print(question_9[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n10. What is a race condition in concurrent programming?")
        question_10 = ["a) When two or more processes or threads try to modify shared data at the same time", "b) When a program executes too slowly", "c) When a program encounters a segmentation fault", "d) When a program exceeds its allocated memory limit"]
        for i in range(len(question_10)):
            print(question_10[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("11. Which of the following is NOT a valid type of SQL injection attack?")
        question_11 = ['a) Union-based SQL injection', 'b) Time-based SQL injection', 'c) Buffer overflow SQL injection', 'd) Blind SQL injection']
        for i in range(len(question_11)):
            print(question_11[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n12. What is the purpose of a 'yield' statement in Python?")
        question_12 = ['a) To terminate a loop', 'b) To pause a function\'s execution and return a value to the caller', 'c) To raise an exception', 'd) To import a module']
        for i in range(len(question_12)):
            print(question_12[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n13. In object-oriented programming, what is inheritance?")
        question_13 = ['a) The process of hiding the implementation details of a class', 'b) The process of creating a new class from an existing class', 'c) The process of overloading operators', 'd) The process of implementing multiple interfaces']
        for i in range(len(question_13)):
            print(question_13[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n14. What does RAID stand for in computer storage?")
        question_14 = ['a) Random Access In-memory Disk', 'b) Redundant Array of Independent Disks', 'c) Read Asynchronous Integrated Data', 'd) Rapid Access In-memory Drive']
        for i in range(len(question_14)):
            print(question_14[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n15. What is the purpose of the 'self' keyword in Python class methods?")
        question_15 = ['a) It refers to the class itself', 'b) It refers to the parent class', 'c) It refers to the current instance of the class', 'd) It refers to the global namespace']
        for i in range(len(question_15)):
            print(question_15[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n16. Which of the following is NOT a valid type of graph in graph theory?")
        question_16 = ['a) Directed graph', 'b) Weighted graph', 'c) Binary graph', 'd) Bipartite graph']
        for i in range(len(question_16)):
            print(question_16[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n17. What is the purpose of the 'super' keyword in Python?")
        question_17 = ['a) It is used to call a method from the superclass', 'b) It is used to declare a variable as a superclass', 'c) It is used to stop execution of a loop', 'd) It is used to define a subclass']
        for i in range(len(question_17)):
            print(question_17[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n18. Which of the following is NOT a valid type of software testing?")
        question_18 = ['a) Unit testing', 'b) Integration testing', 'c) Abstraction testing', 'd) Regression testing']
        for i in range(len(question_18)):
            print(question_18[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n19. What is the purpose of a cache in computer architecture?")
        question_19 = ['a) To store frequently accessed data for faster access', 'b) To prevent unauthorized access to data', 'c) To compress data for efficient storage', 'd) To encrypt sensitive information']
        for i in range(len(question_19)):
            print(question_19[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n20. What does SIMD stand for in parallel computing?")
        question_20 = ['a) Single In-line Memory Data', 'b) Simple Instruction Memory Design', 'c) Single Instruction, Multiple Data', 'd) Serial Input, Multiple Data']
        for i in range(len(question_20)):
            print(question_20[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break


        print("\nYour score is:", score, "out of 20")

        while True:
            yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
            if yes_or_no.lower() == 'y':
                jumphere() 
            elif yes_or_no.lower() == 'n':
                print("Thank you for taking the test. Goodbye!")
                quit()
            else:
                print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('Computer science') and choose_the_difficulty.lower() == ('hard'):
        input('You\'ll be given 30 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')
        score = 0

        print("1. What is the difference between a process and a thread in an operating system?")
        question_1 = ['a) A process shares memory space with other processes, while a thread has its own memory space.',
                      'b) A thread is managed by the scheduler, while a process is managed by the kernel.',
                      'c) A thread can execute multiple tasks simultaneously, while a process can only execute one task at a time.',
                      'd) A process is a program in execution, while a thread is a subset of a process.']
        for i in range(len(question_1)):
            print(question_1[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n2. Explain the concept of deadlock in operating systems.")
        question_2 = ['a) Deadlock occurs when a process holds resources and waits for another process to release resources.',
                      'b) Deadlock occurs when two or more processes are waiting indefinitely for resources held by each other.',
                      'c) Deadlock occurs when a process enters an infinite loop, consuming all CPU resources.',
                      'd) Deadlock occurs when a process consumes excessive memory, causing the system to halt.']
        for i in range(len(question_2)):
            print(question_2[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n3. What is the difference between binary search tree (BST) and AVL tree?")
        question_3 = ['a) BST guarantees that the tree is always balanced, while AVL tree does not.',
                      'b) BST has a constant time complexity for insertion and deletion, while AVL tree has a logarithmic time complexity.',
                      'c) AVL tree allows duplicate values, while BST does not.',
                      'd) AVL tree is a self-balancing binary search tree, whereas BST may become unbalanced.']
        for i in range(len(question_3)):
            print(question_3[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n4. Explain the concept of polymorphism in object-oriented programming.")
        question_4 = ['a) Polymorphism allows objects of different classes to be treated as objects of the same class.',
                      'b) Polymorphism allows a class to inherit attributes and methods from multiple classes.',
                      'c) Polymorphism allows a single function or method to operate on different types of data.',
                      'd) Polymorphism allows a class to have multiple constructors with different parameters.']
        for i in range(len(question_4)):
            print(question_4[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n5. What is the difference between a compiler and an interpreter?")
        question_5 = ['a) A compiler directly executes code, while an interpreter translates code into an intermediate form.',
                      'b) A compiler is faster than an interpreter in executing code.',
                      'c) A compiler translates high-level code into machine code, while an interpreter executes code line by line.',
                      'd) A compiler is platform-independent, while an interpreter is platform-dependent.']
        for i in range(len(question_5)):
            print(question_5[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n6. Explain the concept of dynamic programming.")
        question_6 = ['a) Dynamic programming is a technique for solving problems by using mathematical formulas to derive the solution.',
                      'b) Dynamic programming is a technique for solving problems by breaking them down into smaller subproblems and solving each subproblem only once.',
                      'c) Dynamic programming is a technique for solving problems by exploring all possible solutions exhaustively.',
                      'd) Dynamic programming is a technique for solving problems by using recursion.']
        for i in range(len(question_6)):
            print(question_6[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n7. What is the purpose of the OSI model in computer networks?")
        question_7 = ['a) The OSI model provides a framework for understanding how data is transmitted over a network.',
                      'b) The OSI model specifies the protocols used for wireless communication.',
                      'c) The OSI model defines the architecture of the Internet.',
                      'd) The OSI model ensures secure communication between devices on a network.']
        for i in range(len(question_7)):
            print(question_7[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n8. Explain the concept of pipelining in computer architecture.")
        question_8 = ['a) Pipelining is a technique for improving processor performance by overlapping the execution of multiple instructions.',
                      'b) Pipelining is a technique for reducing latency in memory access.',
                      'c) Pipelining is a technique for encrypting data transmitted over a network.',
                      'd) Pipelining is a technique for compressing data for efficient storage.']
        for i in range(len(question_8)):
            print(question_8[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n9. What is the difference between HTTP and HTTPS?")
        question_9 = ['a) HTTP is a secure protocol, while HTTPS is not.',
                      'b) HTTP uses port 80 for communication, while HTTPS uses port 443.',
                      'c) HTTP is a stateless protocol, while HTTPS is a stateful protocol.',
                      'd) HTTP encrypts data transmitted between the client and server, while HTTPS does not.']
        for i in range(len(question_9)):
            print(question_9[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n10. Explain the concept of Moore's Law.")
        question_10 = ['a) Moore\'s Law states that the cost of computer hardware decreases exponentially over time.',
                       'b) Moore\'s Law states that the speed of computer networks increases linearly over time.',
                       'c) Moore\'s Law states that the processing power of computers doubles every 18 months.',
                       'd) Moore\'s Law states that the number of transistors on integrated circuits doubles approximately every two years.']
        for i in range(len(question_10)):
            print(question_10[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n11. What is the purpose of the CAP theorem in distributed systems?")
        question_11 = ['a) The CAP theorem provides guidelines for designing fault-tolerant distributed systems.',
                       'b) The CAP theorem ensures that distributed systems remain consistent and available.',
                       'c) The CAP theorem states that a distributed system cannot simultaneously guarantee consistency, availability, and partition tolerance.',
                       'd) The CAP theorem specifies the maximum latency allowed in distributed systems.']
        for i in range(len(question_11)):
            print(question_11[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n12. Explain the concept of virtual memory in operating systems.")
        question_12 = ['a) Virtual memory prevents unauthorized access to memory by isolating processes.',
                       'b) Virtual memory allows processes to directly access hardware resources.',
                       'c) Virtual memory extends the available physical memory by using disk space as an overflow.',
                       'd) Virtual memory allows multiple processes to share physical memory.']
        for i in range(len(question_12)):
            print(question_12[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n13. What is the purpose of the TCP/IP protocol suite?")
        question_13 = ['a) The TCP/IP protocol suite defines the rules for data transmission over the Internet.',
                       'b) The TCP/IP protocol suite governs the allocation of IP addresses to devices on a network.',
                       'c) The TCP/IP protocol suite provides a framework for securing network communications.',
                       'd) The TCP/IP protocol suite specifies the hardware requirements for network devices.']
        for i in range(len(question_13)):
            print(question_13[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n14. Explain the concept of a Bloom filter.")
        question_14 = ['a) A Bloom filter is a cryptographic algorithm used for secure communication.',
                       'b) A Bloom filter is a data structure used to test the membership of an element in a set.',
                       'c) A Bloom filter is a sorting algorithm used to arrange elements in ascending order.',
                       'd) A Bloom filter is a compression algorithm used to reduce the size of data.']
        for i in range(len(question_14)):
            print(question_14[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n15. What is the purpose of a heap data structure?")
        question_15 = ['a) A heap is used to store key-value pairs in sorted order.',
                       'b) A heap is used to allocate memory dynamically.',
                       'c) A heap is used to implement priority queues.',
                       'd) A heap is used to perform arithmetic operations efficiently.']
        for i in range(len(question_15)):
            print(question_15[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n16. Explain the concept of deep learning.")
        question_16 = ['a) Deep learning is a supervised learning technique that uses decision trees to classify data.',
                       'b) Deep learning is a machine learning technique that uses neural networks with multiple layers to extract features from data.',
                       'c) Deep learning is a reinforcement learning technique that uses rewards to train agents.',
                       'd) Deep learning is an unsupervised learning technique that uses clustering algorithms to group similar data.']
        for i in range(len(question_16)):
            print(question_16[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n17. What is the purpose of Docker in software development?")
        question_17 = ['a) Docker is a virtualization platform used to run multiple operating systems on a single host.',
                       'b) Docker is a version control system used to track changes in software projects.',
                       'c) Docker is a continuous integration tool used to automate software testing.',
                       'd) Docker is a containerization platform used to package and deploy applications with their dependencies.']
        for i in range(len(question_17)):
            print(question_17[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n18. Explain the concept of quantum computing.")
        question_18 = ['a) Quantum computing is a networking protocol used to connect devices wirelessly.',
                       'b) Quantum computing is a compression algorithm used to reduce the size of data.',
                       'c) Quantum computing is a computing paradigm that uses quantum bits (qubits) to perform computations.',
                       'd) Quantum computing is a cryptographic technique used for secure communication.']
        for i in range(len(question_18)):
            print(question_18[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n19. What is the purpose of MapReduce in distributed computing?")
        question_19 = ['a) MapReduce is a programming model used to process large datasets in parallel across a distributed cluster of computers.',
                       'b) MapReduce is a load balancing technique used to evenly distribute tasks among nodes in a distributed system.',
                       'c) MapReduce is a routing algorithm used to optimize network traffic in distributed systems.',
                       'd) MapReduce is a security protocol used to prevent unauthorized access to distributed resources.']
        for i in range(len(question_19)):
            print(question_19[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n20. Explain the concept of quantum teleportation in quantum computing.")
        question_20 = ['a) Quantum teleportation is a process of transferring quantum information from one qubit to another over large distances.',
                       'b) Quantum teleportation is a process of entangling two qubits to create a shared quantum state.',
                       'c) Quantum teleportation is a process of instantly transmitting classical information between two distant locations.',
                       'd) Quantum teleportation is a process of cloning quantum states to create multiple identical copies.']
        for i in range(len(question_20)):
            print(question_20[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n21. What is the purpose of a Bloom filter in database systems?")
        question_21 = ['a) A Bloom filter is used to speed up database queries by caching frequently accessed data.',
                       'b) A Bloom filter is used to filter malicious traffic from entering a network.',
                       'c) A Bloom filter is used to identify and eliminate duplicate records in a database.',
                       'd) A Bloom filter is used to index data for efficient retrieval.']
        for i in range(len(question_21)):
            print(question_21[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n22. Explain the concept of the Halting problem in computability theory.")
        question_22 = ['a) The Halting problem states that it is impossible to determine whether a given program will halt or run forever.',
                       'b) The Halting problem states that there exists an algorithm that can solve any computational problem.',
                       'c) The Halting problem states that every computable function can be represented as an algorithm.',
                       'd) The Halting problem states that there exists a universal Turing machine that can simulate any other Turing machine.']
        for i in range(len(question_22)):
            print(question_22[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n23. What is the purpose of the A* algorithm in artificial intelligence?")
        question_23 = ['a) The A* algorithm is used to perform automated planning in robotics.',
                       'b) The A* algorithm is used to learn patterns from data in machine learning.',
                       'c) The A* algorithm is used to search for the shortest path in a graph.',
                       'd) The A* algorithm is used to generate natural language text in natural language processing.']
        for i in range(len(question_23)):
            print(question_23[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n24. Explain the concept of big O notation in computer science.")
        question_24 = ['a) Big O notation is used to measure the amount of data stored in a database.',
                       'b) Big O notation is used to analyze the performance of algorithms in terms of their time and space complexity.',
                       'c) Big O notation is used to represent the number of iterations in a loop.',
                       'd) Big O notation is used to define the maximum size of an array.']
        for i in range(len(question_24)):
            print(question_24[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n25. What is the purpose of the OAuth protocol?")
        question_25 = ['a) The OAuth protocol is used for encrypting data transmitted over a network.',
                       'b) The OAuth protocol is used for secure authentication and authorization of users.',
                       'c) The OAuth protocol is used for compressing data for efficient storage.',
                       'd) The OAuth protocol is used for balancing load across multiple servers.']
        for i in range(len(question_25)):
            print(question_25[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n26. Explain the concept of blockchain technology.")
        question_26 = ['a) Blockchain technology is a distributed database that maintains a continuously growing list of records called blocks.',
                       'b) Blockchain technology is a machine learning algorithm used for predicting future trends from historical data.',
                       'c) Blockchain technology is a compression algorithm used to reduce the size of data.',
                       'd) Blockchain technology is a networking protocol used for peer-to-peer file sharing.']
        for i in range(len(question_26)):
            print(question_26[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n27. What is the purpose of the RSA algorithm in cryptography?")
        question_27 = ['a) The RSA algorithm is used for generating random numbers for cryptographic purposes.',
                       'b) The RSA algorithm is used for symmetric encryption of data.',
                       'c) The RSA algorithm is used for public-key encryption and digital signatures.',
                       'd) The RSA algorithm is used for compressing data for efficient storage.']
        for i in range(len(question_27)):
            print(question_27[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n28. Explain the concept of quantum supremacy in quantum computing?")
        question_28 = ['a) Quantum supremacy refers to the ability of a quantum computer to outperform classical computers for certain tasks.',
                       'b) Quantum supremacy refers to the ability of a classical computer to simulate quantum algorithms efficiently.',
                       'c) Quantum supremacy refers to the ability of a classical computer to factor large prime numbers.',
                       'd) Quantum supremacy refers to the ability of a quantum computer to solve NP-complete problems in polynomial time.']
        for i in range(len(question_28)):
            print(question_28[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n29. What is the purpose of a Bloom filter in distributed systems?")
        question_29 = ['a) A Bloom filter is used to prevent unauthorized access to distributed resources.',
                       'b) A Bloom filter is used to reduce the amount of data transferred between distributed nodes.',
                       'c) A Bloom filter is used to route messages between distributed nodes.',
                       'd) A Bloom filter is used to identify malicious nodes in a distributed network.']
        for i in range(len(question_29)):
            print(question_29[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n30. Explain the concept of quantum cryptography?")
        question_30 = ['a) Quantum cryptography is a technique used to optimize routing in quantum networks.',
                       'b) Quantum cryptography is a technique used to simulate quantum algorithms on classical computers.',
                       'c) Quantum cryptography is a technique used to secure communication channels using principles of quantum mechanics.',
                       'd) Quantum cryptography is a technique used to compress data for efficient storage.']
        for i in range(len(question_30)):
            print(question_30[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("Total score:", score, "out of 30")

        while True:
            yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
            if yes_or_no.lower() == 'y':
                jumphere() 
            elif yes_or_no.lower() == 'n':
                print("Thank you for taking the test. Goodbye!")
                quit()
            else:
                print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('anatomy') and choose_the_difficulty.lower() == ('easy'):
        input('You\'ll be given 10 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')
        score = 0

        print("\n1. What is the largest organ in the human body?")
        question_1 = ['a) liver', 'b) heart', 'c) skin', 'd) brain']
        for option in question_1:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n2. Which bone protects the brain?")
        question_2 = ['a) femur', 'b) scapula', 'c) cranium', 'd) sternum']
        for option in question_2:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n3. Which organ produces insulin in the human body?")
        question_3 = ['a) liver', 'b) pancreas', 'c) kidney', 'd) spleen']
        for option in question_3:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'b':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n4. What is the main function of the lungs?")
        question_4 = ['a) digestion', 'b) circulation', 'c) respiration', 'd) excretion']
        for option in question_4:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n5. Which organ is responsible for filtering waste from the blood?")
        question_5 = ['a) liver', 'b) spleen', 'c) kidney', 'd) stomach']
        for option in question_5:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n6. What is the main function of the heart?")
        question_6 = ['a) to pump blood', 'b) to produce hormones', 'c) to digest food', 'd) to store energy']
        for option in question_6:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n7. Which bone is commonly known as the collarbone?")
        question_7 = ['a) radius', 'b) ulna', 'c) clavicle', 'd) patella']
        for option in question_7:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n8. What is the name of the fluid that lubricates joints?")
        question_8 = ['a) bile', 'b) synapse', 'c) synovial fluid', 'd) lymph']
        for option in question_8:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n9. Which organ is responsible for producing red blood cells?")
        question_9 = ['a) liver', 'b) kidney', 'c) bone marrow', 'd) pancreas']
        for i in range(len(question_9)):
            print(question_9[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n10. What is the longest bone in the human body?")
        question_10 = ['a) femur', 'b) tibia', 'c) fibula', 'd) radius']
        for i in range(len(question_10)):
            print(question_10[i])
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break
            
        print("Your total score is ", score, "out of 10")

        while True:
            yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
            if yes_or_no.lower() == 'y':
                jumphere() 
            elif yes_or_no.lower() == 'n':
                print("Thank you for taking the test. Goodbye!")
                quit()
            else:
                print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('anatomy') and choose_the_difficulty.lower() == ('medium'):
        input('You\'ll be given 20 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')
        score = 0

        print("\n1. What is the name of the bone that forms the back of the skull and protects the cerebellum?")
        question_1 = ['a) mandible', 'b) maxilla', 'c) occipital bone', 'd) temporal bone']
        for option in question_1:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n2. Which of the following glands is responsible for producing melatonin?")
        question_2 = ['a) thyroid gland', 'b) adrenal gland', 'c) pineal gland', 'd) pituitary gland']
        for option in question_2:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n3. Which of these blood vessels carries oxygenated blood away from the heart?")
        question_3 = ['a) pulmonary artery', 'b) pulmonary vein', 'c) aorta', 'd) superior vena cava']
        for option in question_3:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n4. What is the medical term for the voice box?")
        question_4 = ['a) larynx', 'b) trachea', 'c) bronchus', 'd) pharynx']
        for option in question_4:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n5. Which part of the brain is responsible for regulating balance and coordination?")
        question_5 = ['a) cerebellum', 'b) cerebrum', 'c) brainstem', 'd) hypothalamus']
        for option in question_5:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n6. What is the scientific term for the collarbone?")
        question_6 = ['a) clavicle', 'b) scapula', 'c) humerus', 'd) radius']
        for option in question_6:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n7. Which of the following is not a type of muscle tissue?")
        question_7 = ['a) skeletal muscle', 'b) cardiac muscle', 'c) smooth muscle', 'd) adipose tissue']
        for option in question_7:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n8. Which of these bones is not part of the human skull?")
        question_8 = ['a) zygomatic bone', 'b) hyoid bone', 'c) metatarsal bone', 'd) nasal bone']
        for option in question_8:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n9. What is the name of the process by which oxygen is transported in the blood?")
        question_9 = ['a) respiration', 'b) diffusion', 'c) osmosis', 'd) circulation']
        for option in question_9:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n10. Which of the following is not a function of the liver?")
        question_10 = ['a) glycogen storage', 'b) bile production', 'c) insulin secretion', 'd) detoxification']
        for option in question_10:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n11. What is the medical term for the thigh bone?")
        question_11 = ['a) femur', 'b) fibula', 'c) tibia', 'd) patella']
        for option in question_11:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n12. Which of the following is not a part of the small intestine?")
        question_12 = ['a) duodenum', 'b) jejunum', 'c) ileum', 'd) colon']
        for option in question_12:
            print

        (option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'd':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n13. What is the name of the process by which food is broken down into smaller molecules that can be absorbed by the body?")
        question_13 = ['a) digestion', 'b) absorption', 'c) assimilation', 'd) excretion']
        for option in question_13:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n14. Which of the following is not a type of white blood cell?")
        question_14 = ['a) lymphocyte', 'b) monocyte', 'c) erythrocyte', 'd) neutrophil']
        for option in question_14:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n15. What is the name of the membrane that surrounds the heart?")
        question_15 = ['a) pericardium', 'b) pleura', 'c) peritoneum', 'd) endocardium']
        for option in question_15:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n16. Which of the following is not a cranial nerve?")
        question_16 = ['a) optic nerve', 'b) vagus nerve', 'c) radial nerve', 'd) trigeminal nerve']
        for option in question_16:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n17. What is the name of the valve that separates the left atrium from the left ventricle in the heart?")
        question_17 = ['a) mitral valve', 'b) tricuspid valve', 'c) aortic valve', 'd) pulmonary valve']
        for option in question_17:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n18. Which of the following hormones is not produced by the adrenal glands?")
        question_18 = ['a) cortisol', 'b) adrenaline', 'c) insulin', 'd) aldosterone']
        for option in question_18:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n19. What is the medical term for the collarbone?")
        question_19 = ['a) clavicle', 'b) scapula', 'c) humerus', 'd) radius']
        for option in question_19:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'a':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("\n20. Which of the following is not a function of the kidneys?")
        question_20 = ['a) regulation of blood pressure', 'b) production of urine', 'c) production of bile', 'd) regulation of electrolyte balance']
        for option in question_20:
            print(option)
        while True:
            user_answer = input("Your answer: ")
            if user_answer.lower() == 'c':
                score += 1
                break
            elif len(user_answer.lower()) > 1:
                print("Please enter only one letter.")
            elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                print("Please enter only one of the options (a, b, c, d).")
            else:
                break

        print("Your total score is ", score, "out of 20")

        while True:
            yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
            if yes_or_no.lower() == 'y':
                jumphere() 
            elif yes_or_no.lower() == 'n':
                print("Thank you for taking the test. Goodbye!")
                quit()
            else:
                print("Please type 'y' or 'n'")

    elif choose_the_topic.lower() == ('anatomy') and choose_the_difficulty.lower() == ('hard'):
            input('You\'ll be given 30 questions each with four answer options. Each right answer gives you one point. Please write only a letter that is in your opinion a correct answer. Good luck! (Press "Enter" button to coninue)')
            score = 0

            print("\n1. Which of the following structures is not part of the urinary system?")
            question_1 = ['a) ureter', 'b) urethra', 'c) vas deferens', 'd) renal pelvis']
            for i in range(len(question_1)):
                print(question_1[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n2. What is the name of the hormone produced by the kidneys that stimulates red blood cell production?")
            question_2 = ['a) erythropoietin', 'b) renin', 'c) aldosterone', 'd) cortisol']
            for i in range(len(question_2)):
                print(question_2[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n2. What is the name of the hormone produced by the kidneys that stimulates red blood cell production?")
            question_2 = ['a) erythropoietin', 'b) renin', 'c) aldosterone', 'd) cortisol']
            for i in range(len(question_2)):
                print(question_2[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break


            print("\n3. What is the medical term for the windpipe?")
            question_3 = ['a) bronchus', 'b) trachea', 'c) larynx', 'd) alveoli']
            for i in range(len(question_3)):
                print(question_3[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break


            print("\n4. Which of the following is not a function of the lymphatic system?")
            question_4 = ['a) fluid balance', 'b) nutrient absorption', 'c) immune defense', 'd) lipid absorption']
            for i in range(len(question_4)):
                print(question_4[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'd':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n5. What is the name of the membrane that lines the abdominal cavity?")
            question_5 = ['a) pericardium', 'b) peritoneum', 'c) pleura', 'd) endocardium']
            for i in range(len(question_5)):
                print(question_5[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n6. Which of the following is not a function of the spleen?")
            question_6 = ['a) blood filtration', 'b) red blood cell production', 'c) immune response', 'd) platelet storage']
            for i in range(len(question_6)):
                print(question_6[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n7. What is the name of the enzyme found in saliva that begins the digestion of carbohydrates?")
            question_7 = ['a) amylase', 'b) pepsin', 'c) lipase', 'd) protease']
            for i in range(len(question_7)):
                print(question_7[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n8. Which of the following hormones is produced by the adrenal cortex?")
            question_8 = ['a) adrenaline', 'b) cortisol', 'c) epinephrine', 'd) norepinephrine']
            for i in range(len(question_8)):
                print(question_8[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n9. What is the name of the small, finger-like projections in the small intestine that increase its surface area?")
            question_9 = ['a) villi', 'b) microvilli', 'c) crypts', 'd) lacteals']
            for i in range(len(question_9)):
                print(question_9[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n10. Which of the following is not a function of the endocrine system?")
            question_10 = ['a) regulation of metabolism', 'b) control of growth and development', 'c) production of urine', 'd) maintenance of electrolyte balance']
            for i in range(len(question_10)):
                print(question_10[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n11. What is the name of the bone that forms the upper arm?")
            question_11 = ['a) humerus', 'b) ulna', 'c) radius', 'd) scapula']
            for i in range(len(question_11)):
                print(question_11[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'd':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n12. Which of the following is not a component of blood?")
            question_12 = ['a) plasma', 'b) platelets', 'c) lymphocytes', 'd) insulin']
            for i in range(len(question_12)):
                print(question_12[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'd':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n13. What is the name of the valve that separates the small intestine from the large intestine?")
            question_13 = ['a) ileocecal valve', 'b) pyloric valve', 'c) sigmoid valve', 'd) duodenal valve']
            for i in range(len(question_13)):
                print(question_13[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n14. Which of the following is not a function of the hypothalamus?")
            question_14 = ['a) regulation of body temperature', 'b) control of hunger and thirst', 'c) production of insulin', 'd) regulation of sleep-wake cycles']
            for i in range(len(question_14)):
                print(question_14[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n15. What is the name of the hormone produced by the pancreas that regulates blood sugar levels?")
            question_15 = ['a) insulin', 'b) glucagon', 'c) adrenaline', 'd) cortisol']
            for i in range(len(question_15)):
                print(question_15[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n16. Which of the following is not a function of the respiratory system?")
            question_16 = ['a) regulation of body temperature', 'b) gas exchange', 'c) oxygen transport', 'd) removal of carbon dioxide']
            for i in range(len(question_16)):
                print(question_16[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n17. What is the name of the largest artery in the human body?")
            question_17 = ['a) aorta', 'b) pulmonary artery', 'c) carotid artery', 'd) femoral artery']
            for i in range(len(question_17)):
                print(question_17[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n18. Which of the following is not a component of the central nervous system?")
            question_18 = ['a) brain', 'b) spinal cord', 'c) peripheral nerves', 'd) meninges']
            for i in range(len(question_18)):
                print(question_18[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n19. What is the name of the valve that prevents blood from flowing back into the left ventricle of the heart?")
            question_19 = ['a) mitral valve', 'b) tricuspid valve', 'c) aortic valve', 'd) pulmonary valve']
            for i in range(len(question_19)):
                print(question_19[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n20. Which of the following is not a function of the liver?")
            question_20 = ['a) bile production', 'b) glycogen storage', 'c) insulin secretion', 'd) detoxification']
            for i in range(len(question_20)):
                print(question_20[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n21. What is the name of the hormone produced by the pineal gland that regulates sleep-wake cycles?")
            question_21 = ['a) melatonin', 'b) serotonin', 'c) dopamine', 'd) oxytocin']
            for i in range(len(question_21)):
                print(question_21[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n22. Which of the following is not a part of the brainstem?")
            question_22 = ['a) medulla oblongata', 'b) cerebellum', 'c) pons', 'd) midbrain']
            for i in range(len(question_22)):
                print(question_22[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n23. What is the name of the valve that separates the left atrium from the left ventricle in the heart?")
            question_23 = ['a) mitral valve', 'b) tricuspid valve', 'c) aortic valve', 'd) pulmonary valve']
            for i in range(len(question_23)):
                print(question_23[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n24. Which of the following is not a function of the adrenal glands?")
            question_24 = ['a) regulation of blood pressure', 'b) production of adrenaline', 'c) production of insulin', 'd) regulation of electrolyte balance']
            for i in range(len(question_24)):
                print(question_24[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'c':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n25. What is the name of the membrane that surrounds the lungs?")
            question_25 = ['a) pleura', 'b) pericardium', 'c) peritoneum', 'd) endocardium']
            for i in range(len(question_25)):
                print(question_25[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n26. Which of the following is not a type of muscle tissue?")
            question_26 = ['a) skeletal muscle', 'b) cardiac muscle', 'c) smooth muscle', 'd) adipose tissue']
            for i in range(len(question_26)):
                print(question_26[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'd':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n27. What is the name of the hormone produced by the kidneys that regulates blood pressure?")
            question_27 = ['a) aldosterone', 'b) angiotensin', 'c) renin', 'd) erythropoietin']
            for i in range(len(question_27)):
                print(question_27[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n28. Which of the following is not a function of the parathyroid glands?")
            question_28 = ['a) regulation of blood calcium levels', 'b) production of insulin', 'c) production of parathyroid hormone', 'd) regulation of bone metabolism']
            for i in range(len(question_28)):
                print(question_28[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n29. What is the name of the structure that connects the kidneys to the bladder?")
            question_29 = ['a) urethra', 'b) ureter', 'c) renal artery', 'd) renal vein']
            for i in range(len(question_29)):
                print(question_29[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'b':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("\n30. Which of the following is not a function of the lymphatic system?")
            question_30 = ['a) nutrient absorption', 'b) fluid balance', 'c) immune defense', 'd) removal of cellular waste']
            for i in range(len(question_30)):
                print(question_30[i])
            while True:
                user_answer = input("Your answer: ")
                if user_answer.lower() == 'a':
                    score += 1
                    break
                elif len(user_answer.lower()) > 1:
                    print("Please enter only one letter.")
                elif user_answer.lower() not in ['a', 'b', 'c', 'd']:
                    print("Please enter only one of the options (a, b, c, d).")
                else:
                    break

            print("Your total score is ", score, "out of 30")

            while True:
                yes_or_no = input("Would you like to take the same test but with another difficulty level or a completely different topic? Type 'y' if yes, type 'n' if no.   ") 
                if yes_or_no.lower() == 'y':
                    jumphere() 
                elif yes_or_no.lower() == 'n':
                    print("Thank you for taking the test. Goodbye!")
                    quit()
                else:
                    print("Please type 'y' or 'n'")

jumphere()




######ЧТОБЫ ПОСЛЕ ЗАВЕРШЕНИЯ ОДНОГО ТЕСТА, БЫЛ ВЫВЕДЕН ИНПУТ СПРАШИВАЮЩИЙ ХОЧЕТ ЛИ ЮЗЕР ПРОЙТИ ДРУГОЙ ТЕСТ ИЛИ ТОТ ЖЕ ТОПИК НО ДРУГОЙ СЛОЖНОСТИ.        (ВЫПОЛНЕНО)
######ЧТОБЫ В СЛУЧАЕ ЧЕГО, ЮЗЕР МОГ ПОКИНУТЬ ТЕСТ НО ПРИ ЭТОМ НЕ ЗЫКРЫВАЯ ТЕРМИНАЛ          (ОТМЕНА. НО РАЗБЕРЕМСЯ С ЭТИМ В ДАЛЬНЕЙШЕМ)


###ПОСМОТРИ СВОИ ЗАПИСИ В ТЕТРАДИ 


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#И САМОЕ ГЛАВНОЕ ЭТО РАЗБЕРИСЬ С КЛАССАМИ!!!!! (ОБЯЗАТЕЛЬНО)               (ВЫПОЛНЕНО)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#задача на данный момент это сделать так, чтобы задавались вопросы             (ВЫПОЛНЕНО)
#по одному с 4 вариантами ответов с одним верным ответом                        (ВЫПОЛНЕНО)
#после ответа идет следующий вопрос (без разницы правильный или не правильный)  (ВЫПОЛНЕНО)
#при низкой сложности будет 10 вопросов                                          (ВЫПОЛНЕНО)                                           
#при средней сложности будет 20 вопросов                                         (ВЫПОЛНЕНО)
#при высокой сложности будет 30 вопросов                                         (ВЫПОЛНЕНО)
#и сложность вопросов тоже будет разнится в зависисмоти от выбранной сложности    (ВЫПОЛНЕНО)
#нельзя чтобы вопросы с других уровней сложности повторялись                      (ВЫПОЛНЕНО)
#добавить функцию подсчета баллов и выдачи результатов после прохождения тестов   (ВЫПОЛНЕНО)


#?????????????????????????????????????????????????????
#ПО ВОЗМОЖНОСТИ ДОБАВИМ ФУНКЦИЮ РАНДОМАЙЗЕРА ВОПРОСОВ                                (ОТМЕНА)
#?????????????????????????????????????????????????????


#добавлено 06.05.24
                    ############ДО 30 МАЯ ТЫ ДОЛЖЕН ЗАКОНЧИТЬ ЭТОТ ПРОЕКТ
#добавлено 14.05.24
                    ############СЕГОДНЯ 14 МАЯ И Я ЗАВЕРШИЛ МОЙ ПРОЕКТ КОТОРЫЙ БЫЛ НАЧАТ 16 МАРТА 24 ГОДА


###########РАЗБЕРИСЬ С ГИТХАБОМ И ИЗУЧИ ЕЕ ТОЖЕ. ЗАЛЕЙ СВОЙ КОД ТУДА
import random


class password_digit_randomizer():
    list_alphabet_lc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t", "u", "v", "w", "x", "y", "z"]
    list_alphabet_uc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z"]
    list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_special_characters = ["!", "<", ">", "§", "$", "%", "&", "/", "{", "[", "]", "}", "(", ")", "=", "?", "+", "~",
                               "*", "#", "-", "_", ".", ":", ",", ";"]


    def randomizeList(lst):
        random.shuffle(lst)
        return lst

    list_numbers = randomizeList(list_numbers)
    list_alphabet_lc = randomizeList(list_alphabet_lc)
    list_alphabet_uc = randomizeList(list_alphabet_uc)
    list_special_characters = randomizeList(list_special_characters)

    def createPassword(nom):
        nom_list = []
        password_list = []
        list_of_lists = ["list_alphabet_lc", "list_alphabet_uc", "list_special_characters", "list_numbers"]
        for i in range(nom):
            print(i)
            for a in range(5):
                print(a)
                element_list = random.choice(list_of_lists)
                digit = random.choice(element_list)
                print(element_list)
                print(digit)
                nom_list.append(digit)
            random.shuffle(list_of_lists)
            password_list.append(nom_list)
            nom_list = []
        print("Passwortliste: ", password_list)





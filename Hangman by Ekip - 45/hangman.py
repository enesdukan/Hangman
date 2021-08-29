import random  # random modülünü projemizemize dahil ediyoruz.


# darağacını tanımlıyoruz.
def display_hangman(tries):
    stages = ["""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      O
                   |
                   |

                   |
                   -
                   """,
              """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
              ]

    return stages[tries]

def main():
    # karşılama metnimizi oluşturuyoruz
    dil = input("Lütfen Dil Seçiniz(EN,TR): ").upper()

    if dil == "EN":
        print("Welcome to HANGMAN!")
        print("_______\n|     |\n|     O\n|    /|\ \n|     |\n|    /\ \n|\n-")
        kategori = input("Please select one of the categories\nCountry = 1\nCities = 2\nFamous people = 3\nAnimals = 4\nRandom = 5   ").upper()

    elif dil == "TR":
        print("Adam Asmaca oyununa hoşgeldiniz!")
        print("_______\n|     |\n|     O\n|    /|\ \n|     |\n|    /\ \n|\n-")
        kategori = input("Lütfen bir kategori seçiniz\nÜlkeler = 1\nŞehirler = 2\nÜnlüler = 3\nHayvanlar = 4\nKarışık = 5   ").upper()

    else:
        print("Geçersiz dil seçtiniz.")

    ### geçersiz cevaptan sonra tekrar başa döndürmek için ne yapmalı

    # kategori ve dil seçimine göre dosyalardan kelime seçiyoruz.
    if dil == "EN" and kategori == "1":
        with open("ülke-ingilizce.txt", "r") as f:
            words = f.readlines()

    elif dil == "EN" and kategori == "2":
        with open("şehir-ingilizce.txt", "r") as f:
            words = f.readlines()

    elif kategori == "3":
        with open("ünlü kişiler.txt", "r") as f:
            words = f.readlines()

    elif dil == "EN" and kategori == "4":
        with open("hayvanlar-ingilizce.txt", "r") as f:
            words = f.readlines()

    elif dil == "EN" and kategori == "5":
        with open("random-ingilizce.txt", "r") as f:
            words = f.readlines()


    elif dil == "TR" and kategori == "1":
        with open("ülke-türkçe.txt", "r") as f:
            words = f.readlines()


    elif dil == "TR" and kategori == "2":
        with open("şehir-türkçe.txt", "r") as f:
            words = f.readlines()


    elif dil == "TR" and kategori == "4":
        with open("hayvanlar-türkçe.txt", "r") as f:
            words = f.readlines()


    elif dil == "TR" and kategori == "5":
        with open("random-türkçe.txt", "r") as f:
            words = f.readlines()

    word = random.choice(words)[:-1]  # kelimeyi ilgili dosyalarımızdan rastgele seçiyoruz.
    tries = 7  # deneme hakkı 7 olarak tanımlıyoruz.
    word = word.upper()

    guesses = []  # tahmin ettiğimiz harfler için  guesses listesi oluşturuyoruz.
    # aşağıda, kelimedeki harf sayısı kadar alt tire (_) yazdırıyoruz
    done = False
    while not done:
        for letter in word:
            if letter.upper() in guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print(" ")
        done = True
        # kalan hak sayısını oyuncunun görmesini sağlıyoruz.
        guess = input("Allowed errors: " + str(tries) + ". Next guess:\n")
        guesses.append(guess.upper())

        if guess.upper() not in word.upper():
            tries = tries - 1
            print(display_hangman(tries))
            if tries == 0: break
            done = True
        for letter in word:
            if letter.upper() not in guesses:
                done = False
    # oyun sonucunu ekrana yazdırıyoruz.
    if tries > 0:
        print("Congrats! " + word + " is the right answer.")

    else:
        print("The word was " + word + " .")
main()

while input("Play again? (Y/N)\n").upper() == "Y":
            main()
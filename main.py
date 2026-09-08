#imports
import random
import os
from json_manager import *
from storage import russian_alphabet, russian_words, russian_to_english_alphabet

def already_in_index(n, indexes):
    for i in indexes:
        if i == n:
            return True

    return False

def run_letter_training(sample_size : int, reps : int):
    global russian_alphabet
    os.system('cls')
    print("Loading sample data...")

    #setting up random sample package
    russian_sample = []
    indexes = []
    j = 0
    while j < sample_size:
        print(f"Obtaining item {j + 1}")
        while True:
            r = random.randint(0, len(russian_alphabet) - 1)
            if already_in_index(r, indexes) == False:
                indexes.append(r)
                break
        russian_sample.append(russian_alphabet[r])
        j += 1


    # running the actual test
    correct = 0
    i = 0
    while i < reps:
        r = random.randint(0, len(russian_sample) - 1)
        letter = russian_sample[r]
        print(letter)
        print("")
        attempt = str(input())
        if attempt == letter:
            correct += 1
            print('')
            print('')
            i += 1
            print(f"CORRECT!! {reps - i} questions left!!")

        else:
            print('')
            print('')
            print(f"Incorrect... {reps - i} questions left!!")
            i += 1

    print(f"You got {correct} out of {reps} correct! That's {(correct/reps)*100}%")
    input()

def learning_letters():
    global russian_to_english_alphabet
    global russian_alphabet

    while True:
        r = random.randint(0, len(russian_alphabet) - 1)

        print(f"{russian_alphabet[r]} \t\t\t\t\t\t\t\t\t(key: {russian_to_english_alphabet[r]}")
        print()
        print()
        my_input = input()

        if my_input == "stop" or my_input == "ыещз":
            break

        if my_input == russian_alphabet[r]:
            print("Correct!!")

        else:
            print("Incorrect...")

        print()
        print()
        print()

def run_word_training(sample_size : int, reps : int):
    global russian_words
    pass

def retrieve_settings(is_alphabet):
    os.system('cls')
    global russian_alphabet
    global russian_words
    if is_alphabet:
        list_name = 'russian alphabet'
        list_size = len(russian_alphabet)
    else:
        list_name = 'russian vocab'
        list_size = int(len(russian_words))

    while True:
        print(f"What should be the sample size? (Note, there are {list_size} items in the {list_name})")
        samplesize = int(input())
        if samplesize <= list_size:
            break
    print("Now how many questions do you want us to throw at you?")
    reps = int(input())

    return samplesize, reps

def main():
    while True:
        os.system('cls')
        print("Welcome to the Russian typing trainer!")
        print('')
        print("Select one of the following options:")

        print('1: Alphabet training')
        print('2: Word training')
        print('3: Stop training')
        print()
        print('4: Learn Alphabet')

        my_input = input()

        if my_input == '3':
            break

        if my_input == '1':
            samplesize, reps = retrieve_settings(True)
            os.system('cls')
            run_letter_training(samplesize, reps)

        if my_input == '2':
            samplesize, reps = retrieve_settings(False)
            os.system('cls')
            run_word_training(samplesize, reps)

        if my_input == '4':
            os.system('cls')
            learning_letters()


if __name__ == '__main__':
    main()
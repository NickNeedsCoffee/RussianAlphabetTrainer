#imports
import os
import json

def create_initial_vocab_repo():
    print('create initial vocab repo')
    russian_words = {'приет' : 'Hi', 'да' : 'Yes'}
    vocab_repo = {'test_vocab': russian_words}

    with open("vocab_repo.json", 'w') as f:
        json.dump(vocab_repo, f, indent=4)

def load_vocab_repo() -> dict:
    with open('vocab_repo.json', 'r') as f:
        data = json.load(f)
        return data

def print_vocab_repo():
    data = load_vocab_repo()
    print(data)
    print(type(data))

def load_vocab_list(list_name: str) -> dict:
    repo = load_vocab_repo()
    return repo[list_name]

def append_vocab_list(mlist: dict[str, str], list_name: str):
    repo = load_vocab_repo()
    repo[str(list_name)] = mlist

    with open("vocab_repo.json", 'w') as f:
        json.dump(repo, f, indent=4)

def remove_vocab_list():
    os.system('cls')
    repo = load_vocab_repo()

    print('Type the name of the list you would like to remove: ')
    print('Here is a list of names')
    for name in repo:
        print(name)
    print('')
    list_name = str(input())

    try:
        repo.pop(str(list_name))

    except:
        print("Couldn't remove that list :(")

    else:
        with open("vocab_repo.json", 'w') as f:
            json.dump(repo, f, indent=4)

        print(f"{list_name} removed successfully :)")

def create_vocab_list():
    contents = {}
    i = 0
    while True:
        os.system('cls')
        print('Write a Russian word (type "STOP123" to stop the loop')
        r_word = str(input())

        if r_word == 'STOP123':
            break

        print('')
        print('Whats the English translation?')
        e_word = str(input())

        contents[r_word] = e_word
        i+=1

    print(f"You added {i} words to your new list, do you wish to save your list? Enter 'y' to save the list.")

    answ = str(input())

    if answ == 'y':
        print('Type a name for your new list:')
        listname = str(input())
        append_vocab_list(contents, listname)

def main():
    #create_initial_vocab_repo()
    #test_vocab_list = {"фыва" : "Test1", "йуцезщшг" : "Test3"}
    #append_vocab_list(test_vocab_list, "test_vocab1")
    print_vocab_repo()
    #create_vocab_list()
    remove_vocab_list()
    print_vocab_repo()

main()
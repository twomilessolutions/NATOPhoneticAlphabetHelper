from NATOTranslator import NATOTranslator
from colorama import init, Fore
init()

def main():
    word = input("\n\nEnter the word, phrase, or sentence you would like the NATO Phonetic translation for: ")

    translator = NATOTranslator()
    translation = translator.translate_string(word)

    print_string = ""
    counter = 0
    counter_limit = 10

    for line in translation:
        print_string = print_string + line
        counter += 1
        if counter >= counter_limit:
            counter = 0
            print_string = print_string + "\n"

    print(Fore.CYAN + print_string)
    
    print(Fore.WHITE + "")
    
    input("Press any key to exit...")

if __name__ == "__main__":
    main()
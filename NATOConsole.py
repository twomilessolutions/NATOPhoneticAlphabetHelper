from NATOTranslator import NATOTranslator
from colorama import init, Fore
init()

def main():
    word = input("\n\nEnter the word, phrase, or sentence you would like the NATO Phonetic translation for: ")

    translator = NATOTranslator()
    translation = translator.translate_string(word)

    for line in translation:
        print(Fore.CYAN + line)
    
    print(Fore.WHITE + "")
    
    input("Press any key to exit...")

if __name__ == "__main__":
    main()
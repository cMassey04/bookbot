from stats import accept_text, new_text, new_sorted
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    sys_new = sys.argv[1]

def get_book_text(sys_new):
    with open(sys_new) as f:
        file_contents = f.read()

    return  file_contents

def main():

    print("============ BOOKBOT ============")
    yes = get_book_text(sys_new)
    print("Analyzing book found at ")
    num_words = accept_text(yes)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    agree = new_text(yes)
    print("--------- Character Count -------")
    yes_new = new_sorted(agree)
    for ye in yes_new:
        if ye["char"].isalpha() == True:
            print(f"{ye['char']}: {ye['num']}")
    print("============= END ===============")


main()

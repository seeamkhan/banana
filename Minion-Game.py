#The Minion Game.
import time

def main():
    str = raw_input()
    minion(str.upper())

def minion(str):
    person_a_name = 'Kevin'
    person_b_name = 'Stuart'
    vowels = ['A','E','I','O','U']
    consonants = ['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    char_list = list(str)
    total_char = len(char_list)
    person_a_words = []
    person_b_words = []

    #Create all possible words
    all_words = []
    for count in xrange(total_char):
        for i in xrange(count, total_char):
            temp_array = []
            for j in xrange(count, i+1):
                 temp_array.append(char_list[j])
            all_words.append(temp_array)
    # print all_words

    first_char = []
    for first_char in all_words:
        if first_char[0] in vowels:
            person_a_words.append(first_char)

    for first_char in all_words:
        if first_char[0] in consonants:
            person_b_words.append(first_char)

    person_a_score = len(person_a_words)
    person_b_score = len(person_b_words)
    if person_a_score == person_b_score:
        print "Draw"
        print "Score:", person_a_score
        print "Score:", person_b_score
    if person_a_score > person_b_score:
        print person_a_name, "wins!"
        print "Score:", person_a_score
    if person_a_score < person_b_score:
        print person_b_name, "wins!"
        print "Score:", person_b_score
    time.sleep(1)
    print "Thanks!"
    time.sleep(3)
    print "Good by.."
    time.sleep(1)


def main():
    str = raw_input("Type a Word(for example, banana; Remember, Kevin loves vowels and Stuart loves consonants): ")
    minion(str.upper())

if __name__ == '__main__':
    main()

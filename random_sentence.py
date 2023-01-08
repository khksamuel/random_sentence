# A random sentence generator based on the oxford dictionary
import random
# import language translate
from translate import Translator

def random_sentence():
    length = random.randint(3, 10)
    # generate 3 random numbers between 1 and 1000
    numbers = random.sample(range(1, 1000), length)
    # open the file
    FILE = open('words.txt', 'r')
    word_list = FILE.readlines()
    sentence = ''
    for i in range(length):
        # get the word at the random line number
        word = word_list[numbers[i]]
        # remove the newline character
        word = word.replace('\n', '')
        sentence += word + ' '
    FILE.close()
    return sentence

if __name__ == '__main__':
    # translate the sentence to spanish
    translator = Translator(to_lang='zh')
    translation = translator.translate(random_sentence())
    print(translation)
    
# make words.txt a python lis
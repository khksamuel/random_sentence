import random
# from translate import Translator

def random_sentence(): # create random sentence based on the "articles, adjs, nouns, verbs, articles, adjs, nouns" format
    articles = open('articles.txt').read().splitlines()
    adjs = open('adjs.txt').read().splitlines()
    verbs = open('verbs.txt').read().splitlines()
    nouns  = open('nouns.txt').read().splitlines()
    return str(' '.join([random.choice(articles), random.choice(adjs), random.choice(nouns), random.choice(verbs), random.choice(articles), random.choice(adjs), random.choice(nouns)]).capitalize() + '.')

if __name__ == '__main__':
    sentence = random_sentence()
    # translartor = Translator(to_lang="zh", from_lang="en")
    # translated = translartor.translate((sentence))
    print(sentence)
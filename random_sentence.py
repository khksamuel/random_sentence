import random

def random_sentence(): # create random sentence based on the "articles, adjs, nouns, verbs, articles, adjs, nouns" format
    articles = open('articles.txt').read().splitlines()
    adjs = open('adjs.txt').read().splitlines()
    verbs = open('verbs.txt').read().splitlines()
    nouns  = open('nouns.txt').read().splitlines()
    return ' '.join([random.choice(articles), random.choice(adjs), random.choice(nouns), random.choice(verbs), random.choice(articles), random.choice(adjs), random.choice(nouns)]).capitalize() + '.'

if __name__ == '__main__':
    print(random_sentence())
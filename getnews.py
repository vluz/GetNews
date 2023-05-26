import pandas as pd
import spacy
import textwrap
import re
from GoogleNews import GoogleNews
from newspaper import Article
from spacy.lang.pt.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


def getarticlefromurl(url):
    article = Article(url)
    try:
        article.download()
        article.parse()
    except:
        return "-----Download Error------"
    return article.text


def summarize(text, per):
    nlp = spacy.load('pt_core_news_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    select_length = int(len(sentence_tokens) * per)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = ''.join(final_summary)
    return summary


f = open("NEWS.txt", "w")
googlenews = GoogleNews(lang='pt', region='PT', period='2d', encode='utf-8')
googlenews.search("Inteligência artificial")
resultado = googlenews.result()
dados = pd.DataFrame(resultado)

for index, row in dados.iterrows():
    f.write("\n\n\n")
    print("\n\n\n")
    f.write(row['title'])
    f.write("\n")
    print(row['title'])
    f.write(row['link'])
    f.write("\n")
    print(row['link'])
    f.write("________________________________________________________________________")
    f.write("\n")
    print("________________________________________________________________________")
    texto = getarticlefromurl(row['link'])
    re.sub('[^A-Za-z0-9 ]+', '', texto)

    if len(texto) > 0:
        sumario = summarize(texto, 0.1)
        stype = "Sumario"
    else:
        sumario = ""

    if len(sumario) > 0:
        f.write(sumario)
        f.write("\n")
        print(textwrap.fill(sumario, 70))
    else:
        sumario = texto
        f.write(sumario)
        f.write("\n")
        print(textwrap.fill(sumario, 70))
        stype = "Original"

    f.write(stype)
    f.write("\n")
    print(stype)

f.close()
#End
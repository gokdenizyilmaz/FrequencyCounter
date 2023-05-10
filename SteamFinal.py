import spacy
from collections import Counter
from nltk.stem import PorterStemmer

def process_text(text):
    #gerekli modüller
    nlp = spacy.load("en_core_web_sm")
    stemmer = PorterStemmer()
    doc = nlp(text)
    

    #irregular verbler için üç listeye ihtiyacımız var , verbs,stemmed_verbs,lemmatized verbs
    verbs = []
    stemmed_verbs = []
    lemmatized_verbs = []
    
    #verbs listesi için pos tag ile metinden verbleri çekiyoruz ve listeleri oluşturuyoruz
    for token in doc:
        if token.pos_ == 'VERB':
            verbs.append(token.text)
            stemmed_verbs.append(stemmer.stem(token.text))
            lemmatized_verbs.append(token.lemma_)

     #karşılaştırma sistemi ile irregular verb tespit ediyoruz
    irregular_verbs = []
    for x, y in zip(stemmed_verbs, lemmatized_verbs):
        if x != y:
            irregular_verbs.append(x)
    
    #irregular verbleri ayrı bir listeye aldıktan sonra normal listeden temizliyoruz
    normal_verbs = []
    for i in verbs:
        if i not in irregular_verbs:
            normal_verbs.append(i)

    #metineki şehir isimleri hariç özel isimleri silen ve geriye kalan isimleri listeye alan listeyi oluşturuyoruz
    lemmas = []
    for token in doc:
        if not token.is_punct and token.pos_ != 'VERB':
            if token.pos_ == 'PROPN':
                if token.ent_type_ == 'GPE':
                    lemmas.append(token.text.lower())
            else:
                lemmas.append(token.lemma_.lower())


    #normal fiilleri içeren listemiz normal_verbs
    #irregular verbleri içeren listemiz irregular_verbs
    #fiil harici kelimeleri içeren listemiz lemmas

    #burada da her bir fiili lemma halinde çıktı aldık           
    lemma_verbs = []
    for verb in normal_verbs:
        doc = nlp(verb)
        lemmav = doc[0].lemma_
        lemma_verbs.append(lemmav)

    #şimdi her bir listenin sıklıklarını alıcaz son durumda lazım olan listelerimiz lemma_verbs,lemmas,irregular_verbs
    words_lemmas = Counter(lemmas)
    verb_lemmas = Counter(lemma_verbs)
    irregular_lemmas = Counter(irregular_verbs)


    #birleştirme ve dicte dönüştürme
    combined_dict = Counter(words_lemmas) + Counter(verb_lemmas) + Counter(irregular_lemmas)
    combined_dict = dict(combined_dict)
    
    return combined_dict

input_text = "I am going to the park. I love playing in the park. The park is a great place to relax. I went to the park. I saw you. I saw him. Jack was in London past week. I swam in the lake"
text = "I swam in the lake last week with John at the London"
output = process_text(text)
print(output)

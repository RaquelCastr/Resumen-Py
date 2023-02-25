import urllib.request
import re
import nltk
from inscriptis import get_text 

#scrapea articulo de wikipedia 
text ='Benito Antonio Martínez Ocasio(born March 10, 1994), known professionally as Bad Bunny, is a Puerto Rican rapper and singer. His musical style is primarily defined as Latin trap and reggaeton, although his music also takes influences from other genres. He rose to prominence in 2016 with his song "Diles", which led to a deal with Hear This Music. He continued gaining traction with songs such as "Soy Peor" and collaborations with Farruko, Karol G, Ozuna, J Balvin, and more during the next few years.His breakthrough came in 2018 with his feature on Cardi B s number-one song "I Like It" alongside J Balvin,and his top-ten song "Mia" featuring Drake.His debut album X 100pre was released in December 2018 by Rimas Entertainment, which peaked at number 11 on the US Billboard 200. He then released his collaborative album Oasis with J Balvin in June 2019, reaching number nine on the Billboard 200. Bad Bunnys second album YHLQMDLG was released on February 29, 2020, and became the highest charting all-Spanish album, reaching number two on the Billboard 200. It was followed up with the compilation album Las que no iban a salir in May, which reached number seven on the chart.In November 2020, Bad Bunny released his fourth album El Último Tour Del Mundo, combining his reggaeton and Latin trap sound with rock music.The album became the first all-Spanish-language album to reach number one on the Billboard 200 and its lead single "Dákiti" debuted in the top ten on the US Billboard Hot 100. In May 2022, his fifth album Un Verano Sin Ti released, which became his second number-one album and topped the Billboard 200 Year-End chart, while four of the albums singles peaked in the top ten on the Billboard Hot 100.Un Verano Sin Ti was the first Spanish-language album to earn a Grammy nomination for Album of the Year.Bad Bunny is credited with helping Spanish-language music achieve mainstream popularity in the worldwide market. In 2020, he became the first non-English language act to be Spotifys most streamed artist of the year and achieved the same record again in 2021.He then had the biggest streaming year for any artist on Spotify in 2022.Bad Bunny has earned three Grammy Awards, four Latin Grammy Awards, eight Billboard Music Awards, and thirteen Lo Nuestro Awards. He was crowned Artist of the Year at the Apple Music Awards 2022'


from nltk import word_tokenize, sent_tokenize
#nltk.download()
#Removing Square Brackets and Extra Spaces
#article_text = re.sub(r'/[[0-9]*\]',' ', article_text)
#article_text = re.sub(r'\s+',' ', article_text)

#formatted_article_text = re.sub('[^a-zA-Z]',' ', article_text)
#formatted_article_text = re.sub(r'\s+',' ', formatted_article_text)

#nltk.download()
#EN ESTA PARTE HACE LA TOKENIZACION
sentence_list = nltk.sent_tokenize(text)

#EN ESTA PARTE ENCUENTRA LA FRECUENCIA DE CADA PALABRA
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] +=1

maximum_frequncy = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

#CALCULA LAS FRASES QUE MAS SE REPITEN
sentence_scores ={}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]



#REALIZA EL RESUMEN DE LAS MEJORES FRASES
import heapq
summary_sentences = heapq.nlargest(7,sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)

from googletrans import Translator
translator = Translator()
textTranslate = translator.translate(summary, src='en', dest='es')
print(textTranslate.text)



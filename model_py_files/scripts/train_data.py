from .libraries import *

df = pd.read_csv(r"static\\data\\faq.csv")
trainning1=df['question'].to_numpy()
nombre_de_qst=len(trainning1)
tokenizer= RegexpTokenizer("\w+")
for i in range(nombre_de_qst) :
    trainning1[i]=trainning1[i].lower()

for i in range(nombre_de_qst) :
    tokenz = tokenizer.tokenize(trainning1[i])
    trainning1[i]=" ".join(tokenz)

unwanted_words = stopwords.words("english")  
for i in range(nombre_de_qst) :
    word_tokenze = word_tokenize(trainning1[i])
    liste = [ i for i in word_tokenze if not i.lower() in unwanted_words ]
    trainning1[i]=" ".join(liste)  
    

for i in range(nombre_de_qst) :
    doc = nlp(u"{0}".format(trainning1[i]))
    listeX=[]
    for token in doc : 
        word_tokenze = word_tokenize(trainning1[i])
        listeX += [ token.lemma_ ]
    trainning1[i]=" ".join(listeX)    

vectorize = CountVectorizer()
vectorize.fit(trainning1)
vector  = vectorize.transform(trainning1)
all_vectors = vector.toarray()
from .train_data import *

def removepunctuations(entre) : 
            entre=entre.lower()
            tokenizer= RegexpTokenizer("\w+")
            for i in range(len(entre)) :
                tokenz = tokenizer.tokenize(entre)
                entre=" ".join(tokenz)
            entre = [entre]    
            return entre

def removestopwords(entre) :        
                unwanted_words = stopwords.words("english")  
                for i in range(len(entre[0])) :
                    word_tokenze = word_tokenize(entre[0])
                    liste = [ i for i in word_tokenze if not i.lower() in unwanted_words ]
                    entre[0]=" ".join(liste)
                return entre   

def lemmatizerfunc(entre) :

                for i in range(len(entre)) :
                    doc = nlp(u"{0}".format(entre[i]))
                    listeX=[]
                    for token in doc : 
                        word_tokenze = word_tokenize(entre[i])
                        listeX += [ token.lemma_ ]
                    entre[i]=" ".join(listeX)
                return entre
def extract(name_of_words_index,vectorizevocabulary_):
            new_dict = {}
            l=[]
            allkeys = name_of_words_index.keys()
            for key in name_of_words_index:
                if(key not in vectorize.vocabulary_.keys()) :
                        l+=[key]
            for el in l :
                name_of_words_index.pop(el)
            return name_of_words_index

def collectThemInput(vector_of_input,name_of_words_index):
            value_words=name_of_words_index.values()
            array = []
            for ele in value_words :
                array +=[vector_of_input[0][ele]]
            return np.array(array) 

def columns_indexes(name_of_words_index) :
            liste=[]
            for key in vectorize.vocabulary_ :
                    for key_input in name_of_words_index.keys() :
                        if key == key_input :
                            liste+=[vectorize.vocabulary_[key]]
                            
                            
            return sorted(liste)

def collectthem(l,true_vector):
                try :
                    S=true_vector[:,l[0]:l[0]+1]
                    for i in range(1,len(l)) :
                            second=true_vector[:,l[i]:l[i]+1]
                            S=np.concatenate((S,second),axis=1)
                    return S 
                except IndexError :
                        return []

def retrieve_answer(new_one,vector_of_input) :
            similarity = 0
            new_list = []
            new_dict = {}
            for i in range(len(new_one)) :
                cosine = cosine_similarity(new_one[i].reshape(1,-1),vector_of_input.reshape(1,-1))
                if(cosine[0][0] > similarity) :
                    new_dict = {}
                    similarity = cosine[0][0]
                    new_dict["reponse"]=new_one[i]
                    new_dict["similarity"]=similarity
                    new_dict["index"]=i
            
            new_list +=[new_dict]
                
            return  new_list

def randomanswer(new_list) :
            if(new_list[0]) :
                rd = random.choice(new_list)
                return rd['index']
            else : 
                m="introuvable"
                return m

def answer(m):
            if(m=="introuvable") :
                return "What you mean ?"
            else :
                row = df.iloc[[m]]
                row=row.to_numpy()
                res = row[0,1]
                return res                                                    
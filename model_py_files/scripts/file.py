from .functions_handle_input import *


def talk(entre) :

        entre = removepunctuations(entre)
   
        entre =removestopwords(entre)    

        entre=lemmatizerfunc(entre)

        vectorizeInput = CountVectorizer()
        vectorizeInput.fit(entre)
        name_of_words_index = vectorizeInput.vocabulary_
        text_input_to_vector = vectorizeInput.transform(entre)
        vector_of_input = text_input_to_vector.toarray()

        name_of_words_index=extract(name_of_words_index,vectorize.vocabulary_)
      
        vector_of_input=collectThemInput(vector_of_input,name_of_words_index)

        l=columns_indexes(name_of_words_index)

        true_vector=vector.toarray()
    
        new_one = collectthem(l,true_vector)

        selection=retrieve_answer(new_one,vector_of_input)           

        m=randomanswer(selection)

        return answer(m)
            

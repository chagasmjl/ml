#-------------------------------------------------------------
# Examples of using keras API to process text data.
# Author: Mario jorge lopes chagas 2017
# Original post from https://machinelearningmastery.com/prepare-text-data-deep-learning-keras/
#--------------------------------------------------------------
from keras.preprocessing.text import text_to_word_sequence, one_hot, hashing_trick, Tokenizer

#define the documents
docs = ['The cat is crazy',
        'good morning.',
        'The the great effort',
        'nice']
#createing Keras class Tokenizer
t = Tokenizer()
#fit the data
t.fit_on_texts(docs)

#print the proprieties of tokenizer 
print('------ Using Keras Tokenizer --------------')
print('# tokenizer.word_index')
print(t.word_index)
print('# tokenizer.word_counts')
print(t.word_counts)
print('# tokenizer.documento_count')
print(t.document_count)
print('# tokenizer.word_docs')
print(t.word_docs)
#return a matrix with occurrencie or frequencies (depends on mode)
encoded_docs = t.texts_to_matrix(docs,mode='binary') #mode options:  binary count tfidf freq
#print the matrix
print('# Result of tokenizer.texts_to_matrix')
print(encoded_docs)

#-----------------------------------------------------------------------
# These are other ways to process text but less usefull then Tokenizer
#------------------------------------------------------------------------
print('------ Other ways to process text --------------')
text = 'The quick brown fox jumped over the lazy dog.'
#tokenize the document
tokenized_text = text_to_word_sequence(text)
#get a vector of unique words
words = set(tokenized_text)
#number of unique words in the vector
vocab_size = len(words)
#assing a unique integer to each word
result = one_hot(text, round(vocab_size*1.3))
#more sofisticated way of hashing
resultHashing = hashing_trick(text,round(vocab_size*1.3),hash_function='md5')
print('### tokenized text with text_to_word_sequece')
print(tokenized_text)
print('### Size of vocabulary')
print(vocab_size)
print('### vector of words')
print(words)
print('### Result of KERAS ONE_HOT() ')
print(result)
print('### Result of KERAS HASHING_TRICK()')
print(resultHashing)


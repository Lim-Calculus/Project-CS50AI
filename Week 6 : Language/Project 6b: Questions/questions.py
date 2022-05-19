import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    file_dictionary=dict()
    current_directory= "." ## Specifies current directory : . 
    directory_path = os.path.join(current_directory, f"{directory}") ## Directory_path : .\corpus
    for file in os.listdir(directory_path):        
        with open(os.path.join(directory_path, file), encoding="utf-8") as f:
            key=file[:]     
            file_dictionary[key] = f.read()
    return file_dictionary


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    tokenized_word=list()
    tokenized_document = nltk.tokenize.word_tokenize(document)
    for word in tokenized_document:
        tokenized_word.append(word.lower())
    stopwords = nltk.corpus.stopwords.words("english")
    punctuation = string.punctuation    
    finalized_list=list()
    for words in tokenized_word:
        if words not in punctuation and words not in stopwords:
            finalized_list.append(words)
    return finalized_list


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    number_of_dictionary = len(documents)    
    frequencies = dict()    
    for files in documents:
        for word in set(documents[files]):
            if word not in frequencies:
                frequencies[word]=1
            elif word in frequencies:
                frequencies[word]+= 1
    
    ## Calculate IDF
    idfs=dict()
    for word in frequencies:        
        idf = math.log(number_of_dictionary/frequencies[word])
        idfs[word]=idf        
    return idfs
            
    
    



def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tfids=dict()    
    for filename in files:
        tfids[filename]=0 
    
    for filename in files:        
        for word in query:
            if word not in query:
                word_frequency = 1
            elif word in query:
                word_frequency = files[filename].count(word)  
            
            ## Calculate term frequency                 
            tf = word_frequency / len(files[filename])
            
            if word not in idfs:
                idf = 1
            elif word in idfs:
                idf=idfs[word]
            
            ### Calculate tf-idf frequency   
            tfids[filename]=tf*idf
            
    top_n_tfids = sorted(tfids, key=tfids.get, reverse=True)[:n]
            
    return top_n_tfids
            
            
            


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    sentence_value = dict()   
    ## for every sentence in sentences 
    for sentence in sentences:
        sentence_value[sentence] = dict()
        sentence_value[sentence]['idf'] = 0
        sentence_value[sentence]['word_counted'] = 0
        # for every word in query
        for word in query:
            # If word is in sentence, add to word count and its idf to the dictionary
            if word in sentences[sentence]:
                sentence_value[sentence]['idf'] += idfs[word]
                sentence_value[sentence]['word_counted'] += 1
        # Add query term density 
        query_term_density = float(sentence_value[sentence]['word_counted'] / len(sentences[sentence]))
        sentence_value[sentence]['query_term_density'] = float(query_term_density)

    #  return a list of the n top sentences that match the query, ranked according to IDF and query term density
    sorted_sentence_value = sorted(sentence_value.keys(), key=lambda sentence: (sentence_value[sentence]['idf'], sentence_value[sentence]['query_term_density']),reverse=True)
    return sorted_sentence_value[:n]   


if __name__ == "__main__":
    main()

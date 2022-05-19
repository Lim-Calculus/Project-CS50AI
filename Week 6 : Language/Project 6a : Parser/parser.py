import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> S Conj S | VP NP | S P S | S NP | S P NP | NP VP | NP VP NP | NP VP NP VP | S AP | NP AP VP NP | S PP S | S Adv | S PP NP | NP VP NP PP | NP PP NP 
AP -> Adj | Adj AP 
NP -> N | Det NP | AP NP | N PP | Det N | Det AP NP | NP Adv
PP -> P NP
VP -> V | V NP | V NP PP | P | V AP | V P | Adv V | VP Adv


"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    word_tokenize_list=list()
    word_tokenize = nltk.tokenize.word_tokenize(sentence)
    ### If the word containing alphabetic character should be excluded
    for x in word_tokenize:
        if x.isalpha():
            word_tokenize_list.append(x.lower())
        
    return word_tokenize_list


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    NP_list = list()
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            NP_list.append(subtree)

    return NP_list


if __name__ == "__main__":
    main()

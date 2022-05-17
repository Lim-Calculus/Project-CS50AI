import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    

    # check if page has outgoing links
    probability_distribution = dict()
    num_links = len(corpus[page])
    num_pages=len(corpus)

    if num_links >=1:            
        for link in corpus:
            rand_prob = (1-damping_factor) / num_pages
            probability_distribution[link] = rand_prob

        for link in corpus[page]:
            spec_prob = damping_factor / num_links
            probability_distribution[link]= probability_distribution[link]+spec_prob
    else:
        for link in corpus:
            probability_distribution[link] = 1 / len(corpus)
   
    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dist = dict()
    for page in corpus:
        dist[page] = 0
    
    page = random.choice(list(corpus.keys()))

    for i in range(1, n):
        current_dist = transition_model(corpus, page, damping_factor)
        for page in dist:
            dist[page] = ((i-1) * dist[page] + current_dist[page]) / i
        
        dist_sequence_list = list(dist.keys())
        dist_weights_list = list(dist.values())
        page = random.choices( dist_sequence_list, dist_weights_list)[0]
    
    return dist

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    num_pages = len(corpus)
    current = dict()
    new= dict()    
    threshold=0.001

    # assigning each page a rank of 1/ total number of pages in the corpus
    for page in corpus:
        current[page] = 1 / num_pages

    # Repeat all calculation for new rank values base on all of the current rank values
    while True:
        for page in corpus:
            rank = 0
            for link in corpus:
                # check every link to the pages
                if page in corpus[link]:
                    rank += (current[link] / len(corpus[link]))
                # if the page has no links, assumes it as having one link for every other page
                if len(corpus[link]) == 0:
                    rank += (current[link]) / len(corpus)
            ##Page rank Calculation
            rank *= damping_factor
            rank += (1 - damping_factor) / num_pages

            new[page] = rank
            
        difference=list() 
        for x in current:
            difference.append(abs(new[x]-current[x]))       
        
        ## If Max difference < Threshold , break the while loop
        max_difference = max(difference)
        if max_difference < threshold:
            break
        else:
            current = new.copy()
    
    return current


if __name__ == "__main__":
    main()

#I acknowledge Nick for the guidance in this work
import wikipedia
import random

NUM_LINKS = 10
MAX_DOCUMENTS =300  ### !IMPORTANT!: MAKING THIS LARGER/SMALLER WILL MAKE YOUR RETRIEVAL TIME LONGER/SHORTER
MAX_DEPTH = 10
SEED = 'facebook'

p = wikipedia.page(SEED)
pages = {}

# choose a random subsample of the links 
subsample = random.sample(p.links, NUM_LINKS)

# I have defined a recursive function to iterate over the graph of links. Read this and understand how it works. 
def retrieve(list_of_links, depth):
    # print the number every 10th document, just to monitor status
    if not (len(pages) % 10): #This can be changed to anything
        print(len(pages))  
    if len(pages) >= MAX_DOCUMENTS: 
        return pages
    if depth >= MAX_DEPTH: 
        return pages
    for link in list_of_links: 
        try: 
            p = wikipedia.page(link)
            pages[link] = p.content
            subsample = random.sample(p.links, min(len(p.links), NUM_LINKS))  # if a page has less than NUM_LINKS links, then asking for a sample of size MIN_LINKS would throw an error, so we use this min trick
            return retrieve(subsample, depth)
        except: 
            continue
        
pages = retrieve(subsample, 0)

pages_links,pages_contents=zip(*zip(pages.keys(),pages.values()))
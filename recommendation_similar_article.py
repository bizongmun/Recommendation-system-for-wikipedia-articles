from sklearn.metrics.pairwise import cosine_similarity

# Write a function that takes in a text document, 
# and uses the cosine similarity to find the top N most similar documents -- in the SVD-reduced, conceptual space -- to 
# that document, and returns the names of those articles (the 'links') as a list. 

def get_similar_docs(doc,n): 
    sims = cosine_similarity(doc, doc)
    return sims.argsort()[:,::-1][:,:n]

print get_similar_docs(corpus_tfidf_Trunkated_svd)
print pages_contents[10],
print ">>>>>>>>>>>>>>>>>>>>>>>"
print pages_contents[264],
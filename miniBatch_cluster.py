from sklearn.cluster import MiniBatchKMeans 

# Cluster with MiniBatchKMeans
#I experiemented with the number of clusters and I found 15 could good job

def minBactch(Ncluster):
    # feel free to experiment with this value, too
    clstr = MiniBatchKMeans(n_clusters=Ncluster)
    clusters = clstr.fit_predict(corpus_tfidf_Trunkated_svd)
    return clusters
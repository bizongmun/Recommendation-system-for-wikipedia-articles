import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD 

#I plot the number of features versus the cummulative variance
#so that I can be able to select good size data without compromising too much on their variance

corpus_tfidf=corpus_tfidf.toarray()
pca = PCA().fit(corpus_tfidf)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance');
plt.show()


#See the plot to get a good sense of the relation between the two quantities. Based on this graph, I select about 250 out 300 features 
#and maintained nearly 90%variance.

N_COMPONENTS = 250
tsvd = TruncatedSVD(N_COMPONENTS)
corpus_tfidf_Trunkated_svd = tsvd.fit_transform(corpus_tfidf)
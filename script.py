import tabpy_client
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
connection = tabpy_client.Client('http://localhost:9004/')

def kmeans(_arg1,_arg2):
	X = np.column_stack([_arg1,_arg2])
	X = StandardScaler().fit_transform(X)
	kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
	return kmeans.labels_.tolist()

connection.deploy('Kmeans-clust',kmeans,'Returns the clustering label for each individual',override=True)

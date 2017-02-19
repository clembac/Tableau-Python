import tabpy_client
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
connection = tabpy_client.Client('http://localhost:9004/')

def pca2(_arg1,_arg2,_arg3):
	X = np.column_stack([_arg1,_arg2,_arg3])
	X = StandardScaler().fit_transform(X)
	pca = PCA(n_components=2)
	pca.fit(X)
	X = pca.transform(X)

	return X[:,1].tolist()

connection.deploy('pca2',pca2,'Returns PCA coordinate 2',override=True)

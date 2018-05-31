
import math

#sample coordinates (rows)
X = np.arange(9).reshape(3,3)
Y = np.array([[0,0],[4,0],[0,3]])
Z = np.array([[1,2,3,4],[5,2,1,9],[3,5,7,1],[5,7,4,6]])

#sample distance matrix (symmetric)
DM = np.array([[0,4,3],[4,0,5],[3,5,0]])

# given Vector points (one coordinate per row) V, returns distance matrix D where d(i,j) = distance between Vi and Vj
def getDM(X):
    XX = X.dot(X.transpose())
    D = np.zeros(XX.shape)
    _, n = XX.shape
    for i in range(n):
        for j in range(n):
            D[i,j] = math.sqrt(XX[i,i] + XX[j,j] - 2*XX[i,j])
    return D

# given Distance Matrix D, returns an nx2 Vector Matrix V i.e, V[i] = (x,y). The point of origin is the centroid of all points in V
def getXY(DM):
    DM2 = np.multiply(DM,DM)
    B = np.zeros(DM.shape)    
    
    a = DM2.sum()*1.0
    b = DM2.sum(axis=0)
    c = DM2.sum(axis=1)    
    n, _ = DM.shape
    for i in range(n):
        for j in range(n):
            B[i,j] = 0.5*( (b[j]+c[i])*1.0/n - DM2[i,j] - a/(n*n))
            
    U,D,_ = np.linalg.svd(B)
    return U.dot(np.diag(np.sqrt(D)))[:,:2]
    
    

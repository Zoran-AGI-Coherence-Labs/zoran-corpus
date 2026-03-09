
import numpy as np
def coherence_score(X, window=5, kS=50.0):
    X=np.asarray(X,float)
    T,N=X.shape
    C,A,D,S=np.zeros(T),np.zeros(T),np.zeros(T),np.zeros(T)
    for t in range(1,T):
        delta=X[t]-X[t-1]
        A[t]=np.linalg.norm(delta)
        past=np.mean(X[max(0,t-window):t],axis=0)
        D[t]=np.linalg.norm(X[t]-past)
        S[t]=np.var(delta)
        C[t]=1.0/(1.0+D[t]+kS*S[t])
    return C,A,D,S

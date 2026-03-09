def S_zuc(beta1,beta2,beta3,dc1,dc2,dc3,lam_j,lam_f,lam_t,lam_nat,lam_narr):
    num=(beta1*beta2*beta3)*(dc1+dc2+dc3)
    den=lam_j+lam_f+lam_t+lam_nat+lam_narr
    return num/den

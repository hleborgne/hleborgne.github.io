import numpy as np

def mNRG(sco,theoric_max):
    """
    theoric_max : real or vector with shape (1,nb_bench)
    """
    ref=np.ones((sco.shape[0],1))*sco[0,:]

    maxi=np.ones(sco.shape)*theoric_max

    denominator = maxi-ref
    denominator=np.where(denominator < 1e-16, 1, denominator)

    return np.median( (sco-ref)/denominator, axis=1)


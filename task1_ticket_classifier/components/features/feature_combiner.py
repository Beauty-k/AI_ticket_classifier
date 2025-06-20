import numpy as np
from scipy.sparse import hstack as sparse_hstack

class FeatureCombiner:
    def __init__(self, engineers):
        self.engineers = engineers

    def combine(self, df):
        features = []
        for eng in self.engineers:
            f = eng.extract(df)
            # Convert 1D arrays to 2D column vectors
            if isinstance(f, np.ndarray) and f.ndim == 1:
                f = f.reshape(-1, 1)
            features.append(f)

        # If any feature is sparse, use sparse hstack
        if any('sparse' in str(type(f)).lower() for f in features):
            return sparse_hstack(features)
        else:
            return np.hstack(features)
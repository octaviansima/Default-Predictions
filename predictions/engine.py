from sklearn.externals import joblib
import numpy as np

class Engine:

    def __init__(self):
        self.cat_pipeline = None
        self.model = None
        self.num_pipeline = None
        self.pca = None

    def load_pickle(self):
        self.cat_pipeline = joblib.load("predictions/saves/cat_pipeline.pkl")
        self.model = joblib.load("predictions/saves/model.pkl")
        self.num_pipeline = joblib.load("predictions/saves/num_pipeline.pkl")
        self.pca = joblib.load("predictions/saves/pca.pkl")

    def pd_to_vector(self, numerical, categorical):
        num_prepared = self.num_pipeline.fit_transform(numerical)
        cat_prepared = self.cat_pipeline.fit_transform(categorical)
        x = np.concatenate((num_prepared, cat_prepared.toarray()), axis=1)
        return x
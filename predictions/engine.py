from sklearn.externals import joblib

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
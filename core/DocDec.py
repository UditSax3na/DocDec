from pathlib import Path
from config.path import DATASETFILE, SVMMODEL, TFIDF_VECTORIZER
from core.ErrorDef.ErrorDef import DatasetNotFound
import pandas as pd
import joblib

class DocDec():
    def __init__(self):
        if not SVMMODEL.exists():
            raise DatasetNotFound()
            exit()
        if not TFIDF_VECTORIZER.exists():
            raise 
        self.MODEL = joblib.load(SVMMODEL)
        self.VECTORIZER = joblib.load(TFIDF_VECTORIZER)


    def Predict(self, x:str|list):
        newDoc = self.VECTORIZER.transform([x])
        print(f'Prediction is : {self.MODEL.predict(newDoc)[0]}')
        return self.MODEL.predict(newDoc)[0]
        
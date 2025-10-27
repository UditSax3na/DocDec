from pathlib import Path

# Folders
ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / 'config'
CORE_DIR = ROOT / 'core'
LOG_DIR = ROOT / 'logs'

# Custom Paths
DATASET = ROOT / 'Dataset'
SAVEDDATA = ROOT / 'SavedData'

# File names
DATASETFILE = SAVEDDATA / 'document_dataset.csv'
SVMMODEL = SAVEDDATA / 'SavedModels' / 'svm_classifier.joblib'
TFIDF_VECTORIZER = SAVEDDATA / 'SavedVectorizer' / 'tfidf_vectorizer.joblib'

# Files
LOG_FILE = LOG_DIR / 'log.log'

# Function to create folder if don't exists  
def dirCheck():
    for path in [CONFIG_DIR, CORE_DIR, LOG_DIR, DATASET, SAVEDDATA]:
        path.mkdir(parents=True, exist_ok=True)
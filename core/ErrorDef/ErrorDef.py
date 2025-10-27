class Error(Exception):
    '''Error base class'''
    pass

class DatasetNotFound(Error):
    '''Dataset not found'''
    pass

class VectorizerNotFound(Error):
    '''VectorizerNotFound on the given Path'''
    pass
from abc import ABC, abstractmethod

class Analyser(ABC):

    classifiers = ["DISGUST", "HAPPINESS", "NEUTRAL", "ANGER", "SURPRISE", "SADNESS", "NOFACE"]

    @abstractmethod
    def loadModel(self):
        pass
    
class DataLoader(ABC):

    @abstractmethod
    def loadData(self,path):
        pass

    @abstractmethod
    def loadMulti(self,folderpath):
        pass
    

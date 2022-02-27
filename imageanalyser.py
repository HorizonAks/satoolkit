import abstracts as ab
from numpy import asarray
import numpy as np
from PIL import Image
import tensorflow as tf
import os
from mtcnn.mtcnn import MTCNN
import utils

#TODO - A function to display image in pyplot

class ImageAnalyser(ab.Analyser):
    """
    Current incapabilities:
        only capable of analysing 1 image at a time
        Multiple faces not supported in detect_face
        Classifiers fixed
    """
    model = None
    __detector = MTCNN()
    def __init__(self,imgarr):
        self.__pixels = imgarr
        if ImageAnalyser.model == None:
            ImageAnalyser.loadModel(r".\ImageModel")
        self.__sentiment = self.predictor()

    def get_results(self):
        return self.__sentiment
    
    @classmethod
    def loadModel(cls,modelpath):
        cls.model = tf.keras.models.load_model(modelpath + r'/bin')

    def predictor(self):
        image = self.detect_face()
        image = image/255.0
        image = tf.constant([[image]])
        image = tf.data.Dataset.from_tensor_slices(image)
        results = ImageAnalyser.model.predict(image)
        #print("Classifier:\n")
        #limited to 1 image
        self.__sentiments = utils.mapper(asarray(results[0]) * 100,emotions)
        #print("Prediction = " + super().classifiers[np.argmax(results[0])])
        return super().classifiers[np.argmax(results[0])]

    def detect_face(self):
        detector = ImageAnalyser.__detector
        results = detector.detect_faces(self.__pixels)
        if len(results) == 0:
            image = Image.fromarray(self.__pixels)
            image = image.resize((160,160))
            return asarray(image)
        x1,y1,width,height = results[0]['box']
        #implement loop for multiple images
        x1,y1 = abs(x1),abs(y1)
        x2,y2 = x1 + width, y1 + height
        face = self.__pixels[y1:y2,x1:x2]
        image = Image.fromarray(face)
        image = image.resize((160,160))
        face_array = asarray(image)
        return face_array



class ImageLoader(ab.DataLoader):
    
    def __init__(self,path,multi=False):
        self.multi = multi
        if multi:
            self.__images = self.loadMulti(path)
        else:
            self.__image = self.loadData(path)

    def loadData(self,path):
        # load image from file
        image = Image.open(path)
        # convert to RGB, if needed
        image = image.convert('RGB')
        # convert to array
        pixels = asarray(image)
        return pixels

    def loadMulti(self,folderpath):
        images = []
        for filename in os.listdir(folderpath):
            img = cv2.imread(os.path.join(folderpath,filename))
            if img is not None:
                images.append(img)
        return images

    def getImageAsArray(self):
        return self.__images if self.multi else self.__image
    

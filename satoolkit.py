from imageanalyser import ImageLoader
from imageanalyser import ImageAnalyser

class invalidType(Exception):
    pass

def analyse(path,typ):
    typ.lower()
    valid = ["image","text","video","audio"]
    if typ == "image":
        img = ImageLoader(path)
        analysed = ImageAnalyser(img.getImageAsArray())
        print("Sentiment:",analysed.get_results())
    elif typ == "text":
        pass
    elif typ == "video":
        pass
    elif typ == "audio":
        pass
    else:
        raise invalidType("Invalid Type Specified, can only parse Image/Video/Text/Audio")


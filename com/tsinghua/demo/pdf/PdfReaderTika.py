import tika
tika.initVM()
from tika import parser

def readPara(path):
    parsed = parser.from_file(path)
    print(parsed["content"].strip())

if __name__ == '__main__':
    path = 'C:\\Users\\FEIFEI\\Desktop\\金融知识图谱项目\\test\\1210827387.PDF'
    readPara(path)
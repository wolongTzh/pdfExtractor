import PyPDF4

def readPara(path):
    with open(path, mode='rb') as f:
        reader = PyPDF4.PdfFileReader(f)
        page = reader.getPage(0)
        print(page.extractText().strip())

if __name__ == '__main__':
    path = 'C:\\Users\\FEIFEI\\Desktop\\金融知识图谱项目\\test\\1210827387.PDF'
    readPara(path)
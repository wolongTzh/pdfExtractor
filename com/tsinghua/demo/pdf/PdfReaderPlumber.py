import pdfplumber as pr
import pandas as pd

def readPdfTables(path):
    pdf = pr.open(path)
    ps = pdf.pages
    for pg in ps:
        tables = pg.extract_tables()
        for table in tables:
            # print(table)
            df = pd.DataFrame(table[1:],columns = table[0])
            for i in range(len(table)):
                # print(table[i])
                for j in range(len(table[i])):
                    table[i][j] = table[i][j]
                    print(table[i][j])
            df1 = pd.DataFrame(table[1:], columns=table[0])
            # print(df)

def readPdfParasRaw(path):
    pdf = pr.open(path)
    ps = pdf.pages
    for pg in ps:
        words = pg.extract_words()
        for word in words:
            print(word)

def readPdfParas(path):
    pdf = pr.open(path)
    content = ''
    for i in range(len(pdf.pages)):
        page = pdf.pages[i]
        print(page.extract_text())
        page_content = '\n'.join(page.extract_text().split('\n')[:-1])
        content = content + page_content
        # print(content)

if __name__ == '__main__':
    path = 'C:\\Users\\FEIFEI\\Desktop\\金融知识图谱项目\\test\\1210827387.PDF'
    readPdfTables(path)


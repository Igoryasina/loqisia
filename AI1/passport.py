import xlwings
import pandas as pd
mas = []
line_words = []
mark = []
allWeights = []
mark2 = []
weightSum = 0
currentCountCols = 0
strr = 'Оценка актуальности выбранной программы по направлению '
case = [
        'AI (Искусственный интеллект)',
        'VR and AR ',
        'Date Tech ',
        'Distributed Sys ',
        'Games ',
        'Robots '
        ]
tableLenght = ['194','61','210','90','92']
wb = xlwings.Book("618EDF20.xlsx")



for i in range(5): 
    data_excel = wb.sheets[str(i)]
    tableRange = 'B1:C' + tableLenght[i]
    data_pd=data_excel.range(tableRange).options(pd.DataFrame, header = 1, index = False).value


    mas = list(data_pd.iloc[:, 0].values)
    allWeights = data_pd.iloc[:,1].values

    with open("PostgreSQL_проектирование_базы_данных_написание_запросов_и_оптимизация.txt","r",encoding="utf-8") as file:
        weightSum = 0
        line = file.read()
        for j in mas:
            if line.find(j) > -1:
                ind = mas.index(j)
                mark.append(allWeights[ind])
                        
                
                weightSum += allWeights[ind]     
                    
    print(strr, case[int(i)], weightSum)
                    
                    
            
            


                         

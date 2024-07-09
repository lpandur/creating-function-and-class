class multiunivariate():
    def quanQual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtypes=='O'):
                #print("qual")
                qual.append(columnName)
            else:
               # print("quan")
                quan.append(columnName)
        return quan,qual
    def freqTable(columnName):
        freqTable=pd.DataFrame(columns=["Unique_Values","Freqency","Ralative _Frequency","cusum"])
        freqTable["Unique_Values"]=dataset[columnName].value_counts().index
        freqTable["Freqency"]=dataset[columnName].value_counts().values
        freqTable["Ralative _Frequency"]=freqTable["Freqency"]/103
        freqTable["cusum"]=freqTable["Ralative _Frequency"].cumsum()
        return freqTable
    def analysis(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5Rule","lesser_outlier","Higher_outlier","mini","max"],columns=quan)
        for columnName in quan:
            descriptive.loc["Mean", columnName] = dataset[columnName].mean()
            descriptive.loc["Median", columnName] = dataset[columnName].median()
            descriptive.loc["Mode", columnName] = dataset[columnName].mode()[0]
            descriptive.loc["Q1:25%", columnName] = dataset.describe()[columnName]["25%"]
            descriptive.loc["Q2:50%", columnName] = dataset.describe()[columnName]["50%"]
            descriptive.loc["Q3:75%", columnName] = dataset.describe() [columnName]["75%"]
            descriptive.loc["99%", columnName] = np.percentile(dataset[columnName],99)
            descriptive.loc["Q4:100%", columnName] = dataset.describe() [columnName]["max"]
            descriptive.loc["IQR", columnName] = descriptive.loc["Q3:75%", columnName]-descriptive.loc["Q1:25%", columnName]
            descriptive.loc["1.5Rule", columnName]=1.5*descriptive.loc["IQR", columnName]
            descriptive.loc["lesser_outlier", columnName]=descriptive.loc["Q1:25%", columnName] -descriptive.loc["1.5Rule", columnName]
            descriptive.loc["Higher_outlier", columnName]= descriptive.loc["Q3:75%", columnName]+descriptive.loc["1.5Rule", columnName]
            descriptive.loc["mini", columnName]=dataset[columnName].min()
            descriptive.loc["max", columnName]=dataset[columnName].max()
        return descriptive


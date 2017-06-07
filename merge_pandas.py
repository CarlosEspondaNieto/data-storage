import pandas as pd
import csv 
import json


#raabrir la el csv
f=pd.read_csv('/home/administradorcito/data-storage/data-graduates/Introduction_01/data/countries.csv')
f.head()
print(f)

with open('/home/administradorcito/data-storage/data-graduates/Introduction_01/data/countries.json') as data_file:
	data=json.load(data_file)
	dataFrame=pd.DataFrame(data)
for i in range(0, len(data)):
	var=['name'][i]=dfaux.loc[:,('name',i)]
var2=pd.read
	
#pd.concat([f, data])






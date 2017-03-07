import pandas as pd
import csv 
import json

#j_df=pd.read_json('/home/administradorcito/data-storage/data-graduates/Introduction_01/data/countries.json')
#j_str=j_df.to_json()
#j_obj = json-loads(j_str)

#for i in j_obj:
 #       print(i)

#for i in j_job['name']
  #      print(i)

#Para abrir la el csv
#f= open('/home/administradorcito/data-storage/data-graduates/Introduction_01/data/countries.csv')
#csv_f= csv.reader(f)

with open('/home/administradorcito/data-storage/data-graduates/Introduction_01/data/countries.json') as data_file:
	data=json.load(data_file)
	data[0]
	#keys = data[0].keys()

#for i in data:
#	print(i)



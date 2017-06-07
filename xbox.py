#import csv
import pandas as pd
import math 
#nd = pd.DataFrame({ 'item': 'xbox',
#					'daystolive' : 3
#	}) 

f = pd.read_csv('xbox.csv')

#full fill None values with 0
f = f.fillna(0)
#f.to_csv(r'dataframexbos.csv', sep= ',')

#Adding a index
f['index'] = range(1, len(f) + 1)

#Creating two lists: item and daystolive
item = ['xbox' for i in range(len(f))]
daystolive = [3 for i in range(len(f))]
#print(item)
#print(daystolive)

#Converting the lists into a Dataframe
itemDays = pd.DataFrame(
	{'item': item,
	'daystolive': daystolive	
	})

#Rearrange the columns
cols = ['item', 'daystolive']
itemDays = itemDays[cols]

#Adding a index
itemDays['index'] = range(1, len(itemDays) + 1)
result = pd.merge(f,itemDays, on = 'index')
#Rearrange the columns of the result
#result = result[['auctionid', 'bid', 'bidtime', 'bidder', 'bidderrate', 'openbid', 'price', 'item', 'daystolive']]
#print(result)
#result.drop('index', axis=1, inplace=True)
print(result)
#result.to_csv(r'xboxData.csv', sep=',')


	
#print(f)
# f = open('../xbox.csv')
#csv_f = csv.reader(f)

#dataFrame=pd.DataFrame(csv_f)
#print(dataFrame)

#for row in csv_f:
#	print(row)

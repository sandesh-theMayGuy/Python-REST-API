import pandas as pd
import numpy as np 

#Readihingng a csv to a data frame
df=pd.read_csv('products.csv')


#Fetching specific coloumns from the dataset
my_products=np.array(df['Products'])

print(my_products) 


# reading json and converting into json

dj = pd.read_json('products.json')
products = np.array(dj['Products'])


print(products) 


### Import Libraries
import requests
import pandas as pd
import json
import csv

### Fetch API Data
response = requests.get("https://restcountries.com/v3.1/all").text


### Add country data to dictionaries
response_value = json.loads(response)
type(response_value)

### Save Data into a csv
# csv_response_value = csv.writer(response_value)

### Read csv file and convert data to pandas dataframe

df = pd.DataFrame(response_value)

### Display head of dataframe
print(df.head())

### Countries with highest population
ratio = df.sort_values(by='population', ascending=False).head(9)
print(ratio)

### Clean data (Dropping Nan values and rounding numerical values in columns

del df["tld"]
del df["cca2"]
del df["ccn3"]
del df["cca3"]
del df["cioc"]
del df["independent"]
del df["status"]
del df["unMember"]
del df["currencies"]
del df["capital"]
del df["altSpellings"]
del df["region"]
del df["car"]
del df["maps"]

del df["demonyms"]
del df["gini"]
del df["subregion"]
del df["languages"]
del df["translations"]
del df["landlocked"]
del df["borders"]
del df["area"]
del df["continents"]
del df["flags"]
del df["coatOfArms"]
del df["startOfWeek"]
del df["postalCode"]
del df["flag"]
del df["fifa"]
del df["capitalInfo"]

col_list =  list(df["idd"])
val = ""
idd = []
name = []
latitude = []
longitude = []
no_of_timezones=[]
for x in range(len(col_list)):
  
  for key1,value1 in col_list[x].items():
      b=""  
      if key1 == "root":
        a = value1
      else:
        b = value1[0]
        
      val = a+b
  idd.append(val)
for char in response_value:
  
  for key, value in char.items():
    
    if key == "name":
      for key2, value2 in value.items():
        if key2 =="common":
          name.append(value2)
    elif key == "latlng":
      latitude.append(value[0])
      longitude.append(value[1])
    elif key == "timezones":
      no_of_timezones.append(len(value))

df["idd"] = idd
df["name"] = name
df["latlng"] = latitude
df.insert(3, "longitude", longitude)
df.columns.values[2:3] = ["latitude"]
df["timezones"] = no_of_timezones
df.columns.values[5:6] = ["no_of timezones"]

### Countries with highest population after cleaning data 

ratio = df.sort_values(by='population', ascending=False).head(9)
print(ratio)

### Save modified dataframe to csv

countries = ratio.to_csv(r'D:\Documents\Documents\JOB\countries.csv')







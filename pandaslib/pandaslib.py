import pandas as pd
import numpy as np
"""print("creat data frame:")
data_dict = {
    "ID": [1, 2, 3, 1, None],
    "name": ["abdul wahab", "waji", "fahad", "rajab", None],
    "age": [12, 34, np.nan, 54, None],
    "salary": [12000, 22000, 34000, 13000, None]
}
print(pd.DataFrame(data_dict))

print("import excel file in pycharm and read:")"""

data=pd.read_excel("wahab1_excel.xlsx")
data1=pd.read_csv("wahab_csv.csv")
data2=pd.read_excel("Book1.xlsx")

#USE HEAD FUCTION:
"""print("Exploring Data.....?","Head function....check value for uper wali uper")
print(data.head(20))

#USE TAIL FUCTION:
print("EXPLORING DATA...?", " TAIL FUNCTION CHECK VALUE FOR DOWN:")
print(data.tail(20))
# USE INFO FUNCTION:
print("CHECK DATA TYPE:")
print(data.info())
#USE DESCRIBE FUNCTION:
print("CHECK FOR..MEAN..MIN,MAX..COUNT..STD..%")
print(data.describe())
#USE ISNULL FUNCTION:
print("CHECK FOR NULL VALUE IN MY EXCEL FILE:")
print(data.isnull())
print("sum of null value:")
print(data.isnull().sum())
print("HANDLING DUPLICATE VALUE IN PANDAS:")
#USE DUPLICATED FUNCTION:
print("CHECK DUPLICATED VALUE FOR ROW WISE IN EXCEL FILE:")
print(data.duplicated())
print("SUM OF DUPLICATED VALUE:")
print(data.duplicated().sum())
print("HANDLING DUPLICATED VALUE IN MY CSV FILE:")
#USE DUPLICATED FUNCTION:
print(data1.duplicated())
print("SUM OF DUPLICATED VALUE:")
print(data1.duplicated().sum())
print("CHECK DUPLICATED VALUE COLUMN WISE:")
print(data1["EEID"].duplicated())
print(data1["EEID"].duplicated().sum())
#USE DROP_DUPLICATES FUNCTION:
print("DROP_DUPLICATES VALUE IN COULMN RESULT GIVE FOR UNIQUE VALUE:")
print(data1.drop_duplicates("EEID"))
print("WORKING WITH MISSING DATA IN PANDAS:")
#USE DROPNA FUNCTION:
print(data1.dropna())# all null value remove:
print("ADD VALUE FOR USE REPLACE FUNCTION:")
#USE FILLNA FUNCTION:
print("HUMARI VALUE KO ADD KARA GA JAHN NULL VALUE HAI:")
print(data1.fillna("wahab"))
#USE REPLACE FUNCTION:
print(data1.replace(np.nan,3000))
print("ADD VALUE FOR SPECIFIC COLUMN:")
data1["salary"]=data1["salary"].replace(np.nan,3000)
print(data1)
print("USE SECOND METHOD:")
print(data1["salary"].mean())
print("WELCOME.......?")
data1["salary"]=data1["salary"].replace(np.nan,24400.0)
print(data1)
#USE BACKWARD FUNCTION:
print("NECHA WALI VALUE KO UPER KAR DAA GA:")
print(data1.fillna(method="bfill"))
#USE FORWARD METHOD:
print("UPER WALI VALUE KO NECHA KAR DA GA:")
print(data1.fillna(method="ffill"))

#COLUMN TRANSFORMATIONS IN PANDAS:
print("EK EXIST COLUMN SA NEW COLUMN CREATE KARNA:")
data.loc[(data["Bonus %"]==0), "GetBonus"]="No Bonus:"
data.loc[(data["Bonus %"]>0),"GetBonus"]="Bonus"
print(data.head(10))
a=np.arange(12)
print(a)
#USE RESHAPE FUNCTION
print("1D ARRAY CONVERT 2D ARRAY:")
print(a.reshape(4,3))

#USE CONCATENATION FUNCTION:
print("ADD TWO COLUMN FOR CREATE ANTHOR COLUMN:")
data2["Full_name"]=data2["first name"]+" "+data2["last_name"]
print(data2)
#STR.UPPER CASE FUNCTION:
print("FIRST NAME CONVERT ALL UPPER CASE LETTER:")
data2["Full_name"]=data2["first name"].str.upper() +" "+ data2["last_name"]
print(data2)
#STR.UPPER CASE FUNCTION:
print("FIRST NAME CONVERT ALL UPPER CASE LETTER:")
data2["Full_name"]=data2["first name"] +" "+ data2["last_name"].str.upper()
print(data2)
#STR.LOWER CASE FUNCTION:
print("UPPER CASE CONVERT FOR LOWER CASE:")
data2["full_name"]=data2["first name"].str.lower()+ " "+ data2["last_name"]
print(data2)
#STR.LOWER CASE FUNCTION:
print("UPPER CASE CONVERT FOR LOWER CASE:")
data2["full_name"]=data2["first name"]+ " "+ data2["last_name"].str.lower()
print(data2)
#USE CAPITALIZE FUNCTION:
print("FIRST LETTER ARE CAPITALIZE:")
data2["full_name"]=data2["first name"].str.capitalize()+" "+ data2["last_name"].str.capitalize()
print(data2)
#CREATE NEW COLUMN:
print("EXISTED COLUMN SA NEW COLUMN NIKAL NA 20% bonus found:")
data2["Bonus"]=(data2["salary"]/100)*20
print(data2)
print("FIND 10% BONUS:")
data2["Bonus"]=(data2["salary"]/100)*10
print(data2)
dict={"month":["january","february","march","april"]}
a=pd.DataFrame(dict)
print(a)
#USE MAP FUNCTION:
print("maping all indexing:")
def extract(value):
    return value[0:3]

a["short_month"] = a["month"].map(extract)
print(a)
# SUMMARIZE DATA:
print("GROUP BY IN PANDAS:")
s=data.groupby("Department").agg({"Gender":"count"})

print("SUB CATERIGE:")
p=data.groupby(["D    epartment","Gender"]).agg({"EEID":"count"})
print(p)
r=data.groupby("Country").agg({"Age":"mean"})
print(r)
i=data.groupby("Country").agg({"Age":"max"})
print(i) 
j=data.groupby("Country").agg({"Age":"min"})
print(j)
k=data.groupby("Country").agg({"Age":"sum"})
print(k)
l=data.groupby("Country").agg({"Age":"count"})
print(l)
l=data.groupby(["Country","Gender"]).agg({"Annual Salary":"mean"})
print(l)
k=data.groupby(["Country","Gender"]).agg({"Annual Salary":"max","Age":"min"})
print(k)

dict1={
    "Emp ID":["E01","E02","E03","E04","E05","E06"],
    "Name":["Wahab","hunain","raja","rajab","ali","fahad  "],
    "Age":[12,34,15,18,19,20]
}
dict2={
"Emp ID":["E01","E02","E03","E04","E05","E06"],
    "Salary":[12000,15000,34000,23000,18000,21000]

}
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)
print("TABLE ONE IS:")
print(df1)
print("TABLE TWO IS:")
print(df2)
#MERGE FUNCTION:
print("THE MERGE OF TWO TABLE BASES OF FOREIGN KEY:")
print(pd.merge(df1,df2,on="Emp ID"))
dict1={
    "Emp ID":["E01","E02","E03","E04","E05","E06"],
    "Name":["Wahab","hunain","raja","rajab","ali","fahad  "],
    "Age":[12,34,15,18,19,20]
}
dict2={
"Emp ID":["E01","E07","E03","E04","E08","E06"],
    "Salary":[12000,15000,34000,23000,18000,21000]

}
df1=pd.DataFrame(dict1)
df2=pd.DataFrame(dict2)
#USE MERGE FUNCTION:
print("TWO TABLE ARE JOIN BUT BUT FOREIGN KEY ARE MISSING:")
print(pd.merge(df1,df2,on="Emp ID"))
#USE JOIN:
print("TWO TABLE ARE MERGE BUT DIFFERENT JOIN USES:")
print(pd.merge(df1,df2,on="Emp ID",how="inner"))
#USE LEFT JOIN:
print("USE LEFT JOIN BUT ALL VALUE PRINT FOR LEFT TABLE DATA:")
print(pd.merge(left=df1,right=df2,on="Emp ID",how="left"))
#USE RIGHT JOIN:
print("TWO TABLE ARE MERGE BUT ALL VALUE PRINT FOR RIGHT TABLE DATA:")
print(pd.merge(left=df1,right=df2,on="Emp ID",how="right"))
sapi1={
    "Emp ID":["E01","E02","E03","E04","E05","E06"],
    "Name":["Wahab","hunain","raja","rajab","ali","fahad  "],
    "Age":[12,34,15,18,19,20]
}
sapi2={
    "Emp ID":["E07","E08","E09","E010","E11","E12"],
    "Name":["chotu","pappu","raju","waju","nehu","rahu"],
    "Age":[12,34,15,18,19,20]
}
df1=pd.DataFrame(sapi1)
df2=pd.DataFrame(sapi2)
 #USE CONCATE FUNCTION:
print("CONCATE OF TWO TABLE:")
print(pd.concat([df1,df2]))
dict={
    "Fruits":["mango","apple","bananna","papaya"],
    "Price": [100,150,50,100],
    "Quantity":[4,6,2,5]

}
df=pd.DataFrame(dict)
print(df)
#PANDAS| COMAPRE DATAFRAME:
print("PANDAS| COMPARE DATAFRAME:")
df1=df.copy()
df1.loc[0,"Price"]=200
df1.loc[1,"Price"]=250
df1.loc[2,"Price"]=50
df1.loc[3,"Price"]=200
df1.loc[0,"Quantity"]=10
df1.loc[1,"Quantity"]=12
df1.loc[2,"Quantity"]=2
df1.loc[3,"Quantity"]=20
print(df1)
#USE COMPARE FUNCTION:
print("COMPARE VALUE TELL ME ABI AUR PHELA KI PRICE BATA TA HAI:")
print(df.compare(df1,align_axis=0))
#USE KEEP EQUAL FUNCTION:
print("USE KEEP EQUAL FUNTION:")
print(df.compare(df1,keep_equal=True))
#USE KEEP SHAPE FUNCTION:
print("USE KEPP_SHAPE TRUE FUNCTION:")
print(df.compare(df1,keep_shape=True))
print("USE KEPP_SHAPE FALSE FUNCTION BUT CHANGING IN MY DATA:")
print(df.compare(df1,keep_shape=False))
dict={
    "Key":["k1","k2","k1","k2"],
    "Name":["john","wahab","zeeshan","Rehan"],
    "Houses":["Red","Green","Blue","Red"]
}
df=pd.DataFrame(dict)
print(df)
#PANDAS| PIVOTING AND MELTING DATAFRAME:
print("PANDAS PIVOTING AND MELTING DATAFRAME:")
pivoted_df=df.pivot(index="Key",columns="Name",values="Houses")
print(pivoted_df)
dict1={
    "Key":["k1","k2","k1","k2"],
    "Name":["john","wahab","zeeshan","Rehan"],
    "Houses":["Red","Green","Blue","Red"],
    "Grades":["1st","2nd","3rd","4th"]
}

df1=pd.DataFrame(dict1)
print(df1)
print("PIVOTING TABLE:")
print(df1.pivot(index="Key", columns="Name",values=["Houses","Grades"]))"""
dict1={
    "Name":["john","wahab","zeeshan","Rehan"],
    "Houses":["Red","Green","Blue","Red"],
    "Grades":["1st","2nd","3rd","4th"]
}
df=pd.DataFrame(dict1)
print("USE MELT FUNCTION:")
print(pd.melt(df,id_vars=["Name"],value_vars=["Houses"]))
#print("ADD COLUMNS GRADES:")
#print(pd.melt(df,id_vars=["Name"],value_vars=["Houses","Grades"]))
print(pd.melt(df,id_vars=["Name"],value_vars=["Houses","Grades"],var_name="Houses&Grades",value_name="values  "))
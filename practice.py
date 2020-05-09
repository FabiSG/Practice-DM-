# -*- coding: utf-8 -*-
"""
Created on Mon May  4 01:17:35 2020

@author: Fabi
"""

"""
====================================================================
=************1. Annual salary per Gender.*************=
====================================================================
"""
import pandas as pd
import matplotlib.pyplot as plt
def Gender(tp,x):
    data=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    salary=data[[tp,"ConvertedComp"]]
    salary_x=[]
    for i in range(len(salary)):
        y=salary.iat[i,0]  # datos por indices               
        if not(pd.isna(y)):
            if ( x in y):
                salary_x.append(salary.iat[i,1])
    gender_x=pd.DataFrame(salary_x)
    gender_x.columns=["ConvertedComp"]
    gender_x=gender_x["ConvertedComp"].describe()
    plt.boxplot(gender_x)
    plt.title('Gender')
    return gender_x
print('**Men**')
print(Gender('Gender','Man'))
print('**Women**')
print(Gender('Gender','Woman'))
print('**Non-binary**')
print(Gender('Gender','Non-binary, genderqueer, or gender non-conforming'))

"""
==========================================================================
=************2. Annual salary per Ethnicity. .*************
==========================================================================
"""
def race(tp,x):
    import pandas as pd
    import matplotlib.pyplot as plt
    data=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    salary=data[[tp,"ConvertedComp"]]
    salary_x=[]
    for i in range(len(salary)):
        y=salary.iat[i,0]  # datos por indices               
        if not(pd.isna(y)):
            if ( x in y):
                salary_x.append(salary.iat[i,1])
    data_x=pd.DataFrame(salary_x)
    data_x.columns=["ConvertedComp"]
    data_x=data_x["ConvertedComp"].describe()
    plt.boxplot(data_x)
    plt.title('Race ')
    return data_x
print('***White or of European descent***')
print(race('Ethnicity','White or of European descent'))
print('***South Asian***')
print(race('Ethnicity','South Asian'))
print('***Hispanic or Latino/Latina***')
print(race('Ethnicity','Hispanic or Latino/Latina'))
print('***East Asian***')
print(race('Ethnicity','East Asian'))
print('***Middle Eastern***')
print(race('Ethnicity','Middle Eastern'))
print('***Black or of African descent***')
print(race('Ethnicity','Black or of African descent'))
print('***Multiracial***')
print(race('Ethnicity','Multiracial'))
print('***Biracial***')
print(race('Ethnicity','Biracial'))
print('*Ethnicity','Native American, Pacific Islander, or Indigenous Australian*')
print(race('Ethnicity','Native American, Pacific Islander, or Indigenous Australian'))

"""
==========================================================================
=************3. Annual salary per DevType. .*************
==========================================================================
"""
def Resu(tp,name):
    df=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    t=df[[tp,'ConvertedComp']]
    sal=[]
    for i in range(0,len(t)):    
        m=t.iat[i,0]
        if not (pd.isna(m)):   
            if(name in m):
                sal.append(t.iat[i,1])           
    df2=pd.DataFrame(sal)
    df2.columns= ['ConvertedComp']
    return df2

def Dt(n):
    df2=Resu('DevType',n)
    h=df2['ConvertedComp'].describe().T
    print(n)
    print(h)
    spread = h['max']#maximo valor a graficar 
    center = h['50%']#parte centrar 
    flier_high =h['75%']
    flier_low = h['25%']
    data = ((spread, center, flier_high, flier_low))
    fig1, ax1 = plt.subplots()
    ax1.set_title('Developer Type')
    ax1.boxplot(data)
Dt('Designer')
Dt('Student')
Dt('Scientist')
Dt('Developer, desktop or enterprise applications')
Dt('Developer, front-end')
Dt('Data or business analyst')
Dt('System administrator')
Dt('Database administrator')
Dt('Developer, back-end')
Dt('Developer, QA or test')
Dt('Academic researcher')
Dt('Developer, full-stack')
Dt('Developer, mobile')
Dt('DevOps specialist')
Dt('Engineer, data')
Dt('Educator')
Dt('Engineer, site reliability')
Dt('Engineering manager')
Dt('Marketing or sales professional')
Dt('Senior executive/VP')
Dt('Product manager')
Dt('Developer, game or graphics')
Dt('Data scientist or machine learning specialist')
Dt('Developer, embedded applications or devices')

def program_gen():
    import pandas as pd
    df=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    R=df['DevType']
    k=[]  
    for i in R:
        if not (pd.isna(i)):
            l=split_type(i)
            for j in l:
                k.append(j)
    df2=pd.DataFrame(k)
    df2.columns= ['Lenguage']
    df2['Lenguage'].value_counts().plot(kind='bar')

program_gen()

"""
==========================================================================
=************4. Annual salary per Country.*************
==========================================================================
"""
def Country(tp,x):    
    import pandas as pd
    data=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    country_x=data[data[tp]== x]
    country_x=country_x["ConvertedComp"].describe()
    print("Mean, median, standard D. annual Salary per Country\n")
    print("Mean: " +str(country_x[1]))
    print("Median: " +str(country_x[2]))
    print("Median: " +str(country_x[5]))
print(Country('Country','United Kingdom'))
print(Country('Country','Bosnia and Herzegovina'))
print(Country('Country','Thailand'))
print(Country('Country','United States'))
print(Country('Country','Canada'))
print(Country('Country','India'))
print(Country('Country','Ukraine'))
print(Country('Country','Antigua and Barbuda'))
print(Country('Country','Germany'))
print(Country('Country','Brazil'))
print(Country('Country','Lithuania'))


"""
==========================================================================
=************5. Bar plot for each developer type. .*************
==========================================================================
"""
def split_type(x):
    l=[]
    aux=" "
    j=0
    for i in x:
        j+=1
        if(i==';'):
            l.append(aux)
            aux=" "
        else:
            aux+=i
            if(j==len(x)):
                l.append(aux)            
    return l

def dev_type():
    import pandas as pd
    df=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    R=df['DevType']
    k=[]  
    for i in R:
        if not (pd.isna(i)):
            l=split_type(i)
            for j in l:
                k.append(j)
    df2=pd.DataFrame(k)
    df2.columns= ['Lenguage']
    df2['Lenguage'].value_counts().plot(kind='bar')

dev_type()

"""
==========================================================================
=************6.                                  .*************
==========================================================================
"""
def YC(df):
    print('Plot histograms with 10 bins for the years of experience with coding per gender')
    df_filter = (df['YearsCode'].notnull()) & (df['YearsCode'] != '')
    df_filter2 = (df['Gender'].notnull()) & (df['Gender'] != '')
    data = df[df_filter2]['Gender'].str.split(';')
    aux = []
    for element in data:
        for e in element:
            if e not in aux:
                aux.append(e)

    genders = aux

    filter_2 = (df_filter) & ( df['YearsCode'] != 'Less than 1 year' ) & ( df['YearsCode'] != 'More than 50 years' )
    for gen in genders:
        print('Género: ' +  gen)
        filter = (filter_2) & (df['Gender'].str.contains(gen))
        df[filter]['YearsCode'].apply(pd.to_numeric).sort_values().hist(bins=10, xrot=90)
        plt.show()
    
YC(data)

"""
==========================================================================
=************7.                                  .*************
==========================================================================
"""
def funcion_7(df):
    df_filter = (df['WorkWeekHrs'].notnull())
    df_filter2 = (df['DevType'].notnull())
    data = df[df_filter2]['DevType'].str.split(';')
    aux = []
    for element in data:
        for e in element:
            if e not in aux:
                aux.append(e)

    devtype = aux
    # wwh = find_vals(df, 'WorkWeekHrs')
    # print(wwh)
    count = 0
    for devtype in devtype:
        print('Tipo de programador: ' +  devtype)
        filter = (df_filter) & (df['DevType'].str.contains(devtype))
        data = df[filter]['WorkWeekHrs'].tolist()
        aux = []
        for d in data:
            if d <= 98:
                aux.append(d)
        aux.sort()
        plt.hist(aux, bins=10)
        plt.savefig(str(count))
        plt.show()
        plt.clf()
        count = count + 1
        

funcion_7(data)

"""
==========================================================================
=************8.                                  .*************
==========================================================================
"""
def funcion_8(df):
    df_filter = (df['Age'].notnull())
    df_filter2 = (df['Gender'].notnull())   
    data = df[df_filter2]['Gender'].str.split(';')
    aux = []
    for element in data:
        for e in element:
            if e not in aux:
                aux.append(e)

    genders = aux
    count = 0
    for gender in genders:
        print('Edad por genero: ' +  gender)
        filter = (df_filter) & (df['Gender'].str.contains(gender))
        data = df[filter]['Age'].tolist()
        data.sort()
        plt.hist(data, bins=10)
        plt.savefig(str(count))
        plt.show()
        plt.clf()
        count = count + 1
        

funcion_8(data)


"""
==========================================================================
=************9. Annual salary per Programming.*************
==========================================================================
"""
def fil(h,t='0'):
    df=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    if(t=='0'):
        li=df[h]
    else:
        li=df[df[h]==t]
    return li

def sep(x):
    l=[]
    aux=" "
    j=0
    for i in x:
        j+=1
        if(i==';'):
            l.append(aux)
            aux=" "
        else:
            aux+=i
            if(j==len(x)):
                l.append(aux)            
    return l

def LanguageWorkedWith(n):
    par=fil('LanguageWorkedWith',n)
    med=par['ConvertedComp'].median()
    par=par['ConvertedComp'].describe().T
    print("Median"+str(med))
    print("Mean"+str(par[1])) #imrpimir solo mediana mean y std 
    print("std"+str(par[2]))

LanguageWorkedWith('HTML/CSS')

"""
===============================================================================
=************10. Correlation between years of experience and annual salary .*************
===============================================================================
"""
def Correlacion(lista1,lista2):
    import math as mt
    lista1AVG=(sum(lista1)/len(lista1))
    lista2AVG= (sum(lista2)/len(lista2))

    x=[]
    y=[]
    xy=[]
    xx=[]
    yy=[]
    xySum=0
    xxSum=0
    yySum=0
    for i in range(len(lista1)):
        x.append(lista1[i]-lista1AVG)
        y.append(lista2[i]-lista2AVG)
        xy.append(x[i]*y[i])
        xx.append(x[i]**2)
        yy.append(y[i]**2)
        xySum+=(xy[i])
        xxSum+=(xx[i])
        yySum+=(yy[i])
    

    xxSqrt=(mt.sqrt(xxSum))
    yySqrt=(mt.sqrt(yySum))

    r=((xySum)/(xxSqrt*yySqrt))
    return(r)

data=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')

def YS(df):
    print('Correlacion entre años de experiencia y salario anual')
    df_filter = (df['ConvertedComp'].notnull())
    df_filter2 = (df['YearsCode'].notnull()) & (df['YearsCode'] != '')
    filter = (df_filter) & (df_filter2)
    filter_3 = (filter) & ( df['YearsCode'] != 'Less than 1 year' ) & ( df['YearsCode'] != 'More than 50 years' )
    data1 = df[filter_3]['YearsCode'].tolist()
    data2 = df[filter_3]['ConvertedComp'].tolist()
    x = []
    y = []
    for d1 in range(len(data1)):
        x.append(int(data1[d1]))
    for d2 in range(len(data2)):
        y.append(int(data2[d2]))
    print('La correlacion', Correlacion(x,y))
YS(data)

"""
==========================================================================
=************11. Correlation between age  and annual salary.*************
==========================================================================
"""
def Fee():
    df=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    l=df['Age']
    l=l.drop_duplicates()
    r=df.corr(method="pearson")['Age']["ConvertedComp"]
    print(r)

Fee()

def Fe():
    print('Correlacion entre la edad y salario anual')
    df_filter = (data['ConvertedComp'].notnull())
    df_filter2 = (data['Age'].notnull())
    filter = (df_filter) & (df_filter2)
    data1 = data[filter]['Age'].tolist()
    data2 = data[filter]['ConvertedComp'].tolist()
    x = []
    y = []
    for d1 in range(len(data1)):
        x.append(int(data1[d1]))
    for d2 in range(len(data2)):
        y.append(int(data2[d2]))
    print('La correlacion', Correlacion(x,y))

Fe()


"""
==========================================================================
=************13. bar plot with the frequencies of the different programming language.*************
==========================================================================
"""
def program_lang():
    import pandas as pd
    df=pd.read_csv('C:/Users/fabis/Documents/DICIS-UG/9 Semestre/Mineria/DM/data/survey_results_public.csv')
    R=df['LanguageWorkedWith']
    k=[]  
    for i in R:
        if not (pd.isna(i)):
            l=split_type(i)
            for j in l:
                k.append(j)
    df2=pd.DataFrame(k)
    df2.columns= ['Lenguage']
    df2['Lenguage'].value_counts().plot(kind='bar')

program_lang()
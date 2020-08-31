import pandas as pd
import numpy as np
from prettytable import PrettyTable
xpread = pd.read_excel("Fast-foods.xlsx")

#Function return rows count
def RowsCount(spread):
    return spread.shape[0]

#Function counts the unique number of restaurants on excel sheet
def RestCount(spread):
    ValueCounts= spread.value_counts('restaurant')
    return ValueCounts.shape[0]

#This functions returns the total number of unique food items under types column
def FoodItemsCount(spread):
    FoodsCount = spread.value_counts('type')
    return FoodsCount.shape[0]

#This function return average calories
def AverageCalories(spread):
    cals = spread['calories']
    totalcals= np.sum(cals)
    Rows = int(spread.shape[0])
    return np.round((totalcals/Rows),2)

#This function returns smallest portion size
def smallesPortion(spread):
    portions= np.min(spread['serving_size'])
    return portions

#Return highest sodium item and sodium content
def higestSodium(spread):
    sodium = (spread["sodium"])
    indexx = np.argmax(sodium)
    resta = [spread['item'][indexx], spread['restaurant'][indexx], spread['sodium'][indexx]]
    return resta

#Return total calories of items on menu
def totalcalsMenu(spread):
    cals = spread['calories']
    totalcals= np.sum(cals)
    return np.round(totalcals,2)

#Return highest amount of sugar food
def HighestSugar(spread):
    sugar = (spread["sugars"])
    indexx = np.argmax(sugar)
    resta = [spread['item'][indexx], spread['restaurant'][indexx], spread['sugars'][indexx]]
    return resta

#Return the quantity of a specific item
def howmany(spread, item):
    ValueCounts = spread.type.value_counts().tolist()
    Values = spread.type.value_counts().index.tolist()
    Indez= Values.index(item)
    return [ValueCounts[Indez]]

#Average Calories per food type
def calFoodtype(spread):
    Listc = PrettyTable(['Food Type', 'Average Calories'])
    Values = spread.type.value_counts().index.tolist()
    for i in Values:
        separateList = spread['type'] == i
        SeparateItems = spread[separateList]
        suma = sum(SeparateItems['calories'])
        ave= np.round(suma / len(SeparateItems.index),2)
        Listc.add_row([i,ave])
    return Listc

#Returns table with highest calorie count item per restaurant [Restaurant , maximum calories ]
def HighestcalItems(spread):
    Listc = []
    Values = spread.restaurant.value_counts().index.tolist()
    for i in Values:
        separateList = spread['restaurant'] == i
        SeparateItems = spread[separateList]
        suma = np.max(SeparateItems['calories'])
        Listc.append([i,suma])
    return Listc

def HighestCalorieRestaurant(spread):
    calorik = (spread["calories"])
    indexx = np.argmax(calorik)
    resta = [spread['item'][indexx], spread['restaurant'][indexx], spread['calories'][indexx]]
    return resta

#Make 2D tble pretty
def maketablepretty(table, title1, title2):
    listk = PrettyTable([title1, title2])
    for i in table:
        listk.add_row([i[0],i[1]])
    return listk



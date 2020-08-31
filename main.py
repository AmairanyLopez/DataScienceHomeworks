import Definitions as fini
import pandas as pd
Spread = pd.read_excel("Fast-foods.xlsx")

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print ('Hello! Welcome to Data Science \n\n\n')


#print rows count
print('1. How many rows are there of fast food data? total number of rows is ' + str(fini.RowsCount(Spread)))

#print count of restaurants
print('2. How many restaurants in this dataset? total number is ' + str(fini.RestCount(Spread)))

#Print the count of food items
print('3. How many different types of foods are reported on this datasheet? total number is ' + str(fini.FoodItemsCount(Spread)))

#Print the average calories
print('4. What is the average number of calories? average calories are '+str(fini.AverageCalories(Spread)))

#Print samllest size portion
print('5. What is the smallest serving size? ' + str(fini.smallesPortion(Spread)))

#Print highest sodium item
lista = fini.higestSodium(Spread)
print('6. What food has the highest amount of sodium? How much is it? The highest is ' +str(lista[0])+' from '+str(lista[1])+' with '+ str(lista[2]))

#Print total calories
print('7. If you ate every menu item on the list, how many calories would that be? It would be '+str(fini.totalcalsMenu(Spread)) +' calories')

#Print highest sugar item
listb = fini.HighestSugar(Spread)
print('8. What food has the highest amount of sugar? How much is it? The highest is ' +str(listb[0])+' from '+str(listb[1])+' with '+str(listb[2]))

#Return how many items
print('9. How many milkshakes are in the data set? There are '+str(fini.howmany(Spread, 'Milkshake'))+' Milkshakes.')

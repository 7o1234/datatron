import pandas as pd
import os
import csv
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 


class Dashboard:
    def __init__(self):
        self.meats = ["Grilled Chicken", "Pulled Pork", "Brisket", "Bacon", "Ham"]
        self.desserts = ["Cheesecake", "Large Chocolate Chunk Cookie"]
        self.drinks = ["Coke","Fanta Orange",  "Dr. Pepper", "Sprite", "Diet Coke","Barq's Root Beer","Powerade - Blue Mountain Berry Blast","Minute Maid Lemonade" ,"Unlimited Fountain Drinks"]
        self.sides =  ["Garlic Bread", "Cheesy Garlic Bread", "Chips"]
        self.chips = ["Doritos", "Lays Classic", "Lays Barbecue", "Cheetos"]
        self.items = ["No Drink","No Side", "No Meat", "No Mac", "No Drizzle","Regular", "Cheddar", "Pepper Jack", "Alfredo", "Grilled Chicken", "Pulled Pork", "Brisket", "Bacon", "Ham", "Broccoli", "Corn", "Onions", "Onions", "Unlimited Fountain Drinks", "Jalapenos", "Tomatoes", "Bell Peppers", "Mushrooms", "Pineapple", "Parmesan", "Breadcrumbs", "BBQ", "Garlic Parmesan", "Buffalo", "Pesto", "Ranch", "Hot Honey", "Garlic Bread", "Cheesy Garlic Bread", "Cheesecake", "Large Chocolate Chunk Cookie", "Chips", "Cheesy Broccoli", "Water", "Coke", "Dr. Pepper", "Sprite", "Diet Coke","Powerade - Blue Mountain Berry Blast","Gluten-Free (ask store for safe toppings)","Minute Maid Lemonade", "Apple Juice" , "XL Shirt" ,"Small Shirt" ,"Medium Shirt", "Large Shirt", "XXL Shirt" , "XXXL Shirt"]
        self.desserts_counter = 0
        self.meat_counter = 0
        self.sides_counter = 0
        self.drinks_counter = 0 
        self.tt = pd.read_csv("tiktok_stats.csv")



        directory = "Roni_s Challenge public/Provided Data [FINAL]"
        data = []
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                temp = pd.read_csv(f,encoding='ISO-8859-1')
                data.append(temp)
        self.df = pd.concat(data)


    def makeDicts(self):
        
        #make a dictionary of all unique items
        dict = {}
        for i in self.items:
            dict[i] = 0
        

        dict_s = {}

        #loop through all modifiers and track occurences in dictionary
        modif = self.df["Modifier"]

        for i in modif:
            if i not in self.items:
                dict_s[i] = 0

        
        for i in modif:
            if i in self.items:
                dict[i] += 1
            if i in self.meats:
                self.meat_counter += 1 
            if i in self.desserts:
                self.desserts_counter += 1 
            if i in self.sides:
                self.sides_counter += 1 
            if i in self.drinks:
                self.drinks_counter += 1 
            elif i not in self.items:
                dict_s[i] += 1
                
        for i in dict_s:
            for j in self.items:
                try:
                    i.index(j) 
                except:
                    continue
                dict[j] += dict_s[i]
                dict_s[i] = 0
            if i in self.chips:
                dict["Chips"] += dict_s[i]
                dict_s[i] = 0
        
                
       
        return dict, dict_s

    def calculateTotals(self):
        water_cost = 0
        Apple_cost = 0
        shirts_cost = 0
        Shirt_addon_cost = 0

        
        modif = self.df["Option Group Name"]
        for i in modif:
            if  i == "Choose Your Shirt":
                Shirt_addon_cost += 19.05
            
            # elif self.df.loc[i] == "Shirt":
            #     shirts_cost += 19.95
            #     print("other shirt added")



        modif = self.df["Modifier"]
        for i in modif:
            if i  == "Water":
                water_cost = water_cost + 1.49
            if i == "Apple Juice":
                Apple_cost = Apple_cost + 2.49
                
        grill = self.df[self.df["Parent Menu Selection"] == "Grilled Cheese Sandwich"]
        grill_2  = grill[grill["Option Group Name"] == "Choose Your Drink" ]   
        noods = self.df[self.df["Option Group Name"] == "Noods"]
        
        drinks_cost = self.drinks_counter * 1.99
        sides_cost = self.sides_counter * 1.99
        desserts_cost = self.desserts_counter *4.99
        meats_cost = self.meat_counter * 1.99
        grill_cost = (grill_2.size) * 8.99
        noods_cost = (noods.size) * 8.99
        
        
        gross_income = (shirts_cost) + (Shirt_addon_cost) + (sides_cost) + (meats_cost) + (desserts_cost) + (drinks_cost) +(water_cost) +(Apple_cost) + (grill_cost) + (noods_cost)
        
        costs = {"Shirts": shirts_cost + Shirt_addon_cost, "Sides": sides_cost, "Meats": meats_cost, "Desserts": desserts_cost,"Drinks": drinks_cost+ water_cost+ Apple_cost,"Grilled Cheese": grill_cost, "Noodles": noods_cost}
        
        return gross_income, costs





db = Dashboard()
d1,d2 = db.makeDicts()
gross,costs = db.calculateTotals()

df = db.tt 
df_binary = df[['Time', 'Plays']] 
# df_binary["Time"] = pd.to_datetime(df_binary["Time"],errors = 'coerce')
# Eliminating NaN or missing input numbers 
df_binary = df_binary.dropna()

print(df_binary)



X = np.array(df_binary['Time']).reshape(-1, 1) 
y = np.array(df_binary['Plays']).reshape(-1, 1) 

# Separating the data into independent and dependent variables 
# Converting each dataframe into a numpy array 
# since each dataframe contains only one column 
df_binary.dropna(inplace = True) 

# Dropping any rows with Nan values 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25) 

# Splitting the data into training and testing data 
regr = LinearRegression() 

regr.fit(X_train, y_train) 
print(regr.score(X_test, y_test)) 

y_pred = regr.predict(X_test) 
plt.scatter(X_test, y_test, color ='b') 
plt.plot(X_test, y_pred, color ='k') 

plt.show() 
# Data scatter of predicted values 

# newdict = {}
# for i in d2:
#     if d2[i] != 0:
#         newdict[i] = d2[i]
# print(newdict)
# df = pd.DataFrame(newdict, index=[0])
# df.to_csv("extras.csv")
# df = pd.DataFrame(d1, index=[0])
# df.to_csv("main.csv")
# df = pd.DataFrame(costs, index=[0])
# df.to_csv("costs.csv")









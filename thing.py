import pandas as pd
df1 = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/april_2024.csv")
df2 = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/august_2024.csv")
df3 = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/july_2024.csv")
df4 = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/june_2024.csv", encoding='ISO-8859-1')
df5 = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/may_2024.csv")
df6 = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/october_2024.csv")
df7 = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/september_2024.csv")

dfs = [df1,df2,df3,df4,df5,df6,df7]
df = pd.concat(dfs)

#make dataframe of all unique entries in modifiers and add them to a list
unique = df["Modifier"].unique()
meats = ["Grilled Chicken", "Pulled Pork", "Brisket", "Bacon", "Ham"]
desserts = ["Cheesecake", "Large Chocolate Chunk Cookie"]
drinks = ["Coke","Fanta Orange",  "Dr. Pepper", "Sprite", "Diet Coke","Barq's Root Beer","Powerade - Blue Mountain Berry Blast","Minute Maid Lemonade" ,"Unlimited Fountain Drinks"]
sides =  ["Garlic Bread", "Cheesy Garlic Bread", "Chips"]
chips = ["Doritos", "Lays Classic", "Lays Barbecue", "Cheetos"]
desserts_counter = 0
meat_counter = 0
drinks_counter = 0 
sides_counter = 0


water_cost = 0
Apple_cost = 0
shirts_cost = 0
Shirt_addon_cost = 0

items = ["No Drink","No Side", "No Meat", "No Mac", "No Drizzle","Regular", "Cheddar", "Pepper Jack", "Alfredo", "Grilled Chicken", "Pulled Pork", "Brisket", "Bacon", "Ham", "Broccoli", "Corn", "Onions", "Onions", "Unlimited Fountain Drinks", "Jalapenos", "Tomatoes", "Bell Peppers", "Mushrooms", "Pineapple", "Parmesan", "Breadcrumbs", "BBQ", "Garlic Parmesan", "Buffalo", "Pesto", "Ranch", "Hot Honey", "Garlic Bread", "Cheesy Garlic Bread", "Cheesecake", "Large Chocolate Chunk Cookie", "Chips", "Cheesy Broccoli", "Water", "Coke", "Dr. Pepper", "Sprite", "Diet Coke","Powerade - Blue Mountain Berry Blast","Gluten-Free (ask store for safe toppings)","Minute Maid Lemonade", "Apple Juice" , "XL Shirt" ,"Small Shirt" ,"Medium Shirt", "Large Shirt", "XXL Shirt" , "XXXL Shirt"]

#make a dictionary of all unique items
dict = {}
for i in items:
    dict[i] = 0

dict["Special Instructions"] = 0
special = []

dict_s = {}

#loop through all modifiers and track occurences in dictionary
modif = df["Modifier"]

for i in modif:
    if i not in items:
        dict_s[i] = 0

for i in modif:
    if i in items:
        dict[i] += 1
    else:
        dict_s[i] += 1
        #special.append(i)

for i in modif:
    if i in meats:
        meat_counter += 1 
for i in modif:
    if i in desserts:
        desserts_counter += 1 
for i in modif:
    if i in sides:
        sides_counter += 1 




for i in modif:
    if  i == "Choose Your Shirt":
        Shirt_addon_cost += 19.05
    elif "Shirt" == i:
        shirts_cost += 19.95



for i in modif:
    if i in drinks:
        drinks_counter += 1 
    
for i in modif:
    if i  == "Water":
        water_cost = water_cost + 1.49
    if i == "Apple Juice":
        Apple_cost = Apple_cost + 2.49
        
for i in dict_s:
    for j in items:
        try:
           i.index(j[0:4]) 
        except:
            continue
        dict[j] += dict_s[i]
        dict_s[i] = 0
    if i in chips:
        dict["Chips"] += dict_s[i]
        dict_s[i] = 0
print(dict)

grill = df[df["Parent Menu Selection"] == "Grilled Cheese Sandwich"]
grill_2  = grill[grill["Option Group Name"] == "Choose Your Drink" ]   
noods = df[df["Option Group Name"] == "Noods"]
    
drinks_cost = drinks_counter * 1.99
sides_cost = sides_counter * 1.99
desserts_cost = desserts_counter *4.99
meats_cost = meat_counter * 1.99
grill_cost = (grill_2.size) * 8.99
noods_cost = (noods.size) * 8.99




gross_income = (shirts_cost) + (Shirt_addon_cost) + (sides_cost) + (meats_cost) + (desserts_cost) + (drinks_cost) +(water_cost) +(Apple_cost) + (grill_cost)



print(gross_income)
print(grill_2.size)
#print(dict)
print(dict_s)














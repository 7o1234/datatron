import pandas as pd
df = pd.read_csv("Roni_s Challenge public/Provided Data [FINAL]/april_2024.csv")


#make dataframe of all unique entries in modifiers and add them to a list
unique = df["Modifier"].unique()
meats = ["Grilled Chicken", "Pulled Pork", "Brisket", "Bacon", "Ham"]
desserts = ["Cheesecake", "Large Chocolate Chunk Cookie"]
drinks = ["Coke", "Dr. Pepper", "Sprite", "Diet Coke","Powerade - Blue Mountain Berry Blast","Minute Maid Lemonade" ,"Unlimited Fountain Drinks"]
sides =  ["Garlic Bread", "Cheesy Garlic Bread", "Chips"]
desserts_counter = 0
meat_counter = 0
drinks_counter = 0 
sides_counter = 0


water_cost = 0
Apple_cost = 0
shirts_cost = 0
Shirt_addon_cost = 0

items = ["No Drink", "No Side", "No Meat", "No Mac", "No Drizzle","Regular", "Cheddar", "Pepper Jack", "Alfredo", "Grilled Chicken", "Pulled Pork", "Brisket", "Bacon", "Ham", "Broccoli", "Corn", "Onions", "Onions", "Unlimited Fountain Drinks", "Jalapenos", "Tomatoes", "Bell Peppers", "Mushrooms", "Pineapple", "Parmesan", "Breadcrumbs", "BBQ", "Garlic Parmesan", "Buffalo", "Pesto", "Ranch", "Hot Honey", "Garlic Bread", "Cheesy Garlic Bread", "Cheesecake", "Large Chocolate Chunk Cookie", "Chips", "Cheesy Broccoli", "Water", "Coke", "Dr. Pepper", "Sprite", "Diet Coke","Powerade - Blue Mountain Berry Blast","Gluten-Free (ask store for safe toppings)","Minute Maid Lemonade", "Apple Juice" , "XL Shirt" ,"Small Shirt" ,"Medium Shirt", "Large Shirt", "XXL Shirt" , "XXXL Shirt"]
#make sure spacing is right
for i in items:
    i = i.strip()

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
    if "Shirt" in i:
        shirts_cost += 19.95



for i in modif:
    if i in drinks:
        drinks_counter += 1 
    
for i in modif:
    if i  == "Water":
        water_cost = water_cost + 1.49
    if i == "Apple Juice":
        Apple_cost = Apple_cost + 2.49

grill = df[df["Parent Menu Selection"] == "Grilled Cheese Sandwich"]
grill_2  = grill[grill["Option Group Name"] == "Choose Your Drink" ]   
noods = df[df["Parent Menu Selection"] == "Noods"]
nood2  = noods[noods["Option Group Name"] == "Choose Your Drink" ]      
    
drinks_cost = drinks_counter * 1.99
sides_cost = sides_counter * 1.99
desserts_cost = desserts_counter *4.99
meats_cost = meat_counter * 1.99
grill_cost = (grill_2.size) * 8.99
noods_cost = (nood2.size) * 8.99




gross_income = (shirts_cost) + (Shirt_addon_cost) + (sides_cost) + (meats_cost) + (desserts_cost) + (drinks_cost) +(water_cost) +(Apple_cost) + (grill_cost)



print(gross_income)
print(grill_2.size)
print(dict)
print(dict_s)

















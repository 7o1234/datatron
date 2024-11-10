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




grill = df[df["Parent Menu Selection"] == "Grilled Cheese Sandwich"]
grill_2  = grill[grill["Option Group Name"] == "Choose Your Drink" ]
print(grill_2.size)
print(dict)
print(dict_s)














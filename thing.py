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
items = ["No Drink", "No Side", "No Meat", "No Mac", "No Drizzle","Regular", "Cheddar", "Pepper Jack", "Alfredo", "Grilled Chicken", "Pulled Pork", "Brisket", "Bacon", "Ham", "Broccoli", "Corn", "Onions", "Onions", "Unlimited Fountain Drinks", "Jalapenos", "Tomatoes", "Bell Peppers", "Mushrooms", "Pineapple", "Parmesan", "Breadcrumbs", "BBQ", "Garlic Parmesan", "Buffalo", "Pesto", "Ranch", "Hot Honey", "Garlic Bread", "Cheesy Garlic Bread", "Cheesecake", "Large Chocolate Chunk Cookie", "Chips", "Cheesy Broccoli", "Water", "Coke", "Dr. Pepper", "Sprite", "Diet Coke","Powerade - Blue Mountain Berry Blast","Gluten-Free (ask store for safe toppings)","Minute Maid Lemonade" ]
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



noods = df[df["Option Group Name"] == "Noods"]

grill = df[df["Parent Menu Selection"] == "Grilled Cheese Sandwich"]
grill_2  = grill[grill["Option Group Name"] == "Choose Your Drink" ]
print(dict)
print(dict_s)

# print(dict)
# print(dict_s)














#!/usr/bin/env python
# coding: utf-8

# ### Prompt:
# You are an analyst for a fastfood restaurant. The company has tasked you to analyze their past transactions. Each row represents a single transaction/order from one of their ten (10) branches. The order is recorded as a __`string`__ which is formatted as: 
# 
# "`[quantity1][item_code1], [quantity2][item_code2], [quantity3][item_code3]`"
# 
# However, because of some technical error, the __number of combo meals purchased__ as well as the __total order value__ was lost, so we'll need to restore that.
# 
# ### You are tasked to come up with the following:
# 1. Given the order column, count how many of each product was purchased
# 2. Given each product count, get the number of supposed combo meals purchased. <br><i>(You may update the product count when the combo meals are counted)</i>.
# 3. Calculate the total order value.
# 4. Determine which branch made the most revenue, and how much?
# 
# ### The combo meals are detailed below:
# 1. Family combo: 4 burgers, 4 fries, 4 drinks
# 2. Big combo: 1 burgers, 1 fries, 1 drinks
# 3. Snack combo: 1 fries, 1 drinks

# In[83]:


# 1. Given the order column, count how many of each product was purchased
import pandas as pd
import numpy as np

df = pd.read_csv("food_transactions.csv")

df['Burger'] = df['order'].apply(lambda x: x[0] if 'Burger' in str(x) else 0)
df['Fries'] = df['order'].apply(lambda x: x[x.find('Fries')-3] if 'Fries' in str(x) else 0)
df['Drink'] = df['order'].apply(lambda x: x[x.find('Drink')-3] if 'Drink' in str(x) else 0)

df["Burger"] = df["Burger"].astype(int)
df["Fries"] = df["Fries"].astype(int)
df["Drink"] = df["Drink"].astype(int)
df


# In[47]:


# 2. Given each product count, get the number of supposed combo meals purchased.
# (You may update the product count when the combo meals are counted).
# The combo meals are detailed below:
# Family combo: 4 burgers, 4 fries, 4 drinks
# Big combo: 1 burgers, 1 fries, 1 drinks
# Snack combo: 1 fries, 1 drinks

# combo = np.array ([["Family_Combo", 4, 4, 4], 
#                   ["Big_Combo", 1, 1, 1],
#                   ["Snack_Combo", 0, 1, 1]])

# combo_meals = pd.DataFrame(combo, columns = ["Meal", "Burgers", "Fries", "Drinks"])

# combo_meals 


# In[111]:


df["Family_Combo_Burger"] = df["Burger"].apply(lambda x: 1 if x == 4 else 0)
df["Family_Combo_Fries"] = df["Fries"].apply(lambda x: 1 if x == 4 else 0)
df["Family_Combo_Drinks"] = df["Drink"].apply(lambda x: 1 if x == 4 else 0)

df["Family_Combo"] = 
df 


# In[ ]:


# 3. Calculate the total order value.

import json



# In[93]:


# 4. Determine which branch made the most revenue, and how much?

df["branch"].unique()


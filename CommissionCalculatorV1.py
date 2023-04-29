# Starting with asking how much commission is with each sold and appointment sold. 
# NOTE: Entering anything that is not an int will result in an error and will fix in future versions. 

commission = int(input("How much does each salesperson make per appointments shown and solds?:\n"))

# Made an empty list of sales reps so the user can have the maximum amount be dynamic as they input each sales rep in. 

sales_rep_list = []

# Made a while loop to allow the user to enter the names of each sales rep into the empty sales rep list. Once user inputs all sales people in they have the option of typing 'quit' to stop the loop.

while True:
  name = input("\nEnter Sales Rep's Name (Type 'quit' to stop adding sales reps):\n")
  if name == 'quit':
    break
  else:
    sales_rep_list.append(name)  
print("\nList of Sales People:\n-----------------------------")
for position,rep in enumerate(sales_rep_list):
  print(f"{position + 1}.{rep}")

# Made an empty list of stores the sales reps are working for so the user can have the maximum amount be dynamic as they input each store in. 

list_of_stores = []

# Made a while loop to allow the user to enter the names of each of the stores into the empty stores list. Once user inputs all stores in they have the option of typing 'quit' to stop the loop. 

while True:
  store_name = input("\nEnter Store Names (Type 'quit' to stop adding stores):\n")
  if store_name == 'quit':
    break
  else:
    list_of_stores.append(store_name)  
print("\nList of Stores:\n-----------------------------")
for position,rep in enumerate(list_of_stores):
  print(f"{position + 1}.{rep}")

# Makes a list and a nested list for the record that is kept for shows and solds per sales reps in each store. The lists created are just for the stores and sales reps.

shows_information = [[0 for _ in range(len(list_of_stores))] for _ in range(len(sales_rep_list))]

solds_information = [[0 for _ in range(len(list_of_stores))] for _ in range(len(sales_rep_list))]

# The for loop is looping for each sales person for each store to enter the amount of shows and solds per sales rep per store.

for reps in range(len(sales_rep_list)):
  for store in range(len(list_of_stores)):
  
    amount_of_shows = int(input(f"\nEnter the amount of shows for {sales_rep_list[reps]} in {list_of_stores[store]}:\n"))
    shows_information[reps][store] = amount_of_shows
    
    amount_of_solds = int(input(f"\nEnter the amount of solds for {sales_rep_list[reps]} in {list_of_stores[store]}:\n"))
    solds_information[reps][store] = amount_of_solds

print("\nResults:\n-----------------------------\n")

# For loop goes through every sales rep totaling the amount of shows, solds, the total amount of shows and solds each sales rep made, the total amount of commission for each sales rep as well as the total commission with the bonuses. This loop sets up all the variables. 

# NOTE: In the future I will update it so it shows much the amount of bonus is made and then the total amount with bonus included.

for rep in range(len(sales_rep_list)):
  total_shows = sum(shows_information[rep])
  total_solds = sum(solds_information[rep])
  shows_commission = sum(shows_information[rep] * commission)
  solds_commission = sum(solds_information[rep] * commission)
  total_commission = shows_commission + solds_commission
  if total_solds > 41:
    bonus = total_commission + 2000
  elif total_solds <  41 and total_solds > 35:
    bonus = total_commission + 1500
  elif total_solds < 35 and total_solds > 30:
    bonus = total_commission + 1000
  elif total_solds < 30 and total_solds > 25:
    bonus = total_commission + 600
  else:
    bonus = total_commission + 300

  # Goes through every store and prints out all the variables created above. 
  
  for store in range(len(list_of_stores)):
    print(f"{sales_rep_list[rep]} has {shows_information[rep][store]} shows and {solds_information[rep][store]} solds in {list_of_stores[store]}")
  print(f"\nTotal shows for {sales_rep_list[rep]}: {total_shows}")
  print(f"Total solds for {sales_rep_list[rep]}: {total_solds}\n")
  print(f"Total shows commission for {sales_rep_list[rep]}: {shows_commission}")
  print(f"Total solds commission for {sales_rep_list[rep]}: {solds_commission}\n")
  print(f"Total commission with bonus for {sales_rep_list[rep]}: {bonus}\n")






  







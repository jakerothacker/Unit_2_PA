sandwich_orders = ["Turkey with mayo", "Fried chicken", "BLT", "Chunky chicken melt", "Ruben", "Pastrami", "PB&J"]

finished_sandwiches = []

num_orders = len(sandwich_orders)
count = 0 

while count < num_orders:
    print(sandwich_orders[count], "was made")
    finished_sandwiches.append(sandwich_orders[count])
    count += 1 


print("The followiing sandwiches are finished", *finished_sandwiches, sep=", ")
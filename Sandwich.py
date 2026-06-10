sandwich_orders = ["Turkey with mayo", "Fried chicken", "BLT", "Chunky chicken melt"]

finished_sandwiches = []

num_orders = len(sandwich_orders)
count = 0 

while count < num_orders:
    print(sandwich_orders[count])
    finished_sandwiches.append(sandwich_orders[count])
    count += 1 


print("End is reached")
print("Finished sandwiches:", finished_sandwiches)
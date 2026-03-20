import os
from functools import reduce
# Создаем папку и файлы
if not os.path.exists("sales"):
    os.makedirs("sales")
    with open("sales/store1.txt", "w") as f:
        f.write("Laptop,3\nMouse,10\nKeyboard,5")
    with open("sales/store2.txt", "w") as f:
        f.write("Monitor,2\nHeadphones,4\nLaptop,1")
    print("done")

# Ридинг файл
products = []
files = os.listdir("sales") # Список of алл файлс

for file_name in files:
    path = os.path.join("sales", file_name)
    with open(path, "r") as f:
        for line in f:
            if line.strip():
                name, qty = line.strip().split(",")
                products.append((name, int(qty))) 


# len() 
total_records = len(products)

# sum() 
total_qty = sum(p[1] for p in products)

# max() и min() 
highest_sale = max(products, key=lambda x: x[1])
lowest_sale = min(products, key=lambda x: x[1])

# map() 
boosted = list(map(lambda x: (x[0], x[1] + 2), products))

# filter() 
popular = list(filter(lambda x: x[1] > 5, products))

# reduce() 
all_qtys = [p[1] for p in products]
product_of_all = reduce(lambda x, y: x * y, all_qtys)

# enumerate()
print("\n Список товаров with indexes")
for i, (name, qty) in enumerate(products, 1):
    print(f"{i} {name} {qty}")

# zip()
names = [p[0] for p in products]
qtys = [p[1] for p in products]
zipped = list(zip(names, qtys))

# sorted()
sorted_list = sorted(products, key=lambda x: x[1], reverse=True)

# save result
with open("sales_report.txt", "w") as report:
    report.write(f"Total records: {total_records}\n")
    report.write(f"Average sold: {total_qty / total_records:.1f}\n")
    report.write(f"Highest sold: {highest_sale[1]}\n")
    report.write(f"Lowestt sold: {lowest_sale[1]}\n\n")
    report.write("very popular products:\n")
    for name, qty in popular:
        report.write(f"{name} {qty}\n")

print("\nalright everything is done")
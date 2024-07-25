
# Fractional Knapsack Problem in Python

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    for i in items:
        if capacity >= i.weight:
            capacity -= i.weight
            total_value += i.value
        else:
            fraction = capacity / i.weight
            total_value += i.value * fraction
            break
    return total_value

# Test the function
#items = [Item(20, 100), Item(30, 120), Item(10, 60)]
#capacity = 50
#print(fractional_knapsack(items, capacity))  # Output: 240.0




file = open("C:\POST\cont2.in", "r")
s = file.read().split()
file.close()
items_num = int(s[0])
bag_volume = int(s[1])
a=[]
b=[]
#print(s)
items = []
for x in range(2,items_num):
    if not x & 1:
      item_volume=int(s[x])
      a.append(s[x])
    else:
      cost=int(s[x])
      b.append(s[x])

#print(a)
#print(b)

for i in range(0,len(a)):
    cost=int(b[i])
    item_volume=int(a[i])
    items.append((cost / item_volume, item_volume))
items.sort(key=lambda x: x[0], reverse=True)
print(items)
items_weight = 0
price = 0
for item in items:
    if bag_volume >= item[1]:
        price += item[0] * item[1]
        bag_volume -= item[1]
    else:
        price += item[0] * bag_volume
        break
#print(round(price, 3))

Tems = []

#tems=Item(1,0)
capacity = bag_volume
print(items)
print(capacity)

#print(items)

for i in items:
   Tems.append(Item(i[0],i[1]))


#for i in Tems:
#  print(i.value)
#print(Tems)


#tems = [Item(20, 100), Item(30, 120), Item(10, 60)]

print(int(s[1]))
print(fractional_knapsack(Tems, int(s[1])))





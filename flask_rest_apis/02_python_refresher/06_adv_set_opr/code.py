friends= {"Kyoiku", "Joyo", "Jinmeyo"}
abroad= {"Kyoiku", "Jinmeyo"}

local_friends= friends.difference(abroad)
print(local_friends)


local= {"Joyo"}
abroad= {"Kyoiku", "Jinmeyo"}

total= local.union(abroad)
print(total)

art= {"Bob", "Jen", "Rolf", "Charlie"}
science= {"Bob", "Jen", "Adam", "Anne"}

both= art.intersection(science)
print(both)

#1
my_list= [33, 33, 34]
print(my_list)
print(my_list[0]+my_list[1]+my_list[2])

#2
my_tuple= (32,)
print(my_tuple)
print(my_tuple[0])

#3
set1= {5, 6, 77, 8, 9, 12}
set2= {5, 77, 9, 10, 12, 13}
print(set1.intersection((set2)))
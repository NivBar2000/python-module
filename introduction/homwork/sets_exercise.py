port_list=[8080,8443,22,8080,4433]
#? print((port_list))

uniq_port=set(port_list)
#? print((port_list))

server_names={"web01","web02","web03"}

#? print("is 22 in uniq port? ", 22 in server_names )

uniq_port.add(3000)
#? print(uniq_port)
uniq_port.remove(22)
uniq_port.discard(22)
#? print(uniq_port)

valid_set={(1, 2), (3, 4)}

first_list=[1,2,5,66,23,44,1,66,3]
uniq_first_list=set(first_list)
#? print(uniq_first_list)

uniq_first_list.add(76)
#? print("is 76? ", 76 in uniq_first_list )


set_of_truples={(1, 2),(3, 4)}
#? print((1, 3) in set_of_truples)
developers={"alice", "bob", "charlie"} 
admins= {"alice", "david"}

#? if "alice" in developers & admins:
   #? print("in both")
   
print( developers.union(admins))
print(developers | admins)
print(developers & admins)
print(developers.difference(admins))
print(developers-admins)
developers.intersection_update(admins)
print(developers)
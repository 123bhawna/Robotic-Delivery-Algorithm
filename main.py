from input_graph import graph
from Company import company
from Customer import robots

g=graph()
g.input_company()

r=robots(g.vertices,2,g.adjacent_lst,g.weight,g.vertices)
r.check_order_possible(g.c)
#r.paths()

members=[]
comp=company(g.c,5,g.vertices,g.adjacent_lst,g.weight)

while(True):
	print("CLIENT SIDE")
	print("--------")
	print("Welcome to our company")
	print("Place your order here for safest and fastest delivery.")
	ch=input("Would you like to place an order?....Press[Y/N] : ")
	if ch=='y' or ch=='Y':
		print("---------")
		v=int(input("Select your location from [1,2,4,5,7,13,15,16,17].\n Please select accordingly: \n 1 - Baal Bhavan \n 2 - Red Hub PG \n 4 - Sector 4 \n 5 - Sector 3 \n 7 - Sector 5 \n 13 - Sector 2 \n 15 - Sector 1 \n 16 - Model Town \n 17 - Shanti Niketan \n Enter : "))
		lst = [1,2,4,5,7,13,15,16,17]
		if v not in lst:
			print("Invalid location!!")
			inp = input("If you are still intrested to place an order...Press[Y/N] : ")
			if(inp == "Y" or inp == "y"):
				print("---------")
				continue
			else:
				print("Application is closed!")
				break

		print("---------")

		h=int(input("Select your hotel location from [3,6,8,9,10,11,12,14,18]. \n Please select accordingly: \n 3 - Kolkata Roll Center \n 6 - Batra's Mahal Deluxe \n 8 - Dawat Restaurant & Party Hall \n 9 - Sardar Ji Malai Chaap \n 10 - Tadka Lazeez \n 11 - Coffee \n 12 - Burger \n 14 - Republic of Chicken \n 18 - Punjabi Masti \n Enter : "))
		
		lst = [3,6,8,9,10,11,12,14,18]
		if h not in lst:
			print("Invalid hotel!!")
			inp = input("If you are still intrested to place an order...Press[Y/N] : ")
			if(inp == "Y" or inp == "y"):
				print("---------")
				continue
			else:
				print("Application is closed!")
				break
		print("---------")

		m=int(input("Have you availed the membership...Press[0 for no, 1 for yes] : "))
		if(m != 0 and m != 1):
			print("Invalid input!!")
			inp = input("If you are still intrested to place an order...Press[Y/N] : ")
			if(inp == "Y" or inp == "y"):
				print("---------")
				continue
			else:
				print("Application is closed!")
				break
		print("---------")

		if(r.order_placing(v,h)):
			print("We have successfully placed your order")
			r.allocating_ID(m,v,h)
			if m==1:
				members.append(r.cID)

		print("-----------------------------------------------")
	elif(ch=='n' or ch=='N'):
		print("OK...Thanks for choosing our company!")
	else:
		print("Invalid input!!")
		inp = input("If you are still intrested to place an order...Press[Y/N] : ")
		if(inp == "Y" or inp == "y"):
			print("---------")
			continue
		else:
			print("Application is closed!")
			break
	
	print("========================================================================================")
	print("IN COMPANY")
	print()

	ch=input("Would you like to send robots now for delivery...press[Y]? Or you want more orders press[N]?...Press[Y/N] ")

	print()

	if ch=='y' or ch=='Y':
		r.robot_scheduing_initialise()
		while len(r.orders_remaining)!=0:
			
			#print("initialising the robot")
			r.initialising_robots()
			v=r.customer_taken()
			t=r.path_taken_hotel(g.c,v)
			print("Pending orders are : ")
			print(r.orders_remaining)
			r.robot_scheduling(t)
			print("---------\n")
		r.refreshing()

	elif ch=='n' or ch=='N':
		pass
	else:
		print("Invalid command!!")

	
	print("Would you like to see some results of survey done on the locations of orders?")
	ch=input()
	if ch=='y' or ch=='Y':
		print("Results of survey :")
		print("Company should start its new headquarter at any of the below locations.")
		print("These are the locations where the company is not delivering orders currently.")
		comp.other_headquarter()

	print("========================================================================================")

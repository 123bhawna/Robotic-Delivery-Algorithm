class graph:

	def __init__(self):
		self.n=18
		self.vertices=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
		self.adjacent_lst={1:[2],2:[1,3],3:[2,4],4:[3,5],5:[4],6:[7,8],7:[6,8,10],8:[6,7,9],9:[8,10,17,18],10:[7,9,11], 11:[10,12,13],12:[11,14],13:[11],14:[12,15],15:[14,16], 16:[15],17:[9,18],18:[9,17]}
		self.weight={(1,2):50,(2,1):50,(2,3):45,(3,2):45,(3,4):30,(4,3):30,(4,5):35,(5,4):35,(6,7):40,(6,8):47,(7,6):40,(7,8):7,(7,10):60,(8,6):47,(8,7):7,(8,9):25,(9,8):25,(9,10):15,(9,17):40,(9,18):30,(10,7):60,(10,9):15,(10,11):10,(11,10):10,(11,12):5,(11,13):6,(12,11):5,(12,14):15,(13,11):6,(14,12):15,(14,15):7,(15,14):7,(15,16):30,(16,15):30,(17,9):40,(17,18):3,(18,9):30,(18,17):3}
		self.c=1

	def input_graph(self):

		print("Please input the city model graph ")
		print("-----------------------------------------------")
			
		self.n=int(input("Please enter the number of possible locations "))
		self.vertices=[i for i in range(1,self.n+1)]
		self.edges=input("Please enter the edges ").split()
		for i in range(0,self.n+1):
			self.adjacent_lst[i]=[]

		self.edges=[(int(e[1]),int(e[3])) for e in self.edges]
		for e in self.edges: #undirected graph
			self.adjacent_lst[int(e[0])].append(int(e[1]))
			self.adjacent_lst[int(e[1])].append(int(e[0]))

		self.c=int(input("Please enter the company location vertex "))
		self.weight={}		
		for e in self.edges:
			j=input(e)
			self.weight[e]=int(j)

	def input_company(self):
		print("========================================================================================")
		self.c=int(input("Select the location for your company from [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]. \n Enter : "))
		print("========================================================================================")

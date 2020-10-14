class company:
	
	def __init__(self,c,max_robot,vertices,adjacent_lst,weight):
		self.initial = 0
		self.location = c
		self.max_robot=max_robot
		self.vertices=vertices
		self.adjacent_lst=adjacent_lst
		self.order_possible={}
		self.weight=weight


	def explore(self,c,cc):
		self.order_possible[c]=cc		
		for i in self.adjacent_lst[c]:
			if self.order_possible[i]==0:
				self.explore(i,cc)

	def dijkstra(self):
		self.dist={}
		flap={}
		mark=self.vertices
		for i in self.vertices:
			self.dist[i]=100000
			flap[i]=False

		self.dist[self.location]=0

		while(len(mark)!=0):
			minv=mark[0]
			for i in mark:
				if self.dist[minv]>self.dist[i]:
					minv=i
			print("dist=",self.dist)		
			for i in self.adjacent_lst[minv]:
				if flap[i]==False:
					if self.dist[i]>self.dist[minv]+self.weight[(minv,i)]:
						self.dist[i]=self.dist[minv]+self.weight[(minv,i)]
			mark.remove(minv)
			flap[minv]=True		


	def other_headquarter(self):
		for i in self.vertices:
			self.order_possible[i]=0
		self.explore(self.location,1)
		cc=2

		for i in self.vertices:
			if self.order_possible[i]==0:
				self.explore(i,cc)
				cc=cc+1
		if cc!=2:
			count={i:0 for i in range(1,cc+1)}
			for i in self.vertices:
				count[self.order_possible[i]]+=1
			maxc=0 
			maxi="nil"
			for i in range(2,cc+1):
				if maxc<count[i]:
					maxc=count[i]
					maxi=i
			lst=[]
			for i in self.vertices:
				if self.order_possible[i]==maxi:
					lst.append(i)

		else:
			lst=[]
			self.dijkstra()
			max=0
			for i in self.vertices:
				if max<self.dist[i]:
					lst=[i]
					max=self.dist[i]
				elif max==self.dist[i]:
					lst.append(i)

		
		print(lst)
		print("-------------------------------------------------")
		print()



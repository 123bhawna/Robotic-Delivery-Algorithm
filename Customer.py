class robots:
	
	def __init__(self,vertices,max_robot,adjacent_lst,weight,hotels):
		self.path=[]
		self.orders_remaining=[]
		self.order_status={}
		self.count_placed_together=0
		self.dist={}
		self.count={}
		self.max_robots=max_robot
		self.vertices=vertices
		self.possible={}
		self.robot_to_be_sent=1
		self.adjacent_lst=adjacent_lst
		self.weight=weight
		self.hotel_status={}
		self.cID=0
		self.cmembership_status={}
		self.clocation={}
		self.chotel_location={}
		self.members=[]
		for i in vertices:
			self.order_status[i]=True
			self.dist[i]=-1
			self.count[i]=0
			self.possible[i]=False


	def paths(self):
		for i in self.vertices:
			self.adjacent_lst[i]=self.merge_sort(self.adjacent_lst[i],0,len(self.adjacent_lst[i])-1,i)
			#print("----")


	def merge_sort(self,lst,u,v,i):
		if u==v:
			return lst[u:v+1]

		mid=(u+v)//2
		a1=self.merge_sort(lst,u,mid,i)
		a2=self.merge_sort(lst,mid+1,v,i)
		ctr=u
		s1=0
		s2=0
		#print("mid=",mid,v, "a1=",a1,"a2=",a2)
		while(s1<=mid-u and s2<=v-mid-1):
			if(self.weight[(i,a1[s1])]<self.weight[(i,a2[s2])]):
				lst[ctr]=a1[s1]
				ctr+=1
				s1+=1
			else:
				lst[ctr]=a2[s2]
				ctr+=1
				s2+=1
		#print("lst at end of while loop",lst)
		while(s1<=mid-u):
			lst[ctr]=a1[s1]
			ctr+=1
			s1+=1

		while(s2<=v-mid-1):
			lst[ctr]=a2[s2]
			ctr+=1
			s2+=1
		#print(lst)
		return lst[u:v+1]


	def initialising_robots(self):
		self.path=[]
		self.count_placed_together=0
		self.best={}
		self.visited={}
		for i in self.vertices:
			self.dist[i]=-1
			self.count[i]=0
			self.possible[i]=False
			self.best[i]=i
			self.visited[i]=0
			self.hotel_status[i]=False

	
	def robot_scheduing_initialise(self):
		self.time={}
		for i in range(1,self.max_robots+1):
			self.time[i]=0


	def explore(self,c,cc):
		self.order_possible[c]=cc		
		for i in self.adjacent_lst[c]:
			if self.order_possible[i]==0:
				self.explore(i,cc)
	

	def robot_scheduling(self,c):
		self.time[self.robot_to_be_sent]+=c
		print("we have sent the robot with Id",self.robot_to_be_sent)
		min=1000000
		minv="nil"
		for i in range(1,self.max_robots+1):
			if min>self.time[i]:
				min=self.time[i]
				minv=i
		self.robot_to_be_sent=minv


	def check_order_possible(self,c):
		self.order_possible={}
		for i in self.vertices:
			self.order_possible[i]=0
		self.explore(c,1)


	def order_placing(self,v,h):
		if self.order_possible[v]==0 or self.order_possible[h]==0:
			print("sorry your city is not possible to reach, we cannot take your order")
			return False
		return True


	def allocating_ID(self,mem,loc,hotel):
		self.cID+=1
		self.cmembership_status[self.cID]=mem
		self.clocation[self.cID]=loc
		self.chotel_location[self.cID]=hotel
		self.orders_remaining.append(self.cID)
		self.order_status[loc]=False
		self.hotel_status[hotel]=False
		if mem==1:
			self.members.append(self.cID)


	def customer_taken(self):
		if len(self.members)!=0:
			return self.members[0]
		return self.orders_remaining[0]		


	def path_taken_hotel(self,c,ID):
		self.path_taken(c,self.chotel_location[ID])
		self.find_path(c,self.chotel_location[ID])
		path1=self.path
		t1=self.dist[c]
		print("Path till hotel",path1)
		if self.clocation[ID] not in path1:
			self.initialising_robots()
			self.path_taken(self.chotel_location[ID],self.clocation[ID])
			self.find_path(self.chotel_location[ID],self.clocation[ID])
			path1.extend(self.path[1:])
			t1=t1+self.dist[self.chotel_location[ID]]
		print("The path taken by the robot is")
		self.print_path(path1)
		print("The total time taken is ",t1)
		return t1


	def find_path(self,c,v):
		if c==v:
			self.path.append(c)
			return
		self.path.append(c)
		self.find_path(self.best[c],v)


	def print_path(self,path):
		count=0
		for i in path:
			self.hotel_status[i]=True
			self.order_status[i]=True

		i=0
		while i<len(self.orders_remaining):
			k=True
			if self.order_status[self.clocation[self.orders_remaining[i]]]==True:
				if self.hotel_status[self.chotel_location[self.orders_remaining[i]]]==True:
					count+=1
					k=False
					if self.cmembership_status[self.orders_remaining[i]]==1:
						self.members.remove(self.orders_remaining[i])
					self.orders_remaining.remove(self.orders_remaining[i])
			if k==True:
				i=i+1
					
	
		print(path)
		print("The total order it has placed together is",count)


	def path_taken(self,c,v):

		self.visited[c]=1
		if c==v:
			self.dist[c]=0
			self.count[c]=0
			self.possible[c]=True
			return

		minimum_dist=1000000
		minv=c
		maxcount=0
		flap=False

		for i in self.adjacent_lst[c]:
				#print("c= ",c,"i= ",i)
				if self.dist[i]==-1:
					if self.visited[i]==0:
						#print("calculating distance of ",i)
						self.path_taken(i,v)
						#print("distance is",i,self.dist[i])
						#print("Count is ",i, self.count[i])
						#print()

				if self.possible[i]==True:
					flap=True
					#print("if the vertex is reachable c= ",c,"i = ",i)
					if self.dist[i]+self.weight[(c,i)]<minimum_dist:
						minimum_dist=self.dist[i]+self.weight[(c,i)] 
						minv=i
						if self.order_status[i]==False:
							maxcount=self.count[i]+1
						else:
							maxcount=self.count[i]
	
					if self.dist[i]+self.weight[(c,i)]==minimum_dist:
						if self.hotel_status[i]==False:
							minv=i


						if self.order_status[i]==False:
							if self.count[i]+1>maxcount:
								minv=i
								maxcount=self.count[i]+1
						else:
							if self.count[i]>maxcount:
								minv=i
								maxcount=self.count[i]


		if flap:
			#print("the minimum vertex is",minv)
			self.dist[c]=minimum_dist
			self.count[c]=maxcount
			self.best[c]=minv
			self.possible[c]=True

		if not flap:
			self.dist[c]=-100
                
		return
	
		
	def refreshing(self):
		self.cID=0
		self.cmembership_status={}
		self.clocation={}
		self.chotel_location={}

	


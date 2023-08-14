class Heap:
    class _Node:
        #This is the class Node which store the time of collision and index of partical whose collision occur with next partical
        def __init__(self):
            self._first_particle=None
            self._total_time=None
    def __init__(self):
        self._list_collision=[]  #This list store those partical whose collision is possible 
        self._index=[]           #This is the tracking list which stores index j of ith partical where j is the index ith partical in collisionlist  if the ith partical is not present in collision list then it stores None 
    
    def collide_particles(self,x,v):
        #Finding the possible collisions between the particals
        for i in range(len(x)):
            self._index.append(None)
        i=0
        while i<len(x)-1:
            if v[i+1]>=v[i]:
                i+=1
            else:
                collision_time=(x[i+1]-x[i])/(v[i]-v[i+1])
                node=self._Node()
                node._first_particle=i
                node._total_time=collision_time
                self._list_collision.append(node)
                self._index[i]=len(self._list_collision)-1
                i+=1
    
    def Heap_Up(self,x):
        #This function Heap up the node which is at index x while maintainig Heap property
        parent=(x-1)//2
        ans=True
        if x==0:
            self._index[self._list_collision[x]._first_particle]=x
        while parent>=0 and ans:
            node=self._list_collision[x]
            parent_node=self._list_collision[parent]
            if parent_node._total_time>node._total_time:
                self._list_collision[x],self._list_collision[parent]=self._list_collision[parent],self._list_collision[x]
                self._index[self._list_collision[x]._first_particle],self._index[self._list_collision[parent]._first_particle]=x,parent
                x=parent
                parent=(x-1)//2
            elif parent_node._total_time==node._total_time:
                if parent_node._first_particle>node._first_particle:
                    self._list_collision[x],self._list_collision[parent]=self._list_collision[parent],self._list_collision[x]
                    self._index[self._list_collision[x]._first_particle],self._index[self._list_collision[parent]._first_particle]=x,parent
                    x=parent
                    parent=(x-1)//2
                else:
                    ans=False
            else:
                ans=False
        
    def enqueue(self,node):
        #This function add a new node in the collision_list and Heap up it 
        self._list_collision.append(node) 
        self._index[node._first_particle]=len(self._list_collision)-1
        self.Heap_Up(len(self._list_collision)-1)
    
    def Heap_Down(self,x):
        #This function Heap down the node which is at index x while maintainig Heap property
        left_child=2*x+1
        right_child=2*x+2
        search=True
        if left_child>=len(self._list_collision):
            self._index[self._list_collision[x]._first_particle]=x
        while left_child<=len(self._list_collision)-1 and search:
            if right_child>len(self._list_collision)-1:
                search=False
                if self._list_collision[left_child]._total_time>self._list_collision[x]._total_time:
                    pass
                elif self._list_collision[left_child]._total_time<self._list_collision[x]._total_time:
                    self._list_collision[left_child],self._list_collision[x]=self._list_collision[x],self._list_collision[left_child]
                    self._index[self._list_collision[left_child]._first_particle],self._index[self._list_collision[x]._first_particle]=left_child,x
                else:
                    if self._list_collision[left_child]._first_particle>self._list_collision[x]._first_particle:
                        pass
                    else:
                        self._list_collision[left_child],self._list_collision[x]=self._list_collision[x],self._list_collision[left_child]
                        self._index[self._list_collision[left_child]._first_particle],self._index[self._list_collision[x]._first_particle]=left_child,x
            else:
                swap=min(self._list_collision[left_child]._total_time,self._list_collision[right_child]._total_time)       
                if self._list_collision[x]._total_time>swap:
                    if self._list_collision[left_child]._total_time>self._list_collision[right_child]._total_time:
                        self._list_collision[x],self._list_collision[right_child]=self._list_collision[right_child],self._list_collision[x]
                        self._index[self._list_collision[right_child]._first_particle],self._index[self._list_collision[x]._first_particle]=right_child,x
                        x=right_child
                    elif self._list_collision[left_child]._total_time<self._list_collision[right_child]._total_time:
                        self._list_collision[x],self._list_collision[left_child]=self._list_collision[left_child],self._list_collision[x]
                        self._index[self._list_collision[left_child]._first_particle],self._index[self._list_collision[x]._first_particle]=left_child,x
                        x=left_child
                    else:
                        if self._list_collision[left_child]._first_particle>self._list_collision[right_child]._first_particle:
                            self._list_collision[x],self._list_collision[right_child]=self._list_collision[right_child],self._list_collision[x]
                            self._index[self._list_collision[right_child]._first_particle],self._index[self._list_collision[x]._first_particle]=right_child,x
                            x=right_child
                        else:
                            self._list_collision[x],self._list_collision[left_child]=self._list_collision[left_child],self._list_collision[x]
                            self._index[self._list_collision[left_child]._first_particle],self._index[self._list_collision[x]._first_particle]=left_child,x
                            x=left_child
                    left_child=2*x+1
                    right_child=2*x+2
                elif self._list_collision[x]._total_time==swap:
                    if self._list_collision[left_child]._total_time>self._list_collision[right_child]._total_time:
                        if self._list_collision[right_child]._first_particle>self._list_collision[x]._first_particle:
                            search=False 
                        else:
                            self._list_collision[x],self._list_collision[right_child]=self._list_collision[right_child],self._list_collision[x]
                            self._index[self._list_collision[right_child]._first_particle],self._index[self._list_collision[x]._first_particle]=right_child,x
                            x=right_child
                    elif self._list_collision[left_child]._total_time<self._list_collision[right_child]._total_time:
                        if self._list_collision[left_child]._first_particle>self._list_collision[x]._first_particle:
                            search=False 
                        else:
                            self._list_collision[x],self._list_collision[left_child]=self._list_collision[left_child],self._list_collision[x]
                            self._index[self._list_collision[left_child]._first_particle],self._index[self._list_collision[x]._first_particle]=left_child,x
                            x=left_child
                    else:
                        if self._list_collision[left_child]._first_particle>self._list_collision[right_child]._first_particle:
                            if self._list_collision[right_child]._first_particle>self._list_collision[x]._first_particle:
                                search=False
                            else:
                                self._list_collision[x],self._list_collision[right_child]=self._list_collision[right_child],self._list_collision[x]
                                self._index[self._list_collision[right_child]._first_particle],self._index[self._list_collision[x]._first_particle]=right_child,x
                                x=right_child
                        else:
                            if self._list_collision[left_child]._first_particle>self._list_collision[x]._first_particle:
                                search=False
                            else:
                                self._list_collision[x],self._list_collision[left_child]=self._list_collision[left_child],self._list_collision[x]
                                self._index[self._list_collision[left_child]._first_particle],self._index[self._list_collision[x]._first_particle]=left_child,x
                                x=left_child
                    left_child=2*x+1
                    right_child=2*x+2
                else:
                    search=False

    def Build_Heap(self):
        i=len(self._list_collision)-1
        while i>=0:
            self.Heap_Down(i)
            i-=1
    def __len__(self):
        return len(self._list_collision)
    def collide_particles_first(self):
        #Finding the first collision of partical
        ans=self._list_collision[0]
        self._index[self._list_collision[0]._first_particle]=None
        self._list_collision[0]=self._list_collision[len(self._list_collision)-1]
        self._list_collision.pop()
        if len(self._list_collision)>0:
            self.Heap_Down(0)
        return ans 

    def update_time(self,i,t):
        #Update the time of collision for the partical i
        if self._list_collision[i]._total_time>t:
            self._list_collision[i]._total_time=t
            self.Heap_Up(i)
        else:
            self._list_collision[i]._total_time=t
            self.Heap_Down(i)

def position_update_time(x):
    #x is the positions of all particles
    #Return a list which contain index of position of particle and the last time position has been updated
    L=[]
    for i in range(len(x)):
        L.append(0)
    return L 

def final_Velocities(L1,L2):
    #L1 is masses of particles and L2 is initial velocities of particles
    #Return final velocities of the particles for which collision happened
    V_1= (2*L1[1]*L2[1] + (L1[0]-L1[1])*L2[0])/(L1[0]+L1[1])
    V_2 = (2*L1[0]*L2[0]+(L1[1]-L1[0])*L2[1])/(L1[0]+L1[1])
    return [V_1,V_2]

def listCollisions(M,x,v,m,T):
    #This is the main function which return all possible tuple of collisions
    L=Heap()
    L.collide_particles(x, v)
    L.Build_Heap()
    answer=[]
    Position=position_update_time(x)
    while m>0 and T>0:
        if len(L)>0:
            first_collision=L.collide_particles_first()
            t_min=first_collision._total_time
            if t_min>T:
                return answer
            else:
                i=first_collision._first_particle
                x[i]+=v[i]*(t_min-Position[i])
                x[i+1]+=v[i+1]*(t_min-Position[i+1])
                Position[i],Position[i+1]=t_min,t_min
                v_1,v_2=v[i],v[i+1]
                v[i],v[i+1]=final_Velocities([M[i],M[i+1]], [v[i],v[i+1]])
                collision_tuple=(round(t_min,4),i,round(x[i],4))
                answer.append(collision_tuple)
                if i!=0 and (i+1)!=len(M)-1:
                    if v[i]>=v[i-1]:
                        pass
                    else:
                        x[i-1]+=v[i-1]*(t_min-Position[i-1])
                        Position[i-1]=t_min
                        t=(x[i]-x[i-1])/(v[i-1]-v[i])
                        if v[i-1]>v_1:
                            L.update_time(L._index[i-1], t+t_min)
                        else:
                            node=L._Node()
                            node._first_particle=i-1
                            node._total_time=t+t_min
                            L.enqueue(node)
                    if v[i+2]>=v[i+1]:
                        pass
                    else:
                        x[i+2]+=v[i+2]*(t_min-Position[i+2])
                        Position[i+2]=t_min
                        t=(x[i+2]-x[i+1])/(v[i+1]-v[i+2])
                        
                        if v_2>v[i+2]:
                            L.update_time(L._index[i+1], t+t_min)
                        else:
                            node=L._Node()
                            node._first_particle=i+1
                            node._total_time=t+t_min
                            L.enqueue(node)
                elif i==0:
                    if v[i+2]>=v[i+1]:
                        pass
                    else:
                        x[i+2]+=v[i+2]*(t_min-Position[i+2])
                        Position[i+2]=t_min
                        t=(x[i+2]-x[i+1])/(v[i+1]-v[i+2])
                        if v_2>v[i+2]:
                            L.update_time(L._index[i+1], t+t_min)
                        else:
                            node=L._Node()
                            node._first_particle=i+1
                            node._total_time=t+t_min
                            L.enqueue(node)
                else:
                    if v[i]>=v[i-1]:
                        pass
                    else:
                        x[i-1]+=v[i-1]*(t_min-Position[i-1])
                        Position[i-1]=t_min
                        t=(x[i]-x[i-1])/(v[i-1]-v[i])
                        if v[i-1]>v_1:
                            L.update_time(L._index[i-1], t+t_min)
                        else:
                            node=L._Node()
                            node._first_particle=i-1
                            node._total_time=t+t_min
                            L.enqueue(node)
        else:
            return answer 
        m-=1
    return answer



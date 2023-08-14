import math
class Heap:
    def __init__(self):
        self._data=[]
    
    def Heap_Up(self,x):
        #x is basically index of the data that must be Heap_Up
        ans=True
        parent=(x-1)//2
        while parent>=0 and ans:
            if self._data[x]>self._data[parent]:
                ans=False
            else:
                self._data[x],self._data[parent]=self._data[parent],self._data[x]
                x=parent
                parent=(parent-1)//2
    def __len__(self):
        return len(self._data)

    def enqueue(self,x):
        self._data.append(x)
        self.Heap_Up(len(self._data)-1)

    def Heap_Down(self,x):
        #x is the index of the data that must be Heaped_Down
        left_child=2*x+1
        right_child=2*x+2
        search=True
        while left_child<len(self._data)-1 and search:
            if right_child>len(self._data)-1:
                search=False
                if self._data[left_child]<self._data[x]:
                    self._data[left_child],self._data[x]=self._data[x] , self._data[left_child]
                else:
                    pass 
            else:
                swap=min(self._data[left_child],self._data[right_child])
                if self._data[x]>swap:
                    if self._data[left_child]>self._data[right_child]:
                        self._data[right_child],self._data[x]=self._data[x] , self._data[right_child]
                        x=right_child
                    else:
                        self._data[left_child],self._data[x]=self._data[x] , self._data[left_child]
                        x=left_child
                    left_child=2*x+1
                    right_child=2*x+2
                else:
                    search=False
    
    def Extract_Min(self):
        ans=self._data[0]  
        self._data[0]=self._data[len(self._data)-1]
        self._data.pop()
        self.Heap_Down(0)
        return ans  

def find_Path(path,s,t):
    required_path=[]
    counter=t
    required_path.append(t)
    while (counter!=s):
        required_path.append(path[counter])
        counter=path[counter]
    i=0
    actual_path=[0 for i in range(len(required_path))]
    while i<len(required_path):
        actual_path[i]=required_path[len(required_path)-i-1]
        i+=1
    return actual_path

def findMaxCapacity(n,links,s,t):
    graph=[[] for i in range(n)]
    i=0
    while i<len(links):
        graph[links[i][0]].append((links[i][1],links[i][2]))
        graph[links[i][1]].append((links[i][0],links[i][2]))
        i+=1
    distance = [0 for i in range(len(graph))]
    path=[0 for i in range(len(graph))]
    Is_visited=[False for i in range(len(graph))]
    if s==t:
        return (0,[t])
    heap=Heap()
    heap.enqueue((-math.inf,s))
    search=True
    length=len(heap)+1
    while(search):
        if length==0:
            search=False
        else:
            pop_element=heap.Extract_Min()
            length-=1 
            if pop_element[1]==t:
                search=False
            if Is_visited[pop_element[1]]:
                continue
            for i in graph[pop_element[1]]:
                k=distance[i[0]]
                distance[i[0]]=max(distance[i[0]],min(-pop_element[0],i[1]))
                if Is_visited[i[0]]==False and k!=distance[i[0]]:
                    path[i[0]]=pop_element[1]
                    heap.enqueue((-distance[i[0]],i[0]))
                    length+=1
            Is_visited[pop_element[1]]=True 
   
    return (distance[t],find_Path(path, s, t))


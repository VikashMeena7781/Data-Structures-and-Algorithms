def merge(L1,L2):
    #Merge function which merge two sorted lists 
    n,m=len(L1),len(L2)
    i,j=0,0
    L=[]
    while (i<n and j<m):
        if L1[i][1]>=L2[j][1]:
            L.append(L2[j])
            j+=1
        else:
            L.append(L1[i])
            i+=1
    if i==n:
        while(j<m):
            L.append(L2[j])
            j+=1
    else:
        while(i<n):
            L.append(L1[i])
            i+=1
    return L 

class PointDatabase:
    class _Node:
        def __init__(self,x):
            self.x=x
            self.left=None
            self.right=None
            self.parent=None
            self.Is_leaf=False 
            self.ylist=[]
    def __init__(self, pointlist):
        self.pointlist = pointlist
        self.x_sorted=sorted(pointlist , key=lambda x:x[0])
        self.tree=self.build(self.x_sorted)
    
    #This function takes a sorted list based on x cordinates and return 2D rangee Tree... (here each node contain a sorted list baesd on y of their predecessor)
    def build(self,L):
        if len(L)==0:
            return None
        elif len(L)==1:
            node=self._Node(L[0])
            node.Is_leaf=True
            node.ylist=[L[0]]
            return node 
        else:
            mid=len(L)//2
            node=self._Node(L[mid])
            node.left=self.build(L[0:mid])
            node.left.parent=node
            if (1+mid<len(L)):
                node.right=self.build(L[1+mid:])
                node.right.parent=node
            if node.right!=None and node.left!=None:
                L1,L2,L3=node.left.ylist,node.right.ylist,[L[mid]]
                L4=merge(L1, L2)
                L5=merge(L4, L3)
                node.ylist=L5
                return node 
            elif node.right!=None and node.left==None:
                L1,L2=node.right.ylist,[L[mid]]
                node.ylist=merge(L1, L2)
                return node
            else:
                L1,L2=node.left.ylist,[L[mid]]
                node.ylist=merge(L1, L2)
                return node
        
    #This function find the splitnode
    def search_split_node(self,node,x1,x2):
        ans = node 
        while ans != None:
            y=ans.x
            x=y[0]
            if x2 <x:
                ans = ans.left
            elif x1 > x:
                ans = ans.right
            elif x1 <= x <= x2 :
                break
        return ans
    #This is binary search function which find data of a sorted list in a given range
    def Search_y_Tree(self,L,y1,y2):
        ans=[]
        if len(L)==0:
            return ans 
        elif len(L)==1:
            if y1<=L[0][1]<=y2:
                ans.append(L[0])
                return ans 
            else:
                return ans 
        else:
            mid=len(L)//2
            if L[mid][1]>y2:
                ans+=self.Search_y_Tree(L[0:mid],y1,y2)
            elif L[mid][1]<y1:
                if (1+mid)<len(L):
                    ans+=self.Search_y_Tree(L[1+mid:],y1,y2)
            else:
                ans.append(L[mid])
                ans+=self.Search_y_Tree(L[0:mid], y1, y2)
                if (1+mid)<len(L):
                    ans+=self.Search_y_Tree(L[1+mid:], y1, y2)
            return ans 
    #This function finds whether a point lies in range or not ... if lie then return True otherwise False 
    def Is_Range(self,point,L):
        x = point[0]
        if (x >= L[0][0]   and x <= L[0][1] ) :
            return True
        else:
            return False
    #This is the main function which returns all the query within the range of query point
    def searchNearby(self,q,d):
        critical_node=self.search_split_node(self.tree, q[0]-d, q[0]+d) 
        ans=[]
        if critical_node==None:
            return ans 
        elif self.Is_Range(critical_node.x,[(q[0]-d,q[0]+d)]):
            if q[1]-d <=critical_node.x[1]<= q[1]+d:
                ans.append(critical_node.x) 
            node_1=critical_node.left
            search=True 
            if node_1!=None:
                while(search):
                    if self.Is_Range(node_1.x, [(q[0]-d,q[0]+d)]):
                        if q[1]-d <=node_1.x[1]<= q[1]+d:
                            ans.append(node_1.x)
                    if (q[0]-d)<= node_1.x[0]:
                        if node_1.right!=None:
                            ans+=self.Search_y_Tree(node_1.right.ylist,q[1]-d, q[1]+d)
                        node_1=node_1.left
                        if node_1 is None:
                            search=False 
                    else:
                        node_1=node_1.right
                        if node_1==None:
                            search=False 
            node_2=critical_node.right
            find=True
            if node_2 !=None:
                while (find):
                    if self.Is_Range(node_2.x, [(q[0]-d,q[0]+d)]):
                        if q[1]-d <=node_2.x[1]<= q[1]+d:
                            ans.append(node_2.x)
                    if (q[0]+d)>=node_2.x[0]:
                        if node_2.left!=None:
                            ans+=self.Search_y_Tree(node_2.left.ylist, q[1]-d, q[1]+d)
                        node_2=node_2.right  
                        if node_2==None:
                            find=False  
                    else:
                        node_2=node_2.left
                        if node_2==None:
                            find=False 
            return ans 
        else:
            return ans 

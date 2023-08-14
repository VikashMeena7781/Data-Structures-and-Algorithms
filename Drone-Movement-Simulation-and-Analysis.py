class Empty(Exception):
    #This is the class which through an exception if there is an empty thing(alike List , Stack etc.)
    pass 
#This is the class Stack()
class Stack:
    ##Nested class _Node which is private 
    class _Node:
        def __init__(self):
            self._element=None    ##Element of the node
            self._next=None       ##Reference of the next node 
    def __init__(self):
        self._head=None       #Pointer to the top node of the linked list 
        self._size=0

    def is_empty(self):
        return self._size==0
    
    def __len__(self):
        return self._size 
    
    def push(self,x):  #Push an element at the top of the Stack
        new_Node = self._Node()
        new_Node._element=x
        if self._size==0:
            self._head=new_Node
            new_Node._next=None
        else:
            old=self._head
            self._head=new_Node
            new_Node._next=old 
        self._size+=1

    def pop(self):         #Remove an element from the top of the Stack if the stack is not empty otherwise throw an error 
        if self._size==0:
            raise Empty("Stack is Empty")
        else:
            Required_Node=self._head
            self._size-=1
            if Required_Node._next==None:
                self._head=None
            else:
                self._head=Required_Node._next
            Required_Node=None
    def top(self):           #Return the top element of the Stack if it is not empty otherwise throw an error
        if self._size==0:
            raise Empty("The Stack is Empty")
        else:
            return (self._head)._element

#This is the required function which will determine the final x,y,z cordinates of the drone and the distance travelled by the drone. 
def findPositionandDistance(P):
   #input :- P is a string 
   #Output :- List containing the final cordinates and the distance travelled by the drone
    x,y,z,d=0,0,0,0  #Initializing the x,y,z cordinates of the drone and the distance to be travelled by the drone.
    L=Stack()         #Initializing the empty Stack()
    i=0
    while i<len(P):  #An iteration over the input string
        if P[i].isnumeric():   #If the ith element of the string is Numerical 
            if len(L)==0:
                j=i+1
                search=True
                final_integer=P[i]
                while j<len(P) and search:   #If there are more than one digit in any integer(as they will be considered as different element of the string) 
                    if P[j].isnumeric():     #then we have to evaluate them through concatenating the digits of that integer.This part of code do the same thing.
                        final_integer+=P[j]
                        j+=1
                    else:
                        ans=[int(final_integer),j]
                        search=False 
                L.push(ans[0])
                i=ans[1]+1    
            else:
                j=i+1
                search=True
                final_integer=P[i]
                while j<len(P) and search:
                    if P[j].isnumeric():       #If there are more than one digit in any integer(as they will be considered as different element of the string) 
                        final_integer+=P[j]         #then we have to evaluate them through concatenating the digits of that integer.This part of code do the same thing.
                        j+=1
                    else:
                        ans=[int(final_integer),j]
                        search=False
                top=L.top()           #If there are brackets over brackets then we will keep track of the suitable factors that should be multiplied(with this factor the cordinates or distance will change) with the cordinates.
                x1=top*ans[0]         #For that we get the top element of the Stack() and multiply it with the recently got integer then push the result in Stack()
                L.push(x1)
                i=ans[1]+1 
        elif P[i]=="+":             #Updating the cordinates and distance 
            if P[i+1]=="X":   
                if len(L)==0:
                    x+=1
                    d+=1
                else:
                    factor=L.top()   #Get the suitable factor with which the codinates or distance will change.
                    x+=factor
                    d+=factor
            elif P[i+1]=="Y":
                if len(L)==0:
                    y+=1
                    d+=1
                else:
                    factor=L.top()
                    y+=factor
                    d+=factor 
            else:
                if len(L)==0:
                    z+=1
                    d+=1
                else:
                    factor=L.top()
                    z+=factor
                    d+=factor 
            i+=2
        elif P[i]=="-":             #Updating the cordinates and distance 
            if P[i+1]=="X":
                if len(L)==0:
                    x-=1
                    d+=1
                else:
                    factor=L.top()
                    x-=factor
                    d+=factor
            elif P[i+1]=="Y":
                if len(L)==0:
                    y-=1
                    d+=1
                else:
                    factor=L.top()
                    y-=factor
                    d+=factor 
            else:
                if len(L)==0:
                    z-=1
                    d+=1
                else:
                    factor=L.top()
                    z-=factor
                    d+=factor
            i+=2
        else:                     #if the character of the string is ")" then we will delete(pop) the top element of the Stack() because we do not need no longer this element provided the length of the 
            if len(L)==0:         # Stack is not zero. If the Stack() is empty then just increment i.
                i+=1
            else:
                L.pop()
                i+=1
    Output=[x,y,z,d]
    return Output


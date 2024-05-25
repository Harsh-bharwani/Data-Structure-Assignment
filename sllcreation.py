class Node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Single_linklist():
    def __init__(self):
        self.__head=None
        self.__size=0
    def size(self):
        return self.__size
    def is_empty(self):
        return self.__size==0
    def append(self,data):
        new_node=Node(data)
        if(self.is_empty()):
            self.__head=new_node
            self.__tail=new_node
        else:
            self.__tail.next=new_node
            self.__tail=new_node
        self.__size+=1        
    def add_at_first(self,data):
        new_node=Node(data)
        if self.is_empty():
            self.__head=new_node
            self.__tail=new_node
        else:
            new_node.next=self.__head
            self.__head=new_node
        self.__size+=1 
    def remove_at_last(self):
        trav=self.__head
        for i in range(self.__size-2):
            trav=trav.next
        temp=trav.next
        trav.next=None
        del(temp)
        self.__size-=1
    def remove_at_first(self):
        temp=self.__head
        self.__head=temp.next
        del(temp)
        self.__size-=1
    def add_at_index(self,index,data):
        new_node=Node(data)
        if index<0 or index>self.__size:
            raise Exception("Invalid_index")
        elif index==0:
            self.add_at_first()
        elif index==self.size:
            self.append()
        id=0
        trav=self.__head
        while id!=index-1:
            trav=trav.next
            id+=1
        new_node.next=trav.next
        trav.next=new_node
        self.__size+=1
    def remove_at_index(self,index):
        if index<0 or index>self.__size-1:
            raise Exception("Invalid Index")
        elif index==0:
            self.remove_at_first()
        elif index==self.__size-1:
            self.remove_at_last()
        else:
            id=0
            trav=self.__head
            for i in range(index-1):
                trav=trav.next
                id+=1
        temp=trav.next
        trav.next=temp.next
        del(temp)
        self.__size-=1
    def __str__(self) -> str:
        trav=self.__head
        l=[]
        while trav!=None:
            l.append(str(trav.data))
            trav=trav.next
        return "".join(l)
    def peekfirst(self):
        '''return the first element if it exists '''
        if(self.is_empty()):
            raise "Emplty LinkedList"
        return self.__head.data
    def peeklast(self):
        '''return the last element if it exists '''
        if(self.is_empty()):
            raise "Emplty LinkedList"
        trav=self.__head
        while(trav.next!=None):
            trav=trav.next
        return trav.data
    # def __remove__(self,node):
    #     if node.prev==None:
    def index_of(self,data):
        trav=self.__head
        id=0
        while(trav!=None):
            if(trav.data==data):
                return id
            trav=trav.next
            id+=1
        return -1
    def __iter__(self): 
        self.__iter = self.__head
        return self


    def __next__(self): 
        if self.__iter is None :
            raise StopIteration
    
        data = self.__iter.data
        self.__iter = self.__iter.next
        return data
    def rotate(self,k):
        k=k%self.__size
        if k==0:
            return self.__str__()
        trav=self.__head
        for i in range(self.size()-k-1):
            trav=trav.next
        newhead=temp= trav.next
        trav.next=None
        for i in range(k-1):
            temp=temp.next
        temp.next=self.__head
        self.__head=newhead
    def reverse(self):
        prev=None
        cur=self.__head
        next=cur.next
        while(cur.next!=None):
            cur.next=prev
            prev=cur
            cur=next
            next=cur.next
        cur.next=prev
        self.__head=cur
    def merge(self,l2):
        sec_list_head=l2.__head
        trav=self.__head
        while(trav.next!=None):
            trav=trav.next
        trav.next=sec_list_head
        self.__size+=l2.size()
    def split(self,index):   # return the splitted string
        trav=self.__head
        for i in range(index-1):
            trav=trav.next
        temp=trav.next
        trav.next=None
        sll2=Single_linklist()
        sll2.__head=temp      
        return sll2,self 
    def interleave(self,l2):
        head=self.__head
        head2=l2.__head
        while head and head2:   # Break when either of them is None
            head_next=head.next
            head2_next=head2.next
            head.next=head2
            if head_next==None:
                break            #Case when the first string is smaller than the second
            head2.next=head_next
            head=head_next
            head2=head2_next
    def middle(self):
        slow=self.__head 
        fast=self.__head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def occurence(self,data):
        trav=self.__head
        id=0
        while(trav!=None):
            if(trav.data==data):
                return id 
            id+=1
            trav=trav.next
        return -1
    def merge(self,l2):
        l1=self.__head
        l2=l2.__head
        cur=newnode=Node(0)
        while(l1 and l2):
            if l2.data<l1.data:
                cur.next=l2
                cur=cur.next
                l2=l2.next
            else:
                cur.next=l1
                cur=cur.next
                l1=l1.next
        if l1:
            cur.next=l1
            # cur=cur.next
        if l2:
            cur.next=l2
            # cur=cur.next
        self.__head=newnode.next

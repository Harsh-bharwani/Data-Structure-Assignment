class Myarray:
    def __init__(self,cap:int):
        self.__capacity=cap
        self.__size=0
        self.__data=[None]*cap
        self.__type=type
    def __getitem__(self,index:int):
        if 0<= index <self.__size:
            return self.__data[index]
        else:
            raise IndexError("Index out of bound")
    def __setitem__(self,index:int,value):
        if 0<= index <self.__size:
            self.__data[index]=value
        else:
            raise IndexError("Index out of bound")
    def __resize(self,factor=2):
        newarray=[None]*(factor*self.__capacity)
        for i  in range(self.__size):
            newarray[i]=self.__data[i]
            self.__capacity=factor*self.__capacity
        self.__data=newarray
    def append(self,value):
        if(self.__size==self.__capacity):
            self.__resize()
        self.__data[self.__size]=value
        self.__size+=1
    def prepend(self,data):
        if self.__size==self.__capacity:
            self.__resize()
        for i in range(self.__size-1,-1,-1):
            self.__data[i+1]=self.__data[i]
        self.__data[0]=data
        self.__size+=1
    def __len__(self):
        return self.__size
    def insert_at(self,index,value):
        if index<0 or index>self.__size:
            raise "Invalid Index"
        if index==0:
            self.prepend()
        elif index==self.__size:
            self.append()
        else:
            if self.__size==self.__capacity:
                self.__resize()
            for i in range(self.__size-1,index-1,-1):
                self.__data[i+1]=self.__data[i]
            self.__data[index]=value
            self.__size+=1
    def del_first(self):
        for i in range(0,self.__size-1):
            self.__data[i]=self.__data[i+1]
        self.__size-=1
    def del_last(self):
        del (self.__data[self.__size-1])
        self.__size-=1
    def delete_at(self,index):
        if index<0 or index>self.__size:
            raise "Invalid Index"
        if index==0:
            self.del_at_last()
        elif index==self.__size-1:
            self.del_at_last()
        else:
            for i in range(index,self.__size-1):
                self.__data[i]=self.__data[i+1]
        self.__size-=1
    def __str__(self):
        l=[]
        for i in range(self.__size):
            l.append(str(self.__data[i]))
        return "".join(l)
    def is_empty(self):
        return bool(not self.__size)
    def rotate(self,k):
        k=k%self.__size
        index=self.__size-1
        for i in range(k):

            self.prepend(self.__data[index])
            self.del_last()
    def reverse(self):
        for i in range(self.__size//2):
            temp=self.__data[i]
            self.__data[i]=self.__data[self.__size-1-i]
            self.__data[self.__size-1-i]=temp
    def concatenate(self,array):
        index=0
        for i in range(array.__size):
            self.append(array.__data[i])
            index+=1
    def merge(self,array):
        i=0
        j=0
        while( i<self.__size and j<array.__size):
            if array.__data[j]<self.__data[i]:
                self.insert_at(i,array.__data[j])
                j+=1
            i+=1
        if j!=array.__size-1:
            for j in range(j,array.__size):
                self.append(array.__data[j])
    def interleave(self,array):
        i=0
        j=0
        while i<self.__size + array.__size  and j <array.__size:
            self.insert_at(i+1,array.__data[j])
            i+=2
            j+=1
    def middle(self):
        return self[(self.__size+1)//2 -1]
    def occurence_of(self,value):
        for i in range(self.__size):
            if self[i]==value:
                return i
        return -1
    def split(self,index):
        new_arr=Myarray(1)
        for i in range(index+1,self.__size):
            new_arr.append(self[i])
        for i in range(index+1,self.__size):
            self.del_last()
        return new_arr,self
  

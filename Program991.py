#DONE
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyLL:
    #DONE
    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self,No):
        newn = Node(No) #object of newn
        #LL is empty
        if(self.first == None):
            self.first = newn
        #It contains atleast 1 node
        else:
            newn.next=self.first
            self.first = newn
        self.iCount = self.iCount + 1

    #DONE
    def InsertLast(self,No):
        newn = Node(No) #object of newn
        #LL is empty
        if(self.first == None):
            self.first = newn
        #It contains atleast 1 node
        else:
            temp = self.first
            while(temp.next != None):
                temp = temp.next
            
            temp.next = newn
        self.iCount = self.iCount + 1
    #DONE
    def InsertAtPos(self,No,Pos):
        #Invalid position filter
        if (Pos < 1 or Pos > (self.iCount +1)):
            print("Invalid Position")
            return
        
        if(Pos == 1):
            self.InsertFirst(No)
            return
        elif(Pos == self.iCount+1):
            self.InsertLast(No)
            return
        else:
            newn = Node(No)
            temp = self.first
            for i in range(1,Pos-1):
                temp = temp.next
            newn.next = temp.next
            temp.next = newn

            self.iCount = self.iCount+1

        

    def DeleteFirst(self,No):
        pass

    def DeleteLast(self,No):
        pass

    def DeleteAtPos(self,No,Pos):
        pass
    #DONE
    def Count(self):
        return self.iCount
    #DONE
    def Display(self):
        temp = self.first
        while (temp != None):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

        print("None")

  
        
def main():
    sobj = SinglyLL() #object of singlyll
    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)
    print("Elements of linked list are : ")
    sobj.Display()

    print("No of elements in linked list are : ",sobj.Count())

    sobj.InsertLast(111)
    sobj.InsertLast(121)

    

    print("Elements of linked list are : ")
    sobj.Display()

    print("No of elements in linked list are : ",sobj.Count())

    sobj.InsertAtPos(75,4)

    print("Elements of linked list are : ")
    sobj.Display()

    print("No of elements in linked list are : ",sobj.Count())

if __name__ =="__main__":
    main()
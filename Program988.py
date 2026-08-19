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
        pass

    def InsertLast(self,No):
        pass

    def InsertAtPos(self,No,Pos):
        pass

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

if __name__ =="__main__":
    main()
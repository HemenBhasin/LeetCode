class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next

class MyLinkedList:

    def __init__(self,head=None):
        self.head=head
        

    def get(self, index: int) -> int:
        curr=self.head
        if index < 0 :
            return -1
        for i in range(index):
            if curr is None:
                return -1
            curr=curr.next
        return curr.data if curr else -1

    def addAtHead(self, value: int) -> None:
        temp=Node(value)
        temp.next=self.head
        self.head=temp

    def addAtTail(self, value: int) -> None:
        temp=Node(value)
        if (self.head!=None):
            t1=self.head
            while (t1.next!=None):
                t1=t1.next
            t1.next=temp  
        else:
            self.head=temp

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        curr=self.head
        temp=Node(val)
        for i in range(index-1):
            if curr is None:
                return
            curr=curr.next
        if curr is None:
            return    
        temp.next=curr.next
        curr.next=temp    

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        curr=self.head
        if index==0:
            self.head=self.head.next
        else:
            for i in range(index-1):
                if curr.next is None:
                    return
                curr=curr.next
            if curr.next:
                curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
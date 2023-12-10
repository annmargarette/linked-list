class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
        
        
    def insert_at_beginning(self, data): 
        new_node = Node(data)
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.tail=new_node
            self.head=new_node
    
    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head:
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=new_node
            self.tail=new_node
    
    def remove_beginning(self):
        if self.head is None:
            return None
        else:
            removed_node = self.head
            self.head = self.head.next
            removed_node.next = None
            return removed_node.data
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node= current_node.next
        return False
    
    
    
def combine(linkedlist1, linkedlist2):
        resulting_list = LinkedList()
        
        while linkedlist1.head or linkedlist2.head:
            if list1.head and list2.head:
                num1 = list1.head.data
                num2 = list2.head.data
                if num1 < num2:
                    resulting_list.insert_at_end(list1.remove_beginning())
                else:
                    resulting_list.insert_at_end(list2.remove_beginning())    
            elif list1.head:
                resulting_list.insert_at_end(list1.remove_beginning())
            else:
                resulting_list.insert_at_end(list2.remove_beginning())
        
        
        return resulting_list
        

list1 = LinkedList()
list2 = LinkedList()

list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)

list2.insert_at_end(1)
list2.insert_at_end(3)
list2.insert_at_end(4)


result = combine(list1, list2)

it = result.head
while it:
    print(it.data, end="")
    if(it.next):
        print(" -> ", end="")
    it = it.next

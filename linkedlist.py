class Node:
    def__init__(self,data):
       self.data=data 
       self.next=None 

n1=Node(10)
n2=Node(15)
n3=Node(20)
n4=Node(30)
new_node=Node(25)

n1.next=n2
n2.next=n3
n3.next=new_node
new_node.next=n4
temp=n1
while temp:
    print(temp.data,end=" -> ")
    temp=temp.next

    print("None")
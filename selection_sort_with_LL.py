#creat class for linked list
import time
from random import randrange


class Node:
    #constructor
    def __init__ (self, initdata):
        self.data = initdata
        self.next = None
    #set data
    def setdata(self, data):
        self.data = data
    #get data
    def getdata(self):
        return self.data
    #set next
    def setnext(self, nextdata):
        self.next = nextdata
    #get nextdata
    def getnext(self):
        return self.next

#creat class to get the data from user
class unordered_linkedlist:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    # sort list
    def select_sort(self,list):
        fixed = self.head
        prevfixed = None
        while fixed != None:
            previous = fixed
            current = fixed.next
            min = fixed.data
            prev = None
            curr = fixed
            while current != None:
                if min > current.data:
                    min = current.data
                    prev = previous
                    curr = current
                else:
                    previous = previous.next
                    current = current.next
            if prev != None:
                prev.setnext(curr.next)
                curr.setnext(fixed)
            if prevfixed == None:
                self.head = curr
            else:
                prevfixed.setnext(curr)
            fixed = curr
            prevfixed = fixed
            fixed = fixed.next
        # return list

    def display(self):
        list = self.head
        while list != None:
            print (list.data() , end=',')
            list = list.next()







start = time.time()

list = unordered_linkedlist()
for i in range(10000):
    list.add(randrange(-1000, 1000))
print ("a")
# print("the list before sotring : ")
# list.display()
list.select_sort(list)
print("the list after sotring : ")
# list.display()
end = time.time()
print()
print("the time that this program takes to execute is :", end - start)
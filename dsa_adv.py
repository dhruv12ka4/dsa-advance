#Question 1
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        h = self.head
        if self.head is None:
            self.head = new_node
            return
        else:
            while h.next!=None:
                h = h.next
            h.next = new_node

    def remove_zeros_from_linkedlist(self, head):
        stack = []
        curr = head
        list = []
        while (curr):
            if curr.data >= 0:
                stack.append(curr)
            else:
                temp = curr
                sum = temp.data
                flag = False
                while (len(stack) != 0):
                    temp2 = stack.pop()
                    sum += temp2.data
                    if sum == 0:
                        flag = True
                        list = []
                        break
                    elif sum > 0:
                        list.append(temp2)

                 if not flag:
                    if len(list) > 0:
                        for i in range(len(list)):
                            stack.append(list.pop())
                    stack.append(temp)
            curr = curr.next
        return [i.data for i in stack]

if __name__ == "__main__":
    l = Linkedlist()

    l.append(4)
    l.append(6)
    l.append(-10)
    l.append(5)
    print(l.remove_zeros_from_linkedlist(l.head))


#Question2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    
    def __init__(self):
        self.head = None

    def reverse(self, head, k):
            
        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

         if next is not None:
            head.next = self.reverse(next, k)
            
        return prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next


llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Given linked list")
llist.printList()
llist.head = llist.reverse(llist.head, 3)

print ("\nReversed Linked list")
llist.printList()
Given linked list
1 2 3 4 5 6 7 8 9 
Reversed Linked list
3 2 1 6 5 4 9 8 7


#Question3

class Node(object):
	def __init__(self, data:int):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		
	def push(self, new_data:int):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next

	def merge(self, p, q):
		p_curr = p.head
		q_curr = q.head


		while p_curr != None and q_curr != None:

	
			p_next = p_curr.next
			q_next = q_curr.next

		
			q_curr.next = p_next 
			p_curr.next = q_curr 

			
			p_curr = p_next
			q_curr = q_next
			q.head = q_curr

llist1 = LinkedList()
llist2 = LinkedList()

llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)

for i in range(8, 3, -1):
	llist2.push(i)

print("First Linked List:")
llist1.printList()

print("Second Linked List:")
llist2.printList()

llist1.merge(p=llist1, q=llist2)

print("Modified first linked list:")
llist1.printList()

print("Modified second linked list:")
llist2.printList()


#Question4
def getPairsCount(arr, n, sum):
     
    count = 0
 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
 
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))


#Question 5
  
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3] 
     
print("Duplicate elements in given array: ")

for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            print(arr[j])


#Question6
def findkmax(k, array):

    array.sort(reverse=True)

    print("K th maximum element is: ", array[k - 1])


def findkmin(k, array):
    array.sort()

    print("K th minimum element is: ", array[k - 1])


array = [1, 7, 6, 8, 9, 2, 4, 5, 3, 0]
k = 2

findkmax(k, array)
findkmin(k, array)


#Question 7
def find(arr):
    arr.sort()
    print("Array after moving all the elements to left:", arr)


array = [1, 3, -1, 4, -3, -5, -6, 3, 7]
find(array)


#Question 8

def reversestr(s):
    
    stack = []
    
    for i in s:
        stack.append(i)
    
    s = ""
    
    while stack:
        s += stack.pop()

    return s
 

if __name__ == "__main__":

    str = "Hello"
    reversed_str = reversestr(str)
    print("Reversed string is: ", reversed_str)


#Question 9 
def postfix_evaluation(s):
    
    s=s.split()

    n=len(s)

    stack =[]

    for i in range(n):

        if s[i].isdigit():

            stack.append(int(s[i]))

        elif s[i]=="+":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)+int(b))

         elif s[i]=="*":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(a)*int(b))

        elif s[i]=="/":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)/int(a))

        elif s[i]=="-":

            a=stack.pop()

            b=stack.pop()

            stack.append(int(b)-int(a))


      return stack.pop()

s="10 2 8 * + 3 -"

val=postfix_evaluation(s)

print(val)


#Question 10

class Queue:
	def __init__(self):
		self.s1 = []
		self.s2 = []

	def enQueue(self, x):
		
		while len(self.s1) != 0:
			self.s2.append(self.s1[-1])
			self.s1.pop()

		self.s1.append(x)

		while len(self.s2) != 0:
			self.s1.append(self.s2[-1])
			self.s2.pop()

	def deQueue(self):
		
		if len(self.s1) == 0:
			print("Q is Empty")
	
		x = self.s1[-1]
		self.s1.pop()
		return x

if __name__ == '__main__':
	q = Queue()
	q.enQueue(1)
	q.enQueue(2)
	q.enQueue(3)

	print(q.deQueue())
	print(q.deQueue())
	print(q.deQueue())
1		
    

               
    

class node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self):
		self.head = None

	def createlist(self, ll):
		self.head = node(ll[0])
		curr = self.head
		
		for i in range(1,len(ll)):
			n = node(ll[i])
			curr.next = n
			curr = n
		self.listall()

	def appendfront(self,val):
		if(self.head):
			newnode = node(val,self.head)
			self.head = newnode
		else:
			self.head = node(val)
		self.listall()

	def listall(self):
		itr = self.head
		while(itr):
			print(itr, end="-->")
			itr = itr.next
		print()

	def appendend(self, val):
		if(self.head):
			itr = self.head
			while(itr.next):
				itr = itr.next
			itr.next = node(val)
		else:
			self.head = node(val)
		self.listall()

	def getsize(self):
		count = 0
		itr = self.head
		while itr:
			count = count + 1
			itr = itr.next

		return count

	def append(self,i,val):
		if(i<0 or i>=self.getsize()):
			print("invalid index")
			return
		count = 0
		itr = self.head
		while(count!=(i-1)):
			itr = itr.next
			count+=1
		newnode = node(val,itr.next)
		itr.next = newnode
		self.listall()

	def remove(self, index):
		if index<0 or index>=self.getsize():
			raise Exception("Invalid Index")
		if index == 0:
			self.head = self.head.next
			
		else:	
			count = 0
			itr = self.head
			while count != index-1 :
				itr = itr.next
				count += 1
			itr.next = itr.next.next
		self.listall()

	def insert_after_value(self, data_after, data_to_insert):

		itr = self.head
		while(itr):
			if(itr.data == data_after):
				n = node(data_to_insert, itr.next)
				itr.next = n
				break
			itr = itr.next
		self.listall()

	def remove_by_value(self, data):
		itr = self.head
		if(itr.data == data):
			self.head = itr.next
			self.listall()
			return

		while(itr):
			if(itr.next.data == data):
				itr.next = itr.next.next
				break
			itr = itr.next
		self.listall()

	def findmiddle(self):
		p1 = self.head
		p2 = self.head

		while(p2 and p2.next):
			p2 = p2.next.next
			p1 = p1.next
		return print(p1.data)

	def reverse(self, head):
		print("current head", head)

		if(head.next == None):
			self.head = head
			return head
		else:
			prev = self.reverse(head.next)
			print("prev",prev)
			print("head is: ", head)
			prev.next = head
			head.next = None

			return head









l1=["banana","mango","grapes","orange", "jackfruit", "peach"]

linkedlist = LinkedList()

linkedlist.createlist(l1)
# linkedlist.findmiddle()
linkedlist.reverse(linkedlist.head)
linkedlist.listall()

# linkedlist.insert_after_value('banana', 'jackfruit')
# linkedlist.remove_by_value('banana')




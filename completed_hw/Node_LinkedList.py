class Node(object):
	def __init__(self,data):
		self.data=data
		self.next=None

	def get_data(self):
		return self.data

	def set_data(initdata):
		self.data=initdata

	def get_next(self):
		return self.next

	def set_next(self,new_next):
		self.next=new_next


class LinkedList(object):
	def __init__(self):
		self.head=None

	def get_tail(self):
		node=self.head
		while node.get_next.get_next!=None:
			node=node.get_next
		return node.get_next

	def insert(self,data):
		NewNode=Node(data)
		if not self.head:
			self.head=NewNode
		else:
			tail=self.get_tail
			tail.set_next=NewNode

	def search(self,val):
		node=self.head:
		while node.get_next.get_next!=None:
			if node.get_next.get_data=val:
				return node.get_next
				break
			else:
				node=node.get_next
	def delete(self,val):
		def del_search(self,val):
			node=self.head:
			while node.get_next.get_next!=None:
				if node.get_next.get_next.get_data==val:
					return node.get_next
				else:
					node=node.get_next
		node=del_search(val)
		temp=node.get_next
		node.get_next=temp.get_next


	def print_backwards(self):
		t=()
		while node.get_next!=None:
			t=t+node.get_data
			node=node.get_next
			t=t[::-1]
			for x in t:
				print(t)



			










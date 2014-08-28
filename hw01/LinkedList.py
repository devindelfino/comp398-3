import csv

class Node:
	# initialize the node (each member of the list will be a node)
	# nodes contain the book name, author, and a next pointing to the next
	# element of the list
    def __init__(self, book=None, author=None, next=None):
        self.book = book
        self.author  = author
        self.next = next

    # defines what will be printed when attempting to print a Node object
    def __str__(self):
        return str(self.book) + ", " + str(self.author)


class BookList:
	# initalize the (at first empty) list
	# list contains the head and tail, both of which are empty
	def __init__(self):
		self.head = None
		self.tail = None

	# allows you to add a new book to the list
	# must provide the new book title and the new author name
	def newBook(self, newBook, newAuthor):
		
		# if the list is empty, assigns new book to head of the list
		if self.head == None:
			self.head = Node(newBook, newAuthor)
			self.head.next = self.tail
		# if the list has a head but no tail, assigns new book to tail
		else: # if self.head != None
			if self.tail == None:
				self.tail = Node(newBook, newAuthor)
				self.head.next = self.tail
			# if the list is not empty, assigns new book to end of list 
			# and moves tail to new book
			else: # self.tail != None
				self.tail.next = Node(newBook, newAuthor)
				self.tail = self.tail.next

	def searchList(self, searchTerm):
		
		hit = "This book/author is not on this list."

		if (self.head.book or self.head.author) == searchTerm: 
			hit = "This book/author was found, here is the full listing: \n" + str(self.head)
		else:
			mover = self.head.next
			while hit == "This book/author is not on this list." and mover != None:
				if (mover.book or mover.author) == searchTerm:
					hit = "This book/author was found, here is the full listing: \n" + str(mover)
				else:
					mover = mover.next

		print hit


	def printAll(self):

		if self.head != None:
			# creates an empty string that will hold the entire list and adds 
			# first (head) item
			allBooks = ""
			allBooks = allBooks + str(self.head)

			# using mover to keep track of place, iterates through the list
			# and adds each book/author to allBooks with appropriate newlines
			mover = self.head.next

			while mover != self.tail:
				allBooks = allBooks + "\n" + str(mover)
				mover = mover.next

			# adds the last item of list
			allBooks = allBooks + "\n" + str(self.tail)

			print allBooks

		else:
			#if the list is empty (self.head is None)
			print "This list is empty."


			
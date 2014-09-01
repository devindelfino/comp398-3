"""Contains classes to be implemented by driver program for linked list.

"""

class Node(object):
    """Create Nodes to be used by LinkedList.
    """

    # initialize the node (each member of the list will be a node)
    # nodes contain the book name, author, and a next pointing to the next
    # element of the list
    def __init__(self, book=None, author=None, next=None):
        """Initializes Node class object.

        Args:
            book (str): Human readable string that is the book title.
            author (str): Human readable string that is the book author.

        Attributes:
            book (str): Human readable string that is the book title.
            author (str): Human readable string that is the book author.
            next (Node): Node class member that comes after the current
              Node in the linked list.

        Returns:
            none
        """
        self.book = book
        self.author = author
        self.next = next

    # defines what will be printed when attempting to print a Node object
    def __str__(self):
        """Overrides str() operator for Node class.

        Returns:
            Human readable string of the book title followed by the book
            author, separated with a comma.
        """
        return str(self.book) + ", " + str(self.author)


class BookList(object):
    """Create a Linked List to be filled with Nodes from the Node class.
    """
    # initalize the (at first empty) list
    # list contains the head and tail, both of which are empty
    def __init__(self):
        """Attributes:
            head (Node): Node class object that contains the book title and
              author of the first list entry and links with next to the second
              list entry.
            tail (Node): Node class object that contains the book title and
              author of the last list entry.
        """
        self.head = None
        self.tail = None

    # allows you to add a new book to the list
    # must provide the new book title and the new author name
    def new_book(self, title, author):
        """Creates new Node containing book info and links it to list.

        Args:
            newBook (str): Human readable string that is the book title.
            newAuthor (str): Human readable string that is the book author.

        Returns:
            none
        """
        # if the list is empty, assigns new book to head of the list
        if self.head == None:
            self.head = Node(title, author)
            self.head.next = self.tail
        # if the list has a head but no tail, assigns new book to tail
        else: # if self.head != None
            if self.tail == None:
                self.tail = Node(title, author)
                self.head.next = self.tail
            # if the list is not empty, assigns new book to end of list
            # and moves tail to new book
            else: # self.tail != None
                self.tail.next = Node(title, author)
                self.tail = self.tail.next

    def search_list(self, term):
        """Locates search term within linked list.

        Args:
            searchTerm (str): Human readable string that is the name of the
              book or author the user is searching the list for.

        Returns:
            none
        """
        hit = "This entry is not on this list."

        if (self.head.book or self.head.author) == term:
            hit = "This entry was found, here is the full listing: \n"
            hit = hit + str(self.head)
        else:
            mover = self.head.next
            while hit == "This entry is not on this list." and mover != None:
                if (mover.book or mover.author) == term:
                    hit = "This entry was found, here is the full listing: \n"
                    hit = hit + str(mover)
                else:
                    mover = mover.next

        print hit

    def printall(self):
        """Prints all list entries to output. 

        Returns:
            none
        """
        if self.head != None:
            # creates an empty string that will hold the entire list and adds
            # first (head) item
            all_entries = ""
            all_entries = all_entries + str(self.head)

            # using mover to keep track of place, iterates through the list
            # and adds each book/author to allBooks with appropriate newlines
            mover = self.head.next

            while mover != self.tail:
                all_entries = all_entries + "\n" + str(mover)
                mover = mover.next

            # adds the last item of list
            all_entries = all_entries + "\n" + str(self.tail)

            print all_entries

        else:
            #if the list is empty (self.head is None)
            print "This list is empty."

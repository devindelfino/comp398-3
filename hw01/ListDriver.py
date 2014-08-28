import csv
import LinkedList

def main():

	# (1: create an empty list)
	BannedBooks = LinkedList.BookList()

	# (2: add a single node to the list)
	BannedBooks.newBook("Gee", "Whiz")

	# (3: populate the list from a flat file database)

	# open my database and add each item to BannedBooks
	# 'rU' instead of 'r' prevents a csv.Error: 
	# (new-line character seen in unquoted field)
	with open('bannedbooks.csv', 'rU') as csvfile:			
		boop = csv.reader(csvfile, delimiter=' ')
		for row in boop:
			newRow = row[0].split(", by ")
			BannedBooks.newBook(newRow[0], newRow[1])

	# (4: search the list for a value)

	# if found, should return full node information
	# otherwise, should return, "This book/author is not on this list":
	BannedBooks.searchList("Harry Potter (series)") 		# hit
	print ""
	BannedBooks.searchList("Pumpkin")						# miss


	# (5: display a plaintext form of the list)

	# should print to console/output title and entire list
	print "\n =========== \n"
	print "Most Challenged/Banned Books of the Aughts: \n"

	# print all the items in BannedBooks
	BannedBooks.printAll()

	# if asked to print an empty list, "This list is empty" should appear:
	print "\n =========== \n"
	EmptyListTest = LinkedList.BookList()
	EmptyListTest.printAll()


if __name__ == "__main__":
	main()
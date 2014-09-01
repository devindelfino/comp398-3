"""The driver program.

    This program implements the functionality of LinkedList2.py
    according to the specifications of comp398 hw01 assignment
    as outlined in the commented code.

    As stated for hw02, this code (and the code of LinkedList2)
    is formated according to a specific style guide:
    https://google-styleguide.googlecode.com/svn/trunk/pyguide.html?

    This code was also checked using pylint and all relevant issues
    corrected:
    http://www.pylint.org/
"""

import csv
import LinkedList

def main():
    """Contains the test suite to demonstrate functioning code.
    """
    # (1: create an empty list)
    banned_books = LinkedList.BookList()

    # (2: add a single node to the list)
    banned_books.new_book("Gee", "Whiz")

    # (3: populate the list from a flat file database)

    # open my database and add each item to banned_books
    # 'rU' instead of 'r' prevents a csv.Error:
    # (new-line character seen in unquoted field)
    with open('bannedbooks.csv', 'rU') as csvfile:
        boop = csv.reader(csvfile, delimiter=' ')
        for row in boop:
            row = row[0].split(", by ")
            banned_books.new_book(row[0], row[1])

    # (4: search the list for a value)

    # if found, should return full node information
    # otherwise, should return, "This entry is not on this list":
    banned_books.search_list("Gee")            # hit
    print ""
    banned_books.search_list("Pumpkin")        # miss


    # (5: display a plaintext form of the list)

    # should print to console/output title and entire list
    print "\n =========== \n"
    print "Most Challenged/Banned Books of the Aughts: \n"

    # print all the items in BannedBooks
    banned_books.printall()

    # if asked to print an empty list, "This list is empty" should appear:
    print "\n =========== \n"
    empty_list = LinkedList.BookList()
    empty_list.printall()

    # ========================================
    print "\n =========== \n"

    # (1: create an empty list)
    states = LinkedList.BookList()

    # (2: add a single node to the list)
    states.new_book("Virgin Islands", "VI")

    # (3: populate the list from a flat file database)

    # open my database and add each item to states
    # 'rU' instead of 'r' prevents a csv.Error:
    # (new-line character seen in unquoted field)
    with open('statesabb.csv', 'rU') as csvfile:
        boop = csv.reader(csvfile, delimiter='\n')
        for row in boop:
            row = row[0].split(",")
            states.new_book(row[0], row[1])

    # (4: search the list for a value)

    # if found, should return full node information
    # otherwise, should return, "This entry is not on this list":
    states.search_list("New York")           # hit
    print ""
    states.search_list("Puerto Rico")        # miss


    # (5: display a plaintext form of the list)

    # should print to console/output title and entire list
    print "\n =========== \n"
    print "States and their abbreviations: \n"

    # print all the items in StatesAbb
    states.printall()


if __name__ == "__main__":
    main()

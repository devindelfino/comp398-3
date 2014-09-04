Review.md
=========

Style Guide Evaluation
----------------------

This code was written in Python, and reviewed according to the [PEP 8](http://legacy.python.org/dev/peps/pep-0008/) style guide:

Structure: 
	
	Files are clear and direct. The README.md should maybe include a list of the files and state which does what -- however obviously they're well named files so it's pretty self explanatory. 

Code Layout:

	Indentation: Lines 2, 3, 8 and 127 of linkedlist.py exceed the 79 character maximum, otherwise good. 

	Tabs/Spacing: Tabs are used, spaces would be preferable. (4 spaces per tab.)

	Newlines: Inconsistent with use of one or two newlines. Only one newline should be used to separate method functions. 

	Imports: Good

	Whitespace in Expressions/Statements: Good

	Comments: Inline comments should be at least two spaces away from the end of the statement. Docstrings should start on the first line of the class/function/method/etc., not preceeding it. 

	Variable Naming: Source code names are good, as are class names. However function/method names should be lowercase, not camelcase, with the use of underscore as necessary (to improve readability).

	Class Definitions: Classes are defined the old way, should inherent 'object' as opposed to being empty. I.e., "LinkedList(object)" as opposed to "LinkedList()."

-Note: running the code through Pylint, linkedlist.py got a score of -6.81/10, and driver.py got a score of 0/10. I think most of the issue was though that tabs were used instead of spacing. 

Code Evaluation
---------------

I ran the code myself and got the desire output from driver.py. It runs fully functionally. However, in the assignment the driver program was meant to demonstrate all the desired elements required for hw01, and while the code for searching the list is present, it is not implemented in the driver.py. 

Within the LinkedList class, I think it might make more sense to put the methods of the LinkedList class before the Node class and its methods -- however I can see why you'd put the Node class first, and I think that's probably a personal preference thing. 

All the variable names are very abstract and general; this same code would work/make sense for pretty much any list. 

As far as possible runtime errors, the only I can think of might be with loading in the file. On the user end (so not really a runtime error?), if there is something wrong with their file/it doesn't load correctly, the code doesn't currently tell them this. So they might not be aware why the code isn't working completely because it isn't explicit that the populate step has failed. 
README.md
=========

This program allows you to convert a basic markdown file into its corresponding html code. It will convert headers, paragraphs, emphasis, ordered and unordered lists, inline links and images, and code. 

Status:
------

Everything appears to work as intended. I generated my desired output when I called test.md and README.md in the Driver.py. 

Known Issues:
------------------------

+   Multiple links or images in one line will return an error. 
+   Paragraphs within lists does not convert as such. 

Contents:
---------

+   readme.md: this file
+   Converter.py: handles conversion functionality
+   Driver.py: demonstrates the conversion in effect
+   test.md: source file to be used in Driver.py
+   testoutput.html: output from converting test.md
+   readmeoutput.html: output from converting this readme.md
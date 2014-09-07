README.md
=========

This program allows you to convert a basic markdown file into its corresponding html code. It will convert headers, paragraphs, emphasis, ordered and unordered lists, inline links and images, and code. 

Status:
------

Everything appears to work as intended. I generated my desired output when I called test.md and README.md in the Driver.py. 

Possible Runtime Errors:
------------------------

To avoid the converter seeing two dashes -- in a sentence and interpreting it as needing to convert the previous line to a h2 header, I put in a condition that to interpret it as needing an h2 header there should be at least three dashes. However this means if a user had a two or one character h2 header it wouldn't be converted. 

Some conversions are not currently supported for multiple conversions within the same line. Multiple links or images in one line will return an error. 

Contents:
---------

+   readme.md: this file
+   Converter.py: handles conversion functionality
+   Driver.py: demonstrates the conversion in effect
+   test.md: source file to be used in Driver.py
+   testoutput.html: output from converting test.md
+   readmeoutput.html: output from converting this readme.md
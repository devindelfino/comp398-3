README.md
=========

This is a data visualization of the Wheaton course schedule. The visualization attempts to adhere to WCAG 2.0 guidelines for accessibility, by offering a very simple visualisation with a high contranst foreground and background, and text that can be largely resized. There is also no non-text information that needs to be presented in a different way, as elements are always either equivalent to or nested within the previous element. In this way, when read aloud, each element follows the previous one, and is titled to be distinguishable. Also, all text is embedded as text elements of svgs, so no text is presented as an unreadable image. Moving through the file is completely doable with the keyboard. 

Issues - I really got nowhere with a data scraper, which is why my visualization doesn't cover all the data (I hand copied enough to make the layout clear). I started on a python script that would take in a list of all majors/all courses/etc. and output the corresponding html, but it's unfinished and without the scraper pretty useless. 

INCLUDED FILES:

-   README.md: this file
-   schedule.html: the data visualization
-   style.css: the css styling for schedule.html
-   codemaker.py: the starts of the scraper/conversion of data to html process
import re

class Converter(object):

    def __init__(self, filename):

        self.original = filename
        self.string = ""
        self.converted = ""


    def __str__(self):
        """Overrides str() operator for Converter class.

        Returns:
        Human readable string of the markdown file converted to html
        """

        self.file_to_string()
        self.convert()

        # return self.converted
        return self.converted


    def file_to_string(self):
        """Converts user inputed file to a string. 

        Returns:
        Human readable string of the markdown file
        """

        f = open(self.original, 'r')
        filestring = f.read()
        f.close() 

        self.string = filestring


    def convert(self):

        split_file = self.string.split('\n')
        
        i = 0

        for i in xrange(len(split_file)):

            #Inserts headers
            h1_matches_under = re.findall('(=+)[^()]', split_file[i])
            h2_matches_under = re.findall('(-+){3,}[^()]', split_file[i])
            h1_matches = re.findall(r'# ', split_file[i])
            h2_matches = re.findall(r'## ', split_file[i])
            h3_matches = re.findall(r'### ', split_file[i])

            if h1_matches_under: 
                split_file[i-1] = re.sub("<p>", "<h1>", split_file[i-1])
                split_file[i-1] = re.sub("</p>", "</h1>", split_file[i-1])
                split_file[i] = "Delete this line."
            elif h2_matches_under:
                split_file[i-1] = re.sub("<p>", "<h2>", split_file[i-1])
                split_file[i-1] = re.sub("</p>", "</h2>", split_file[i-1])
                split_file[i] = "Delete this line."
            
            if h3_matches:
                split_file[i] = "<h3>" + str(re.sub("### ", "", split_file[i])) + "</h3>"
            elif h2_matches:
                split_file[i] = str(re.sub("## ", "<h2>", split_file[i])) + "</h2>"
            elif h1_matches:
                split_file[i] = str(re.sub("# ", "<h1>", split_file[i])) + "</h1>"            
            

            #Inserts blockquotes
            blockquote_match = re.match('>', split_file[i])

            if blockquote_match:
                if re.search("<h[123]>", split_file[i]):
                    split_file[i] = "<blockquote>" + split_file[i][2:] + "</blockquote>"
                else:
                    split_file[i] = "<blockquote><p>" + split_file[i][2:] + "</p></blockquote>"


            #Inserts emphasis, strong emphasis, and code
            strong_emphasis_matches = re.findall('[\*_]{2,}[^\*_]+[\*_]{2,}', split_file[i])
            emphasis_matches = re.findall('[\*_][^\*_]+[\*_]', split_file[i])
            code_matches = re.findall('`.*?`', split_file[i])

            for hit in strong_emphasis_matches:
                split_file[i] = re.sub("[\*_]{2,}", "<strong>", split_file[i], 1)
                split_file[i] = re.sub("[\*_]{2,}", "</strong>", split_file[i], 1)
            for hit in emphasis_matches:
                split_file[i] = re.sub("[\*_]", "<em>", split_file[i], 1)
                split_file[i] = re.sub("[\*_]", "</em>", split_file[i], 1)
            for hit in code_matches:
                split_file[i] = re.sub("`", "<code>", split_file[i], 1)
                split_file[i] = re.sub("`", "</code>", split_file[i], 1)
            

            #Inserts lists
            unlist_matches = re.findall("[\*\+-]   ", split_file[i])
            orlist_matches = re.findall("\d+\.   ", split_file[i])

            if unlist_matches:
                if re.search("<ul>", split_file[i-1]) or re.search("<li>", split_file[i-1]):
                    split_file[i] = str(re.sub("[\*\+-]   ", "<li>", split_file[i])) + "</li>"
                else:
                    split_file[i] = str(re.sub("[\*\+-]   ", "<ul>\n<li>", split_file[i])) + "</li>"

                if i+1 is not len(split_file):
                    if re.match("[\*\+-]   ", split_file[i+1]):
                        pass
                    else:
                        split_file[i] = split_file[i] + "\n</ul>"
                else:
                    split_file[i] = split_file[i] + "\n</ul>"

            if orlist_matches:
                if re.search("<ol>", split_file[i-1]) or re.search("<li>", split_file[i-1]):
                    split_file[i] = str(re.sub("\d+\.   ", "<li>", split_file[i])) + "</li>"
                else:
                    split_file[i] = str(re.sub("\d+\.   ", "<ol>\n<li>", split_file[i])) + "</li>"

                if i+1 is not len(split_file):
                    if re.match("\d+\.   ", split_file[i+1]):
                        pass
                    else:
                        split_file[i] = split_file[i] + "\n</ol>"
                else:
                    split_file[i] = split_file[i] + "\n</ol>"


            #Inserts links
            link_name_matches = re.findall('[^!]\[.*?\]', split_file[i])
            image_name_matches = re.findall('!\[alt .*?\]', split_file[i])

            for hit in link_name_matches:
                link_url = re.findall('\(.*?\)', split_file[i])
                split_file[i] = re.sub('\(.*?\)', '', split_file[i])
                split_file[i] = re.sub('\[.*?\]', '<a href="' + 
                                str(link_url[0][1:-1]) +'">' + 
                                str(hit[2:-1]) + '</a>', 
                                split_file[i])

            for hit in image_name_matches:
                image_url = re.findall('\(.*?\)', split_file[i])
                split_file[i] = re.sub('\(.*?\)', '', split_file[i])
                split_file[i] = re.sub('!\[alt (.*?)\]', '<img src="' + 
                                str(image_url[0][1:-1]) + '" alt="' +
                                str(hit[6:-1]) + '"/>', 
                                split_file[i])

            
            #Inserts paragraph tags
            allmatches = not (h1_matches_under
                        or h2_matches_under 
                        or h1_matches 
                        or h2_matches 
                        or h3_matches 
                        or blockquote_match 
                        or unlist_matches 
                        or orlist_matches)

            if allmatches == True:
                split_file[i] = "<p>" + split_file[i] + "</p>"

            i += 1


        split_file = [x for x in split_file if x != 'Delete this line.']
        html_file = '\n'.join(split_file)
        self.converted = html_file














        
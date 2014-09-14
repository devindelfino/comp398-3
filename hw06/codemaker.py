
def main():

	class Course(object):

		def __init__(self):
			self.check = "done"

		def make_major(self, coursename, height):
			major_string = '<g transform="translate(0,' + height + ') id="all">\n <rect width="100%" height="50" fill="blue"></rect>' + '\n <text x="37" y="15" dy="1em" fill="white">' + coursename + '</text> \n </g>'
			return major_string

		def make_course(self, Y, name, 
						 location, professor, CRN, time, exam):
			course_string = '<g id="all"> <g transform="translate(50,' + str(Y) + ')"> <rect width="400" height="50" fill="purple"></rect> <text x="37" y="15" dy="1em" fill="white" id="text">' + name + '</text> </g>   <!-- Details --> <g transform="translate(450, ' + str(Y) + ')">  <rect width="100%" height="50" fill="#009900"></rect> <text x="5%" y="20" dy="1em" fill="white">' + location + '</text> <text x="30%" y="20" dy="1em" fill="white">' + professor + '</text> <text x="52%" y="20" dy="1em" fill="white">' + CRN + '</text> </g> <g transform="translate(450, ' + str(Y+50) + ')"> <rect width="100%" height="50" fill="#009900"></rect> <text x="5%" y="15" dy="1em" fill="white">' + time + '</text> <text x="30%" y="15" dy="1em" fill="white">' + exam + '</text> </g>  </g>'
			return course_string


	WebApp = Course()

	CS = WebApp.make_major("Computer Science", "0")

	Foundations = WebApp.make_course(50, "Foundations", "Sci Center", "Margnes", "1843", "MWF 3", "Dec 12")


	print WebApp.check

	print Foundations







if __name__ == "__main__":
    main()
courses = {
    "js": "Javascript 101",
    "python": ["Python 101", "Python 201"],
    "html": "HTML 101"

}

print (courses.get ("js", None))

if courses.get("css", "Default Value here.."):
    print("Well Enrolled in CSS ")

if courses.get ("css", None):
    pass
else:
    print("Not enrolled in CSS 101")
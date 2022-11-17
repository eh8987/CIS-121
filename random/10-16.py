class Documents:


    def __init__(self,authors,date):
        self.authors = authors
        self.date = date

    def getAuthors(self):
        return self.authors


    def addAuthor(self,new):
        if type(new) == str:
            self.authors.append(new)

    def getDate(self):
        return self.date

    def __str__(self):
        print (
            "=============Document Data==============" + "\n"
            f"Authors: {self.authors}" + "\n"
            f"Date: {self.date}" + "\n"

        )
        return ""

class Book(Documents):

    def __init__(self,authors,date,title):
        super().__init__(authors,date)
        self.title = title

    def getTitle(self):
        return self.title


    def __str__(self):
        print (
            "=============Book Data==============" + "\n"
            f"Authors: {self.authors}" + "\n"
            f"Date: {self.date}" + "\n"
            f"Title: {self.title}" + "\n"
        )

        return ""

class Email(Documents):

    def __init__(self,authors,date,subject,to):
        super().__init__(authors,date)
        self.subject = subject
        self.to = to

    def getSubject(self):
        return self.subject

    def getTo(self):
        return self.to

    def __str__(self):
        print (
            "=============Email Data==============" + "\n"
            f"Authors: {self.authors}" + "\n"
            f"Date: {self.date}" + "\n"
            f"Subject: {self.subject}" + "\n"
            f"To: {self.to}" + "\n"
        )
        return ""













#main.py becuase i dont want to make another file

narnia = Book("C.S Lewis","1999","Narnia")

print(narnia)

email = Email("Ethan","11/16/2022","Ethan is so cool","Everyone")

print(email)
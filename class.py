class book:
    isbn = "1283403"
    def __init__(self,name,year,pages,author):
        self.name = name
        self.year = year
        self.pages = pages
        self.author = author
        #self.isbn = "1283403"
        

richdad = book("Rich dad & Poor dad",1988,120,"James")
recipes = book("How to cook rice",2022,10,"Joy")

print(recipes.isbn)
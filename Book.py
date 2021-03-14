class Book:
    def __init__(self, name, author, time, species, chapter):
        self.studName = name
        self.studAuthor = author
        self.studTime = time
        self.studSpecies = species
        self.studChapter = chapter
    def showInfo(self):
        print(self.studName)
        print(self.studAuthor)
        print(self.studTime)
        print(self.studSpecies)
        print(self.studChapter)
x = Book("三國演義","羅貫中","元末明初","Historical fiction","120回")
x1 = Book("水滸傳","施耐庵","北宋宣和","Historical fiction","120回")
x2 = Book("西遊記","吳承恩","明朝中葉","Historical fiction","100回")
x.showInfo()
x1.showInfo()
x2.showInfo()
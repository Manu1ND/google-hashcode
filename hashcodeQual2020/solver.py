
class Library:
	def __init__(self, libraryID, nOfBooksInLibrary, signUpDays, booksShipPerDay, booksInLibrary, daysLeft):
		self.libraryID = libraryID
		self.nOfBooksInLibrary = nOfBooksInLibrary
		self.signUpDays = signUpDays
		self.booksShipPerDay = booksShipPerDay
		self.booksInLibrary = booksInLibrary
		self.para = min((daysLeft - signUpDays)*booksShipPerDay, len(booksInLibrary))

	def updateLib(self, booksShipped, daysLeft):
		for book in booksShipped and self.booksInLibrary:
			self.booksInLibrary.remove(book)
		self.nOfBooksInLibrary = len(self.booksInLibrary)
		self.para = min((daysLeft - self.signUpDays)*self.booksShipPerDay, len(self.booksInLibrary))
	
def sendBooks(library, daysLeft):
	libraryID = library.libraryID
	if library.nOfBooksInLibrary < library.booksShipPerDay * daysLeft:
		nOfBooksShipped = library.nOfBooksInLibrary
	else:
		nOfBooksShipped = library.booksShipPerDay * daysLeft
	
	booksShipped = []
	for i in range(nOfBooksShipped):
		booksShipped.append(library.booksInLibrary.pop())
	
	return libraryID, nOfBooksShipped, booksShipped

def solver(input):  # not be changed

	nOfDifferentBooks, nOfLibraries, nOfDays = map(
		int, input.readline().split())  # first line
	
	scoreOfBooks = list(map(int, input.readline().split())) # list
	libraries = []
	for libraryID in range(nOfLibraries):
		nOfBooksInLibrary, signUpDays, booksShipPerDay = map(int, input.readline().split())
		booksInLibrary = input.readline().split() # list bookID
		booksInLibrary.sort(key=lambda x: scoreOfBooks[int(x)], reverse=True)
		libraries.append(Library(libraryID, nOfBooksInLibrary, signUpDays, booksShipPerDay, booksInLibrary, nOfDays))
		
	libraries.sort(key=lambda x: x.para, reverse=True)
	
	libraryCount = 0
	result = []
	while len(libraries) > 0:
		currentDay=0
		if currentDay < nOfDays:
			libraryCount += 1
			currentDay += libraries[0].signUpDays
			libraryID, nOfBooksShipped, booksShipped = sendBooks(libraries[0],nOfDays-currentDay - 1)
			libraries.pop(0)
			if libraryCount % 100 == 0:
				for lib1 in libraries:
					lib1.updateLib(booksShipped, nOfDays-currentDay - 1)
				libraries.sort(key=lambda x: x.para, reverse=True)
			
			result.append(str("{} {}\n".format(libraryID, nOfBooksShipped)))
			result.append(' '.join(booksShipped) + '\n')
	
	result.insert(0, str(libraryCount) + '\n')			
				
	return result  # not be changed

class Street:
	def __init__(self, startIntersectionID, endIntersectionID, streetDuration):
		self.startIntersectionID = startIntersectionID
		self.endIntersectionID = endIntersectionID
		self.streetDuration = streetDuration
		self.nOfCarsPassing = 0

	def addCarNumber(self):
		self.nOfCarsPassing += 1


class Car:
	def __init__(self, nOfStreetsCarTravels, streetsCarTravels):
		self.nOfStreetsCarTravels = nOfStreetsCarTravels
		self.streetsCarTravels = streetsCarTravels  # list


class Intersection:
	def __init__(self):
		self.streetNames = []
		self.time = []

	def addInter(self, streetName, greenTime):
		self.streetNames.append(streetName)
		self.time.append(greenTime)


def solver(input):  # not be changed

	duration, nOfIntersections, nOfStreets, nOfCars, bonusPoint = map(
		int,
		input.readline().split())

	intersections = []
	for i in range(nOfIntersections):
		intersections.append(Intersection())

	streets = {}
	for i in range(nOfStreets):
		streetInfo = list(input.readline().split())
		startIntersectionID = int(streetInfo[0])
		endIntersectionID = int(streetInfo[1])
		streetName = streetInfo[2]
		streetDuration = int(streetInfo[3])

		streets[streetName] = Street(
			startIntersectionID, endIntersectionID, streetDuration)
		intersections[endIntersectionID].addInter(streetName, 1)

	cars = []
	for i in range(nOfCars):
		carInfo = list(input.readline().split())
		nOfStreetsCarTravels = int(carInfo[0])
		streetsCarTravels = carInfo[1:]  # list
		for street in streetsCarTravels:
			streets[street].addCarNumber()
		cars.append(Car(nOfStreetsCarTravels, streetsCarTravels))

	#streets = sorted(streets.items(), key=lambda x: x[1].nOfCarsPassing, reverse=True)		
	result = []
	result.append(str(len(intersections))+'\n')

	ID = 0
	for i in intersections:
		result.append(str(ID)+'\n')
		ID+= 1
		result.append(str(len(i.streetNames))+'\n')
		for x in range(len(i.streetNames)):
			result.append(str(i.streetNames[x])+' '+str(i.time[x])+'\n')

	return result  # not be changed

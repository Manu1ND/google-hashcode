class task:
    def __init__(self, taskID, scorePoint, assemblyPoints):
        self.taskID = taskID
        self.scorePoint = scorePoint
        self.assemblyPoints = assemblyPoints


def solver(input):  # not be changed
    width, height, nofarms, nofmountpoints, noftasks, nofsteps = map(
        int, input.readline().split())
    taskID = 0
    cells = []
    mountPoints = []
    tasks = []

    for i in range(nofmountpoints):
        x, y = input.readline().split()
        mountPoints.append([x, y])

    for i in range(noftasks):
        score, nOfAssemlyPoints = input.readline().split()
        assemblyPoints = input.readline().split()

        assemblyPointsCoords = []
        for x, y in zip(assemblyPoints[::2], assemblyPoints[1::2]):
            assemblyPointsCoords.append([x, y])

        tasks.append(task(taskID, score, assemblyPointsCoords))
        taskID += 1

    tasks.sort(key=lambda x: x.scorePoint, reverse=True)

	#horizontalPhotos.sort(key=lambda x: x.nOfTags, reverse=True)
	#verticalPhotos.sort(key=lambda x: x.nOfTags, reverse=True)

class Slide:
    def __init__(self, photoIDs, nOfTags, tags):
        self.photoIDs = photoIDs
        self.nOfTags = nOfTags
        self.tags = tags


class Photo:
    def __init__(self, photoID, nOfTags, tags):
        self.photoID = photoID
        self.nOfTags = nOfTags
        self.tags = tags


def interestFactor(slideATags, slideBTags):
    slideATags = set(slideATags)
    slideBTags = set(slideBTags)
    onlyA = slideATags - slideBTags
    onlyB = slideBTags - slideATags
    intersection = slideATags & slideBTags
    return min(len(onlyA), len(onlyB), len(intersection))


def bestSlideFromHorizontal(mainSlide, horizontalPhotos):
    maxInterestFactor = 0
    horizontalSlide = ''

    for i in range(0, min(4, len(horizontalPhotos))):
        tempinterestFactor = interestFactor(
            mainSlide.tags, horizontalPhotos[i].tags)
        if maxInterestFactor < tempinterestFactor:
            maxInterestFactor = tempinterestFactor
            photoIDs = horizontalPhotos[i].photoIDs
            nOfTags = horizontalPhotos[i].nOfTags
            tags = horizontalPhotos[i].tags
            horizontalPhoto = horizontalPhotos[i]

    if maxInterestFactor == 0:
        photoIDs = horizontalPhotos[0].photoIDs
        nOfTags = horizontalPhotos[0].nOfTags
        tags = horizontalPhotos[0].tags
        horizontalPhoto = horizontalPhotos[0]

    horizontalSlide = Slide(photoIDs, nOfTags, tags)
    return horizontalPhoto, horizontalSlide, maxInterestFactor


def bestSlideFromVertical(mainSlide, verticalPhotos):
    maxInterestFactor = 0
    verticalSlide = ''
    mainVerticalPhoto = verticalPhotos.pop(0)
    photoIDs = set([mainVerticalPhoto.photoID])
    tags = set()
    maxPhotoIDs = set()
    x = min(2, len(verticalPhotos))

    for i in range(0, x):
        verticalSlide1Tags = set(mainVerticalPhoto.tags) | set(
            verticalPhotos[i].tags)
        tempinterestFactor1 = interestFactor(
            mainSlide.tags, verticalSlide1Tags)

        verticalSlide2Tags = set(mainVerticalPhoto.tags) | set(
            verticalPhotos[-(i+1)].tags)
        tempinterestFactor2 = interestFactor(
            mainSlide.tags, verticalSlide2Tags)

        if(tempinterestFactor1 > tempinterestFactor2):
            tempinterestFactor = tempinterestFactor1
            tempTags = verticalSlide1Tags
            tempPhotoIDs = verticalPhotos[i].photoID
            tempVerticalPhoto = verticalPhotos[i]
        else:
            tempinterestFactor = tempinterestFactor2
            tempTags = verticalSlide2Tags
            tempPhotoIDs = verticalPhotos[-(i+1)].photoID
            tempVerticalPhoto = verticalPhotos[-(i+1)]

        if maxInterestFactor < tempinterestFactor:
            maxInterestFactor = tempinterestFactor
            maxPhotoIDs = set([tempPhotoIDs])
            verticalPhoto = tempVerticalPhoto
            tags = tempTags
            nOfTags = len(tags)

    photoIDs = list(photoIDs | maxPhotoIDs)

    if maxInterestFactor == 0:
        photoIDs.append(verticalPhotos[0].photoID)
        tags = set(mainVerticalPhoto.tags) | set(verticalPhotos[0].tags)
        nOfTags = len(tags)
        verticalPhoto = verticalPhotos[0]

    verticalSlide = Slide(photoIDs, nOfTags, tags)
    return verticalPhoto, verticalSlide, maxInterestFactor


def solver(input):  # not be changed
    slides = []
    horizontalPhotos = []
    verticalPhotos = []

    nOfPhotos = int(input.readline())  # first line

    photoID = 0
    while line := input.readline().split():
        orientation = line[0]
        nOfTags = line[1]
        tags = line[2:]
        if(orientation == 'V'):
            verticalPhotos.append(Photo(photoID, nOfTags, tags))
            photoID += 1
        else:
            photoIDs = [photoID]
            horizontalPhotos.append(Slide(photoIDs, nOfTags, tags))
            photoID += 1

    horizontalPhotos.sort(key=lambda x: x.nOfTags, reverse=True)
    verticalPhotos.sort(key=lambda x: x.nOfTags, reverse=True)

    # slide 0
    if (len(horizontalPhotos) > 0):
        slides.append(horizontalPhotos[0])
        horizontalPhotos.pop(0)
    else:
        vSlide = ''
        photoIDs = [verticalPhotos[0].photoID]
        photoIDs.append(verticalPhotos[1].photoID)
        tags = set(verticalPhotos[0].tags) | set(verticalPhotos[1].tags)
        nOfTags = len(tags)
        vSlide = Slide(photoIDs, nOfTags, tags)
        slides.append(vSlide)
        verticalPhotos.pop(0)
        verticalPhotos.pop(0)

    while(len(horizontalPhotos) != 0 and len(verticalPhotos) > 1):
        mainSlide = slides[-1]
        horizontalPhoto, horizontalSlide, horizontalInterestFactor = bestSlideFromHorizontal(
            mainSlide, horizontalPhotos)
        verticalPhoto, verticalSlide, verticalInterestFactor = bestSlideFromVertical(
            mainSlide, verticalPhotos)

        if(verticalInterestFactor > horizontalInterestFactor):
            slides.append(verticalSlide)
            verticalPhotos.remove(verticalPhoto)
        else:
            slides.append(horizontalSlide)
            horizontalPhotos.remove(horizontalPhoto)

    while(len(horizontalPhotos) != 0):
        mainSlide = slides[-1]
        horizontalPhoto, horizontalSlide, horizontalInterestFactor = bestSlideFromHorizontal(
            mainSlide, horizontalPhotos)
        slides.append(horizontalSlide)
        horizontalPhotos.remove(horizontalPhoto)

    while(len(verticalPhotos) > 1):
        mainSlide = slides[-1]
        verticalPhoto, verticalSlide, verticalInterestFactor = bestSlideFromVertical(
            mainSlide, verticalPhotos)
        slides.append(verticalSlide)
        verticalPhotos.remove(verticalPhoto)

    ''' for i in horizontalPhotos:
		print("Hor")
		print(i.photoIDs)
		print(i.nOfTags)
		print(i.tags)

		
	for i in verticalPhotos:
		print("Ver")
		print(i.photoID)
		print(i.nOfTags)
		print(i.tags)   '''

    result = []
    result.append(str(len(slides)) + "\n")
    for slide in slides:
        abc = (' ').join(map(str, slide.photoIDs)) + "\n"
        result.append(abc)

    return result  # not be changed

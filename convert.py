from os import X_OK
import numpy

biomeLines = open("biome.pgm").readlines()
terrainLines = open("terrain.pgm").readlines()

# print(pgmLines)

encoding = ""
count = 0
width = 0
height = 0
maxlevel = 0

row = 0
rowCount = 0

biomeArray = []
terrainArray = []

for line in biomeLines:
    count += 1
    if(count == 1):
        encoding = line.strip()
        continue
    if(count == 2):
        wh = line.strip().split(" ")
        width = int(wh[0])
        height = int(wh[1])
        continue
    if(count == 3):
        maxlevel = int(line.strip())
        # create empty array
        biomeArray = numpy.tile(6.9, (width, height))
        continue

    if(rowCount == width):
        row += 1
        rowCount = 0

    biomeArray[row][rowCount] = int(line.strip()) / maxlevel
    rowCount += 1

count = 0
row = 0
rowCount = 0

for line in terrainLines:
    count += 1
    if(count == 1):
        encoding = line.strip()
        continue
    if(count == 2):
        wh = line.strip().split(" ")
        width = int(wh[0])
        height = int(wh[1])
        continue
    if(count == 3):
        maxlevel = int(line.strip())
        # create empty array
        terrainArray = numpy.tile(6.9, (width, height))
        continue

    if(rowCount == width):
        row += 1
        rowCount = 0

    terrainArray[row][rowCount] = int(line.strip()) / maxlevel
    rowCount += 1


#[",".join(item) for item in noiseArray.astype(str)]
biomeCharacterArray = numpy.tile("|", (width, height))
terrainCharacterArray = numpy.tile("|", (width, height))

# convert biome noise map to characters
ocean = 0.50
beach = 0.53
swamp = 0.60  # inside forest tiles
forest = 0.68
plains = 0.80
taiga = 0.85
hills = 0.90
snowy = 0.92
mountains = 0.95

for x in range(0, width):
    for y in range(0, height):
        if(biomeArray[x][y] < ocean):
            # ocean tile
            biomeCharacterArray[x, y] = str(".")
        elif(biomeArray[x][y] < beach):
            # beach tile, use secondary biome noise to disperse
            noiseValueThere = terrainArray[x, y]
            if(terrainArray[x][y] < 0.75):
                biomeCharacterArray[x, y] = str("~")
            else:
                biomeCharacterArray[x, y] = str("!")
        elif(biomeArray[x][y] <= forest):
            if(terrainArray[x][y] < 0.175):
                # swamp tile
                biomeCharacterArray[x, y] = str("=")
            else:
                # forest tile
                biomeCharacterArray[x, y] = str("!")
        elif(biomeArray[x][y] <= plains):
            # plains tile
            biomeCharacterArray[x, y] = str("*")
        elif(biomeArray[x][y] <= taiga):
            # taiga tile
            biomeCharacterArray[x, y] = str("#")
        elif(biomeArray[x][y] <= hills):
            # hills tile
            biomeCharacterArray[x, y] = str("$")
        elif(biomeArray[x][y] <= snowy):
            # snowy plains tile
            biomeCharacterArray[x, y] = str("%")
        elif(biomeArray[x][y] <= mountains):
            # mountains tile
            biomeCharacterArray[x, y] = str("&")
        else:
            # snowy mountains tile
            biomeCharacterArray[x, y] = str("@")


numpy.savetxt("biome.txt", biomeCharacterArray,
              fmt='%s', delimiter=' ', newline='\n')

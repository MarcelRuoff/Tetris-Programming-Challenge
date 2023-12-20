import sys

# Spefifying the different shapes available

shapes = {
    "Q" : [[0,0], [0,1], [1,0], [1,1]], 
    "Z" : [[1,0], [1,1], [0,1], [0,2]], 
    "S" : [[0,0], [0,1], [1,1], [1,2]], 
    "T" : [[1,0], [1,1], [0,1], [1,2]], 
    "I" : [[0,0], [0,1], [0,2], [0,3]], 
    "L" : [[0,0], [1,0], [0,1], [2,0]], 
    "J" : [[0,0], [0,1], [1,1], [2,1]]
}


def processLine(actionSequence: list[str]):
    playfield = [[0] * 10] # Create the initial line of the playfield
    
    for action in actionSequence:

        addShapeToPlayfield(action, playfield)

        prunePlayfield(playfield)
    prunePlayfield(playfield)

    return len(playfield)


    
def addShapeToPlayfield(action, playfield):

    playfieldHeight = len(playfield)
    y = 0

    for i in range(playfieldHeight):

        for shapeElement in shapes[action[0]]:
            if i + shapeElement[0] > playfieldHeight - 1:
                continue
            elif playfield[i + shapeElement[0]][int(action[1]) + shapeElement[1]]:
                y = i + 1
                break

    for shapeElement in shapes[action[0]]:
        if y + shapeElement[0] > len(playfield) - 1:
            playfield.append([0] * 10)
        
        playfield[y + shapeElement[0]][int(action[1]) + shapeElement[1]] = 1



def prunePlayfield(playfield):

    for i in reversed(range(len(playfield))):
        if all(playfield[i]) or not any(playfield[i]):
            playfield.pop(i)



if __name__ == "__main__":
    
    # Specifying the file path
    file_path = sys.argv[1]
    outFile = sys.argv[2]

    # Open the file in read mode and run the Tetris Engine
    resultingHeight = []
    with open(file_path, 'r') as file:
        # Read and process each line in the file
        for line in file:

            #Process the action sequence and return the resulting height of the stack
            resultingHeight.append(processLine(actionSequence = line.split(",")))

    with open(outFile,'w') as o:
        for line in resultingHeight:
            o.write(str(line) + "\n")

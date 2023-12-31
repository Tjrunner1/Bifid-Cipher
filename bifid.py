

alphaList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
polybiusSquare = []

def main():
    print("Please enter the square's key: ")
    key = input()
    makeSquare(key)
    print("Enter encode or decode for your message")
    cmd = input()
    print("Enter period")
    period = input()
    try:
        period = int(period)
    except:
        period = 1
    if (cmd == "encode"):
        print("Enter message to be encoded")
        message = input()
        
        encodedMsg = encode(message, period)
        print(encodedMsg)
        print("Finished encoding")
    elif (cmd == "decode"):
        print("Enter message to be decoded")
        message = input()
        
        decodedMsg = decode(message, period)
        print(decodedMsg)
        print("Finished decoding")
    else:
        print("Command didn't work, terminating program")

def makeSquare(key):
    key = key.upper()
    rowOfFive = []
    for c in key:
        if c=="J":
            c="I"

        if c in alphaList:
            alphaList.remove(c)
            rowOfFive.append(c)
        else:
            pass

        if len(rowOfFive) == 5:
            polybiusSquare.append(rowOfFive)
            rowOfFive = []

    for c in alphaList:
        rowOfFive.append(c)

        if len(rowOfFive) == 5:
            polybiusSquare.append(rowOfFive)
            rowOfFive = []
            
    return
    
        

def encode(message, period):
    # Convert to coordiantes
    coords = convert_to_coords(message)
    
    # Shuffle based on period
    encodedNumbers = period_shuffle(coords, period)
    
    # Turn back into letters
    encodedMessage = coords_to_letters(encodedNumbers, period)
    
    return encodedMessage

def decode(message, period):
    # Convert to coordinates
    coords = convert_to_coords(message)
    
    # Unshuffle the coordinates
    unshuffledCoords = period_unshuffle(coords, period)
    
    # Turn back to letters 
    encodedMessage = coords_to_letters(unshuffledCoords, period)
    
    return encodedMessage
    
             
def coords_to_letters(encodedNumbers, period):
    encodedMessage = ""
    
    for i in range(len(encodedNumbers)//2):
        row = encodedNumbers.pop(0)
        col = encodedNumbers.pop(0)
        encodedMessage += polybiusSquare[row][col]

    return encodedMessage
        
def convert_to_coords(message):
    encodedNumbers = []
    
    for c in message:
        c = c.capitalize()
        for row in range(5):
            try:
                if c == "J":
                    c = "I"
                col = polybiusSquare[row].index(c)
                encodedNumbers.append(row)
                encodedNumbers.append(col)
            except:
                pass
            
    return encodedNumbers

def period_unshuffle(coords, period):
    encodedMessage = []
    
    while len(coords) != 0:
        cutList = []
        for i in range(period):
            try:
                cutList.append(coords.pop(0))
                cutList.append(coords.pop(0))
            except:
                pass
        encodedMessage += uncombine_numbers(cutList)
        
    return encodedMessage

def uncombine_numbers(encodedNumbers):
    smushedNumbers = []
    for i in range(len(encodedNumbers)//2):
        smushedNumbers.append(encodedNumbers[i])
        smushedNumbers.append(encodedNumbers[len(encodedNumbers)//2 + i])
        
    return smushedNumbers
 
def period_shuffle(coords, period):
    encodedMessage = []
    
    while len(coords) != 0:
        cutList = []
        for i in range(period):
            try:
                cutList.append(coords.pop(0))
                cutList.append(coords.pop(0))
            except:
                pass
        encodedMessage += combine_numbers(cutList)
        
    return encodedMessage
    
def combine_numbers(encodedNumbers):
    smushedNumbers = []
    for i in range(0, len(encodedNumbers), 2):
        smushedNumbers.append(encodedNumbers[i])
    for i in range(1, len(encodedNumbers), 2):
        smushedNumbers.append(encodedNumbers[i])
    return smushedNumbers
        
if __name__=="__main__": 
    main()
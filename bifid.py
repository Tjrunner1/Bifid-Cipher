

polybiusSquare = [["P", "O", "L", "Y", "B"],
                  ["I", "U", "S", "C", "H"],
                  ["E", "R", "A", "D", "F"],
                  ["G", "K", "M", "N", "Q"],
                  ["T", "V", "W", "X", "Z"]]


def main():
    print("Enter encode or decode for your message")
    cmd = input()
    if (cmd == "encode"):
        print("Enter message to be encoded")
        message = input()
        print("Enter period")
        period = input()
        try:
            period = int(period)
        except:
            period = 1
        
        encodedMsg = encode(message, period)
        print(encodedMsg)
        print("Finished encoding")
    elif (cmd == "decode"):
        print("Enter message to be decoded")
        message = input()
        
        decode(message)
        print("Finished decoding")
    else:
        print("Command didn't work, terminating program")

def encode(message, period):
    # Convert to coordiantes
    coords = convert_to_coords(message)
    # print(coords)
    
    # Shuffle based on period
    encodedNumbers = period_shuffle(coords, period)
    # print(encodedNumbers)
    
    # Turn back into letters
    encodedMessage = coords_to_letters(encodedNumbers, period)
    # print(encodedMessage)
    
    return encodedMessage

def decode(message):
    # Calculate the period
    period = len(message.split(" ", 1)[0])
    
    # Convert to coordinates
    coords = convert_to_coords(message)
    print(coords)
    
    # Unshuffle the coordinates
    unshuffledCoords = period_unshuffle(coords, period)
    print(unshuffledCoords)
    
             
def coords_to_letters(encodedNumbers, period):
    encodedMessage = ""
    
    for i in range(len(encodedNumbers)//2):
        row = encodedNumbers.pop(0)
        col = encodedNumbers.pop(0)
        if i % period == 0 and i != 0:
            encodedMessage += " "
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
    pass
 
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
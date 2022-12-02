import sys

preCalculatedOutput = {
    "AX":3, "AY":4, "AZ":8, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":2, "CY":6, "CZ":7 
}

score = 0

for line in sys.stdin:
    first, second = line.split()

    
    score += preCalculatedOutput[first+second]


    
    
print(score)
        
    


    
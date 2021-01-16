def getElevationCoordinates(inLen,cardboards):
    '''getElevationCoordinates returns a list of tuples where each tuple has X,H which denotes change of height H at a particular x axis co-odrinate X'''
    cardboards.sort() #sort the cardboard list on basis of x1, followed by x2, followed by h

    cardboardsPP=[cardboards[0]] #stores the result of preprocessing
    prev=0 #prev is maintained to reduce the additional time consumed in accessing the previous element with negative index

    #pre process the input
    for i in range(1,inLen):
        prevX1,prevX2,prevH=cardboardsPP[prev]
        currX1,currX2,currH=cardboards[i]

        #if the new cardboard doesn't coincide with exisiting
        if currX1>prevX2:
            cardboardsPP.append((prevX2,currX1,0))
            cardboardsPP.append(cardboards[i])
            prev+=2

        #New cardboard is subsumed partially or totally into one of existing
        else:
            #Partially subsumed
            if currX2>prevX2:
                #if new cardboard is taller than existing
                if currH>prevH:
                    cardboardsPP[prev]=(prevX1,cardboards[i][0],prevH)
                    cardboardsPP.append(cardboards[i])
                    prev+=1
                #new cardboard is shorter than existing
                else:
                    cardboardsPP.append((prevX2,currX2,currH))
                    prev+=1

            #Completely subsumed
            else:
                #new cardboard is taller than existing
                if currH>prevH:
                    #previous and current cardboard coincide
                    if currX1==prevX1 and currX2==prevX2:
                        cardboardsPP[prev]=cardboards[i]
                    #previous and current cardboards are ending at same point
                    elif currX2==prevX2:
                        cardboardsPP[prev]=(prevX1,currX1,prevH)
                        cardboardsPP.append((currX1,currX2,currH))
                        prev+=1
                    #previous and current cardboards are starting at same point
                    elif currX1==prevX1:
                        cardboardsPP[prev]=cardboards[i]
                        cardboardsPP.append((currX2,prevX2,prevH))
                        prev+=1
                    #current one is in between the previous one
                    else:
                        cardboardsPP[prev]=(prevX1,currX1,prevH)
                        cardboardsPP.append((currX1,currX2,currH))
                        cardboardsPP.append((currX2,prevX2,prevH))
                        prev+=2

    #build result on basis of the preprocessed array
    res=[(x1,h) for x1,_,h in cardboardsPP]
    res.append((cardboardsPP[prev][1],0)) #add to denote the end
    return res

if __name__ == '__main__':
    n=int(input()) #number of cardboards
    cardboards=[] #Contains list of tuples where each tuple denotes x1,x2,h of a cardboard
    #build the list of tuples from the user's input
    for _ in range(n):
        cardboards.append(tuple(map(int,input().strip().split())))
    
    print (getElevationCoordinates(n,cardboards))
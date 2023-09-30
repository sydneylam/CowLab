import sys
import heifer_generator as hg
from cow import Cow
cowData = hg.HeiferGenerator()
 

def _list_cows(cows: list[Cow]):
    return hg.HeiferGenerator.cowNames
 

def _find_cow(name: str, cows: list[Cow]):
    if (name == 'heifer'):
        return cowData.cowImages[0]
    elif (name == 'kitteh'):
        return cowData.cowImages[1]
    else:
        return False
   
def _get_message(args: list[str], startingIndex:int= 1):
    message = str()
    for word in range(startingIndex, len(args)):
        if not (word == len(args)-1):
            message += args[word]+' '
        else:
            message+= args[word]
    return message
 
def main():
    args = sys.argv
    #List cows
    if args[1]=='-l':
        # cows=str()
        # for cow in _list_cows(hg.get_cows()):
        #     cows+= cow + ' '
        cows = _get_message(_list_cows(hg.get_cows()),0)
        print(f"Cows available: {cows}")
       
    #Picking out cows
    elif args[1] =='-n':
        message = _get_message(args,3)
       
        cow = _find_cow(args[2], hg.get_cows())
        if cow==False:
            print(f"Could not find {args[2]} cow!")
        else:
            print(message)
            print(cowData.quoteLines+cow)
           
    #If only a message is sent, default cow
    else:
        message = _get_message(args)
       
        print(message)
        print(cowData.quoteLines+_find_cow('heifer', hg.get_cows()))
 

if __name__ == "__main__":
    main()

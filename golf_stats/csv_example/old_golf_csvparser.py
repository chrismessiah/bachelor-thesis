#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import numpy as np

def prepare_stats(filename):
    # Read stats from csv file
    golfstats = []
    with open(filename) as f:
        golfcsv = csv.reader(f, delimiter=',', quotechar='"')

        for row in golfcsv:
            golfstats.append(row)

    # Create golfer objects and populate list of golfers
    golfers = []
    #print("Golfstats 0: ", golfstats[0][0])
    #print(type(golfstats[0][0]))

    for items in golfstats[1:]:
        golfer = {}
        golfer["name"] = items[3]
        golfer["total"] = items[4]
        golfer["thru"] = items[5]
        golfer["round"] = items[6]
        golfer["R1"] = items[7]
        golfer["R2"] = items[8]
        golfer["R3"] = items[9]
        golfer["R4"] = items[10]
        golfer["strokes"] = items[11]
        golfers.append(golfer)

    #Write golfer objects to file
    with open(filename[:-4] + ".txt", "w") as f:
        for players in golfers:
            f.write(str(players))
            f.write("\n")

def get_golfer_stats(filename):
    with open(filename, "r") as f:
        golfer = f.readlines()

    golfer_objects = []
    #print("Golfer length: ", golfer)
    for items in golfer:
        golfer_objects.append(eval(items))

    return golfer_objects


def calc_stats(golfers):
    """ Calculate som statistics, cutting players that has not made final round. 
    We need to add a flag for cut players. How much will this skew our results? How often does it happen?"""
    scored_players = 0
    scores = []
    nonvalid = ['', '-- ']

    print(golfers)
    def calc_vs_field(golfers):
        i = 0
        while i <= len(golfers):
            temp_golfers = golfers[:i] + golfers[i+1:]
            for players in temp_golfers: 
                if players["thru"] == 'F ':
                    temp_scores.append(float(players["strokes"]) / 4)
                else:
                    pass

            temp_scores = np.asarray(temp_scores)
            
            
            i += 1




    calc_vs_field(golfers)
    """
        i = 0
        while i <= len(scores):
            #Remove current players score
            print(i)
            part_score = scores[:i] + scores[i + 1:]
            print(len(scores), len(part_score))
            part_score = np.asarray(part_score)
            i += 1

            print(golfers[i]["name"])

        print("HOJ", len(scores))

    calc_vs_field(scores, golfers)

    """
    """
    Here we have a slight problem, scores on pgatour.com indicate Stroke diff vs field, we have z-score. 
    Luckily its almost a normal distributin anyway. But we will have decide on the accuracy we want. 

    First however this has to be fixed so the z-score for each player is calculated vs the field not including 
    himself. (Slightly better but worse than z-score?)

    #Full field scores
    scores = np.asarray(scores)
    print("Standard deviation:", np.std(scores))
    print("Mean: ", np.mean(scores))
    print("WINNER stats:")
    print("Name: ", golfers[0]["name"])
    print("Avg Score / Round: ", scores[0])
    z = (scores[0] - np.mean(scores)) / np.std(scores)
    print("Z-score: ", z)
    print("-")
    sdiff = scores[0] - np.mean(scores)
    print("Stroke diff vs field", sdiff)
    print("'z-differror", abs(((sdiff / z)-1)*100), "%") #Difference in percentage
    print("---------------------------------")

"""
if __name__ == '__main__':
    #prepare_stats("shriners.csv")
    #a = get_golfer_stats("shriners.txt")
    #print("shriners")
    #calc_stats(a)
    #print("FRYS.COM")
    #prepare_stats("frys.csv")
    #b = get_golfer_stats("frys.txt")
    #calc_stats(b)    
    print("CIMB")
    prepare_stats("CIMB.csv")
    b = get_golfer_stats("CIMB.txt")
    calc_stats(b)
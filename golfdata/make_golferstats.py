#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CBS-sports test
import urllib2
import os
from bs4 import BeautifulSoup

def clean_string(t):
    golf_str = str(t.contents)
    golf_str = golf_str.strip("[u']")
    golf_str = " ".join(golf_str.split())

    return golf_str

def try_to_int(score_string):
    try:
        score_string = int(score_string)
    except ValueError:
        if 'E' in score_string:
            score_string = 0
        else:
            pass
    return score_string

def make_golfer_stats(html):
    """ Takes a saved pgatour.com/tournaments/[Tournamentname].html page and returns 
    a list of golfer stat objects """
    soup = BeautifulSoup(str(html), 'html.parser')
    golfers = []

    tr = soup.find_all("tr", "row-main")
    for tags in tr:
        player = {}
    
        # Get player name
        td = tags.find_all("td", "col-player")
        for t in td:
            link = t.find_all("a", "name")
            try:
                name = str(link[0].contents).strip("[u']") #Clean names
                name = " ".join(name.split())
                player["name"] = name
                
            except IndexError:
                pass
        
        #Get player total score diff (against par)
        td = tags.find_all("td", "col-total")
        for t in td:
            total = clean_string(t)
            total = try_to_int(total)
            player["total"] = total
    
        #Get player Through F/--
        td = tags.find_all("td", "col-thru")
        for t in td:
            thru = clean_string(t)
            player["thru"] = thru
    
        #Get player round scores
        td = tags.find_all("td", "col-rx")
        x = 1
        for t in td:
            score = clean_string(t)
            score = try_to_int(score)
            player["R" + str(x)] = score
            x += 1
    
        td = tags.find_all("td", "col-strokes")
        for t in td:
            strokes = clean_string(t)
            strokes = try_to_int(strokes)
            player["strokes"] = strokes
    
        td = tags.find_all("td", "col-round")
        for t in td:
            per_round = clean_string(t)
            per_round = try_to_int(per_round)
            player["per_round"] = per_round
    
        #Add golfers to list
        golfers.append(player)

    return golfers

def main(file_list):
    """ Takes a list of pga tournament names and saves a list of stat objects for each player and 
    competition to file """

    for tournament in file_list:  
        with open(tournament) as f:
            html = f.readlines()

        stats = make_golfer_stats(html)
        #print(stats)

        with open(tournament[:-5] + "_stats.txt", "w") as f:
            for players in stats:
                f.write(str(players))
                f.write("\n")

        print("Wrote stats to file for: ", tournament)

def get_file_list():
    dirlist = os.listdir(".")
    valid = []
    for items in dirlist:
        if items[:3] == "pga" and items[-4:] == "html":
            valid.append(items)
    print("Getting stats for: ", valid)
    return valid

if __name__ == '__main__':
    file_list = get_file_list()
    main(file_list)
    print("Done")


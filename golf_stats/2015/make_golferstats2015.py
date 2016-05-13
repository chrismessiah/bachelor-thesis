#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CBS-sports test
import urllib2
import os
from bs4 import BeautifulSoup
import unicodedata

def clean_string(t):
    golf_str = str(t.contents)
    golf_str = golf_str.strip("[u']")
    golf_str = golf_str.replace('\\xa0', ' ')

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

    tr = soup.find_all("tr")
    for tags in tr[5:]:
        player = {}
    
        # Get player name
        td = tags.find_all("td")

        name = clean_string(td[0])
        #print(name)
        player["name"] = name
        try: 
            #SORRY FOR THIS
            r1 = clean_string(td[2])
            r1 = try_to_int(r1)        
            r2 = clean_string(td[3])
            r2 = try_to_int(r2)        
            r3 = clean_string(td[4])
            r3 = try_to_int(r3)        
            r4 = clean_string(td[5])
            r4 = try_to_int(r4)

            player["R1"] = r1
            player["R2"] = r2
            player["R3"] = r3
            player["R4"] = r4

            score = clean_string(td[6])
            score = try_to_int(score)
            player["score"] = score
        except IndexError:
            print("IndexError when trying to press tags with content:", tags)

        #Add golfers to list
        if player.has_key("name"):
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
        if items[:3] == "pga" and items[-9:] == "2015.html":
            valid.append(items)
    print("Getting stats for: ", valid)
    return valid

if __name__ == '__main__':
    file_list = get_file_list()
    main(file_list)
    print("Done")

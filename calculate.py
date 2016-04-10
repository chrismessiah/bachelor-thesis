# -*- coding: utf-8 -*-
import datetime 
import numpy as np 

def get_tweets_from_file(filename):
	with open(filename, "r") as f:
		tweet = f.readlines()

	tweet_objects = []
	for items in tweet:
		tweet_objects.append(eval(items))

	return tweet_objects

def tweet_interval_avg(dateObj, num_days, tweet_objects):
    """Takes a datetime object, an int and a list of tweetobjecs and returns the average score
    for tweets within that span. 

    Example dateOjb: dateObj = datetime.datetime.strptime("2015-06-01 00:00:00", "%Y-%m-%d %H:%M:%S") """

    span = datetime.timedelta(days= num_days).total_seconds()
    print("SPAN: ", datetime.timedelta(days= num_days), 
        "Seconds:", datetime.timedelta(days= num_days).total_seconds())

    total_score = 0
    hits = 0
    for items in tweet_objects:
        #print((items["date"] - dateObj))
        if (abs(items["date"] - dateObj).total_seconds()) < span:
            print("Hit within span, score: ", items["score"])
            total_score += items["score"]
            hits += 1

    return total_score / hits

def tweets_per_golfer(tweets):
    golf_list = []
    for tweet in tweets:
        golfers = {}
        if tweet["realname"] not in golfers:
            golfers[ tweet["realname"] ] = 1
        else:
            golfers[ tweet["realname"] ] += 1

        golfers["oldest"] = tweet["date"]
        golf_list.append(golfers)
    return golf_list

def get_stats_from_file(filename):
    stat_objects = [] 
    with open(filename, "r") as f:
        stats = f.readlines()

    for items in stats:
        stat_objects.append(eval(str(items)))

    return stat_objects

def create_competition_stat_object():
    """Makes a golfcompetition object"""

    pga_northerntrust_2015 = {"name": "pga_northerntrust_2015", "date": ["2015-02-16", "2015-02-22"]}
    pga_ohlclassic_2015 = {"name": "pga_ohlclassic_2015", "date": ["2014-11-10", "2014-11-16"]}
    pga_pebblebeach_2015 = {"name": "pga_pebblebeach_2015", "date": ["2015-02-09", "2015-02-15"]}
    pga_arnoldpalmer_2015 = {"name": "pga_arnoldpalmer_2015", "date": ["2015-03-16", "2015-03-22"]}          
    pga_pgachampionship_2015 = {"name": "pga_pgachampionship_2015", "date": ["2015-08-10", "2015-08-16"]}
    pga_barclays_2015 = {"name": "pga_barclays_2015", "date": ["2015-08-24", "2015-08-30"]}              
    pga_playerschampions_2015 = {"name": "pga_playerschampions_2015", "date": ["2015-05-04", "2015-05-10"]}
    pga_bmw_2015 = {"name": "pga_bmw_2015", "date": ["2015-09-14", "2015-09-20"]}                   
    pga_puertoricoopen_2015 = {"name": "pga_puertoricoopen_2015", "date": ["2015-03-02", "2015-03-08"]}
    pga_bridgestone_2015 = {"name": "pga_bridgestone_2015", "date": ["2015-08-03", "2015-08-09"]}           
    pga_quickenloans_2015 = {"name": "pga_quickenloans_2015", "date": ["2015-07-27", "2015-08-02"]}
    pga_cadillacchampionship_2015 = {"name": "pga_cadillacchampionship_2015", "date": ["2015-03-02", "2015-03-08"]}  
    pga_rbccanadianopen_2015 = {"name": "pga_rbccanadianopen_2015", "date": ["2015-07-20", "2015-07-26"]}
    pga_cimbclassic_2015 = {"name": "pga_cimbclassic_2015", "date": ["2014-10-20", "2014-10-26"]}           
    pga_rbcheritage_2015 = {"name": "pga_rbcheritage_2015", "date": ["2015-04-13", "2015-04-19"]}
    pga_farmersinsurance_2015 = {"name": "pga_farmersinsurance_2015", "date": ["2015-02-02", "2015-02-08"]}
    pga_cocacola_2015 = {"name": "pga_cocacola_2015", "date": ["2015-09-21", "2015-09-27"]}            
    pga_sanderson_2015 = {"name": "pga_sanderson_2015", "date": ["2014-11-03", "2014-11-09"]}
    pga_deutchebank_2015 = {"name": "pga_deutchebank_2015", "date": ["2015-08-31", "2015-09-07"]}           
    pga_shriners_2015 = {"name": "pga_shriners_2015", "date": ["2014-10-13", "2014-10-19"]}
    pga_frys_2015 = {"name": "pga_frys_2015", "date": ["2014-10-06", "2014-10-12"]}                  
    pga_sonyopen_2015 = {"name": "pga_sonyopen_2015", "date": ["2015-01-12", "2015-01-18"]}
    pga_greenbrier_2015 = {"name": "pga_greenbrier_2015", "date": ["2015-06-29", "2015-07-05"]}            
    pga_thememorial_2015 = {"name": "pga_thememorial_2015", "date": ["2015-06-01", "2015-06-07"]}
    pga_hondaclassic_2015 = {"name": "pga_hondaclassic_2015", "date": ["2015-02-23", "2015-03-01"]}          
    pga_theopen_2015 = {"name": "pga_theopen_2015", "date": ["2015-07-13", "2015-07-19"]}
    pga_houstonopen_2015 = {"name": "pga_houstonopen_2015", "date": ["2015-03-30", "2015-04-05"]}           
    pga_usopen_2015 = {"name": "pga_usopen_2015", "date": ["2015-06-15", "2015-06-21"]}
    pga_hsbcchampions_2015 = {"name": "pga_hsbcchampions_2015", "date": ["2014-11-03", "2014-11-09"]}         
    pga_valspar_2015 = {"name": "pga_valspar_2015", "date": ["2015-03-09", "2015-03-15"]}
    pga_humana_2015 = {"name": "pga_humana_2015", "date": ["2015-01-19", "2015-01-25"]}                
    pga_wastemanagement_2015 = {"name": "pga_wastemanagement_2015", "date": ["2015-01-26", "2015-02-01"]}
    pga_hyundai_2015 = {"name": "pga_hyundai_2015", "date": ["2015-01-05", "2015-01-12"]}               
    pga_wellsfargo_2015 = {"name": "pga_wellsfargo_2015", "date": ["2015-05-11", "2015-05-17"]}
    pga_johndeere_2015 = {"name": "pga_johndeere_2015", "date": ["2015-07-06", "2015-07-12"]}             
    pga_wyndham_2015 = {"name": "pga_wyndham_2015", "date": ["2015-08-17", "2015-08-23"]}
    pga_masters_2015 = {"name": "pga_masters_2015", "date": ["2015-04-16", "2015-04-12"]}               
    pga_zurich_2015 = {"name": "pga_zurich_2015", "date": ["2015-04-20", "2015-04-26"]}
    pga_valero_2015 = {"name": "pga_valero_2015", "date": ["2015-03-23", "2015-03-29"]}
    pga_crowneplaza_2015 = {"name": "pga_crowneplaza_2015", "date": ["2015-05-18", "2015-05-24"]}
    pga_attbyronnelson_2015 = {"name": "pga_attbyronnelson_2015", "date": ["2015-05-25", "2015-05-31"]}
    pga_fedexstjude_2015 = {"name": "pga_fedexstjude_2015", "date": ["2015-06-08", "2015-06-14"]}

    dates_1415 = [pga_northerntrust_2015 ,pga_ohlclassic_2015 ,pga_pebblebeach_2015 ,pga_arnoldpalmer_2015 ,
    pga_pgachampionship_2015 ,pga_barclays_2015 ,pga_playerschampions_2015 ,pga_bmw_2015 ,
    pga_puertoricoopen_2015 ,pga_bridgestone_2015 ,pga_quickenloans_2015 ,pga_cadillacchampionship_2015 ,
    pga_rbccanadianopen_2015 ,pga_cimbclassic_2015 ,pga_rbcheritage_2015 ,pga_farmersinsurance_2015 ,
    pga_cocacola_2015 ,pga_sanderson_2015 ,pga_deutchebank_2015 ,pga_shriners_2015 ,pga_frys_2015 ,
    pga_sonyopen_2015 ,pga_greenbrier_2015 ,pga_thememorial_2015 ,pga_hondaclassic_2015 ,pga_theopen_2015 ,
    pga_houstonopen_2015 ,pga_usopen_2015 ,pga_hsbcchampions_2015 ,pga_valspar_2015 ,pga_humana_2015 ,
    pga_wastemanagement_2015 ,pga_hyundai_2015 ,pga_wellsfargo_2015 ,pga_johndeere_2015 ,pga_wyndham_2015 ,
    pga_masters_2015 ,pga_zurich_2015 ,pga_valero_2015 ,pga_crowneplaza_2015 ,pga_attbyronnelson_2015 ,
    pga_fedexstjude_2015 ]

    return dates_1415

def make_z_scores(stat_objects):
    scores = []
    for items in stat_objects:
        try:
            scores.append( float( items["score"] ) )
        except KeyError:
            pass
        except ValueError:
            #print(items["name"], "'s score:", items["score"], "invalid")
            scores.append(0)

    scores = np.array(scores)
    mean = np.mean(scores)
    std = np.std(scores)

    z_scores = []

    for i, score in enumerate(scores):
        z = calc_zscore(score, mean, std)
        z_scores.append(z)
        stat_objects[i]["z-score"] = z

    z_mean = np.mean(np.array(z_scores))

    return stat_objects, mean, z_mean

def calc_zscore(x, mean, std):
    z = (x - mean) / std 
    return z

def make_individual_stats(competions):
    # name: [stat_aray]
    player_stats = {}
    for competition in competitions:
        for player in competition["player_stats"]:
            try:
                print(player["z-score"])
                if player["name"] not in player_stats:
                    player_stats[ player["name"] ] = [ player["z-score"] ]
                else:
                    player_stats[ player["name"] ].append(player["z-score"])
            except KeyError:
                print("KeyError, no z-score for player")
                print(player)

    return player_stats


if __name__ == '__main__':
    #tweets = get_tweets_from_file("golfersRun27mars.txt")
    #avg = tweet_interval_avg(datetime.datetime.strptime("2015-06-01" ,"%Y-%m-%d"), 3, tweets)
    #print("Average within 5 days from 2016-06-01: ", avg)
    #print(tweets_per_golfer(tweets))
    competitions = create_competition_stat_object()
    for competition in competitions:
        #print("Getting stats for", competition["name"])
        stat_objects = get_stats_from_file("golfdata/2015/" + competition["name"] + "_stats.txt")
        player_stats, mean, z_mean = make_z_scores(stat_objects)

        competition["player_stats"] = player_stats
        competition["mean"] = mean
        competition["z-mean"] = z_mean

    for competition in competitions:
        #print(competition["mean"])
        with open("competition_stats.csv", "a") as f:
            f.write(competition["name"])
            f.write(",")
            f.write(str(competition["mean"]))
            f.write(",")
            f.write(str(competition["z-mean"]))
            f.write(",")
            f.write("\n")

    player_stats = make_individual_stats(competitions)

    for name, score in player_stats.iteritems():
        score = np.array(score)
        mean = np.mean(score)
        with open("zscores_2015.csv", "a") as f:
            # Delt
            if len(score) > 10:
                f.write(str(name))
                f.write(",")
                f.write(str(mean))
                f.write(",")
                f.write(str(len(score)))
                f.write(",")
                f.write("\n")






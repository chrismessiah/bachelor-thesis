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


def tweet_interval_counter_and_score_avg(date, num_days_before, tweet_objects):
    tweet_counter = 0
    total_score = 0
    span = abs(datetime.timedelta(days = num_days_before).total_seconds())
    for tw in tweet_objects:
        if num_days_before < 0: # tweets after tournament
            if date < tw["date"] and  0 < (tw["date"] - date).total_seconds() < span:
                tweet_counter += 1
                total_score += tw["score"]
        if num_days_before > 0: # tweets before tournament
            if tw["date"] < date and  0 < (date - tw["date"]).total_seconds() < span:
                tweet_counter += 1
                total_score += tw["score"]
    if tweet_counter == 0:
        return None, tweet_counter
    else:
        return total_score / tweet_counter, tweet_counter

def get_stats_from_file(filename):
    stat_objects = []
    with open(filename, "r") as f:
        stats = f.readlines()

    for items in stats:
        stat_objects.append(eval(str(items)))

    return stat_objects

def create_competition_stat_object():
    """Makes a golfcompetition object, should be moved to a static file but whatevs"""

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

    return stat_objects, mean, z_mean, std

def calc_zscore(x, mean, std):
    z = (x - mean) / std
    # print("x",x,"mean", mean, "std", std, "z", z)
    return z

def make_individual_stats(competitions):
    # name: [stat_aray]
    player_stats = {}
    for competition in competitions:
        for player in competition["player_stats"]:
            try:
                if player["name"] not in player_stats:
                    player_stats[ player["name"] ] = [ player["z-score"] ]
                else:
                    player_stats[ player["name"] ].append(player["z-score"])
            except KeyError:
                pass#print("KeyError, no z-score for player in ", competition["name"])
                #print(player)

    return player_stats

# makes sure all golfers have participated on R1
def clean_stat_object(stat_objects):
    new_stat_objects = []
    for stat in stat_objects:
        try:
            int(stat["R1"]) # throw error if bad value
            new_stat_objects.append(stat) # append if good value
        except KeyError:
            pass # {'name': 'ROUNDS'}
        except ValueError:
            pass # {'R4': '', 'R1': '', 'R2': '', 'R3': '', 'score': '', 'name': 'Erik Compton'}
    return new_stat_objects

def correct_round_data(stat_objects):
    for golfer_data in stat_objects:
        if not(str(golfer_data["R2"]).isdigit()): # Missed 3 rounds
            golfer_data["R2"] = golfer_data["R1"]
            golfer_data["R3"] = golfer_data["R1"]
            golfer_data["R4"] = golfer_data["R1"]
        elif not(str(golfer_data["R3"]).isdigit()): # Missed 2 rounds
            mean = int(round(np.mean([golfer_data["R1"], golfer_data["R2"]])))
            golfer_data["R3"] = mean
            golfer_data["R4"] = mean
        elif not(str(golfer_data["R4"]).isdigit()): # Missed 1 rounds
            mean = int(round(np.mean([golfer_data["R1"], golfer_data["R2"], golfer_data["R3"]])))
            golfer_data["R4"] = mean
        else: # Finished
            pass
            #print(golfer_data)
        golfer_data["score"] = golfer_data["R1"] + golfer_data["R2"] + golfer_data["R3"] + golfer_data["R4"]
        #print(golfer_data)
    return stat_objects

def make_competition_stats(write = False):
    competitions = create_competition_stat_object()
    for competition in competitions:
        #print("Getting stats for", competition["name"])
        stat_objects = get_stats_from_file("../get_golfstats/stats2015/" + competition["name"] + "_stats.txt")
        stat_objects = clean_stat_object(stat_objects)
        stat_objects = correct_round_data(stat_objects)
        player_stats, mean, z_mean, std = make_z_scores(stat_objects)

        competition["player_stats"] = player_stats
        competition["mean"] = mean
        competition["z-mean"] = z_mean
        competition["std"] = std

    if write:
	    with open("competition_stats.csv", "a") as f:
	        for competition in competitions:
		        f.write(competition["name"])
		        f.write(",")
		        f.write(str(competition["mean"]))
		        f.write(",")
		        f.write(str(competition["z-mean"]))
		        f.write(",")
		        f.write(str(competition["std"]))
		        f.write(",")
		        f.write("\n")

    player_stats = make_individual_stats(competitions)
    for name, score in player_stats.iteritems():
        score = np.array(score)
        mean = np.mean(score)
        if write:
        	with open("zscores_2015.csv", "a") as f:
	            if len(score) > 10:
	                f.write(str(name))
	                f.write(",")
	                f.write(str(mean))
	                f.write(",")
	                f.write(str(len(score)))
	                f.write(",")
	                f.write("\n")

    return player_stats, competitions
def error_handler(name, golfer_id):
    """A stupid function to handle stupid errors (Jokesters with non-realnames a real_name on twitter)"""
    if name == "cameron percy":
        return sum(player_stats["Cameron Percy"]) / len(player_stats["Cameron Percy"])
    elif int(golfer_id) == 387448282:
        return sum(player_stats["Steve Flesch"]) / len(player_stats["Steve Flesch"])
    elif int(golfer_id) == 534842435:
        return sum(player_stats["Phil Mickelson"]) / len(player_stats["Phil Mickelson"])
    elif int(golfer_id) == 2575022059:
        return sum(player_stats["Mike Weir"]) / len(player_stats["Mike Weir"])
    elif int(golfer_id) == 2980287125:
        return sum(player_stats["Fabian Gomez"]) / len(player_stats["Fabian Gomez"])
    elif int(golfer_id) == 2586530467:
        return sum(player_stats["Matt Jones"]) / len(player_stats["Matt Jones"])
    elif int(golfer_id) == 37843534:
        return sum(player_stats["J.J. Henry"]) / len(player_stats["J.J. Henry"])
    elif int(golfer_id) == 72758634:
        print("No official stats for Y.E. Yang (same on PGA Tour.com as far as I can tell)")
        return None
    elif int(golfer_id) == 74791999:
        return sum(player_stats["Bubba Watson"]) / len(player_stats["Bubba Watson"])
    elif int(golfer_id) == 174596509:
        return sum(player_stats["Sangmoon Bae"]) / len(player_stats["Sangmoon Bae"])
    elif int(golfer_id) == 180081562:
        return sum(player_stats["Seung-Yul Noh"]) / len(player_stats["Seung-Yul Noh"])
    elif int(golfer_id) == 188039706:
        return sum(player_stats["Rory McIlroy"]) / len(player_stats["Rory McIlroy"])
    elif int(golfer_id) == 244768359:
        return sum(player_stats["Adam Hadwin"]) / len(player_stats["Adam Hadwin"])
    elif int(golfer_id) == 283052420:
        return sum(player_stats["Michael Putnam"]) / len(player_stats["Michael Putnam"])
    elif int(golfer_id) == 306549170:
        return sum(player_stats["Chris Stroud"]) / len(player_stats["Chris Stroud"])
    elif int(golfer_id) == 342791510:
        return sum(player_stats["Max Homa"]) / len(player_stats["Max Homa"])
    elif int(golfer_id) == 373511205:
        return sum(player_stats["Marc Leishman"]) / len(player_stats["Marc Leishman"])
    elif int(golfer_id) == 382202772:
        return sum(player_stats["Michael Kim"]) / len(player_stats["Michael Kim"])
    elif int(golfer_id) == 558220594:
        return sum(player_stats["Will MacKenzie"]) / len(player_stats["Will MacKenzie"])
    elif int(golfer_id) == 1138456724:
        return sum(player_stats["Jason Kokrak"]) / len(player_stats["Jason Kokrak"])
    elif int(golfer_id) == 1924882021:
        return sum(player_stats["Andrew Svoboda"]) / len(player_stats["Andrew Svoboda"])
    elif int(golfer_id) == 2790755710:
        return sum(player_stats["Tony Fina"]) / len(player_stats["Tony Fina"])
    elif int(golfer_id) == 174780495:
        print("No official stats for Thorbjorn Olesen (same on PGA Tour.com as far as I can tell)")
        return None
    elif int(golfer_id) == 1152096636:
        print("No official stats for DJ Trahan found")
        return None
    else:
        raise KeyError(name + " ID: " + golfer_id)

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

def check_performance_vs_tweets(tweets, competitions, player_stats, relative_or_absolute, days_before, tweet_lower_limit, write = False):
    days = days_before
    #print(player_stats)
    with open("../twitter_mining/golfer_twitter_ids.txt") as f:
        golferIDs = f.read().splitlines()
    data_pairs = []
    #TODO: Make into a loop for all golfers!

    for golfer in golferIDs:
        golfer_tweets = []
        golfer_afinnscore = []
        for tweet in tweets:
            if int(golfer) == tweet["user_id"]:
                golfer_tweets.append(tweet)
                golfer_afinnscore.append(tweet["score"])

        #print(golfer_tweets)
        if len(golfer_tweets) > 0:
            oldest = golfer_tweets[0]["date"]

            for tw in golfer_tweets:
                if tw["date"] < oldest:
                    oldest = tw["date"]

            #print(oldest)
            #print(len(golfer_tweets))


            golfer_name = golfer_tweets[0]["realname"]
            golfer_afinn_mean = np.mean(np.array(golfer_afinnscore)) #Get golfer AFINN average
            #Make golfer afinnmeans file
            #print(golfer_name, golfer_afinn_mean)
            #with open("golfer_happymean.csv", "a") as f:
            #    try:
            #        f.write(golfer_name)
            #        f.write(",")
            #        f.write(str(golfer_afinn_mean))
            #        f.write(",")
            #        f.write("\n")
            #    except UnicodeEncodeError:
            #        f.write("UnicodeError player")
            #        f.write(",")
            #        f.write(str(golfer_afinn_mean))
            #        f.write(",")
            #        f.write("\n")
            #Get golfer average score:
            try:
                golfer_mean_z = sum(player_stats[golfer_name]) / len(player_stats[golfer_name])
            except KeyError:
                golfer_mean_z = error_handler(golfer_name, golfer)

            #print(golfer_name, "AfinnMean: ", golfer_afinn_mean, "Z-mean: ", golfer_mean_z)
            for competition in competitions:
                """ Get golfers relative Afinn score """
                date = datetime.datetime.strptime(competition["date"][0], "%Y-%m-%d") # 0 is start date, 1 is end date
                interval_avg, tweet_counter = tweet_interval_counter_and_score_avg(date, days, golfer_tweets)
                if interval_avg != None:
                    if relative_or_absolute == "a":
                        afinn_diff = interval_avg # absolute
                    elif relative_or_absolute == "r":
                        afinn_diff = interval_avg - golfer_afinn_mean # relative
                    else:
                        print("ERROR ON R/A")
                else:
                    afinn_diff = None
                """ Get golfers Z-score for competition"""
                for stat in competition["player_stats"]:
                    try:
                        if stat["name"] == golfer_name:
                            score_diff = stat["z-score"] - golfer_mean_z
                    except KeyError:
                        print("ERROR! No Z-score found for:", stat," in ", competition["name"])
                if afinn_diff != None:
                    # if afinn_diff > 0:
                    #     data_pairs.append([afinn_diff, score_diff])
                    data_pairs.append([afinn_diff, score_diff])
                if tweet_counter >= tweet_lower_limit and write and interval_avg != None:
                    with open("output_datapairs.csv", "a") as f:
                        for items in data_pairs:
                            f.write(str(items[0]))
                            f.write(",")
                            f.write(str(items[1]))
                            f.write(",")
                            f.write("\n")
                data_pairs = []
        else:
            print("Error on golferID ",golfer)

    return data_pairs

if __name__ == '__main__':

	# *************** STARTING PARAMETERS *************
    relative_or_absolute = "r" # a or r
    days_before = 3 # Can be negative to imply AFTER competition
    tweet_lower_limit = 1 # ≥ 1
    # *************** STARTING PARAMETERS *************

    tweets = get_tweets_from_file("../twitter_mining/all_tweets.txt")
    player_stats, competitions = make_competition_stats(write = False)

    check_performance_vs_tweets(tweets, competitions, player_stats, relative_or_absolute, days_before, tweet_lower_limit, write = True)

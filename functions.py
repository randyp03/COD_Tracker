import requests, time, csv, os

# function formats date parameter
def format_date(date):
    formatted_date = time.strftime('%Y-%m-%d', time.localtime(date))
    return formatted_date

# function formates time parameter
def format_time(match_time):
    formatted_time = time.strftime('%H:%M:%S', time.localtime(match_time))
    return formatted_time

# calls api url and returns data
def get_api_call(url, cookies):
    payload={}
    headers = {
        'Cookie': f"ACT_SSO_COOKIE={cookies['ACT_SSO_COOKIE']}; ACT_SSO_COOKIE_EXPIRY={cookies['ACT_SSO_COOKIE_EXPIRY']}; atkn={cookies['atkn']};"
    }

    response = requests.get(url, headers=headers, data=payload)
    return response

# creates csv file if not already created
def create_csv_file():
    try:
        with open('cod_match_stats.csv', 'r+') as f:
            header = f.readline()
            if header != 'MatchID,Date,StartTime,EndTime,Map,Mode,Kills,KD_Ratio,Accuracy,Damage,Points\n':
                f.write('MatchID,Date,StartTime,EndTime,Map,Mode,Kills,KD_Ratio,Accuracy,Damage,Points\n')
    
        f.close()
    except FileNotFoundError:
        file = open('cod_match_stats.csv', 'w')
        file.close

# finds and returns the most recent entry date in csv file
def find_most_recent_date(filename = '/cod_match_stats.csv'):
    with open(filename, 'r') as f:
        readCSV = csv.reader(f, delimiter=',')
        next(readCSV, None)
        recent_date = '2021-01-01'
        for row in readCSV:
            if row[1] > recent_date:
                recent_date = row[1]
    return recent_date

# function will format player data and turn in into a dictionary
def format_match_data(match_data, recent_date):
    player_stats_dict = {}
    match_count = 0

    for match in match_data:
        if str(format_date(match['utcStartSeconds'])) > recent_date:
            match_count += 1
            player_stats_dict[f'match{match_count}'] = {
                                                        'MatchID': match['matchID'],
                                                        'Date': f"{format_date(match['utcStartSeconds'])}",
                                                        'StartTime': f"{format_time(match['utcStartSeconds'])}",
                                                        'EndTime': f"{format_time(match['utcEndSeconds'])}",
                                                        'Map': match['map'], 
                                                        'Mode': match['mode'],
                                                        'Kills': match['playerStats']['kills'],
                                                        'KD_Ratio': match['playerStats']['kdRatio'],
                                                        'Accuracy': match['playerStats']['accuracy'],
                                                        'Damage': match['playerStats']['damageDealt'],
                                                        'Points': match['playerStats']['scorePerMinute']
                                                    }
        elif str(format_date(match['utcStartSeconds'])) == recent_date:
            break

    return player_stats_dict

# appends captured and formatted data into csv file
def append_before_training_file(player_stats=None, filename = '/cod_match_stats.csv'):
    file = open(filename , 'a')

    for match in player_stats.values():
        file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' %(match['MatchID'],
                                                          match['Date'],
                                                          match['StartTime'],
                                                          match['EndTime'],
                                                          match['Map'],
                                                          match['Mode'],
                                                          match['Kills'],
                                                          match['KD_Ratio'],
                                                          match['Accuracy'],
                                                          match['Damage'],
                                                          match['Points']))

    file.close()

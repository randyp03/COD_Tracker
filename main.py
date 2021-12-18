import functions

# url to get api call
url = 'https://my.callofduty.com/api/papi-client/crm/cod/v2/title/cw/platform/uno/gamer/{{username}}/matches/mp/start/0/end/0/details'

# login cookies used to get past capcha
cookies = {
    'ACT_SSO_COOKIE' : '{{ACT_SSO_COOKIE}}',
    'ACT_SSO_COOKIE_EXPIRY' : '{{ACT_SSO_COOKIE_EXPIRY',
    'atkn' : '{{atkn}}'
}


response = functions.get_api_call(url, cookies)

# gets the match data of the last 50 matches
match_data = response.json()['data']['matches'][0:50]

# creates csv file and header if not already created
functions.create_csv_file()

# get the most recent match date in csv file
recent_date = functions.find_most_recent_date()

# formats the newest data entered into a dictionary
player_stats = functions.format_match_data(match_data, recent_date)

# adds new data to the csv
functions.append_before_training_file(player_stats)

if len(player_stats) == 0:
    print('No new matches found')
else:
    print(f"{len(player_stats)} new matches were added")

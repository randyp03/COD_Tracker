# COD_Tracker

Python scripts gets access to the multiplayer match data in Call of Duty: Cold War with the help of [an API created here](https://documenter.getpostman.com/view/5519582/SzzgAefq#03b6293c-c18b-4f8e-8d2a-0693dcd353e6)

The script:
- Captures the data of the last 50 matches played.
- Creates a csv file to input the match data
- Reads the csv file to see what is the most recent match date saved
- Writes new match data to the csv file

If Cold War match data is wanted
- Sign in to your Call of Duty account via web-browser
- Get the tokens ACT_SSO_COOKIE, ACT_SSO_COOKIE_EXPIRY, and atkn tokens
- Enter your platform-specific Call of Duty usersame (Example given by [API website:](https://documenter.getpostman.com/view/5519582/SzzgAefq#03b6293c-c18b-4f8e-8d2a-0693dcd353e6) MellowD#6992980 = MellowD%236992980)

If Modern Warfare (2019) or other recent Call of Duty games match data is wanted, refer to the [Call of Duty API](https://documenter.getpostman.com/view/5519582/SzzgAefq#03b6293c-c18b-4f8e-8d2a-0693dcd353e6)

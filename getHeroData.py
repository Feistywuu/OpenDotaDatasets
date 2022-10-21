
import requests, json, time, os
import pandas as pd


# get hero dota
def get_hero_stats():
    data = requests.get("https://api.opendota.com/api/heroStats").json()
    pd.DataFrame(data).to_csv("hero_stats.csv", sep=",")
    with open('hero_stats.json', 'w') as outfile:
        json.dump(data, outfile)


'References'
# https://www.reddit.com/r/DotA2/comments/leakdy/how_to_do_statistics_on_dota_2_with_python/
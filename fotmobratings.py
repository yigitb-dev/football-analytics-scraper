from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

eng_league = f"https://www.fotmob.com/tr/leagues/47/stats/season/27110/players/rating/premier-league?page="
tr_leauge = f"https://www.fotmob.com/tr/leagues/71/stats/season/27244/players/rating/super-lig?page="
bel_league = f"https://www.fotmob.com/tr/leagues/40/stats/season/27152/players/rating/first-division?page="
spa_league = f"https://www.fotmob.com/tr/leagues/87/stats/season/27233/players/rating/laliga?page="
ned_league = f"https://www.fotmob.com/tr/leagues/57/stats/season/27131/players/rating/eredivisie?page="
fra_league = f"https://www.fotmob.com/tr/leagues/53/stats/season/27212/players/rating/ligue-1?page="

def get_fotmob_ratings(url):

    options = Options()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)

    data = []

    page = 0
    while True:
        driver.get(url + f"{page}")
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        players = soup.find_all("div", class_="css-1u3ja2l-LeagueSeasonStatsTableRowCSS e4r748v9")
        
        if not players:  # stop if page is empty
            break
        
        for player in players:
            name = player.find("span", class_="css-cfc8cy-TeamOrPlayerName e4r748v6").text.strip()
            rating = player.find("span", class_="css-1mzgpr3-StatValue e4r748v8").text.strip()
            data.append({
                "name": name,
                "rating": rating
            })
        
        page += 1

    driver.quit()
    return pd.DataFrame(data)

df = get_fotmob_ratings(eng_league)
df.to_csv("player_ratings.csv", index=False)
print(df.head())
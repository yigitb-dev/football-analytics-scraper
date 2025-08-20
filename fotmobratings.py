from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_fotmob_ratings():

    options = Options()
    options.add_argument("--headless")  
    driver = webdriver.Chrome(options=options)

    data = []

    for i in range(28):

        url = f"https://www.fotmob.com/tr/leagues/71/stats/season/27244/players/rating/super-lig?page={i}"
        driver.get(url)

        if i == 0:
            # Wait for the page to load completely
            time.sleep(5) 


        soup = BeautifulSoup(driver.page_source, "html.parser")


        players = soup.find_all("div", class_="css-1u3ja2l-LeagueSeasonStatsTableRowCSS e4r748v9")

        for player in players:
            name = player.find("span", class_="css-cfc8cy-TeamOrPlayerName e4r748v6").text.strip()
            rating = player.find("span", class_="css-1mzgpr3-StatValue e4r748v8").text.strip()
            data.append({
                "name": name,
                "rating": rating
            })

    driver.quit()
    return pd.DataFrame(data)

df = get_fotmob_ratings()
df.to_csv("superlig_player_ratings.csv", index=False)
print(df.head())
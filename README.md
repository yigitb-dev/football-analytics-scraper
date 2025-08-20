# ⚽ Football Analytics Scraper

A Python-based web scraper that collects player ratings from [Fotmob](https://www.fotmob.com).  
The data can be exported into CSV format for further football analytics and machine learning experiments.

## 🚀 Features
- Scrapes player ratings across multiple leagues (Premier League, Süper Lig, La Liga, Ligue 1, Eredivisie, Belgian First Division).  
- Exports results into a clean CSV format.  
- Built with `Selenium`, `BeautifulSoup`, and `Pandas`.  
- Easily extendable to include more leagues and stats.  

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yigitb-dev/football-analytics-scraper.git
   cd football-analytics-scraper

2. Install dependencies:

  pip install -r requirements.txt
  
  ▶️ Usage

3. Run the scraper:

  python scraper.py


The output CSV file will be saved in the project folder.

📊 Example Output
name,rating
Mauro Icardi,7.42
Edin Džeko,7.10
Kerem Aktürkoğlu,7.05
...

📌 To-Do

 Add team names alongside player ratings.

 Scrape more advanced stats (goals, assists, expected goals, etc.).

 Add command-line arguments for league selection.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

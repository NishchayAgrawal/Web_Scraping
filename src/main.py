from Web_Scrap import FlipkartScraper
from SQL import SQLDatabase

if __name__ == "__main__":
    scraper = FlipkartScraper()
    scraper.fetch_data(page_range=range(2, 10))
    data = scraper.create_csv()

    sql = SQLDatabase()
    sql.create_connection()
    sql.create_table()
    sql.insert_data("laptop_data", data)

import requests
import pandas as pd
from bs4 import BeautifulSoup
from SQL import SQLDatabase

class FlipkartScraper:
    def __init__(self):
        self.product_names = []
        self.prices = []
        self.descriptions = []
        self.reviews = []

    def fetch_data(self, page_range):
        for i in page_range:
            url = f"https://www.flipkart.com/search?q=laptop+under+15000&page={i}"
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "lxml")
            box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

            names = box.find_all("div", class_="_4rR01T")
            prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
            desc = box.find_all("ul", class_="_1xgFaf")
            reviews = box.find_all("div", class_="_3LWZlK")

            # This will ensure all lists have the same length
            min_length = min(len(names), len(prices), len(desc), len(reviews))

            for j in range(min_length):
                name = names[j].text
                price = prices[j].text
                description = desc[j].text
                review = reviews[j].text

                self.product_names.append(name)
                self.prices.append(price)
                self.descriptions.append(description)
                self.reviews.append(review)

    def create_csv(self):
        data = pd.DataFrame({
            "Product Name": self.product_names,
            "Prices": self.prices,
            "Description": self.descriptions,
            "Review": self.reviews
        })
        #data.to_csv(filename, index=False)
        return data

if __name__ == "__main__":
    scraper = FlipkartScraper()
    scraper.fetch_data(page_range=range(2, 10))
    #scraper.create_csv("data.csv")
    data = scraper.create_csv()
    sql = SQLDatabase()
    sql.create_connection()
    sql.create_table()
    sql.insert_data("laptop_data",data)


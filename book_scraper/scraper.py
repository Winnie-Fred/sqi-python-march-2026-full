import requests

from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"


try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Something went wrong. Check your internet connection and try again")
else:
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # h1_elem = soup.find("h1")
        # print(h1_elem)
        # h1_elems = soup.find_all("h1")
        # print(h1_elems)
        
        product_articles = soup.select("div li article.product_pod")
        no_of_books = len(product_articles)
        print(f"No of books: {no_of_books}")

        price_p_elems = soup.select("div li article.product_pod div.product_price p.price_color")

        prices = [float(price_p_elem.text[2:]) for price_p_elem in price_p_elems]        
        try:
            print(f"Average price: {round(sum(prices)/no_of_books, 2)}")
        except ZeroDivisionError:
            print("Avergae price: ", None)

        titles_a_elememts = soup.select("div li article.product_pod h3 a")
        print(titles_a_elememts)

        books_with_prices = {title_a_element.get("title"): price for title_a_element, price in zip(titles_a_elememts, prices)}

        print(books_with_prices)

        print(f"Most expensive book: {max(books_with_prices, key=books_with_prices.get)}")

    else:
        print(f"Unexpected status code: {response.status_code}")
        
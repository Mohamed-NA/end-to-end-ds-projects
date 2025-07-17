import requests
import pandas as pd
from bs4 import BeautifulSoup

book_data = []

# Sending a request to the website
for page in range(1, 50):  # Assuming there are 5 pages
    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    #url = 'https://books.toscrape.com/' # For the first page only
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Finding all book containers
    books = soup.find_all('article', class_='product_pod')
    # Or we can use soup.find_all('article', {'class': 'product_pod'})

    # Extracting book details

    for book in books:
        title = book.h3.a['title']
        # To remove the the symbol Â from the price, we can use the replace method
        # price = book.find('p', class_='price_color').text.strip().replace('Â', '')
        price = book.find('p', class_='price_color').text[1:].strip()
        availability = book.find('p', class_='instock availability').text.strip()
        # The rating is stored in the class attribute of the p tag, e.g., 'star-rating Three'
        rating = book.find('p', class_='star-rating')['class'][1]
        book_data.append({'Book Name': title, 'Book Price': price, 'Book State': availability, 'Book Rating': rating})

# Creating a DataFrame
books_df = pd.DataFrame(book_data)

# Saving the DataFrame to an Excel file
excel_file = 'books_data.xlsx'
books_df.to_excel(excel_file, index=False)
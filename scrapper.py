import requests
from bs4 import BeautifulSoup
import sqlite3
URL = "http://books.toscrape.com/" 


def create_table():
    con = sqlite3.connect("books.sqlite3")
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE if not exists books(
                id integer primary key autoincrement,
                title text,
                currency text,
                price real
            );
        """
    )
    con.commit()
    con.close()

def insert_book(title,currency,price):
    conn= sqlite3.connect("books.sqlite3")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO books (title,currency,price) VALUES (?,?,?)",
        (title,currency,price),
    )
    conn.commit()
    conn.close()
def scrape_books(url):
    response = requests.get(url)
    if response.status_code != 200:
        return[]
    
    books = []
#set encoding explicitily to handle special character correctly
    response.encoding = response.apparent_encoding
    print(response.text)
    soup= BeautifulSoup(response.text, "html.parser")
    book_elements=soup.find_all("article",class_="product_pod")

    for book in book_elements:
        title = book.h3.a['title']
        price_text = book.find('p',class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])
        books.append(
            {"title":title, 
             "currency": currency,
             "price":price,
             }
        )
       
    print("All books have been scrapped ")
    return books

def save_to_json(books):
    import json

    with open ("books.json","w",encoding="utf-8") as f:
        json.dump(books, f,indent =4,ensure_ascii=False)

create_table()
books =scrape_books(URL)
save_to_json(books)


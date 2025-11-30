import requests
from bs4 import BeautifulSoup # Импорт библиотек для парсинга

base_url = 'https://books.toscrape.com/' # переменная для корневого URL сайта

for number in range(1, 51): # Перебираем страницы сайта

    url = f'https://books.toscrape.com/catalogue/page-{number}.html' # Задаем переменную для ссылки на каждую страницу

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml') ### получаем html-код страницы

    data = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") # получаем html-код всех карточек с информацией о книгах

    for book in data:
        book_name = book.find('img').get('alt')
        book_price = book.find('p', class_="price_color").text[1:]
        image = base_url + book.find('img').get('src')                ### проходимся по каждой книге текущей страницы и собираем информацию о ней

        print('name: ', book_name + '\n' + 'price: ',  book_price + '\n' + 'image: ', image) # вывод информации о всех книгах на сайте








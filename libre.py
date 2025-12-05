import xlsxwriter
from attempt import array  # импорт библиотеки и функции из файла

def writer(parametr):  # Функция для сбора данных в xlsx-файл
    book = xlsxwriter.Workbook("C:\\Users\\Владимир Персиков\\Desktop\\parser\\books.xlsx") # указание пути и название xlsx-файла
    page = book.add_worksheet("Книги") # указание названия страницы

    row = 0
    column = 0   ### создание переменных для строки и колонны, в которых будут лежать данные

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)  ### настройка размера указанных колонн

    for item in parametr:  # проходимся по данным, которые получили из функции array()

        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])  ### запись информации по нужным столбикам

        row += 1

    book.close() # завершение работы функции

writer(array()) #вызов функции

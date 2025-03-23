# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """Специальный класс, который отвечает за обработку входящих запросов от клиентов"""
    def do_GET(self):
        print(self.path)
        if self.path == "/" or self.path == "/main.html":
            self.serve_file("main.html")
        elif self.path == "/catalog.html":
            self.serve_file("catalog.html")
        elif self.path == "/category_1.html":
            self.serve_file("category_1.html")
        elif self.path == "/contact.html":
            self.serve_file("contact.html")
        elif self.path == '/logo/logo.jpeg':
            self.jpeg_file('logo/logo.jpeg')
        elif self.path == '/logo/thumbnails.jpg':
            self.jpeg_file('logo/thumbnails.jpg')
        else:  # Если путь не найден
            self.send_error(404, "Page Not Found")

    def serve_file(self, filename):
        """Обслуживает HTML-файлы"""
        filepath = os.path.join(os.path.dirname(__file__), filename)
        try:
            # Проверяем, существует ли файл
            if not os.path.exists(filepath):
                self.send_error(404, f'{filepath}')
                return

            # Читаем содержимое файла
            with open(filepath, encoding="utf-8") as file:
                content = file.read()

            # Отправляем заголовки
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()  # Завершение формирования заголовков ответа

            # Отправляем содержимое файла
            self.wfile.write(bytes(content, "utf-8"))
        except Exception as e:
            # Обрабатываем ошибки
            self.send_error(500, f"Server Error: {e}")


    def jpeg_file(self, filename):
        '''Обрабатываем получение данных jpeg файлов'''

        filepath = os.path.join(os.path.dirname(__file__), filename)
        print(filepath)
        try:
            # Проверяем, существует ли файл
            if not os.path.exists(filepath):
                self.send_error(404, f'{filepath}')
                return

            # Читаем содержимое файла
            with open(filepath, 'rb') as file:
                content = file.read()

            # Отправляем заголовки
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()  # Завершение формирования заголовков ответа

            # Отправляем содержимое файла
            self.wfile.write(bytes(content))
        except Exception as e:
            # Обрабатываем ошибки
            self.send_error(500, f"Server Error: {e}")




if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")













#
#
# class MyServer(BaseHTTPRequestHandler):
#     """
#         Специальный класс, который отвечает за
#         обработку входящих запросов от клиентов
#     """
#     def do_GET(self):
#
#         if self.path == "/":
#             self.serve_file("main.html")
#         elif self.path == "/catalog":
#             self.serve_file("catalog.html")
#         elif self.path == "/category_1":
#             self.serve_file("category_1.html")
#         elif self.path == "/contact":
#             self.serve_file("contact.html")
#
#
#         """ Метод для обработки входящих GET-запросов """
#         self.send_response(200) # Отправка кода ответа
#         self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
#         self.end_headers() # Завершение формирования заголовков ответа
#         with open('main.html', encoding='utf-8') as f:
#             my_data = f.read()
#             self.wfile.write(bytes(my_data, "utf-8")) # Тело ответа
#
# if __name__ == "__main__":
#     # Инициализация веб-сервера, который будет по заданным параметрах в сети
#     # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
#     webServer = HTTPServer((hostName, serverPort), MyServer)
#     print("Server started http://%s:%s" % (hostName, serverPort))
#
#     try:
#         # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
#         pass
#
#     # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
#     webServer.server_close()
#     print("Server stopped.")
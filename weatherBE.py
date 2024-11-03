from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from weatherFE import *
import requests

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.get_data)

    def get_data(self):
        city = self.ui.lineEdit.text()
        api_key = '92f8aaa04b1879d44dd100312b04796b'  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                self.ui.temp.setText(
                    f'Temperature: {temperature}°C\n'
                    f'Description: {weather_description}\n'
                    f'Humidity: {humidity}%\n'
                    f'Wind Speed: {wind_speed} m/s'
                )
                self.ui.city.setText("City: {}".format(city))
            else:
               self.ui.city.setText("City: {} Not found".format(city))
                
        except Exception as e:
            self.ui.temp.setText(f'Error: {str(e)}')


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())


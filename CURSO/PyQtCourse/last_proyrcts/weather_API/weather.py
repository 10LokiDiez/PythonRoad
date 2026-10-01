import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QLineEdit, QPushButton,QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityl = QLabel("Ingrese la ciudad: ", self)
        self.cityin = QLineEdit(self)
        self.getbutton = QPushButton("Acceder Clima", self)
        self.tempel = QLabel(self)
        self.emoji = QLabel(self)
        self.description = QLabel(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Clima App")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.cityl)
        vbox.addWidget(self.cityin)
        vbox.addWidget(self.getbutton)
        vbox.addWidget(self.tempel)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description)
        self.setLayout(vbox)
        
        self.cityl.setAlignment(Qt.AlignCenter)
        self.cityin.setAlignment(Qt.AlignCenter)
        self.tempel.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)
        
        self.cityl.setObjectName("citylabel")
        self.cityin.setObjectName("cityinput")
        self.getbutton.setObjectName("weatherbutton")
        self.tempel.setObjectName("temperature")
        self.emoji.setObjectName("emojilabel")
        self.description.setObjectName("description")
        
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Calibri;
            }               
            QLabel#citylabel{
                font-size:40px;
                font-style:italic;
            }
            QLineEdit#cityinput{
                font-size:40px;
                font-family: Century Gothic;
            }
            QPushButton#weatherbutton{
                font-size:30px;
                font-weight: bold;
            }
            QLabel#temperature{
                font-size:75px;
            }
            QLabel#emojilabel{
                font-size:100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description{
                font-size:50px;
            }
                           
            """)
        
        self.getbutton.clicked.connect(self.get_weather)
        
    def get_weather(self):
        api_key = "23ed78032bc101aa82f6c9627e6b6ad6"
        city = self.cityin.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as httpError:
            match response.status_code:
                case 400:
                    self.display_error("Consulta Erronea:\nPor favor revisa lo ingresado")
                case 401:
                    self.display_error("No autorizado:\nAPI invalida")
                case 403:
                    self.display_error("Denegado:\nEl acceso es negado")
                case 404:
                    self.display_error("No se encontro:\nLa ciudad no se encontro")
                case 500:
                    self.display_error("Error interno del Servidor:\nPor favor intentalo luego...")
                case 502:
                    self.display_error("Error en la puerta de entrada:\nNo hay respuesta del servidor")
                case 503:
                    self.display_error("Servicio deshabilitado:\nServido deshabilitado")
                case 504:
                    self.display_error("Tiempo de espera agotado:\nNo hay respuesta del servidor")
                case _:
                    self.display_error(f"Error HTTP ocurrio:\n {httpError}")
        except requests.exceptions.ConnectionError:
            self.display_error(f"Error de Conexion:\nRevisa tu internet")
        except requests.exceptions.Timeout:
            self.display_error(f"Tiempo de espera agotado")
        except requests.exceptions.TooManyRedirects:
            self.display_error(f"Muchas redirecciones:\nRevisa el URL")
        except requests.RequestException as reqer:
            self.display_error(f"Request Error:\n{reqer}")
        
    
    def display_error(self, message):
        self.tempel.setStyleSheet("font-size:30px;")
        self.tempel.setText(message)
        self.emoji.clear()
        self.description.clear()
    
    def display_weather(self, data):
        temperature_k = data['main']['temp']
        temp_c = temperature_k - 273.15
        self.tempel.setStyleSheet("font-size:75px;")
        weatherdes = data["weather"][0]["description"]
        self.description.setText(weatherdes)
        
        weatherid = data["weather"][0]["id"]
        self.emoji.setText(self.get_emoji(weatherid))
        self.tempel.setText(f"{temp_c:.0f}°")
    
    @staticmethod
    def get_emoji(weather_id):
        if 232 >= weather_id >=200:
            return "⛈️"
        elif 300<= weather_id <=321:
            return "🌦️"
        elif 500<= weather_id <=531:
            return "🌧️"
        elif 600<= weather_id <=622:
            return "❄️"
        elif 701<= weather_id <=741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌬️"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801<= weather_id <=804:
            return "☁️"
        else:
            return ""
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())
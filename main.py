from flask import Flask, render_template, request


app = Flask(__name__)

def get_weather_data(city: str):
    API_KEY = '959e43520afb37043f9b5cd615e0ccb1'
    idioma = 'es'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    r = request.get(url).json()
    print(r)
    return r

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        ciudad = request.form.get('txt_ciudad')
        if ciudad !='' :
            r = get_weather_data(ciudad)
            print('HOLA SOY UN POST', r)
            coor = r.get('coord', {})
            weather = r.get('weather')
            main = r.get('main', {})
            return render_template('index.html', weather=weather, ciudad=ciudad, coor=coor, main=main, by='Mariella Nay')
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5008)






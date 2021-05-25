from flask import Flask
from flask.globals import request
from PIL import Image
# from PIL import ImageEnhance
from PIL import ImageFilter
from io import BytesIO

from flask.helpers import send_file

#Intanciar la clase app 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world :D"


#Variable de entorno: almaceno información de manera global


#Cuadno vayas a esa ruta: Ejecuta ese metodo
# Es un URL dinámico
@app.route('/greeting/<nombre>', methods = ['GET'])
def greeting(nombre):
    return f'hello {nombre}'

@app.route('/sorteo/<nombre>/<number>')
def sorteo(nombre, number):
    return f'<b> {nombre}: </b> {number}'


# así buscaría: http://127.0.0.1:5000/search?q=autos
@app.route('/search')
def search():
    query = request.args.get('q')
    return f'search: {query}'


#Tomar una imagen y lo ha corado en varios
#http://localhost:5000/cat.jpg?width=150&height=150
@app.route('/cat.jpg')
def cat():
    width = request.args.get('width')
    height = request.args.get('height')

    size = (int(width), int(height))

    img = Image.open('gato.jpg')
    img2 = img.filter(ImageFilter.BLUR)

    # applier = ImageEnhance.Brightness(img)
    # img2 = applier.enhance(5)

    img2.thumbnail(size)
    img_io = BytesIO()
    img2.save(img_io, "JPEG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")
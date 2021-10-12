from html.entities import name2codepoint
from re import U
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

# 'postgresql://<usuario>:<contraseña>@<direccion de la db>:<puerto>/<nombre de la db>

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/tienda'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oqeyqjxvtgabsw:b725feeade390b604b07cc18aa8aee5156bd63e64a25b9d2f14f4ae82f30fd13@ec2-54-161-189-150.compute-1.amazonaws.com:5432/dfacl5b6rvkdn5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

# Importar los modelos

from models import Product, User  

# Crear esquema de la base de datos

db.create_all()
db.session.commit()

# Rutas de Páginas

@app.route("/")
def get_home():
    return render_template("index.html")

# Ruta para crear el usuario

@app.route("/registro")
def register():
    return render_template("registro.html")

@app.route("/create_user", methods=["POST"])
def create_user():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"] 

    user = User(name, email, password)
    db.session.add(user)
    db.session.commit()   

    return redirect(url_for("login")) 

# Ruta de logueo de usuario

@app.route('/ingreso')
def login():
  return render_template("ingreso.html")

@app.route('/check_user', methods=['POST'])
def check_user():
    email = request.form["email"]
    password = request.form["password"]
    user = User.query.filter(User.password==password,User.email==email)
    
    try:
        if(user[0] is not None):
            return redirect("/product")          

    except:
        return redirect("/registro")     
 
# Rutas para productos

@app.route("/product", methods=["GET", "POST"])
def crud_product():
    if request.method == "GET":
        return render_template("registro_pro.html")        
        
    elif request.method == "POST":

    # Registrar un producto

        request_data = request.form
        name = request_data["name"]
        brand = request_data["brand"]
        presentation = request_data["presentation"]
        category = request_data["category"]
        price = request_data["price"]
        amount = request_data["amount"]
        due_date = request_data["due_date"]
        income_type = request_data["income_type"]
        supplier = request_data["supplier"]
        location = request_data["location"]

        product = Product(name, brand, presentation, category, price, amount, due_date, income_type, supplier, location)
        db.session.add(product)
        db.session.commit()

        print("Nombre:" + name)
        print("Marca:" + brand)
        print("Presentación:" + presentation)
        print("Categoria:" + category)
        print("Precio:" + price)
        print("Cantidad:" + amount)
        print("Fecha de Vencimiento:" + due_date)
        print("Tipo de Ingreso:" + income_type)
        print("Proveedor:" + supplier)
        print("Ubicación:" + location)       
           
        return redirect("/product")

# Ruta para actualizar productos

@app.route('/doupdateproduct', methods=['POST'])
def doupdateproduct():
    if request.method == "POST":
        request_data = request.form        
        id = request_data['id']
        name = request_data["name"]
        brand = request_data["brand"]
        presentation = request_data["presentation"]
        category = request_data["category"]
        price = request_data["price"]
        amount = request_data["amount"]
        due_date = request_data["due_date"]
        income_type = request_data["income_type"]
        supplier = request_data["supplier"]
        location = request_data["location"]

        product = Product.query.get(int(id))
        product.name = name
        product.brand = brand
        product.presentation = presentation
        product.category = category
        product.price = price
        product.amount = amount
        product.due_date = due_date
        product.income_type = income_type
        product.supplier = supplier
        product.location = location
        
        db.session.commit()        

        return redirect("/updateproduct")

@app.route('/updateproduct', methods=['GET','POST'])
def update_product():
    if request.method == "GET":
        return render_template("form_actualizar_pro.html")

    elif request.method =="POST":        
        request_data = request.form
        name = request_data["name"]
        old_product = Product.query.filter_by(name=name).first()
        return render_template("actualizacion_pro.html", old_product=old_product)
     
    return redirect("/doupdateproduct")

# Ruta para consultar productos

@app.route('/getproduct')
def get_product():
    products = Product.query.all()
    print(products)
    return render_template("lista_producto.html", products=products)

# Ruta para eliminar productos

@app.route('/deleteproduct', methods=["GET", "POST"])
def delete_product():

    if request.method == "GET":
        return render_template("eliminacion_pro.html")

    elif request.method == "POST":    

        request_data = request.form
        name = request_data["name"]
        
        product = Product.query.filter_by(name=name).first()        
        db.session.delete(product)
        db.session.commit()

        return redirect("/deleteproduct")


if __name__ == "__main__":
    app.run()


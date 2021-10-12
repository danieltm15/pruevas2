from app import db

# Tabla Producto

class Product(db.Model):
    __tablename__ = 'Product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    brand = db.Column(db.String)
    presentation = db.Column(db.String)
    category = db.Column(db.String)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    due_date = db.Column(db.Date, nullable=True)
    income_type = db.Column(db.String)
    supplier = db.Column(db.String)
    location = db.Column(db.String)

    # constructor tabla producto

    def __init__(self,name,brand,presentation,category,price,amount,due_date,income_type,supplier,location):
        self.name = name
        self.brand = brand
        self.presentation = presentation
        self.category = category
        self.price = price
        self.amount = amount
        self.due_date = due_date
        self.income_type = income_type
        self.supplier = supplier
        self.location = location

# Tabla Administrador

class Administrator(db.Model):
    __tablename__ = 'Administrator'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # constructor tabla Administrador

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Tabla Cajero

class Cashier(db.Model):
    __tablename__ = 'Cashier'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # constructor tabla Cajero

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Tabla Factura de Venta

class Invoice(db.Model):
    __tablename__ = 'Invoice'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    amount = db.Column(db.Integer)
    unit_value = db.Column(db.Integer)
    total_value = db.Column(db.Integer)

    # constructor tabla Factura de Venta

    def __init__(self, date, amount, unit_value, total_value):
        self.date = date
        self.amount = amount
        self.unit_value = unit_value
        self.total_value = total_value

# Tabla Comprobante de Egreso

class Egress_invoice(db.Model):
    __tablename__ = 'Egress_invoice'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)    
    egress_type = db.Column(db.String)
    total_value = db.Column(db.Integer)

    # constructor tabla Comprobante de Egreso

    def __init__(self, date, egress_type, total_value):
        self.date = date
        self.egress_type = egress_type        
        self.total_value = total_value

# Tabla Usuarios

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # constructor tabla usuarios

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Tabla Inventario

class Inventory(db.Model):
    __tablename__ = 'Inventory'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.ForeignKey("Product.id"))
    quantity = db.Column(db.Integer)
    input_date = db.Column(db.Date)
    output_date = db.Column(db.Date)

    # constructor tabla inventario

    def __init__(self, product_id, quantity, input_date, output_date):
        self.product_id = product_id
        self.quantity = quantity
        self.input_date = input_date
        self.output_date = output_date

# Tabla Ingresos

class Incomes(db.Model):
    __tablename__ = 'Incomes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    product_id = db.Column(db.ForeignKey("Product.id"))
    quantity = db.Column(db.Integer)
    total_value = db.Column(db.Integer)
    invoice_id = db.Column(db.ForeignKey("Invoice.id"))

    # constructor tabla Ingresos

    def __init__(self, date, product_id, quantity, total_value, invoice_id):
        self.date = date
        self.product_id = product_id
        self.quantity = quantity
        self.total_value = total_value
        self.invoice_id = invoice_id

# Tabla Egresos

class Egress(db.Model):
    __tablename__ = 'Egress'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    egress_type = db.Column(db.String)    
    total_value = db.Column(db.Integer)
    egress_invoice_id = db.Column(db.ForeignKey("Egress_invoice.id"))
    

    # constructor tabla Egresos

    def __init__(self, date, egress_type, total_value, egress_invoice_id):
        self.date = date
        self.egress_type = egress_type        
        self.total_value = total_value
        self.egress_invoice_id = egress_invoice_id

# Tabla Reportes

class Reports(db.Model):
    __tablename__ = 'Reports'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.ForeignKey("User.id"))
    date = db.Column(db.Date)    
    report_type = db.Column(db.String)
    invoice_id = db.Column(db.ForeignKey("Invoice.id"), nullable=True)   
    contable_balance = db.Column(db.Integer)
    inventory_balance = db.Column(db.Integer)

    # constructor tabla Reportes

    def __init__(self, user_id, date, report_type, contable_balance, inventory_balance):
        self.user_id = user_id
        self.date = date
        self.report_type = report_type       
        self.contable_balance = contable_balance
        self.inventory_balance = inventory_balance

        

       


from flask import Flask, render_template, request, redirect, url_for
from static.model.pizza import Pizza
from static.model.topping import Topping
from static.model.order import Order
from static.model.sales import Sales

app = Flask(__name__)

order = Order()
sales = Sales()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order_page():
    if request.method == 'POST':
        pizza_name = request.form['pizza']
        pizza = Pizza(pizza_name.capitalize(), 8.00)
        
        if pizza_name == 'custom':
            pizza = Pizza("Custom Pizza", 5.00)

        toppings = request.form.getlist('toppings')
        for topping in toppings:
            if topping == 'extra_cheese':
                pizza.add_topping(Topping('Extra Cheese', 1.50))
            elif topping == 'mushrooms':
                pizza.add_topping(Topping('Mushrooms', 1.00))
            elif topping == 'peppers':
                pizza.add_topping(Topping('Peppers', 1.00))
        
        order.add_pizza(pizza)
        return redirect(url_for('order_page'))

    return render_template('order.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment_page():
    if request.method == 'POST':
        payment_method = request.form['payment_method']
        sales.record_sale(order)
        return redirect(url_for('index'))

    return render_template('payment.html', order_summary=str(order), total=order.get_total())

@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    summary = None
    if request.method == 'POST':
        password = request.form['password']
        if password == 'admin123':
            summary = sales.get_sales_summary()
    return render_template('admin.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

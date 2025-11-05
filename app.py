from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime
from expert_system import analyze_sales, recommend_car

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="558732",   
        database="car_sales_db"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC")
    sales = cursor.fetchall()
    cursor.close()
    conn.close()

    ai_insights = analyze_sales(sales)
    # By default no recommendation shown
    return render_template('index.html', sales=sales, ai_insights=ai_insights, recommendation=None)

@app.route('/add', methods=['POST'])
def add_sale():
    customer = request.form['customer']
    car_model = request.form['car_model']
    price = request.form['price']
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sales (customer_name, car_model, price, sale_date)
        VALUES (%s, %s, %s, %s)
    """, (customer, car_model, price, date))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_sale(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sales WHERE sale_id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_sale(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        customer = request.form['customer']
        car_model = request.form['car_model']
        price = request.form['price']

        cursor.execute("""
            UPDATE sales
            SET customer_name=%s, car_model=%s, price=%s
            WHERE sale_id=%s
        """, (customer, car_model, price, id))

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM sales WHERE sale_id=%s", (id,))
        sale = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('edit.html', sale=sale)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Read form input
    budget = request.form.get('budget')
    purpose = request.form.get('purpose')
    fuel = request.form.get('fuel')

    # Get recommendation from expert system
    recommendation = recommend_car(budget, purpose, fuel)

    # Re-fetch sales & insights to render the same dashboard
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sales ORDER BY sale_id DESC")
    sales = cursor.fetchall()
    cursor.close()
    conn.close()

    ai_insights = analyze_sales(sales)
    return render_template('index.html', sales=sales, ai_insights=ai_insights, recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)

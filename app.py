from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

# Function to get stock prices

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period='2d')["Close"]
    current_price = price.iloc[-1]
    previous_price = price.iloc[-2]
    change = "up" if current_price > previous_price else "down"
    return round(current_price, 2), change

# Home page

@app.route("/")
def index():
    vas_price, vas_change = get_stock_price("VAS.AX")
    vgs_price, vgs_change = get_stock_price("VGS.AX")
    return render_template("index.html", vas_price=vas_price, vas_change=vas_change, vgs_price=vgs_price, vgs_change=vgs_change)

if __name__ == '__main__':
    app.run(debug=True)
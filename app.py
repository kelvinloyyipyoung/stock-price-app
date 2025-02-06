from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

# Function to get stock prices

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period='1d')["Close"].iloc[-1]
    return round(price, 2)

@app.route("/")
def index():
    vas_price = get_stock_price("VAS.AX")
    vgs_price = get_stock_price("VGS.AX")
    return render_template("index.html", vas_price=vas_price, vgs_price=vgs_price)


if __name__ == "__main__":
    app.run(debug=True)

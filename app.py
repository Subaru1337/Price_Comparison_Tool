from flask import Flask, render_template, request
import amazon_price
import flipkart_price
from ebay_scraper import scrape_cheapest_product

app = Flask(__name__)


@app.route('/')
def index():
    # Render the index page for user input
    return render_template('index.html')


@app.route('/compare', methods=['POST'])
def compare_prices():
    # Get the user's input from the form
    product_name = request.form['product_name']

    # Get prices from all three platforms
    amazon_result = amazon_price.amazon(product_name)
    flipkart_result = flipkart_price.get_price(product_name)
    ebay_result = scrape_cheapest_product(product_name)

    # Format results
    amazon_price_display = None
    amazon_link = None
    if amazon_result:
        amazon_price_display = f"{product_name}: ₹{amazon_result['price']}"
        amazon_link = amazon_result['url']

    flipkart_price_display = None
    flipkart_link = None
    if flipkart_result:
        flipkart_price_display = flipkart_result['price']
        flipkart_link = flipkart_result['url']

    ebay_price_display = None
    ebay_link = None
    if ebay_result:
        ebay_price_display = f"{product_name}: ${ebay_result['price']}"
        ebay_link = ebay_result['link']

    # Pass data to the template for display
    return render_template('index.html', 
                         amazon_price=amazon_price_display,
                         amazon_link=amazon_link,
                         flipkart_price=flipkart_price_display,
                         flipkart_link=flipkart_link,
                         ebay_price=ebay_price_display,
                         ebay_link=ebay_link)


if __name__ == '__main__':
    app.run(debug=True)

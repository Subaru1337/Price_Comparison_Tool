# Price Comparison Web Application

## Overview

This project is a **Price Comparison Web Application** built using the **Flask** web framework in Python. The application allows users to input a product name and receive price comparisons from three major e-commerce platforms:

* **Amazon** (India)
* **Flipkart** (India)
* **eBay** (International)

The app scrapes or fetches the prices and links to the cheapest or relevant products from these platforms and displays them side by side, helping users make informed purchase decisions easily without visiting multiple sites.



## Features

* User-friendly web interface to input product queries.
* Real-time price fetching from Amazon, Flipkart, and eBay.
* Display of product prices with direct clickable links to the product pages.
* Supports price display in INR (₹) for Amazon and Flipkart, and USD (\$) for eBay.
* Clean and responsive UI using HTML templates.
* Error handling for products not found or unavailable prices.



## How It Works

1. **User Input**: The user enters the product name they want to search for on the homepage.
2. **Backend Processing**: Upon submitting the form:

   * The Flask app invokes scraping or API functions from three modules:

     * `amazon_price.amazon(product_name)`
     * `flipkart_price.get_price(product_name)`
     * `ebay_scraper.scrape_cheapest_product(product_name)`
   * These functions return price and product URL details.
3. **Data Rendering**: The app formats the results and sends them back to the same webpage.
4. **User Output**: The page updates to show prices and links from all three platforms for easy comparison.


## Project Structure

```
price-comparison-app/
│
├── app.py                      # Main Flask application file
├── templates/
│   └── index.html              # HTML template for the front-end
├── amazon_price.py             # Module to scrape Amazon product prices
├── flipkart_price.py           # Module to scrape Flipkart product prices
├── ebay_scraper.py             # Module to scrape eBay product prices
├── static/                     # Folder for CSS, JS, and images (if any)
└── README.md                   # Project documentation (this file)
```

---

## Technologies Used

* **Python 3.x**
* **Flask** – Lightweight web framework for Python
* **Requests** – For HTTP requests to scrape data
* **BeautifulSoup4** – For parsing HTML content from the e-commerce websites
* **HTML/CSS** – Frontend rendering via Jinja2 templates in Flask

---

## Setup & Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/price-comparison-app.git
cd price-comparison-app
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install required packages:**

```bash
pip install -r requirements.txt
```

4. **Run the Flask application:**

```bash
python app.py
```

5. **Access the app:**

Open your web browser and navigate to `http://127.0.0.1:5000/`

---

## Usage

* Enter the product name you want to search for (e.g., "smartphone", "headphones", "laptop").
* Click the **Compare** button.
* The page will display the prices from Amazon, Flipkart, and eBay along with clickable links to the product pages.
* If any platform does not have the product or price data, it will be indicated accordingly.

---

## Important Notes

* **Scraping Restrictions**: The scraping modules (`amazon_price.py`, `flipkart_price.py`, `ebay_scraper.py`) depend on the current structure of the websites and may break if the websites update their layout.
* **Legal Considerations**: Always ensure your scraping activities comply with the respective website's Terms of Service.
* **Currency Differences**: Prices from eBay are shown in USD, while Amazon and Flipkart show prices in INR.
* **Limited Scope**: This project is a basic price comparison tool designed for educational purposes and might not include all edge cases or extensive error handling.

---

## Future Enhancements

* Add support for more e-commerce platforms like Snapdeal, Paytm Mall, etc.
* Implement user login and saved searches.
* Add sorting/filtering options based on price, rating, or seller.
* Deploy the app on cloud platforms like Heroku or AWS.
* Use official APIs (if available) instead of web scraping for better reliability.
* Integrate caching to reduce scraping frequency and improve speed.

---

## Acknowledgments

* Inspired by various price comparison websites and open-source scraping projects.
* Thanks to the creators of Flask, Requests, and BeautifulSoup for enabling easy web scraping and app development.
* Special thanks to the online developer communities for troubleshooting and guidance.

---

## Contact

For questions or contributions, please contact:

* Your Name: [Varad Mhatre](betatester013370@gmail.com)
* GitHub: [Subaru1337](https://github.com/Subaru1337)

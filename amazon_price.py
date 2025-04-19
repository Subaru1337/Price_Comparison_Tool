from bs4 import BeautifulSoup
import requests

# Headers for making requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

# Global variable to store the Amazon URL
amazon_url = None

# Amazon price extraction function
def amazon(name):
    try:
        global amazon_url
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon_url = f'https://www.amazon.in/s?k={name2}'
        res = requests.get(amazon_url, headers=headers)
        print("\nSearching in Amazon...")
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Find the first product that matches the search term
        products = soup.select('.s-result-item')
        for product in products:
            try:
                title = product.select_one('.a-text-normal').getText().strip()
                price = product.select_one('.a-price-whole')
                link = product.select_one('a.a-link-normal')
                
                if price and link and name.lower() in title.lower():
                    return {
                        'price': price.getText().strip(),
                        'url': 'https://www.amazon.in' + link['href'] if link['href'].startswith('/') else link['href']
                    }
            except:
                continue
                
        return None
    except Exception as e:
        print(f"Error in Amazon search: {str(e)}")
        return None

# Convert price format function
def convert(a):
    b = a.replace(" ", '')
    c = b.replace("INR", '')
    d = c.replace(",", '')
    f = d.replace("₹", '')
    g = int(float(f))
    return g

# Compare prices function (only Amazon price)
def compare_prices():
    name = input("Product Name:\n")
    result = amazon(name)

    if result:
        print("\nAmazon price: ₹", result['price'])
        print("URL: ", result['url'])
    else:
        print("Amazon: No product found!")

    print(
        "---------------------------------------------------------URLs--------------------------------------------------------------")
    print("Amazon : \n", amazon_url)
    print(
        "---------------------------------------------------------------------------------------------------------------------------")

# amazon_price.py
def get_price(product_name):
    result = amazon(product_name)
    if result:
        return f"{product_name}: ₹{result['price']}"
    return None

if __name__ == "__main__":
    compare_prices()

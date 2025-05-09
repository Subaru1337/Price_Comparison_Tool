# Price Comparison Tool

A web-based tool that compares product prices across multiple e-commerce platforms including Amazon, Flipkart, and eBay.

## Features

- Real-time price comparison across multiple platforms
- Direct links to product pages
- Clean and intuitive user interface
- Accurate product matching
- Filters out accessories and irrelevant items

## Technologies Used

- Python
- Flask (Web Framework)
- BeautifulSoup4 (Web Scraping)
- Requests (HTTP Library)
- Bootstrap (Frontend Framework)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd price-comparison-tool
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
- Create a `.env` file in the root directory
- Add your ScraperAPI key:
```
SCRAPER_API_KEY=your_api_key_here
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter the product name you want to compare
4. View the prices from different platforms
5. Click on the links to visit the product pages

## Project Structure

```
price-comparison-tool/
├── app.py                 # Main Flask application
├── amazon_price.py        # Amazon price scraper
├── flipkart_price.py      # Flipkart price scraper
├── ebay_scraper.py        # eBay price scraper
├── requirements.txt       # Project dependencies
├── templates/
│   └── index.html         # Main web interface
└── README.md              # Project documentation
```

## Features in Detail

### Price Comparison
- Compares prices across Amazon, Flipkart, and eBay
- Shows the most relevant products
- Filters out accessories and unrelated items

### User Interface
- Clean and modern design
- Responsive layout
- Easy-to-use search functionality
- Clear price display
- Direct links to product pages

### Scraping Capabilities
- Handles different product formats
- Manages rate limiting
- Implements error handling
- Uses rotating user agents
- Bypasses common anti-scraping measures

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Web scraping library
- [Bootstrap](https://getbootstrap.com/) - Frontend framework

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Future Improvements

- Add more e-commerce platforms
- Implement price history tracking
- Add price alerts
- Include product specifications comparison
- Add user accounts for saving searches
- Implement API endpoints for programmatic access #   P r i c e _ C o m p a r i s o n _ T o o l 
 
 

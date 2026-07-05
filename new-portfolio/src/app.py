from flask import Flask, render_template, make_response
from bs4 import BeautifulSoup
import requests
import csv
import io
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html') 

@app.route('/scraping')
def scraping():
    return render_template('scraping.html')

@app.route('/scraping/static')
def static_scraping():
    return render_template('static_scraping.html')

@app.route('/scraping/api')
def api_scraping():
    return render_template('api_scraping.html')
@app.route('/scraping/static/books')
def books_to_scrape():
    # URL of the practice scraping site
    url = "https://books.toscrape.com/"
    
    # Live scraping execution
    scraped_books = []
    try:
        # 1. Fetch the raw HTML content of the website
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # 2. Parse the raw HTML with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 3. Target the specific product article elements
            book_elements = soup.find_all('article', class_='product_pod')
            
            for index, book in enumerate(book_elements, start=1):
                # Extract title from the image tag alt attribute or link title attribute
                title = book.h3.a['title']
                
                # Extract price text string
                price = book.find('p', class_='price_color').text
                
                # Extract rating status from class names (e.g., class="star-rating Three")
                rating_classes = book.find('p', class_='star-rating')['class']
                rating = rating_classes[1] if len(rating_classes) > 1 else "Unknown"
                
                # Extract availability text wrapper status
                availability = book.find('p', class_='instock availability').text.strip()
                
                # Form structure to ship directly into your templates dashboard
                scraped_books.append({
                    "id": index,
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "availability": availability
                })
    except Exception as e:
        print(f"Scraping error occurred: {e}")
        # Fallback empty state array if site is down or network disconnects
        scraped_books = []

    # Ship data live to the frontend page container layout
    return render_template('books_data.html', books=scraped_books)

@app.route('/notebook/<path:notebook_name>')
def notebook_view(notebook_name):
    notebook_mapping = {
        'books-to-scrape': 'notebooks/Books to scrap.ipynb',
        'amazon': 'notebooks/Web Scrapping Amazon Laptops .ipynb',
        'quotes-to-scrape': 'notebooks/Quotes To Scrape.ipynb',
        'old-reddit': 'notebooks/old reddit (1) (1).ipynb',
        'goodreads': 'notebooks/Goodreads.ipynb',
        'gyansetu-codroidhub': 'notebooks/Gyansetu Codroidhub.ipynb',
        'github': 'notebooks/GitHub.ipynb',
        'openweather': 'notebooks/OpenWeather.ipynb',
        'nasa': 'notebooks/NASA.ipynb',
        'news': 'notebooks/News.ipynb',
        'nike': 'notebooks/Nike.ipynb',
        'flipkart': 'notebooks/Flipkart.ipynb',
        'amazon-dynamic': 'notebooks/Amazon Dynamic.ipynb',
        'imdb': 'notebooks/IMDb.ipynb',
        'bbc': 'notebooks/BBC.ipynb'
    }
    
    notebook_path = notebook_mapping.get(notebook_name, 'notebooks/Books to scrap.ipynb')
    notebook_display_name = notebook_name.replace('-', ' ').title()
    return render_template('notebook_view.html', notebook_name=notebook_display_name, notebook_path=notebook_path)

# Helper function to generate CSV response
def generate_csv_response(filename, headers, data):
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(headers)
    writer.writerows(data)
    
    response = make_response(output.getvalue())
    response.headers['Content-Disposition'] = f'attachment; filename={filename}'
    response.headers['Content-type'] = 'text/csv'
    return response

# Dynamic Scraping Route
@app.route('/scraping/dynamic')
def dynamic_scraping():
    return render_template('dynamic_scraping.html')

# API Scraping Project Routes (Generate CSV)
@app.route('/scraping/api/gyansetu')
def api_gyansetu():
    headers = ['ID', 'Course Name', 'Instructor', 'Duration', 'Price']
    data = [
        [1, 'Python for Beginners', 'John Doe', '40 Hours', '$49'],
        [2, 'Web Development Bootcamp', 'Jane Smith', '60 Hours', '$99'],
        [3, 'Data Science Fundamentals', 'Bob Wilson', '50 Hours', '$79'],
        [4, 'Machine Learning Basics', 'Alice Brown', '45 Hours', '$89'],
        [5, 'Cybersecurity Essentials', 'Charlie Davis', '35 Hours', '$59']
    ]
    return generate_csv_response('gyansetu-codroidhub.csv', headers, data)

@app.route('/scraping/api/github')
def api_github():
    headers = ['ID', 'Repository Name', 'Owner', 'Stars', 'Forks', 'Language']
    data = [
        [1, 'flask', 'pallets', 66000, 16000, 'Python'],
        [2, 'tensorflow', 'tensorflow', 180000, 89000, 'Python'],
        [3, 'react', 'facebook', 220000, 45000, 'JavaScript'],
        [4, 'node', 'nodejs', 100000, 28000, 'JavaScript'],
        [5, 'pandas', 'pandas-dev', 42000, 17000, 'Python']
    ]
    return generate_csv_response('github.csv', headers, data)

@app.route('/scraping/api/openweather')
def api_openweather():
    headers = ['ID', 'City', 'Country', 'Temperature (°C)', 'Humidity (%)', 'Weather']
    data = [
        [1, 'New York', 'US', 22, 65, 'Partly Cloudy'],
        [2, 'London', 'UK', 18, 70, 'Rainy'],
        [3, 'Tokyo', 'JP', 25, 55, 'Sunny'],
        [4, 'Paris', 'FR', 20, 60, 'Cloudy'],
        [5, 'Sydney', 'AU', 16, 75, 'Windy']
    ]
    return generate_csv_response('openweather.csv', headers, data)

@app.route('/scraping/api/nasa')
def api_nasa():
    headers = ['ID', 'Date', 'Title', 'Explanation', 'Image URL']
    data = [
        [1, '2026-07-01', 'The Sombrero Galaxy', 'A spiral galaxy in the constellation Virgo', 'https://apod.nasa.gov/apod/image/2607/sombrero.jpg'],
        [2, '2026-06-30', 'Mars Rover Curiosity', 'Selfie from the Red Planet', 'https://apod.nasa.gov/apod/image/2606/curiosity.jpg'],
        [3, '2026-06-29', 'Andromeda Galaxy', 'Our nearest galactic neighbor', 'https://apod.nasa.gov/apod/image/2606/andromeda.jpg'],
        [4, '2026-06-28', 'Orion Nebula', 'Stellar nursery in Orion', 'https://apod.nasa.gov/apod/image/2606/orion.jpg'],
        [5, '2026-06-27', 'Jupiter and Its Moons', 'Gas giant and its Galilean satellites', 'https://apod.nasa.gov/apod/image/2606/jupiter.jpg']
    ]
    return generate_csv_response('nasa.csv', headers, data)

@app.route('/scraping/api/news')
def api_news():
    headers = ['ID', 'Title', 'Source', 'Published Date', 'URL']
    data = [
        [1, 'Tech Giants Announce New AI Features', 'TechCrunch', '2026-07-02', 'https://techcrunch.com/news1'],
        [2, 'Global Climate Summit Reaches Agreement', 'BBC News', '2026-07-01', 'https://bbc.com/news2'],
        [3, 'SpaceX Launches New Satellite Constellation', 'Space.com', '2026-06-30', 'https://space.com/news3'],
        [4, 'Breakthrough in Renewable Energy Storage', 'CNN Business', '2026-06-29', 'https://cnn.com/news4'],
        [5, 'New Medical Treatment Shows Promise', 'Healthline', '2026-06-28', 'https://healthline.com/news5']
    ]
    return generate_csv_response('news.csv', headers, data)

# Dynamic Scraping Project Routes
@app.route('/scraping/dynamic/nike')
def dynamic_nike():
    products = [
        {"id": 1, "name": "Air Max 90", "category": "Shoes", "price": "$120", "color": "White/Black", "availability": "In Stock"},
        {"id": 2, "name": "Air Jordan 1", "category": "Shoes", "price": "$170", "color": "Red/Black", "availability": "Limited Stock"},
        {"id": 3, "name": "Dri-FIT T-Shirt", "category": "Apparel", "price": "$35", "color": "Blue", "availability": "In Stock"},
        {"id": 4, "name": "Tech Fleece Hoodie", "category": "Apparel", "price": "$85", "color": "Gray", "availability": "In Stock"},
        {"id": 5, "name": "Zoom Pegasus 40", "category": "Shoes", "price": "$130", "color": "Black", "availability": "Out of Stock"},
        {"id": 6, "name": "Nike Air Force 1 '07", "category": "Shoes", "price": "$115", "color": "White", "availability": "In Stock"},
        {"id": 7, "name": "Nike Pro Leggings", "category": "Apparel", "price": "$55", "color": "Black", "availability": "In Stock"},
        {"id": 8, "name": "Nike Dunk Low", "category": "Shoes", "price": "$110", "color": "White/Green", "availability": "Limited Stock"},
        {"id": 9, "name": "Nike Windrunner Jacket", "category": "Apparel", "price": "$100", "color": "Navy", "availability": "In Stock"},
        {"id": 10, "name": "Nike React Infinity Run", "category": "Shoes", "price": "$160", "color": "Blue/White", "availability": "In Stock"}
    ]
    return render_template('nike_data.html', products=products)

@app.route('/scraping/dynamic/flipkart')
def dynamic_flipkart():
    products = [
        {"id": 1, "name": "iPhone 15 Pro", "category": "Electronics", "price": "₹134,999", "rating": "4.7", "reviews": "12,500"},
        {"id": 2, "name": "Samsung Galaxy S24", "category": "Electronics", "price": "₹99,999", "rating": "4.6", "reviews": "9,800"},
        {"id": 3, "name": "Dell XPS 15", "category": "Laptops", "price": "₹119,990", "rating": "4.5", "reviews": "5,600"},
        {"id": 4, "name": "Sony WH-1000XM5", "category": "Audio", "price": "₹29,990", "rating": "4.8", "reviews": "18,000"},
        {"id": 5, "name": "LG OLED C3", "category": "TVs", "price": "₹149,990", "rating": "4.7", "reviews": "8,900"},
        {"id": 6, "name": "OnePlus 12", "category": "Electronics", "price": "₹64,999", "rating": "4.6", "reviews": "7,200"},
        {"id": 7, "name": "HP Spectre x360", "category": "Laptops", "price": "₹99,999", "rating": "4.4", "reviews": "4,100"},
        {"id": 8, "name": "Apple AirPods Pro 2", "category": "Audio", "price": "₹24,990", "rating": "4.8", "reviews": "22,000"},
        {"id": 9, "name": "Samsung 65-inch QLED TV", "category": "TVs", "price": "₹129,990", "rating": "4.6", "reviews": "6,500"},
        {"id": 10, "name": "Mi 14", "category": "Electronics", "price": "₹49,999", "rating": "4.5", "reviews": "5,800"}
    ]
    return render_template('flipkart_data.html', products=products)

@app.route('/scraping/dynamic/amazon')
def dynamic_amazon():
    products = [
        {"id": 1, "name": "Echo Dot (5th Gen)", "category": "Smart Home", "price": "$49.99", "rating": "4.6", "prime": "Yes"},
        {"id": 2, "name": "Kindle Paperwhite", "category": "Electronics", "price": "$139.99", "rating": "4.7", "prime": "Yes"},
        {"id": 3, "name": "Fire TV Stick 4K", "category": "Streaming", "price": "$49.99", "rating": "4.5", "prime": "Yes"},
        {"id": 4, "name": "Instant Pot Duo", "category": "Kitchen", "price": "$89.99", "rating": "4.7", "prime": "Yes"},
        {"id": 5, "name": "Anker PowerCore 20000", "category": "Accessories", "price": "$39.99", "rating": "4.8", "prime": "Yes"},
        {"id": 6, "name": "Apple iPad 10th Gen", "category": "Electronics", "price": "$329.00", "rating": "4.7", "prime": "Yes"},
        {"id": 7, "name": "Logitech MX Master 3S", "category": "Accessories", "price": "$99.99", "rating": "4.8", "prime": "Yes"},
        {"id": 8, "name": "Ninja Air Fryer Max XL", "category": "Kitchen", "price": "$149.99", "rating": "4.7", "prime": "Yes"},
        {"id": 9, "name": "Sony PS5 DualSense Controller", "category": "Gaming", "price": "$69.99", "rating": "4.6", "prime": "Yes"},
        {"id": 10, "name": "Bose QuietComfort Ultra", "category": "Audio", "price": "$379.00", "rating": "4.7", "prime": "Yes"}
    ]
    return render_template('amazon_dynamic_data.html', products=products)

@app.route('/scraping/dynamic/imdb')
def dynamic_imdb():
    movies = [
        {"id": 1, "title": "The Shawshank Redemption", "year": 1994, "rating": "9.7", "genre": "Drama", "director": "Frank Darabont"},
        {"id": 2, "title": "The Godfather", "year": 1972, "rating": "9.2", "genre": "Crime/Drama", "director": "Francis Ford Coppola"},
        {"id": 3, "title": "The Dark Knight", "year": 2008, "rating": "9.0", "genre": "Action/Thriller", "director": "Christopher Nolan"},
        {"id": 4, "title": "Pulp Fiction", "year": 1994, "rating": "8.9", "genre": "Crime/Drama", "director": "Quentin Tarantino"},
        {"id": 5, "title": "Inception", "year": 2010, "rating": "8.8", "genre": "Sci-Fi/Thriller", "director": "Christopher Nolan"},
        {"id": 6, "title": "Schindler's List", "year": 1993, "rating": "9.0", "genre": "Biography/Drama", "director": "Steven Spielberg"},
        {"id": 7, "title": "The Lord of the Rings: Return of the King", "year": 2003, "rating": "9.0", "genre": "Adventure/Fantasy", "director": "Peter Jackson"},
        {"id": 8, "title": "Forrest Gump", "year": 1994, "rating": "8.8", "genre": "Drama/Romance", "director": "Robert Zemeckis"},
        {"id": 9, "title": "Fight Club", "year": 1999, "rating": "8.8", "genre": "Drama/Thriller", "director": "David Fincher"},
        {"id": 10, "title": "Interstellar", "year": 2014, "rating": "8.7", "genre": "Adventure/Sci-Fi", "director": "Christopher Nolan"}
    ]
    return render_template('imdb_data.html', movies=movies)

@app.route('/scraping/dynamic/bbc')
def dynamic_bbc():
    articles = [
        {"id": 1, "headline": "World Leaders Meet for Economic Summit", "category": "Politics", "date": "2026-07-02", "author": "Sarah Johnson"},
        {"id": 2, "headline": "Record Temperatures Hit Southern Europe", "category": "Weather", "date": "2026-07-01", "author": "Michael Chen"},
        {"id": 3, "headline": "Premier League Season Kicks Off This Weekend", "category": "Sports", "date": "2026-06-30", "author": "David Williams"},
        {"id": 4, "headline": "New Study Reveals Climate Change Impact", "category": "Science", "date": "2026-06-29", "author": "Emma Davis"},
        {"id": 5, "headline": "Award-Winning Film Opens in Theaters", "category": "Entertainment", "date": "2026-06-28", "author": "Lisa Rodriguez"},
        {"id": 6, "headline": "Tech Giant Unveils New AI Features at Annual Conference", "category": "Technology", "date": "2026-06-27", "author": "James Wilson"},
        {"id": 7, "headline": "Healthcare Workers Receive New Training Program", "category": "Health", "date": "2026-06-26", "author": "Maria Garcia"},
        {"id": 8, "headline": "Space Agency Announces New Mars Mission Plans", "category": "Science", "date": "2026-06-25", "author": "Tom Anderson"},
        {"id": 9, "headline": "Stock Markets Rally After Positive Economic Data", "category": "Business", "date": "2026-06-24", "author": "Jennifer Lee"},
        {"id": 10, "headline": "New Museum Exhibition Celebrates Local Artists", "category": "Arts", "date": "2026-06-23", "author": "Robert Brown"}
    ]
    return render_template('bbc_news_data.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
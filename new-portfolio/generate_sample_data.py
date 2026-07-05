import pandas as pd
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# 1. Books to Scrape
books_data = {
    "title": [
        "A Light in the Attic",
        "Tipping the Velvet",
        "Soumission",
        "Sharp Objects",
        "Sapiens: A Brief History of Humankind"
    ],
    "price": ["£51.77", "£53.74", "£50.10", "£47.82", "£54.23"],
    "rating": ["Three", "One", "One", "Four", "Five"],
    "availability": ["In stock (22 available)"] * 5
}
pd.DataFrame(books_data).to_csv('data/books_to_scrape.csv', index=False)

# 2. Amazon Laptops
amazon_data = {
    "laptop_name": [
        "Dell Inspiron 15 3000",
        "HP Pavilion 14",
        "Lenovo ThinkPad X1 Carbon",
        "Apple MacBook Air 13",
        "ASUS ROG Strix G15"
    ],
    "price": ["$599.99", "$699.99", "$1299.99", "$999.99", "$1199.99"],
    "rating": [4.2, 4.5, 4.8, 4.7, 4.6],
    "reviews": [1234, 890, 567, 2345, 789]
}
pd.DataFrame(amazon_data).to_csv('data/amazon_laptops.csv', index=False)

# 3. Quotes to Scrape
quotes_data = {
    "quote": [
        "The world as we have created it is a process of our thinking.",
        "It is our choices, Harry, that show what we truly are.",
        "There are only two ways to live your life. One is as though nothing is a miracle.",
        "The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.",
        "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring."
    ],
    "author": [
        "Albert Einstein",
        "J.K. Rowling",
        "Albert Einstein",
        "Jane Austen",
        "Marilyn Monroe"
    ],
    "tags": [
        "change,deep-thoughts,thinking,world",
        "abilities,choices",
        "inspirational,life,live,miracle,miracles",
        "aliteracy,books,classic,humor",
        "be-yourself,inspirational"
    ]
}
pd.DataFrame(quotes_data).to_csv('data/quotes_to_scrape.csv', index=False)

# 4. Old Reddit
reddit_data = {
    "post_title": [
        "Just finished my first Python project!",
        "How to get started with web scraping?",
        "What's your favorite data science library?",
        "Best practices for GitHub repositories",
        "New to cybersecurity, where to begin?"
    ],
    "author": ["tech_newbie", "scraper101", "data_wizard", "git_guru", "cyber_beginner"],
    "score": [1500, 230, 890, 456, 789],
    "comments": [123, 45, 89, 56, 78]
}
pd.DataFrame(reddit_data).to_csv('data/old_reddit.csv', index=False)

# 5. Goodreads
goodreads_data = {
    "book_title": [
        "The Great Gatsby",
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Hunger Games"
    ],
    "author": ["F. Scott Fitzgerald", "Harper Lee", "George Orwell", "Jane Austen", "Suzanne Collins"],
    "rating": [3.91, 4.28, 4.19, 4.28, 4.33],
    "reviews": ["3,000,000+", "4,500,000+", "4,000,000+", "3,500,000+", "6,000,000+"]
}
pd.DataFrame(goodreads_data).to_csv('data/goodreads.csv', index=False)

# 6. Gyansetu Codroidhub
gyansetu_data = {
    "course_title": [
        "Python for Beginners",
        "Web Development with Django",
        "Machine Learning Fundamentals",
        "Data Structures & Algorithms",
        "Cybersecurity Essentials"
    ],
    "instructor": ["Dr. Sharma", "Prof. Verma", "Dr. Singh", "Prof. Patel", "Dr. Gupta"],
    "duration": ["4 weeks", "6 weeks", "8 weeks", "10 weeks", "5 weeks"],
    "students": [1500, 2300, 1800, 3200, 2100]
}
pd.DataFrame(gyansetu_data).to_csv('data/gyansetu_codroidhub.csv', index=False)

# 7. GitHub
github_data = {
    "repo_name": [
        "awesome-python",
        "tensorflow",
        "django",
        "pandas",
        "requests"
    ],
    "owner": ["vinta", "tensorflow", "django", "pandas-dev", "psf"],
    "stars": [170000, 180000, 75000, 42000, 50000],
    "forks": [22000, 85000, 30000, 17000, 9500]
}
pd.DataFrame(github_data).to_csv('data/github_repos.csv', index=False)

# 8. OpenWeather
weather_data = {
    "city": ["New York", "London", "Tokyo", "Paris", "Sydney"],
    "temperature": [22.5, 18.0, 28.0, 21.5, 15.0],
    "humidity": [65, 70, 80, 55, 60],
    "weather_condition": ["Partly Cloudy", "Rainy", "Sunny", "Clear", "Windy"]
}
pd.DataFrame(weather_data).to_csv('data/openweather.csv', index=False)

# 9. NASA
nasa_data = {
    "apod_date": ["2026-07-01", "2026-06-30", "2026-06-29", "2026-06-28", "2026-06-27"],
    "title": [
        "The Sombrero Galaxy",
        "Curiosity Rover Selfie",
        "Aurora Australis",
        "Saturn's Rings",
        "Andromeda Galaxy"
    ],
    "explanation": ["A beautiful spiral galaxy", "Mars rover on red planet", "Southern lights", "Planetary rings", "Neighbor galaxy"],
    "url": ["https://apod.nasa.gov"] * 5
}
pd.DataFrame(nasa_data).to_csv('data/nasa_apod.csv', index=False)

# 10. News
news_data = {
    "headline": [
        "AI Breakthrough: New Model Achieves Human-Level Performance",
        "Global Climate Summit Reaches Historic Agreement",
        "SpaceX Launches Next-Gen Satellite Constellation",
        "New Medical Treatment Shows Promise for Rare Disease",
        "Tech Giant Unveils Revolutionary Product"
    ],
    "source": ["TechCrunch", "BBC News", "Reuters", "CNN Health", "The Verge"],
    "published_at": ["2026-07-01", "2026-06-30", "2026-06-29", "2026-06-28", "2026-06-27"],
    "url": ["https://newsapi.org"] * 5
}
pd.DataFrame(news_data).to_csv('data/news_headlines.csv', index=False)

print("✅ All sample CSV files generated successfully in 'data' folder!")

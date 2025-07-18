import os, requests, dotenv

dotenv.load_dotenv()

NEWS_API = os.getenv("NEWS_API")
STOCK_API = os.getenv("STOCK_API")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": STOCK_API,
}

from_ = ""
to_ = ""

try:
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    stock_data = response.json()
    last_two = stock_data
    stocks = stock_data["Time Series (Daily)"]
    two_stocks = list(stocks.items())[:2]
    
    from_ = two_stocks[1][0]
    to_ = two_stocks[0][0]
    
    yes = two_stocks[0][-1]["4. close"]
    pre = two_stocks[1][-1]["4. close"]
    
    # difference and percentage calculation
    difference = float(yes) - float(pre)
    percentage = (difference / float(yes)) * 100
    
    # upper triangle symbol for positive and negative changes
    symbol = "🔼 " if difference > 0 else "🔽 "
    p_symbol = "🔼 " if percentage > 0 else "🔽"
    
    print(f"Difference: {symbol}{abs(difference):.2f}")
    print(f"Percentage: {p_symbol}{abs(percentage):.2f}%")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching stock data: {e}")


# from_ = "2025-07-12"  # Example date, adjust as needed
# to_ = "2025-07-11"    # Example date, adjust as needed
news_params = {
    "apiKey": NEWS_API,
    "q": "Tesla",
    "from": from_,
    "to": to_,
    "language": "en",
}

try:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    
    articles = news_data["articles"][:3]
    
    for article in articles:
        title = article["title"]
        description = article["description"]
        url = article["url"]
        date = article["publishedAt"]
        print(f"Title: {title}\nDescription: {description}\nURL: {url}\nDate: {date}\n")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching news data: {e}")
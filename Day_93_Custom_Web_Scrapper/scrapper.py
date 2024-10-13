import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


# Got lots of error in this file:(((((((:((

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {url}\n{e}")
        return None


def parse_headlines(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    headlines = []

    # Update the selector according to the website's HTML structure
    for item in soup.select('.gs-c-promo-heading__title'):
        title = item.get_text(strip=True)
        if title:
            headlines.append(title)

    return headlines


def save_to_csv(data, filename):
    if not os.path.exists('data'):
        os.makedirs('data')

    df = pd.DataFrame(data, columns=['Headline'])
    file_path = os.path.join('data', filename)
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")


def main():
    url = "https://www.bbc.com/news"
    html_content = fetch_page(url)

    if html_content:
        headlines = parse_headlines(html_content)

        if headlines:
            print("Extracted Headlines:")
            for idx, headline in enumerate(headlines, 1):
                print(f"{idx}. {headline}")

            # Save the headlines to a CSV file
            save_to_csv(headlines, 'headlines.csv')
        else:
            print("No headlines found.")
    else:
        print("Failed to retrieve the webpage content.")


if __name__ == "__main__":
    main()

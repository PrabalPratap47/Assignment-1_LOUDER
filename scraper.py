import requests
from bs4 import BeautifulSoup

def fetch_events():
    url = 'https://www.example-events-website.com/sydney-events'  # Replace with your actual events URL
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    events = []

    # Example: Suppose events are in <div class="event-item"> blocks
    for event_div in soup.find_all('div', class_='event-item'):
        title_tag = event_div.find('h3', class_='event-title')
        date_tag = event_div.find('span', class_='event-date')
        location_tag = event_div.find('span', class_='event-location')

        if title_tag and date_tag and location_tag:
            title = title_tag.get_text(strip=True)
            date = date_tag.get_text(strip=True)
            location = location_tag.get_text(strip=True)

            events.append({
                'title': title,
                'date': date,
                'location': location
            })

    return events

if __name__ == '__main__':
    events = fetch_events()
    for e in events:
        print(e)

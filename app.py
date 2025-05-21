from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample full event data (replace with your actual DB or scraping data)
sydney_events = [
    {"id": 1, "title": "Sydney Opera Concert", "date": "2025-06-10", "url": "https://eventsite.com/sydney-opera-concert"},
    {"id": 2, "title": "Harbour Bridge Climb", "date": "2025-06-15", "url": "https://eventsite.com/harbour-bridge-climb"},
    {"id": 3, "title": "Sydney Food Festival", "date": "2025-07-01", "url": "https://eventsite.com/sydney-food-festival"},
    {"id": 4, "title": "Art Exhibition", "date": "2025-07-10", "url": "https://eventsite.com/art-exhibition"},
    {"id": 5, "title": "Beach Volleyball Tournament", "date": "2025-07-20", "url": "https://eventsite.com/beach-volleyball"},
    {"id": 6, "title": "Jazz Night", "date": "2025-07-25", "url": "https://eventsite.com/jazz-night"},
]

australia_events = [
    {"id": 10, "title": "Melbourne Cup", "date": "2025-11-05", "url": "https://eventsite.com/melbourne-cup"},
    {"id": 11, "title": "Brisbane Food Market", "date": "2025-08-15", "url": "https://eventsite.com/brisbane-food-market"},
    {"id": 12, "title": "Perth Music Festival", "date": "2025-09-20", "url": "https://eventsite.com/perth-music-festival"},
    {"id": 13, "title": "Adelaide Art Fair", "date": "2025-10-10", "url": "https://eventsite.com/adelaide-art-fair"},
    {"id": 14, "title": "Canberra Film Festival", "date": "2025-12-01", "url": "https://eventsite.com/canberra-film-festival"},
    {"id": 15, "title": "Darwin Cultural Fest", "date": "2025-12-15", "url": "https://eventsite.com/darwin-cultural-fest"},
]

@app.route('/')
def index():
    return render_template('index.html', sydney_events=sydney_events, australia_events=australia_events)

@app.route('/api/get_ticket', methods=['POST'])
def get_ticket():
    data = request.json
    email = data.get('email')
    event_id = data.get('event_id')
    subscribe = data.get('subscribe')

    if not email or not event_id:
        return jsonify({"success": False, "message": "Email and Event ID required."})

    # Normally save email, subscription info etc. here

    # Find event URL by id
    all_events = sydney_events + australia_events
    event = next((e for e in all_events if e['id'] == event_id), None)
    if not event:
        return jsonify({"success": False, "message": "Event not found."})

    # Redirect user to actual event URL after ticket reservation
    return jsonify({"success": True, "redirect": event["url"]})

if __name__ == '__main__':
    app.run(debug=True)

from knowledge_base import model
from datetime import timedelta, datetime

place_time_estimates = {
    "tourist_attraction": 2, 
    "museum": 3, 
    "art_gallery": 2, 
    "park": 1.5, 
    "shopping_mall": 2, 
    "library": 1.5,
    "book_store": 1,
    "cafe": 1, 
    "clothing_store": 1, 
    "university": 1, 
    "train_station": 0.5, 
    "shoe_store": 1, 
    "mosque": 1, 
    "synagogue": 1,
    "church": 1,
}
def extract_lat_lng(chunk):
    # Split the chunk by line breaks to isolate lines
    lines = chunk.split('\n')
    
    # Get the last two lines, which should contain the Latitude and Longitude
    lat_line = lines[-2].strip()  # Second-to-last line (Latitude)
    lng_line = lines[-1].strip()  # Last line (Longitude)
    
    # Extract the numeric values for Latitude and Longitude
    lat = float(lat_line.split(":")[1].strip())  # Convert to float after the 'Latitude:' label
    lng = float(lng_line.split(":")[1].strip())  # Convert to float after the 'Longitude:' label
    
    return lat, lng

def estimate_time(chunk):
    types = chunk.split('Types: ')[1].split('\n')[0]
    types = types.split(", ")
    time = max(place_time_estimates.get(t, 0) for t in types)
    return time
    
def generate_day(itinerary, city_name, lat, lng, persona):
    day = {}
    start_time = datetime.strptime("09:00", "%H:%M")
    
    # Before noon
    while start_time.hour < 12:
        suggestion = model.generate_itinerary(
            city_name, lat, lng,
            persona.days, persona.culture, persona.history,
            persona.art, persona.nature, persona.walking_tours,
            persona.shopping, 
            itinerary
        )
        itinerary.append(suggestion)
        lat, lng = extract_lat_lng(suggestion)
        duration = estimate_time(suggestion)
        end_time = start_time + timedelta(hours=duration)
        key = f"{start_time.strftime('%H:%M')}–{end_time.strftime('%H:%M')}"
        day[key] = suggestion

        start_time = end_time + timedelta(minutes=15) # 15-minute break/travel buffer

    # Lunch
    lunch_end = start_time + timedelta(hours=1)
    key = f"{start_time.strftime('%H:%M')}–{lunch_end.strftime('%H:%M')}"
    day[key] = "Lunch"
    start_time = lunch_end

    # Afternoon until 7PM
    while start_time.hour < 19:
        # Generate next suggestion
        suggestion = model.generate_itinerary(
            city_name, lat, lng, persona.days,
            persona.culture, persona.history,
            persona.art, persona.nature,
            persona.walking_tours, persona.shopping,
            itinerary
        )
        itinerary.append(suggestion)
        lat, lng = extract_lat_lng(suggestion)
        duration = estimate_time(suggestion)
        end_time = start_time + timedelta(hours=duration)

        key = f"{start_time.strftime('%H:%M')}–{end_time.strftime('%H:%M')}"

        day[key] = suggestion
        start_time = end_time

    return itinerary, day
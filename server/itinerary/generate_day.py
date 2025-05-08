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
    "restaurant": 1.5
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

def parse_time_range(range):
    start_str, end_str = range.split("–")
    start = datetime.strptime(start_str.strip(), "%Y-%m-%d %H:%M")
    end = datetime.strptime(end_str.strip(), "%Y-%m-%d %H:%M")
    return start, end


def ranges_overlap(start1, end1, start2, end2):
    return max(start1, start2) < min(end1, end2)

def is_not_valid_activity(start_time, end_time, excluded):
    for time in excluded:
        excl_start, excl_end = parse_time_range(time)
        if ranges_overlap(start_time, end_time, excl_start, excl_end):
            return excl_end
    return None

def generate_day(itinerary, city_name, lat, lng, persona, curr_day):
    day = {}
    start_time = datetime.strptime("09:00", "%H:%M")
    start_time = datetime.combine(curr_day, start_time.time())
    lunch = False
    
    while start_time.hour < 19:
        suggestion = None
        if start_time.hour >= 12 and start_time.hour <= 13 and not lunch:
            lunch = True
            suggestion = model.generate_food(city_name, start_time)
        else: 
            suggestion = model.generate_itinerary(
                city_name, start_time, lat, lng,
                persona.culture, persona.history,
                persona.art, persona.nature, persona.walking_tours,
                persona.shopping, 
                itinerary
            )
        itinerary.append(suggestion)
        lat, lng = extract_lat_lng(suggestion)
        duration = estimate_time(suggestion)
        end_time = start_time + timedelta(hours=duration)
        
        invalid_end_time = is_not_valid_activity(start_time, end_time, persona.breaks)
        if invalid_end_time:
            # skip!
            print("we skipping this one chat")
            print(invalid_end_time)
            start_time =  invalid_end_time + timedelta(minutes=15)
        else:
            key = f"{start_time.strftime("%Y-%m-%d %H:%M")}–{end_time.strftime("%Y-%m-%d %H:%M")}"
            day[key] = suggestion

            start_time = end_time + timedelta(minutes=15) # 15-minute break/travel buffer

    # dinner!
    dinner = model.generate_food(city_name, start_time)
    duration = estimate_time(dinner)
    end_time = start_time + timedelta(hours=duration)
    key = f"{start_time.strftime("%Y-%m-%d %H:%M")}–{end_time.strftime("%Y-%m-%d %H:%M")}"
    day[key] = dinner
    
    return itinerary, day
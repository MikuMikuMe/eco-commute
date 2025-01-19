Creating a complete Python program for an eco-friendly commute planner involves integrating various APIs for live traffic, weather data, mapping services, and potentially public transport data. Given the complexity of this task and the need for real-time data, the following example outlines a structured approach. You will need proper API keys for accessing these services.

Below is a basic skeleton code to get you started:

```python
import requests
import json
from datetime import datetime

# Constants for API usage (You need to replace 'YOUR_API_KEY' with your actual API keys)
MAPS_API_KEY = 'YOUR_MAPS_API_KEY'
WEATHER_API_KEY = 'YOUR_WEATHER_API_KEY'
TRAFFIC_API_KEY = 'YOUR_TRAFFIC_API_KEY'

def get_weather_data(location):
    """Fetches current weather data for a specified location."""
    try:
        # Replace with the actual weather API endpoint
        weather_url = f'https://api.weather.com/v3/location/{location}?apiKey={WEATHER_API_KEY}'
        response = requests.get(weather_url)
        response.raise_for_status()
        return response.json()  # Process and return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve weather data: {e}")
        return None

def get_public_transport_routes(start, end):
    """Fetches possible public transport routes from start to end location."""
    # Replace with the actual transit API endpoint
    try:
        transit_url = f'https://api.transit.com/routes?start={start}&end={end}&apiKey={MAPS_API_KEY}'
        response = requests.get(transit_url)
        response.raise_for_status()
        return response.json()  # Process and return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve transit data: {e}")
        return None

def get_bike_routes(start, end):
    """Fetches biking routes between start and end locations."""
    try:
        bike_url = f'https://api.cyclingroutes.com/route?start={start}&end={end}&apiKey={MAPS_API_KEY}'
        response = requests.get(bike_url)
        response.raise_for_status()
        return response.json()  # Process and return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve biking routes: {e}")
        return None
    
def get_traffic_info(location):
    """Fetches live traffic data for a specified location."""
    try:
        traffic_url = f'https://api.trafficinfo.com/current?location={location}&apiKey={TRAFFIC_API_KEY}'
        response = requests.get(traffic_url)
        response.raise_for_status()
        return response.json()  # Process and return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve traffic data: {e}")
        return None

def suggest_commute_options(start, end):
    """Suggests the most eco-friendly commute options."""
    # Get data from the APIs
    weather_data = get_weather_data(start)
    transit_routes = get_public_transport_routes(start, end)
    bike_routes = get_bike_routes(start, end)

    # Handle no data scenarios
    if weather_data is None:
        print("No weather information available.")
    if transit_routes is None:
        print("No transit route information available.")
    if bike_routes is None:
        print("No biking route information available.")

    # Logic to calculate the best option
    # A simplified example of decision making:
    if weather_data and weather_data['condition'] not in ['Rain', 'Snow']:
        if bike_routes:
            print("Biking is a viable option.")
    if transit_routes:
        print("Public transportation is available.")

def main():
    """Main function to execute the program."""
    # Example locations as input, should be obtained dynamically through user input or system input
    start_location = "40.712776,-74.005974"  # Example: New York City
    end_location = "40.730610,-73.935242"    # Example: Manhattan NY

    # Call the function to suggest the best options
    suggest_commute_options(start_location, end_location)

if __name__ == "__main__":
    main()
```

### Key Points:

1. **API Integration**: The program integrates multiple APIs - weather, traffic, and public transportation. You will need to research and obtain API keys for these services.

2. **Error Handling**: The program catches exceptions using `try-except` blocks for API calls to handle network errors or data retrieval issues.

3. **Comments**: The code includes comments describing each function's purpose and general program flow.

4. **Eco-Friendly Decisions**: This simplified version uses basic weather conditions to decide on a bike versus public transit route. More complex logic can be built based on distance, cost, and real-time traffic data.

5. **Extensibility**: The current setup serves as a baseline. You can expand it to include cycling stations, walking paths, and real-time updates by incorporating additional APIs and more sophisticated logic.

This program offers a starting framework and will need further development for a fully functional application. You should consult specific API documentation to tailor calls for comprehensive data and refine decision-making criteria for eco-friendly travel.
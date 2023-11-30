import tkinter as tk
import requests

def get_weather_data(city):
    # Replace with your OpenWeatherMap API key
    api_key = "55cb161261ffd0e816f0d318d69173b5"

    # Construct the API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Send the API request and get the response
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the JSON response to a Python dictionary
        data = response.json()

        # Extract the relevant weather information
        weather_data = {
            "city": data["name"],
            "weather_description": data["weather"][0]["description"],
            "temperature": round(data["main"]["temp"] - 273.15, 2),
            "humidity": data["main"]["humidity"],
        }

        return weather_data
    else:
        print("Error:", response.status_code)
        return None

def update_weather_data():
    city = city_entry.get()
    weather_data = get_weather_data(city)

    if weather_data:
        weather_description_label.config(text=weather_data["weather_description"])
        temperature_label.config(text=f"{weather_data['temperature']}°C")
        humidity_label.config(text=f"{weather_data['humidity']}%")
    else:
        weather_description_label.config(text="Unable to fetch weather data")
        temperature_label.config(text="-")
        humidity_label.config(text="-")

# Create the main window
window = tk.Tk()
window.title("Weather Information")

# Create input field for city name
city_label = tk.Label(window, text="City:")
city_label.grid(row=0, column=0)

city_entry = tk.Entry(window)
city_entry.grid(row=0, column=1)

# Create button to fetch weather data
update_button = tk.Button(window, text="Update Weather", command=update_weather_data)
update_button.grid(row=1, column=0, columnspan=2)

# Create labels to display weather information
weather_description_label = tk.Label(window, text="Description: -")
weather_description_label.grid(row=2, column=0, columnspan=2)

temperature_label = tk.Label(window, text="Temperature: -°C")
temperature_label.grid(row=3, column=0, columnspan=2)

humidity_label = tk.Label(window, text="Humidity: -%")
humidity_label.grid(row=4, column=0, columnspan=2)

# Run the main loop
window.mainloop()
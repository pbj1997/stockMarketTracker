import requests
from bs4 import BeautifulSoup

# Function to get weather information from Naver
def get_weather(city_name):
    # Naver Weather URL (this is just an example URL; you may need to adjust the query based on the city)
    url = f"https://search.naver.com/search.naver?query={city_name}+날씨"
    
    # Send a request to the website
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the temperature
    temperature = soup.find('div', class_='temperature_text').get_text(strip=True)
    
    # Extract the weather condition
    condition = soup.find('p', class_='summary').get_text(strip=True)
    
    # Extract additional information (like rain probability, wind, etc.)
    rain = soup.find('span', class_='rainfall').get_text(strip=True)
    
    # Print the extracted weather information
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}")
    print(f"Weather Condition: {condition}")
    print(f"Rain Probability: {rain}")

# Main code
if __name__ == '__main__':
    # User input for the city name (in Korean, as the Naver Weather page is in Korean)
    city = input("Enter the city name in Korean (e.g., 서울 for Seoul): ")
    
    # Get and display the weather for the input city
    get_weather(city)

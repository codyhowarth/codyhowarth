import requests
import json

# Base URL for the TAP service
TAP_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

# SQL query to count the total number of exoplanets
QUERY = "SELECT COUNT(*) AS total_exoplanets FROM ps"

# Parameters for the request
params = {
    "query": QUERY,
    "format": "json"
}

def get_exoplanet_count():
  try:
      # Make the HTTP GET request to the TAP service
      response = requests.get(TAP_URL, params=params)
      response.raise_for_status()  # Raise an exception for HTTP errors

      # Parse the JSON response
      data = response.json()

      # Extract and print the total number of exoplanets
      total_exoplanets = data[0]['total_exoplanets']
      print(f"Total number of discovered exoplanets: {total_exoplanets}")
      return total_exoplanets

  except requests.exceptions.RequestException as e:
      print(f"An error occurred: {e}")
  except (KeyError, IndexError) as e:
      print(f"Unexpected data format: {e}")

def get_latest_earth_image():
    # Base URL for NASA's EPIC API
    EPIC_API_URL = "https://api.nasa.gov/EPIC/api/natural/images"
    
    # Your NASA API key (replace with your actual key)
    API_KEY = "DEMO_KEY"  # Replace "DEMO_KEY" with your actual NASA API key

    try:
        # Make the HTTP GET request to the EPIC API
        response = requests.get(EPIC_API_URL, params={"api_key": API_KEY})
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        if data:
            # Extract the latest image details
            latest_image = data[0]
            image_date = latest_image['date']
            image_name = latest_image['image']
            base_url = "https://epic.gsfc.nasa.gov/archive/natural"
            date_only = image_date.split(" ")[0]  # Extract just the date part
            year, month, day = date_only.split("-")
            image_url = f"{base_url}/{year}/{month}/{day}/png/{image_name}.png"
            print(f"Latest Earth image URL: {image_url}")
            return image_url
        else:
            print("No images available.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except (KeyError, IndexError) as e:
        print(f"Unexpected data format: {e}")


if __name__ == "__main__":
    get_exoplanet_count()
    get_latest_earth_image()
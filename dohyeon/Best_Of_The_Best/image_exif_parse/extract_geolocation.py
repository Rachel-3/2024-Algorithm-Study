import os
from exif import Image
from datetime import datetime
import folium
from folium import plugins

def dms_to_decimal(degrees, minutes, seconds):
    return degrees + (minutes / 60.0) + (seconds / 3600.0)

def extract_location_and_time(image_path):
    with open(image_path, "rb") as f:
        img = Image(f)

    gps_latitude = img.gps_latitude
    gps_longitude = img.gps_longitude

    decimal_latitude = dms_to_decimal(*gps_latitude)
    decimal_longitude = dms_to_decimal(*gps_longitude)
    
    datetime_original = img.get('datetime_original', 'Unknown')
    
    if datetime_original != 'Unknown':
        datetime_original = datetime.strptime(datetime_original, '%Y:%m:%d %H:%M:%S')

    return [decimal_latitude, decimal_longitude, datetime_original, image_path]

# Extract data from images
image_dir = 'JohnDoe/JohnDoe'
dir_files = os.listdir(image_dir)
image_data = []

for i in dir_files:
    try:
        image_path = os.path.join(image_dir, i)
        image_info = extract_location_and_time(image_path)
        if image_info[2] != 'Unknown':  # Only include images with valid datetime
            image_data.append(image_info)
    except Exception as e:
        print(f"Error processing {i}: {e}")

# Sort data by datetime
image_data.sort(key=lambda x: x[2])

# Create a map centered at the first image location
m = folium.Map(location=[image_data[0][0], image_data[0][1]], zoom_start=12)

# Coordinates for the red line
coordinates = [(lat, lon) for lat, lon, dt, path in image_data]

# Add red line to the map
folium.PolyLine(coordinates, color="red", weight=2.5, opacity=1).add_to(m)

# Add markers to the map with numbers
for idx, (lat, lon, dt, path) in enumerate(image_data, start=1):
    folium.Marker(
        location=[lat, lon],
        popup=f"{idx}: {dt}",
        tooltip=f"Image {idx}",
        icon=folium.DivIcon(
            html=f"""<div style="font-size: 12pt; color : blue">{idx}</div>"""
        )
    ).add_to(m)

# Save map to HTML
m.save('image_path_map.html')

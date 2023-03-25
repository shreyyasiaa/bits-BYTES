import pyproj
from PIL import Image, ImageDraw
wgs84 = pyproj.Proj("+init=EPSG:4326")  
web_mercator = pyproj.Proj("+init=EPSG:3857")  

lon = -122.4194  
lat = 37.7749  
x, y = pyproj.transform(wgs84, web_mercator, lon, lat)
print("Longitude and latitude coordinates: {}, {}".format(lon, lat))
print("Pixel coordinates: {}, {}".format(x, y))

map_image = Image.open("Screenshot 2023-03-25 at 10.43.53 AM.png")

draw = ImageDraw.Draw(map_image)

x = -13627665.271218073
y = 4547675.354340557

marker_size = 100000
marker_color = (255, 0, 0)  

draw.rectangle((x-marker_size, y-marker_size, x+marker_size, y+marker_size), fill=marker_color)

map_image.save("map.png")

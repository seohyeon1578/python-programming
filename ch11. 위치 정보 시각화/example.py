import folium

lat1, long1 = 37.52860, 126.93431
lat2, long2 = 37.52400, 126.91889
lat3, long3 = 37.51865, 126.92041

lat = [lat1, lat2, lat3]
long = [long1, long2, long3]
name = ['여의도 한강 공원', '여의도 공원', '샛강생태공원']
icon = ['home', 'flag', 'heart']
color = ['purple', 'red', 'blue']

map_y = folium.Map([lat1 , long1], zoom_start=15)
for i in range(3):
  folium.Marker([lat[i], long[i]], tooltip=name[i], icon=folium.Icon(color=color[i], icon=icon[i], prefix='fa')).add_to(map_y)
map_y
from decimal import Decimal
from tags.tag import Tag
import json


class MapLeaflet(Tag):
   def __init__(self, name_id, height="500px", width="100%", center_lat=-15.76, center_lon=-47.89, zoom_level=5, attrs=None):
       super().__init__("div", attrs, name_id, content=" ")
       # É uma boa prática definir a altura e largura via CSS ou atributo 'style'
       # Em vez de ter uma classe genérica, você já está usando o 'style' direto.
       # self.add_class('map-container') # Pode manter ou remover, dependendo do seu CSS
       self.add_attr("style", f"height: {height}; width: {width};")


       self.center_lat = center_lat
       self.center_lon = center_lon
       self.zoom_level = zoom_level
       self.points = []


   def add_point(self, latitude, longitude, name=None, popup_content=None):
       """Adiciona um ponto ao mapa."""
       point_data = {
           "latitude": float(latitude),  # Garante que seja float para JSON
           "longitude": float(longitude), # Garante que seja float para JSON
           "name": name,
           "popup_content": popup_content
       }
       self.points.append(point_data)


   def add_points_from_list(self, point_list, lat_field='latitude', lon_field='longitude', name_field=None, popup_field=None):
       """Adiciona uma lista de pontos ao mapa, usando nomes de campos.
          Converte Decimal para float ao adicionar."""
       for item in point_list:
           lat = getattr(item, lat_field)
           lon = getattr(item, lon_field)


           # Converte Decimal para float, se for o caso
           if isinstance(lat, type(Decimal('0.0'))): # Verifica se é um objeto Decimal
               lat = float(lat)
           if isinstance(lon, type(Decimal('0.0'))): # Verifica se é um objeto Decimal
               lon = float(lon)


           name = getattr(item, name_field) if name_field and hasattr(item, name_field) else None
           popup = getattr(item, popup_field) if popup_field and hasattr(item, popup_field) else None
           self.add_point(lat, lon, name, popup)


   def get_html(self):
       """Retorna apenas o HTML da div do mapa."""
       return super().make_html() # Chama o make_html da classe pai (Tag)


   def get_javascript(self):
       """Gera a tag <script> com o JavaScript para inicializar o Leaflet e adicionar os pontos."""
       # Usamos json.dumps para converter a lista de dicionários Python para um array JSON válido no JS
       points_json = json.dumps(self.points, ensure_ascii=False)


       script_content = f"""
       // Garante que o script só rode após o DOM estar carregado e Leaflet disponível
       document.addEventListener('DOMContentLoaded', function() {{
           // Verifica se L (Leaflet) está definido
           if (typeof L === 'undefined') {{
               console.error('Leaflet library (L) is not loaded. Ensure leaflet.js is included before this script.');
               return;
           }}


           var map = L.map('{self.attrs['id']}').setView([{self.center_lat}, {self.center_lon}], {self.zoom_level});


           L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
               attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
           }}).addTo(map);


           var points = {points_json}; // Os pontos serão injetados aqui como JSON


           points.forEach(function(point) {{
               var popupHtml = '';
               if (point.name) {{
                   popupHtml += '<b>' + point.name + '</b><br>';
               }}
               if (point.popup_content) {{
                   popupHtml += point.popup_content + '<br>';
               }}
               popupHtml += 'Lat: ' + point.latitude.toFixed(4) + '<br>Lon: ' + point.longitude.toFixed(4);


               L.marker([point.latitude, point.longitude])
                   .addTo(map)
                   .bindPopup(popupHtml);
           }});
       }});
       """
       return Tag("script", content=script_content).make_html()

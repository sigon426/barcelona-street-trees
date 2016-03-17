from xml.dom import minidom
import string
from geojson import GeometryCollection, Point, LineString, Feature, FeatureCollection
import json


kml = minidom.parse("arbolado_viario_3.kml")

Placemarks = kml.getElementsByTagName("Placemark")
print 'nodes:' 
print len(Placemarks)


geom_points = []

for node in Placemarks:
    name = node.getElementsByTagName("name")

    point = node.getElementsByTagName("Point")
    coordinates = point[0].getElementsByTagName("coordinates")
    coordinatesText = coordinates[0].firstChild.data
    array = coordinatesText.split(',')
    coordinatesArray = [float(array[0]), float(array[1])]

    description = node.getElementsByTagName("description")
    descText = description[0].firstChild.data
    descText2 = string.replace(descText, '<b>', '')
    descText2 = string.replace(descText2, '</b>', '')
    descText2 = string.replace(descText2, '<h1>', '')
    descText2 = string.replace(descText2, '</h1>', '')
    descText2 = string.replace(descText2, '-', '')
    array2 = descText2.split('<br>')
    
    treeCode =  array2[0].split(':')[1]
    ETRS89_x =  float(array2[1].split(':')[1])
    ETRS89_y =  float(array2[2].split(':')[1])
    Espacio_Verde = array2[3].split(':')[1]
    direcc = array2[4].split(':')[1]
    alzada = array2[5].split(':')[1]
    nombre_cientifico = array2[6].split(':')[1]
    nombre_castellano = array2[7].split(':')[1]
    nombre_catalan = array2[8].split(':')[1]
    especie = string.replace(array2[9].split(':')[1], ' ', '')
    anchura = array2[10].split(':')[1]
    data_plantacion = array2[11].split(':')[1]
    posicion = array2[12].split(':')[1]
    tipo_agua = array2[13].split(':')[1]
    tipo_riego = array2[14].split(':')[1]
    tipo_superficie = array2[15].split(':')[1]
    tipo_soporte = array2[16].split(':')[1]
    cubierta = array2[17].split(':')[1]


    properties = {
        'codi':treeCode,
        'especie': especie, 
        'name_esp': nombre_castellano, 
        'name_cat': nombre_catalan, 
        'name_sci': nombre_cientifico, 
        'alzada': alzada, 
        'direcc': direcc,
        'date': data_plantacion,
        'weight': anchura,
        'position': posicion,
        'irrigation': tipo_riego,
        'type_of_water': tipo_agua,
        'type_sup': tipo_superficie,
        'soporte': tipo_soporte,
        'cubierta': cubierta
    }

    geom_points.append(Feature(geometry=Point((coordinatesArray[1], coordinatesArray[0])), properties=properties))


# create a Feature Collection from the points array
myGeojson = FeatureCollection(geom_points) 

# save the geojson file
with open("arbolado_viario_3.json", "w") as f:
    f.write(json.dumps(myGeojson))



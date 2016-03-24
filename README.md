# Barcelona street trees

Arbolado viario de la ciudad de Barcelona. 

Arbrat viari de la ciutat de Barcelona.

Data updated on 16 mar 2016 from:

http://opendata.bcn.cat/opendata/ca/catalog/ext/MEDI_AMBIENT/arbratviari/

Dataset uploaded on cartodb; viz_id = ae91d3c2-f1aa-11e5-90bc-0ef7f98ade21



You can make queries to this dataset like this:

https://mac.cartodb.com/api/v2/sql?q=select distinct name_sci, name_esp, esp_count as count from barcelona_trees

https://mac.cartodb.com/api/v2/sql?q=select * from barcelona_trees where esp_count < 2


Or get geojson data:

´´´
var myURL = https://mac.cartodb.com/api/v2/sql?format=GeoJSON&q=select * from barcelona_trees where esp_count < 2

$.getJSON(myURL, function(mygeojson) {
    console.log(mygeojson);
});
´´´
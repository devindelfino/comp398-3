README.md
=========

This gatra.geojson file contains the four stops on the Gatra 140 route, identified by their gps coordinates, and the following metadata about each stop:

-  point: coordinates
-  name: string
-  address: string
-  stop: number (1-4)
-  origin: boolean (first stop)
-  destination: boolean (last stop)
-  nearby attractions: list of strings
-  all pickups yearlong: list of strings
-  am pickups yearlong: list of strings
-  am pickups breaks (only times during fall and winter break): list of strings
-  pm pickups yearlong: list of strings
-  pm pickups breaks: list of strings
-  distance from previous stop (in miles): number
-  distance to next stop (in miles): number
-  time estimate of travel from current to next stop (in minutes): number

All data from [gatra website](http://www.gatra.org/index.php/routes/mansfield-norton/wheaton-t-shuttleroute-140/) and [google maps](https://www.google.com/maps/preview). 

Mapbox version can be found [here](https://a.tiles.mapbox.com/v4/lithiah.jkpa4139/page.html?access_token=pk.eyJ1IjoibGl0aGlhaCIsImEiOiJEQkVqUG1FIn0.5GQslk_hmYegLEgjDISfEA#11/-71.1684/41.9427).

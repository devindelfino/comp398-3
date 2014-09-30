README.md
=========

This gatra.geojson file contains the four stops on the Gatra 140 route, identified by their gps coordinates, and the following metadata about each stop:

-  point: coordinates
-  name: string
-  address: string
-  stop: number (first-fourth)
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

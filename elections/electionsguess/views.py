from django.http import HttpResponse
from electionsguess.trial import constituencies 


def search_constituencies(request,place):

  flag=0 
  for constituency in constituencies:
     if place == constituency:
       flag=1
  if flag==1:
    html= "<!DOCTYPE html>
    <html>
 <head>
  <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
  <title>SEARCH</title>
  <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.no-icons.min.css" rel="stylesheet">
  <script type="text/javascript">
    function enterNumber(){
         var e = document.getElementById('campaigns');
            if (!/^[0-9]+$/.test(e.value)) 
                  { 
                        alert("Please enter only number.");
                            e.value = e.value.substring(0,e.value.length-1);
                                }}  
  </script>
     <script type="text/javascript"
           src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCH5tMEPYn-SUGeHHObZwcWlyWdgeRVtwo&sensor=true">
               </script>
                   <script type="text/javascript">
                         function initialize() {
                                   var mapOptions = {
                                               center: new google.maps.LatLng(28.6100, 77.2300),
                                                                 zoom: 8,
                                                                           mapTypeId: google.maps.MapTypeId.ROADMAP
                                                                                     };
                                           var map = new google.maps.Map(document.getElementById("map-canvas"),
                                                           mapOptions);
                                                 }
      google.maps.event.addDomListener(window, 'load', initialize);
          </script>
              <style type="text/css">
                     #map-canvas { height: 200px ; width:675px}
                       </style>
                        </head>
                          <body>
                           <div class = "container">
                            <h1>SEARCH RESULTS</h1>
                             <label>Search Results</label>
                             <!-- Fill up form with input fields and button -->
                              <form class="well form-search" action="url" method="get">
                              <table>
                              <tr>
                              <td>
                              <p>Enter the name of the party</p>
                              </td>
                               <td>
                               <input type="text" name="Name" id="partyname">
                                </td>
                                 </tr>
                               <tr>
                               <td>
                               <p>Major Caste Support</p>
                                </td>
                                <td>
                                <input type="text" name="Caste" id="castesupport">
                                </td>
                                </tr>
                                <tr>
                                <td>
                                <p>Enter the number of campaigns</p>
                                </td>
                                <td>
                                <input type="text" name="campaigns" id="campaigns" onkeyup=enterNumber()>
                                </td>
                                </tr>
                                <tr>
                                <td>
                                </td>
                                <td>
                                <button type="submit" value="submit" class="btn btn-primary">Submit</button>
                                </td>
                                </tr>
                                </table>
                      <div id="map-canvas"/>
                     </form>
                      </div>
                       </body>
                        </html> "
    return HttpResponse(html)
  else:
    return redirect("earlierview")

def home_page(request){
 html="<!DOCTYPE html>
  <html>
 <head>
 <title>Home Page</title>
 <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.no-icons.min.css" rel="stylesheet">
</head>
<body>
 <div class = "container">
  <h1>Elections</h1>
   <form action="url1" method="get">
    Constituency name:<input type="text" name = "constituency">
     <button type="submit" value="submit" class = "btn btn-primary">Submit</button>
      </form>
       </div>
       </body>
       </html>"
 return HttpResponse(html)

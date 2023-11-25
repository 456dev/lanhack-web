function main() {
	output = document.getElementById("output")
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", "/api/get-uids", false);
  xmlHttp.send( null );
  output.innerText = xmlHttp.responseText;
}

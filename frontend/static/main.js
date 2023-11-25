function main() {
  updateUIDList();
  setInterval(updateUIDList, 5000);
}

function updateUIDList() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", "/api/get-uids", false);
  xmlHttp.send(null);
  var response = JSON.parse(xmlHttp.responseText);
  setUIDList(response["uids"]);
}

function setUIDList(uids) {
  var list = document.getElementById("uid-list");
  list.innerHTML = "";
  uids.forEach(function(uid) {
    list.appendChild(createUIDElement(uid));
  });
}

function createUIDElement(uid) {
  var element = document.createElement("li");
  element.className = "list-group-item list-group-item-light fs-4";
  element.innerText = uid.uid;
  return element;
}

function start() {
  updateUIDList();
}

function updateUIDList() {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", "/api/get-uids", false);
  xmlHttp.send(null);
  var response = JSON.parse(xmlHttp.responseText);
  setUIDList(response["uids"]);
}

async function clearUIDList() {
  await fetch("/api/clear-uids", {method: "POST"})
  updateUIDList()
}




function setUIDList(uids) {
  var list = document.getElementById("uid-list");
  list.innerHTML = "";
  uids.forEach(addUIDToList);
}

function addUIDToList(uid) {
  var list = document.getElementById("uid-list");
  list.prepend(createUIDElement(uid));
}

function createUIDElement(uid) {
  var element = document.createElement("button");
  element.setAttribute("type", "button");
  element.setAttribute("class", "list-group-item list-group-item-action fs-2");
  element.innerHTML = uid.uid;
  return element;
}

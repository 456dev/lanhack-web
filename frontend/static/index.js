function start() {
  updateUIDList();
}

function updateUIDList() {
  let xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", "/api/get-uids", false);
  xmlHttp.send(null);
  let response = JSON.parse(xmlHttp.responseText);
  setUIDList(response["uids"]);
}

async function clearUIDList() {
  await fetch("/api/clear-uids", {method: "POST"})
  updateUIDList()
}

async function exportAsCsv() {
  let xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", "/api/get-uids", false);
  xmlHttp.send(null);
  let response = JSON.parse(xmlHttp.responseText);


  let csvish = "timestamp,uid\n"
  if (response !== null) {
    let uidData = response["uids"]
    for (const uidDatum of uidData) {
      let uid = uidDatum["uid"]
      let timestamp = uidDatum["timestamp"]
      csvish += (timestamp + "," + uid + "\n")
    }
  }

  let currentTime = new Date()
  currentTime.toISOString()
  window.open(window.URL.createObjectURL(
      new File([csvish], "export_" + currentTime.toISOString() + ".csv",
          {type: "text/csv"})), "_blank")
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

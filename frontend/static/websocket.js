// Create a new WebSocket connection

let socket = new WebSocket('ws://' + window.location.host + '/api/ws');

function setupWebsockets() {
  socket.addEventListener('message', (event) => {
    addUIDToList(JSON.parse(event.data));
  });
  socket.addEventListener("close", (event) => {
    setTimeout(event => {window.location.reload()}, 1000);
  })
  socket.addEventListener("error", (event) => {
    setTimeout(event => {window.location.reload()}, 1000);

  })
}
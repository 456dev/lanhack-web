// Create a new WebSocket connection

let socket

function setupWebsockets() {
  socket = new WebSocket('ws://' + window.location.host + '/api/ws');
  socket.addEventListener('message', (event) => {
    addUIDToList(JSON.parse(event.data));
  });
  socket.addEventListener("close", ev => {
    setTimeout(setupWebsockets, 1000);
  })
  socket.addEventListener("error", ev => {
    setTimeout(setupWebsockets, 1000);

  })
}

setupWebsockets()
// Create a new WebSocket connection
const socket = new WebSocket('ws://' + window.location.host + '/api/ws');

// Add an event listener to the WebSocket connection
socket.addEventListener('message', (event) => {
  addUIDToList(JSON.parse(event.data));
});

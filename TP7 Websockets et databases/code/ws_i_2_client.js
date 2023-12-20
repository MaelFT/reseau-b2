const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:8765')
ws.onopen = () => {
  ws.send('hello world')
}

ws.onmessage = (message) => {
  console.log(message.data)
}
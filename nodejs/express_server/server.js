const express = require('express')
const port = 8030
var app = express()

// respond with "hello world" when a GET request is made to the homepage
app.get('/', function (req, res) {
    console.log("message received")
  res.send('hello dude')
})

app.listen(port, () => {
  console.log(`Example app listening at http://0.0.0.0:${port}`)
})
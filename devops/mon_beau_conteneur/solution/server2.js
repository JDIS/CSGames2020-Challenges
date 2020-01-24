const express = require('express')
const app = express()
const port = 5000

app.get('/', (req, res) => res.send('This is buggy :('))

app.listen(port, '0.0.0.0', () => console.log(`My buggy server on port ${port}!}`))

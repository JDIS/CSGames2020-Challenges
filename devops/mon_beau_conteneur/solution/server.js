const express = require('express')
const app = express()
const port = 5000

app.get('/', (req, res) => res.send('Good job! {Cl0udIsSoC00L}'))

app.listen(port, '0.0.0.0', () => console.log(`My super server on port ${port}! {L0gsDoM@tter!}`))

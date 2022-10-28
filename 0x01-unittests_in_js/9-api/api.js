const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
})
.listen(7865, () => {
  console.log('API available on localhost port 7865');
});
app.get('/cart/:id([0-9]*)', (req, res) => {
  res.send('Payment methods for cart ' + request.params.id);
})
.listen(7865, () => {
  console.log('API available on localhost port 7865');
});
module.exports = app;

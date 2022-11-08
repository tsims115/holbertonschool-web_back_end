import redis from 'redis';
const express = require('express');
const app = express();
const util = require('util');
const client = redis.createClient();
app.listen(1245)

const listProducts = [
  {
    id: 1,
    name: "Suitcase 250",
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: "Suitcase 450",
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: "Suitcase 650",
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: "Suitcase 1050",
    price: 550,
    stock: 5
  },
]

console.log("Connected!");

function getItemById(id) {
  return listProducts[id - 1];
}

function reserveStockById(itemId, stock) {
  return () => {
    client.set(itemId, stock, redis.print);
  }
}

async function getCurrentReservedStockById(itemId) {
  return await util.promisify(client.get).bind(client)(itemId);
}

app.get('/list_products', (req, res) => {
  let newProducts = [];
  for (let i = 0; i < listProducts.length; i++) {
    newProducts.push({
      "itemId": listProducts[i].id,
      "itemName": listProducts[i].name,
      "price": listProducts[i].price,
      "initialAvailableQuantity": listProducts[i].stock
    });
  }
  res.send(newProducts);
});

app.get('/list_products/:itemId', (req, res) => {
  const id = req.params.itemId;
  console.log(req.params.itemId);
  if (id > listProducts.length) {
    res.send({ "status": "Product not found" });
  } else {
    const current_stock = getCurrentReservedStockById(req.params.itemId);
    console.log(current_stock);
    const item = getItemById(req.params.itemId);
    res.send({
      "itemId": item.id,
      "itemName": item.name,
      "price": item.price,
      "initialAvailableQuantity": item.stock,
      "currentQuantity": current_stock
    });
  }
});

app.get('/reserve_product/:itemId', (req, res) => {
  const id = req.params.itemId;
  if (id > listProducts.length) {
    res.send({ "status": "Product not found" });
  } else {
    const current_stock = getCurrentReservedStockById(req.params.itemId);
    const item = getItemById(req.params.itemId);
    if (current_stock  <= 0) {
      res.send({ "status":"Not enough stock available", "itemId": req.params.itemId });
    } else {
      reserveStockById(req.params.itemId, 1)();
      res.send({ "status": "Reservation confirmed", "itemId": req.params.itemId });
    }
  }
});


module.exports = app;

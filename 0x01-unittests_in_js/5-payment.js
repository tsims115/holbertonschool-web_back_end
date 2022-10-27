const Utils = require('./utils');

module.exports = function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const t = Utils.calculateNumber("SUM", totalAmount, totalShipping);
  console.log(`The total is: ${t}`);
};

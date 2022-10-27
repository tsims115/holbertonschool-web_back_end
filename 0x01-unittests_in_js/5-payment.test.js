const chai = require("chai");
const expect = chai.expect;
const sendPaymentRequestToApi = require('./4-payment');
const sinon = require("sinon");
const Utils = require('./utils');

describe('payment function', function () {
  describe('sendPaymentRequestToApi', function () {
      let s;
      beforeEach(function() {
        s = sinon.stub(console, 'log');
      });

      afterEach(function() {
        s.restore();
      });
      it('sendPaymentRequestToApi', function () {
        sendPaymentRequestToApi(100, 20);
        expect(s.calledWith('The total is: 120')).to.be.true;
      });
      it('sendPaymentRequestToApi', function () {
        sendPaymentRequestToApi(10, 10);
        expect(s.calledWith('The total is: 20')).to.be.true;
      });
  });
});

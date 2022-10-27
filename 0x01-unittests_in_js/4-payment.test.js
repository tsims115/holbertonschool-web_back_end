const chai = require("chai");
const expect = chai.expect;
const sendPaymentRequestToApi = require('./4-payment');
const sinon = require("sinon");
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function () {
  describe('sendPaymentRequestToApi', function () {
      it('sendPaymentRequestToApi', function () {

        
        const s = sinon.stub(Utils, "calculateNumber").returns(10);
        sendPaymentRequestToApi(100, 20);
        expect(s.calledWith('SUM', 100, 20)).to.be.true;
        s.restore();
      });
  });
});

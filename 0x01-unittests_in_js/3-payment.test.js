const chai = require("chai");
const expect = chai.expect;
const sendPaymentRequestToApi = require('./3-payment');
const sinon = require("sinon");
const Utils = require('./utils');

describe('sendPaymentRequestToApi', function () {
  describe('sendPaymentRequestToApi', function () {
      it('sendPaymentRequestToApi', function () {

        const s = sinon.spy(Utils, "calculateNumber");
        sendPaymentRequestToApi(1.0, 112.0);
        expect(s.calledWith('SUM', 1.0, 112.0)).to.be.true;
        s.restore();
      });
  });
});

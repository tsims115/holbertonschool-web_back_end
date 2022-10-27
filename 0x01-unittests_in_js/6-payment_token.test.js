const chai = require("chai");
const expect = chai.expect;
chai.use(require("chai-as-promised"));
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('payment function', function () {
  describe('getPaymentTokenFromAPI', function () {
      it('getPaymentTokenFromAPI', function (done) {
        expect(getPaymentTokenFromAPI(true)).to.eventually.equal({data: 'Successful response from the API' });
        done();
      });
  });
});

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('returns the right success message', (done) => {
    getPaymentTokenFromAPI(true).then(({ data }) => {
      expect(data).to.equal('Successful response from the API');
      done();
    });
  });
});

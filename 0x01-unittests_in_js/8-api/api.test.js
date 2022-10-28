const { expect } = require('chai');
const request = require('request');

describe('test suite', () => {
  it('test GET', () => new Promise((done) => {
    request('http://localhost:7865/', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      expect(response.request.method).to.be.equal('GET');
      done();
    });
  }));
});

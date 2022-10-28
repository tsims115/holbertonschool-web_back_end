const { expect } = require('chai');
const request = require('request');
const sinon = require('sinon');

describe('Test the response from app', () => {
  cspy = sinon.spy(console, "log");
  it('returns the right success message', () => {
    
    request('http://localhost:7865', function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal("Welcome to the payment system");
    });

  });
});

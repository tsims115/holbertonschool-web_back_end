const { expect } = require('chai');
const request = require('request');
const sinon = require('sinon');

describe('Test the response from app', () => {
  it('returns the right success message', () => {
    
    request('http://localhost:7865', function (error, response, body) {
    console.log('statusCode:', response && response.statusCode);
    console.log('body:', body);
    });
    expect(cspy.calledWith("API available on localhost port 7865")).to.be.true;
  });
});

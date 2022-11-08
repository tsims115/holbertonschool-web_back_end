import createPushNotificationsJobs from './8-job.js';
const kue = require('kue');
const chai = require("chai");
const expect = chai.expect;
const assert = require('assert');

const queue = kue.createQueue();

const list = [
  {
      phoneNumber: '4153518780',
  message: 'This is the code 1234 to verify your account'
  }
];

describe('createPushNotificationsJobs', function () {
  before(() => {
    queue.testMode.enter();
  });
  
  afterEach(() => {
    queue.testMode.clear();
  });
  
  after(() => {
    queue.testMode.exit()
  });

  it('display an error message if jobs is not an array', function () {
    createPushNotificationsJobs(list, queue);
    expect(() => createPushNotificationsJobs(1, queue)).to.throw(Error);
    expect(queue.testMode.jobs.length).to.equal(1);
  });
  
  it('create two new jobs to the queue', function () {
    queue.createJob('TestJob', { Job: 'This is a test' }).save();
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('TestJob');
    expect(queue.testMode.jobs[0].data).to.eql({ Job: 'This is a test' });
  });
});



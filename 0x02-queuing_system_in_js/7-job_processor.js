const kue = require('kue'), queue = kue.createQueue();

const blacklist = ['4153518780', '4153518781'];
function sendNotification(phoneNumber, message, job, done) {
  if (blacklist.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    next(0);
    done();
  }

  function next(i) {
    job.progress(i, 2);
    if (i == 1) done()
    else next(i + 1);
  }

}

queue.process('push_notification_code_2', function(job, done){
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
  });

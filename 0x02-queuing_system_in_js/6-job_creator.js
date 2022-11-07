const kue = require('kue'), queue = kue.createQueue();
const data = {
  phoneNumber: "918-111-1241",
  message: "This is a test",
}
const job = queue.create('push_notification_code', data)
.save( function(err){
  if( !err ) {
    console.log(`Notification job created: ${job.id}`);
  }
}).on('complete', function(result) {
  console.log('Notification job completed')
}).on('failed', function(err) {
  console.log('Notification job failed');
});

module.exports = function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  } else {
    for (const val of jobs){
      try {
      let job = queue.create('push_notification_code_3', val)
      .save( function(err){
        if( !err ) {
          console.log(`Notification job created: ${job.id}`);
        }
      }).on('complete', function(result) {
        console.log(`Notification job ${job.id} completed`)
      }).on('failed', function(err) {
        console.log(`Notification job ${job.id} failed: ${err}`);
      }).on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`)
      });
    } catch(err) {}
    }
  }
}

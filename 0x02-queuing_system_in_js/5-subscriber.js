import redis from 'redis'
const client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error}`);
}).on('message', function(channel, msg) {
  if (msg === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  } else {
    console.log(msg);
  }
});

client.subscribe('holberton school channel');

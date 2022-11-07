import redis from 'redis'
const client = redis.createClient();

const data = {
  'Portland' : 50,
  'Seattle' : 80,
  'New York' : 20,
  'Bogota' : 20,
  'Cali' : 40,
  'Paris' : 2
}

let i;

client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

for (const [k, v] of Object.entries(data)) {
  client.hset('HolbertonSchools', k, v, redis.print);
}

client.hgetall("HolbertonSchools", function(err, value) {
  console.log(value);
});

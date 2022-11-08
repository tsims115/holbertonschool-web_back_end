import redis from 'redis'
const client = redis.createClient();
const util = require('util');

client.on('connect', function() {
  console.log('Redis client connected to the server');
}).on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  return () => {
    client.set(schoolName, value, redis.print);
  };
}

async function displaySchoolValue(schoolName) {
  console.log(await util.promisify(client.get).bind(client)(schoolName));
};

displaySchoolValue("Holberton");
setNewSchool('HolbertonSanFrancisco', '100')();
displaySchoolValue('HolbertonSanFrancisco');

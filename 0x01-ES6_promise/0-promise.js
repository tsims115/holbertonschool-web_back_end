export default function getResponseFromAPI() {
  const myPromsie = new Promise((resolve, reject) => {
    resolve('resolved');
    reject(Error('Error'));
  });
  return myPromsie;
}

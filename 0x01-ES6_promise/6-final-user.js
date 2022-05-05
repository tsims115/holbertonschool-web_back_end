import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignUp(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);
  async function promiseFunct() {
    const settlesPromises = await Promise.allSettled([userPromise, photoPromise]).then((results) => results);
    return settlesPromises;
  }
  return promiseFunct();
}
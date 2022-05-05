import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignUp(firstName, lastName, fileName) {
  const u = signUpUser(firstName, lastName);
  const p = uploadPhoto(fileName);
  async function promiseFunct() {
    const settlesPromises = await Promise.allSettled([u, p],).then((results) => results);
    return settlesPromises;
  }
  const promise = promiseFunct();
  return promise;
}

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignUp(firstName, lastName, fileName) {
  const use = signUpUser(firstName, lastName);
  const phot = uploadPhoto(fileName);
  async function f1() {
    const prom = await Promise.allSettled([use, phot]).then((result) => result);
    return prom;
  }
  const prom = f1();
  return prom;
}

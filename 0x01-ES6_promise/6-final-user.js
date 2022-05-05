import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return await Promise.allSettled([signUpUser(firstName), uploadPhoto(fileName)])
    .then((results) => results);
}

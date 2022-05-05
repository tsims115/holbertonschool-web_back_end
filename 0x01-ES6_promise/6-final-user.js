import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const settledPromises = await Promise.allSettled([signUpUser(firstName), uploadPhoto(fileName)]).then((results) => results);
  return settledPromises;
}

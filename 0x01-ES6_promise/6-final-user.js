import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const settledPromises = await Promise.allSettled(
    [signUpUser(firstName, lastName), uploadPhoto(fileName)],
  )
    .then((results) => results);
  const obj = settledPromises[1];
  obj.reason = obj.reason.toString();
  obj.value = obj.reason;
  delete obj.reason;
  return settledPromises;
}

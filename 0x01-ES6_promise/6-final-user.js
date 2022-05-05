import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  uploadPhoto(fileName);
  return await signUpUser(firstName, lastName);
}

import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return [
    await signUpUser(firstName, lastName)
      .then((response) => ({
        status: 'success',
        response,
      }))
      .catch((response) => ({
        status: 'unsuccessful',
        value: response.ToString(),
      })),
    await uploadPhoto(fileName)
      .then((response) => ({
        status: 'success',
        response,
      }))
      .catch((response) => ({
        status: 'unsuccessful',
        value: response.ToString(),
      })),
  ];
}

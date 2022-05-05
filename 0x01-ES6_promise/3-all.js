import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  uploadPhoto()
    .then(
      (result) => { process.stdout.write(result.body); },
    )
    .catch(
      () => { console.log('Signup system offline'); },
    );
  createUser()
    .then(
      (result) => {
        process.stdout.write(` ${result.firstName} `);
        process.stdout.write(`${result.lastName}\n`);
      },
    )
    .catch(
      () => { console.log('Signup system offline'); },
    );
}

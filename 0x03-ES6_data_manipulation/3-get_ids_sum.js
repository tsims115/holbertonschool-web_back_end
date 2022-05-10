export default function getStudentIdsSum(studentList) {
  return studentList.reduce((ps, cs) => ps + cs.id, 0);
}

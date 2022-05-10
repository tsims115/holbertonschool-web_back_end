export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList.map((s) => {
    let grade = newGrades.filter((g) => g.studentId === s.id);
    if (grade.length === 0) {
      grade = 'N/A';
    } else {
      grade = grade[0].grade;
    }
    return { ...s, grade };
  });
}

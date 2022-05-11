export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const newList = studentList.filter((s) => s.location === city);
  return newList.map((s) => {
    let grade = newGrades.filter((g) => g.studentId === s.id);
    if (grade.length === 0) {
      grade = 'N/A';
    } else {
      grade = grade[0].grade;
    }
    return { ...s, grade };
  });
}

export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments(allEmp) {
      return Object.keys(this.allEmployees).length;
    },
  };
}

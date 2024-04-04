// LeetCode Problem 181: Employees Earning More Than Their Managers

// Sample input data (as command line arguments):
// node employees.js 1 Joe 70000 3 2 Henry 80000 4 3 Sam 60000 Null 4 Max 90000 Null

// Parse command line arguments
const args = process.argv.slice(2);
const employees = [];

for (let i = 0; i < args.length; i += 4) {
  const id = parseInt(args[i]);
  const name = args[i + 1];
  const salary = parseInt(args[i + 2]);
  const managerId = args[i + 3] === "Null" ? null : parseInt(args[i + 3]);

  employees.push({ id, name, salary, managerId });
}

// Find employees earning more than their managers
const result = employees.filter((emp) => {
  if (emp.managerId === null) return false; // Skip employees without managers
  const manager = employees.find((mgr) => mgr.id === emp.managerId);
  return emp.salary > manager.salary;
});

// Print the result
console.log("Employees earning more than their managers:");
result.forEach((emp) => console.log(emp.name));
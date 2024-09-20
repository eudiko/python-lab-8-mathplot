import numpy as np

# Define the structured array data type
employee_dtype = np.dtype([
    ('Employee_ID', np.int32),
    ('Department', 'U20'),
    ('Years_of_Experience', np.float32),
    ('Projects_Completed', np.int32),
    ('Client_Satisfaction_Rating', np.float32)
])

# Generate random data for 20 employees
np.random.seed(42)  # For reproducibility

departments = ['Engineering', 'HR', 'Marketing', 'Sales', 'Finance']
employees = np.array([
    (i+1,
     np.random.choice(departments),
     round(np.random.uniform(0, 15), 1),
     np.random.randint(1, 21),
     round(np.random.uniform(1.0, 5.0), 1))
    for i in range(20)
], dtype=employee_dtype)

# (b) Function to filter employees by department
def filter_by_department(department):
    return employees[employees['Department'] == department]

# (c) Identify the employee with the highest Client Satisfaction Rating
def employee_with_highest_rating():
    max_rating_index = np.argmax(employees['Client_Satisfaction_Rating'])
    return employees[max_rating_index]

# (d) Calculate the average number of projects completed and years of experience
def calculate_averages():
    avg_projects = np.mean(employees['Projects_Completed'])
    avg_experience = np.mean(employees['Years_of_Experience'])
    return avg_projects, avg_experience

# (e) Identify employees with less than 2 years of experience
def employees_with_less_experience(years=2):
    return employees[employees['Years_of_Experience'] < years]

# Example usage:
print("Employee Data:")
print(employees)

# Filter employees from 'Engineering' department
engineering_employees = filter_by_department('Engineering')
print("\nEmployees in Engineering Department:")
print(engineering_employees)

# Employee with the highest Client Satisfaction Rating
top_rated_employee = employee_with_highest_rating()
print("\nEmployee with the highest Client Satisfaction Rating:")
print(top_rated_employee)

# Calculate averages
avg_projects, avg_experience = calculate_averages()
print(f"\nAverage Projects Completed: {avg_projects}")
print(f"Average Years of Experience: {avg_experience}")

# Employees with less than 2 years of experience
inexperienced_employees = employees_with_less_experience()
print("\nEmployees with less than 2 years of experience:")
print(inexperienced_employees)

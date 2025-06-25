import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample employee data
num_records = 1000

employee_ids = np.arange(1001, 1001 + num_records)
names = [f'Employee_{i}' for i in range(1, num_records + 1)]
departments = np.random.choice(['IT', 'HR', 'Finance', 'Marketing', 'Sales', 'Operations'], num_records)
ages = np.random.randint(22, 60, num_records)
salaries = np.random.randint(45000, 150000, num_records)
experience = np.random.randint(1, 40, num_records)
performance_score = np.random.randint(1, 6, num_records)
joining_dates = pd.date_range(start="2000-01-01", periods=num_records, freq='D')

# Create DataFrame
employee_data = pd.DataFrame({
    'Employee_ID': employee_ids,
    'Name': names,
    'Department': departments,
    'Age': ages,
    'Salary': salaries,
    'Experience_Years': experience,
    'Performance_Score': performance_score,
    'Joining_Date': joining_dates
})

# Save as CSV
employee_data.to_csv("employee_data.csv", index=False)
print("Employee dataset saved as 'employee_data.csv'.")

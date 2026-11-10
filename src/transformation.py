from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "processed"

def transform_data(df):
    clean = df.copy()
    clean["employee_name"] = clean["employee_name"].astype("string").str.strip().str.title()
    clean["department_name"] = clean["department_name"].astype("string").str.strip().str.title()
    clean["attendance_date"] = pd.to_datetime(clean["attendance_date"]).dt.strftime("%Y-%m-%d")
    clean["present"] = (clean["status"] == "Present").astype(int)
    clean["absent"] = (clean["status"] == "Absent").astype(int)
    clean["leave"] = (clean["status"] == "Leave").astype(int)
    employee = clean.groupby(["employee_id", "employee_name", "department_id", "department_name"], as_index=False).agg(
        days_present=("present", "sum"), days_absent=("absent", "sum"),
        days_on_leave=("leave", "sum"), total_recorded_days=("status", "count"))
    employee["attendance_percentage"] = (employee["days_present"] / employee["total_recorded_days"] * 100).round(2)
    department = employee.groupby(["department_id", "department_name"], as_index=False).agg(
        employee_count=("employee_id", "nunique"), days_present=("days_present", "sum"),
        days_absent=("days_absent", "sum"), days_on_leave=("days_on_leave", "sum"),
        total_recorded_days=("total_recorded_days", "sum"))
    department["attendance_percentage"] = (department["days_present"] / department["total_recorded_days"] * 100).round(2)
    return employee, department

def save_outputs(employee, department):
    OUT.mkdir(parents=True, exist_ok=True)
    employee.to_csv(OUT / "hr_employee_summary.csv", index=False)
    department.to_csv(OUT / "hr_department_summary.csv", index=False)
    print("Transformation complete: summary reports saved")

if __name__ == "__main__":
    from src.integration import integrate_data
    from src.validation import validate_data
    data = integrate_data()
    validate_data(data)
    save_outputs(*transform_data(data))

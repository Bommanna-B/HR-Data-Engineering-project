from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"

def integrate_data():
    employees = pd.read_csv(RAW / "employees.csv")
    departments = pd.read_csv(RAW / "departments.csv")
    attendance = pd.read_csv(RAW / "attendance.csv")
    employee_dept = employees.merge(departments, on="department_id", how="left", validate="many_to_one")
    integrated = attendance.merge(employee_dept, on="employee_id", how="left", validate="many_to_one")
    OUT.mkdir(parents=True, exist_ok=True)
    integrated.to_csv(OUT / "hr_integrated.csv", index=False)
    print(f"Integration complete: {len(integrated)} attendance rows")
    return integrated

if __name__ == "__main__":
    integrate_data()

import pandas as pd

VALID_STATUSES = {"Present", "Absent", "Leave"}

def validate_data(df):
    required = ["employee_id", "employee_name", "department_id", "department_name", "attendance_date", "status"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df.empty:
        raise ValueError("No attendance records found")
    if df[required].isna().any().any():
        raise ValueError("Required HR fields contain blanks or unmatched IDs")
    if not df["status"].isin(VALID_STATUSES).all():
        raise ValueError("Invalid attendance status; use Present, Absent, or Leave")
    if pd.to_datetime(df["attendance_date"], errors="coerce").isna().any():
        raise ValueError("Invalid attendance date")
    if df.duplicated(["employee_id", "attendance_date"]).any():
        raise ValueError("Duplicate attendance record for an employee and date")
    print("Validation successful: all checks passed")

if __name__ == "__main__":
    from src.integration import integrate_data
    validate_data(integrate_data())

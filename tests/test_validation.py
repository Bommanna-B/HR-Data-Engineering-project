import pandas as pd
import pytest
from src.validation import validate_data

def sample():
    return pd.DataFrame([{
        "employee_id": 1001, "employee_name": "Ananya Rao",
        "department_id": 10, "department_name": "Technology",
        "attendance_date": "2026-10-01", "status": "Present"
    }])

def test_valid_record_passes():
    validate_data(sample())

def test_invalid_status_fails():
    df = sample()
    df.loc[0, "status"] = "Holiday"
    with pytest.raises(ValueError, match="Invalid attendance status"):
        validate_data(df)

def test_duplicate_employee_date_fails():
    df = pd.concat([sample(), sample()], ignore_index=True)
    with pytest.raises(ValueError, match="Duplicate attendance"):
        validate_data(df)

def test_missing_employee_name_fails():
    df = sample()
    df.loc[0, "employee_name"] = None
    with pytest.raises(ValueError, match="blanks"):
        validate_data(df)

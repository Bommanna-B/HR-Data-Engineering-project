from src.integration import integrate_data
from src.validation import validate_data
from src.transformation import transform_data, save_outputs, OUT

def run_pipeline():
    print("=== HR DATA PIPELINE STARTED ===")
    integrated = integrate_data()
    validate_data(integrated)
    integrated.to_csv(OUT / "hr_validated.csv", index=False)
    employee, department = transform_data(integrated)
    save_outputs(employee, department)
    print("=== HR DATA PIPELINE COMPLETED ===")

if __name__ == "__main__":
    run_pipeline()

# HR Data Engineering Project

A beginner-friendly end-to-end project using Python and pandas. It integrates employee, department, and attendance CSV files; validates data quality; transforms the data; and writes HR summary reports. All sample records are fictional.

## Open and run in VS Code (Windows)
1. Extract this ZIP.
2. VS Code -> File -> Open Folder -> select `hr_data_engineering_project`.
3. Terminal -> New Terminal. Make sure terminal is at the project root (contains `src`, `data`, `tests`).
4. In PowerShell run:

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m src.pipeline
```

If activation is blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
For Command Prompt use `.venv\Scripts\activate.bat`.

## Expected output
- `data/processed/hr_integrated.csv`: joined data
- `data/processed/hr_validated.csv`: validated records
- `data/processed/hr_employee_summary.csv`: employee attendance report
- `data/processed/hr_department_summary.csv`: department attendance report

Run tests:
```powershell
python -m pytest -v
```

Run individual stages from project root:
```powershell
python -m src.integration
python -m src.validation
python -m src.transformation
```

## Project structure
```text
hr_data_engineering_project/
├── data/raw/       # employees.csv, departments.csv, attendance.csv
├── data/processed/ # generated reports
├── src/            # integration, validation, transformation, pipeline
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## GitHub: push this folder
1. Sign in to https://github.com and choose **+ > New repository**.
2. Name it `hr-data-engineering-project`. Choose Public or Private.
3. Leave **Add a README**, `.gitignore`, and license unchecked (this folder already has files). Click Create repository.
4. Copy the repository HTTPS URL.
5. In VS Code, open this extracted project folder. Open Terminal > New Terminal.
6. Confirm you are in the correct folder:
```powershell
pwd
dir
```
You should see `README.md`, `src`, `data`, and `tests`.
7. Configure Git once per computer (use your own details):
```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```
8. From the project root run these commands, replacing the URL with the exact URL copied from GitHub:
```powershell
git init
git add .
git status
git commit -m "Initial commit: HR data engineering project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/hr-data-engineering-project.git
git push -u origin main
```
9. Complete GitHub browser sign-in if prompted, then refresh the repository page.

For future changes:
```powershell
git add .
git commit -m "Describe your changes"
git push
```

## Common Git errors
- `src refspec main does not match any`: usually no commit exists yet or you are in the wrong folder. Check `pwd`, then run `git add .` and `git commit -m "Initial commit"` before pushing.
- `remote origin already exists`: use `git remote set-url origin YOUR-REPOSITORY-URL`.
- `repository not found`: check the URL and your repository access.
- `nothing to commit`: no new changes are staged; check `git status`.

## Privacy
All included records are fictional. Never push real employee names, IDs, attendance, medical, bank, or payroll information to a public GitHub repository. Use an approved private company repository and follow company data policies for real HR data.

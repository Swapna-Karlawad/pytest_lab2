from Employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Swapna\n"
        "Employee ID: E1001\n"
        "Department: BCA\n"
        "Salary: 50000\n"
    )
    assert employee_details("Swapna", "E1001", "BCA", 50000) == expected_output

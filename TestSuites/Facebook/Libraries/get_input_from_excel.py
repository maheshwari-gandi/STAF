from Utilities import xloperations as e


excel_path =r"C:\Users\GANMAHES\RobotPlatform\testcase_file.xlsx"
sheetNo = "Sheet4"


def read_excel_data(testcase):
    username = ''
    password = ''
    for r in range(2, e.getrowcount(excel_path, sheetNo)):
        if e.getcelldata(excel_path, sheetNo, r, 1) == testcase:
            username = e.getcelldata(excel_path, sheetNo, r, 4)
            password = e.getcelldata(excel_path, sheetNo, r, 5)
            break
    return username, password


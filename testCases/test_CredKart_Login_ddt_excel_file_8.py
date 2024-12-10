# import time
#
# import pytest
# from coverage.files import actual_path
# from selenium.webdriver.common.by import By
# from utilities.XLutils import ExcelUtiles
#
# class Test_Credkart_login_DDT:
#     excel_file_path = r"D:\Batch Notes\PythonAutomation\CT20\Python_Pytest_Framework\Test_Data\Test_Data.xlsx"
#     """
#     This class contains test cases for CredKart login functionality using DDT.
#     """
#     @pytest.mark.web
#     @pytest.mark.credkart
#     @pytest.mark.skip
#     def test_CredKart_Login_01(self, driver_setup):
#         self.driver = driver_setup
#         self.driver.get("https://automation.credence.in/login")
#         self.driver.maximize_window()
#         self.rows = ExcelUtiles.RowCount(self.excel_file_path, "CredKart_login_Data")
#         print(f"Number of rows in Excel: {self.rows}")
#         Result_List = []
#         for r in range (2, self.rows+1):
#             print(f"Row number: {r}")
#             self.username= ExcelUtiles.ReadData(self.excel_file_path, "CredKart_login_Data", r, 1)
#             self.password= ExcelUtiles.ReadData(self.excel_file_path, "CredKart_login_Data", r, 2)
#             self.expected_result = ExcelUtiles.ReadData(self.excel_file_path, "CredKart_login_Data", r, 3)
#             print(f"Username: { self.username}")
#             print(f"Password: { self.password}")
#             print(f"Expected_result: { self.expected_result}")
#
#             # Enter the username
#             username = self.driver.find_element(By.ID, "email")
#             username.send_keys(self.username)
#
#             # Enter the password
#             password = self.driver.find_element(By.ID, "password")
#             password.send_keys(self.password)
#
#             # Click the login button
#             self.driver.find_element(By.CLASS_NAME, "btn").click()
#             Actual_Result = "login_fail"
#
#             # Verify that the user is logged in
#             try:
#                 MenuButton = self.driver.find_element(By.CLASS_NAME, "dropdown-toggle")
#                 MenuButton.click()
#                 Logout_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
#                 Logout_button.click()
#                 print("User is logged in")
#                 Actual_Result = "login_pass"
#                 #time.sleep(5)
#             except:
#                 print("User is not logged in")
#
#             if self.expected_result == Actual_Result:
#                 test_case_status= "Pass"
#             else:
#                 test_case_status = "Fail"
#
#             ExcelUtiles.WriteData(self.excel_file_path, "CredKart_login_Data", r, 4, Actual_Result)
#             ExcelUtiles.WriteData(self.excel_file_path, "CredKart_login_Data", r, 5, test_case_status)
#             Result_List.append(test_case_status)
#             self.driver.get("https://automation.credence.in/login")
#
#         print(f"Result_List: {Result_List}")
#         if "Fail" in Result_List:
#             assert False, "Test Case Failed"
import unittest
Login_site = __import__("login")
Log_Out = __import__("logout")
Package_Details = __import__("packages_details")
Sign_UP = __import__("signup")
Change_Password = __import__("change_password")
#Add_Cart = __import__("add_cart")
Check_Out = __import__("check_out")



loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(Login_site))
suite.addTests(loader.loadTestsFromModule(Log_Out))
suite.addTests(loader.loadTestsFromModule(Package_Details))
suite.addTests(loader.loadTestsFromModule(Sign_UP))
suite.addTests(loader.loadTestsFromModule(Change_Password))
#suite.addTests(loader.loadTestsFromModule(Add_Cart))
suite.addTests(loader.loadTestsFromModule(Check_Out))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
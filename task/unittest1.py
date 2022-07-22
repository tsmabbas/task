
try:
    from app import app
    import unittest

except Exception as e:
    print("Some Modules are Missing {} ".format(e))    

class FlaskTest(unittest.TestCase):

    #Check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index1(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index1(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)  

    def test_index1(self):
        tester = app.test_client(self)
        response = tester.get("/sign_up")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)          

if __name__ == "__main__":    
    unittest.main()
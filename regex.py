import re
class RegExpr:
   def __init__(self, data):
       self.data = data



   def email_id(self):
       pattern = "([a-z0-9_.])+\@+([a-z0-9])+(\.)+([a-z]{2,6})"
       if re.match(pattern, self.data):
           return True
       else:
           return False

   # regex for PAN number
   def pan_number(self):
       pattern = "^[A-Za-z]{5}[0-9]{4}[A-Za-z]{1}$"
       if re.match(pattern, self.data):
           return True
       else:
           return False



   # regex for bangladesh mobile numbers
   def bangladesh_mobile_numbers(self):
       pattern = "01[^1-4]\d{8}"
       if re.match(pattern, str(self.data)):
           return True
       else:
           return False


 # regex for alphanumeric password
   def alphanumericpassword(self):
       pattern = "(^[A-Za-z0-9#?!@$%^/&*-]{16}$)"
       if re.match(pattern, str(self.data)):
           return True
       else:
           return False


print(RegExpr("kamalaguvi@gmail.com").email_id())


print(RegExpr("ABCDE1234a").pan_number())


print(RegExpr("01054694200").bangladesh_mobile_numbers())

print(RegExpr("abCDfh//22ij6789").alphanumericpassword())


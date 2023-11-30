import sys
sys.path.append(r'C:\Users\Lym\Documents\GitHub\Selenium-python')
from time import sleep

from v2.seleniumFunctions import seleniumFunctions


# seleniumFunctions.browseSauceDemo()
# seleniumFunctions.safe_clicker('//input[@id="user-name"]', 1, 30, "standard_user")
# seleniumFunctions.safe_clicker('//input[@id="password"]', 1, 30, "secret_sauce")
# seleniumFunctions.safe_clicker('//input[@id="login-button"]', 1, 30, "")
# sleep(10)

seleniumFunctions.browseOrangeHrmLive()
seleniumFunctions.safe_clicker('//input[@name="username"]', 1, 30, "Admin")
seleniumFunctions.safe_clicker('//input[@name="password"]', 1, 30, "admin123")
seleniumFunctions.safe_clicker('//button[text()=" Login "]', 1, 30, "")
sleep(10)

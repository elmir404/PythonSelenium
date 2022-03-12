import imp
import click
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from io import BytesIO
import getpass
#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then
#invoke actual browser
session = "--user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data"
chrome_driver_path ="C:\\Users\\Admin\\Desktop\\screenshoot\\chromedriver.exe"
url="https://www.e-gov.az/az/services/read/3766/0"
opt=Options()
opt.add_argument("--user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default".format(getpass.getuser()))
driver = webdriver.Chrome(executable_path=chrome_driver_path,chrome_options=opt)
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get(url)
#to refresh the browser
driver.refresh()
driver.find_element_by_class_name('loadable-big'),click()
# identifying the logo to capture the screenshot
s= driver.find_element_by_xpath("//img")
# to get the element location
location = s.location
# to get the dimension the element
size = s.size
#to save the screenshot of complete page
p = driver.get_screenshot_as_png("logo_tutorialspoint.png")
#to get the x axis
l = location['x']
#to get the y axis
t = location['y']
# to get the length the element
b = location['y']+size['height']
# to get the width the element
r = location['x']+size['width']
# to open the captured image with PIL
imgOpen = Image.open(BytesIO(p))
# to crop the captured image to size of the logo
imgLogo = p.crop(l, t, r, b)
# to save the cropped image
imgLogo.save("logo_tutorialspoint.png")
#to close the browser
driver.close()

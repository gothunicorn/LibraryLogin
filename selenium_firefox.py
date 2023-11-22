# geckodriver_path = "C:\Program Files\selenium_firefox\geckodriver.exe"

# a. Check if the username field accepts a valid username (accepts text only) and if the
# password field accepts a valid password.
# b. Check if the wrong username and valid password allow access to any specific account.
# c. Check minimum and maximum required length of username and password
# d. Check if the valid username and wrong password allow access to any specific account.
# h. Check if the invalid credentials open the random account.
# j. Check if the logout link function is as expected.
# i. Check if the user is logged in, allows you to log out by using the link at the bottom of
# the application.
# g. Check if the invalid username and password trigger/error warning if any character is
# used other than text.

# e. Check if the forgot username link leads to a username recovery page.
# f. Check if the forgot password link leads to the password recovery page.




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login(username, password):
    # Create a Firefox WebDriver instance
    options = webdriver.FirefoxOptions()
    options.set_preference("executable_path", "path")
    driver = webdriver.Firefox(options=options)

    # Open the Streamlit login page
    driver.get("http://localhost:8501")  # Adjust the URL based on your Streamlit app's address

    # Find and fill in the username and password fields
    username_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[3]/div/div[1]/div/input'))
    )
    username_field.send_keys(username)

    password_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[4]/div/div[1]/div/input')
    password_field.send_keys(password)

    # Click the login button
    login_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[5]/div/button')
    login_button.click()

    # Wait for a few seconds to see the result (adjust as needed)
    time.sleep(1)

    # Check for the expected messages
    if "Login successful" in driver.page_source:
        print("Login successful!")
        logout_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[7]/div/button')
        logout_button.click()
        print("Logout successful!")
    elif "Invalid login credentials" in driver.page_source:
        print("Invalid login credentials error message displayed.")
    else:
        print("Unexpected result.")

    # Close the browser
    driver.quit()


def test_register(username, password, phno, email, secpass):
    # Create a Firefox WebDriver instance
    options = webdriver.FirefoxOptions()
    options.set_preference("executable_path", "path")
    driver = webdriver.Firefox(options=options)

    # Open the Streamlit login page
    driver.get("http://localhost:8501")  # Adjust the URL based on your Streamlit app's address

    wait = WebDriverWait(driver, 5)
    register_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div[2]/div/div/label[2]/div[2]/div/p')))
    register_button.click()

    wait = WebDriverWait(driver, 5)
    register_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div[2]/div/div/label[2]/div[2]/div/p')))
    register_button.click()

    # Find and fill in the username and password fields
    username_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[3]/div/div[1]/div/input'))
    )
    username_field.send_keys(username)

    password_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[5]/div/div[1]/div/input')
    password_field.send_keys(password)

    phoneno_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[8]/div/div[1]/div/input')
    phoneno_field.send_keys(phno)

    # Click the login button
    email_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[6]/div/div[1]/div/input')
    email_field.send_keys(email)

    spassword_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[11]/div/div[1]/div/input')
    spassword_field.send_keys(secpass)

    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[12]/div/button')
    submit_button.click()

    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[12]/div/button')
    submit_button.click()

    # Wait for a few seconds to see the result (adjust as needed)
    time.sleep(1)

    # Check for the expected messages
    if "User data successfully submitted!" in driver.page_source:
        print("Registration successful!")
    elif "Not a valid phone number." in driver.page_source:
        print("Invalid phone number error message displayed.")
    elif "Not a valid email address." in driver.page_source: 
        print("Invalid email credentials error message displayed.")
    elif "Username taken." in driver.page_source:
        print("Username taken credentials error message displayed.")
    elif "Invalid Username. The UserName should have only letters and be atleast 5 charachters long" in driver.page_source:
        print("Invalid username credentials error message displayed.")    
    elif "Please fill in all the required fields." in driver.page_source:
        print("All the fields were not inputted")
    else:
        print("Unexpected result.")

    # Close the browser
    driver.quit()


def test_forgot(username, secpass, pword):
    # Create a Firefox WebDriver instance
    options = webdriver.FirefoxOptions()
    options.set_preference("executable_path", "path")
    driver = webdriver.Firefox(options=options)

    # Open the Streamlit login page
    driver.get("http://localhost:8501")  # Adjust the URL based on your Streamlit app's address

    wait = WebDriverWait(driver, 5)
    forgot_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div[2]/div/div/label[3]/div[2]/div/p')))
    forgot_button.click()

    wait = WebDriverWait(driver, 5)
    forgot_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div[2]/div/div/label[3]/div[2]/div/p')))
    forgot_button.click()

    # Find and fill in the username and password fields
    username_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[3]/div/div[1]/div/input'))
    )
    username_field.send_keys(username)

    spassword_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[5]/div/div[1]/div/input')
    spassword_field.send_keys(secpass)

    password_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[6]/div/div[1]/div/input')
    password_field.send_keys(pword)

    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[7]/div/button')
    submit_button.click()

    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[7]/div/button')
    submit_button.click()

    # Wait for a few seconds to see the result (adjust as needed)
    time.sleep(3)

    # Check for the expected messages
    if "User information verified!" in driver.page_source:
        print("Password updation successful!")
    elif "Invalid user information" in driver.page_source:
        print("Invalid user credentials error message displayed.")
    else:
        print("Unexpected result.")

    # Close the browser
    driver.quit()



def test_forgot_username(email, secpass):
    # Create a Firefox WebDriver instance
    options = webdriver.FirefoxOptions()
    options.set_preference("executable_path", "path")
    driver = webdriver.Firefox(options=options)

    # Open the Streamlit login page
    driver.get("http://localhost:8501")  # Adjust the URL based on your Streamlit app's address

    wait = WebDriverWait(driver, 5)
    forgot_username_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div[2]/div/div/label[4]/div[2]/div/p')))
    forgot_username_button.click()

    wait = WebDriverWait(driver, 5)
    forgot_username_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div[2]/div/div/label[4]/div[2]/div/p')))
    forgot_username_button.click()

    # Find and fill in the username and password fields
    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[3]/div/div[1]/div/input'))
    )
    email_field.send_keys(email)

    spassword_field = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[6]/div/div[1]/div/input')
    spassword_field.send_keys(secpass)

    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[7]/div/button')
    submit_button.click()

    submit_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[7]/div/button')
    submit_button.click()

    # Wait for a few seconds to see the result (adjust as needed)
    time.sleep(3)

    # Check for the expected messages
    if "User information verified!" in driver.page_source:
        print("Username retrieval successful!")
    elif "Invalid user information" in driver.page_source:
        print("Invalid user credentials error message displayed.")
    else:
        print("Unexpected result.")

    # Close the browser
    driver.quit()



if __name__ == "__main__":

    test_login("richard", "rich")      #valid username and password
    test_login("abcdefg", "456")      #invalid username and password
    test_login("richard", "123")        #valid username and invalid password 

    test_register("ric", "richa", "1234567520", "richa@gmail.com", "doggo")     #Invalid user name
    test_register("richa", "richa", "1234567520", "richa@gmail", "doggo")      #Invalid email
    test_register("richa", "richa", "123jj45", "richa@gmail.com", "doggo")        #Invalid phone number  
    test_register("richa", "richa", "1234567520", "richa@gmail.com", "doggo")   #All valid
    test_register("richa", "richa", "1234567520", "richa@gmail.com", "doggo")   #Username taken

    test_forgot("richa","doggo","riri")     #Sucessful updation
    test_login("richa","riri")              #Sucessful login
    test_forgot("richa","abcd","qwert")     #Unsucessful updation
    test_login("richa","qwert")             #Unsucessful login

    test_forgot_username("richa@gmail.com","doggo")     #Sucessful retrieval
    test_forgot_username("ri@gmail.com","doggo")        #Invalid retrieval
    test_forgot_username("richa@gmail.com","d")         #Invalid retrieval

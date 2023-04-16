import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def extract_page_num():
    # Open the CSV file and read the data
    with open('Untitled.csv', encoding="utf8") as file:
        reader = csv.reader(file)
        column_list = []

        # Iterate over each row in the CSV file
        for row in reader:
            # Append the value in the first column to the list
            column_list.append(row[1])

    # Print the list of column values
    return column_list
def main(url):  
  # Create a new instance of the Safari driver
  driver = webdriver.Chrome()
  # Navigate to the web page
  driver.get(url)
  driver.maximize_window()
  time.sleep(5)
  def main_page():
    # Wait for the page to load
    # Find the login link element using XPath
    # <a href="/login" class="btn btn-primary btn-sm">Login</a>
    login_link = driver.find_element(By.XPATH, "//a[@href='/login' and @class='btn btn-primary btn-sm']")
    # Click the login link
    login_link.click()  
  def login_page():
      print('login_page_start')
      name = 'fares@jana-sa.org'
      password = 'Jana@2023'
      search_el = driver.find_element("id", "login_email")
      search_el.send_keys(name)
      # Password
      """
      <input name="password" type="text">
      """
      time.sleep(1)
      search_el1 = driver.find_element("id", "login_password")
      search_el1.send_keys(password)
      # Click
      """
      <button type="submit" />
      """
      time.sleep(1)
      submit_btn_el = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
      submit_btn_el.click()
      time.sleep(8)   
  def finance_page():
      # Find the button element

      div_element = driver.find_element(By.XPATH, '//*[@id="page-Form/Finance"]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/button')
      div_element.click()
      time.sleep(2)
      sub_div_element = driver.find_element(By.XPATH, '//*[@id="page-Form/Finance"]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/ul/li[1]/a')
      sub_div_element.click()  
  main_page()
  login_page()
  finance_page()
  time.sleep(10)
  print("process done")
# Close the driver and end the session
  driver.quit()
extracted_num = extract_page_num()
my_list = extracted_num
my_list.pop(0)

for list in my_list:
    url = f"https://jana.is.sa/desk#Form/Finance/{list}"

    if __name__ == "__main__":
        main(url)
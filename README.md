# Web Scraping with Selenium - Finance Data Extraction

This Python script utilizes the Selenium library to perform web scraping and extract finance data from a web page. The script interacts with a website, logs in, and navigates to the finance section to extract the required information. 

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python (version 3.x)
- Selenium library (`pip install selenium`)
- ChromeDriver (compatible with your Chrome browser version)

## Usage

1. Clone this repository or download the script file (`script.py`) to your local machine.

2. Ensure that you have the required CSV file (`Untitled.csv`) in the same directory as the script. The CSV file should contain the necessary data for navigation.

3. Update the login credentials in the `login_page()` function. Replace the `name` and `password` variables with your actual login details.

4. Run the script using the command: `python script.py`

   The script will iterate over the rows in the CSV file, extract the page URLs, and perform the following steps for each URL:

   - Open a Chrome browser window.
   - Navigate to the provided URL.
   - Log in using the specified credentials.
   - Access the finance section.
   - Wait for the data to load.
   - Perform any necessary data extraction or manipulation.

   The extracted finance data will be printed to the console.

5. After the script finishes processing all URLs, it will automatically close the browser window.

## Note

- Make sure to download and place the appropriate ChromeDriver executable in the same directory as the script. You can download the ChromeDriver from the official Selenium website (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference).

- The script uses a CSS selector and XPath to locate elements on the web page. If the structure of the target website changes, you may need to update these selectors accordingly.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to the terms of the license.

## Disclaimer

Please use this script responsibly and in compliance with the website's terms of service. Web scraping may be subject to legal restrictions or limitations.

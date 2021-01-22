
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By



def wait_for_id(browser, el_id, timeout = 10):
    ## timeout for finding element in browser  by their ids
    
    try:
        element_present = EC.presence_of_element_located((By.ID, el_id))
        WebDriverWait(browser, timeout).until(element_present)

        return True

    except:
        print(f"Can't Find after Waiting for element with id {el_id}")
        return False
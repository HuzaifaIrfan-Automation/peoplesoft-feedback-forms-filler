



## login to nust cms

##############################################################################################################
#########################################  Logging in to Nust Cms  ###################################
##############################################################################################################

from ..wait_for import wait_for_id

from .credentials import username, password


def login_cms(browser):
    wait_for_id(browser,'userid')

    user_input_box = browser.find_element_by_id('userid')
    user_input_box.send_keys(username)

    user_input_box = browser.find_element_by_id('pwd')
    user_input_box.send_keys(password)

    browser.find_element_by_class_name('psloginbutton').click()


    print("Logging in to CMS")

    return True

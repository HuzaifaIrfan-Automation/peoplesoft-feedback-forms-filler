
##############################################################################################################
#########################################  Getting Iframe Url from Form   ###################################
##############################################################################################################


forms_tables_url='https://cms.nust.edu.pk/psp/ps/EMPLOYEE/PSFT_HR/c/QA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL?FolderPath=PORTAL_ROOT_OBJECT.FEED_BACK_FORMS.QA_FEEDBACK_FORMS.QA_STNDT_MANAGE_CO_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder'


def open_forms_tables_view(browser):

    
    browser.get(forms_tables_url)
    print("Opening the Forms Tables Page")



    #find iframe element and url
    iframe_el = browser.find_element_by_css_selector("iframe")

    iframe_url=iframe_el.get_attribute('src')

    print("Open the Iframe of the URL")

    # go to actual form
    browser.get(iframe_url)
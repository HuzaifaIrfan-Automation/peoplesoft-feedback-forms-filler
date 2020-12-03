
from selenium import webdriver      
  
# For using sleep function because selenium  
# works only when the all the elements of the  
# page is loaded. 
import time  

from selenium.webdriver import Firefox

from selenium.webdriver.firefox.options import Options
   
from selenium.webdriver.common.keys import Keys  



from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# opts = Options()
# opts.set_headless()
# assert opts.headless  # Operating in headless mode

#  browser = Firefox(options=opts)

browser = Firefox()

from credentials import username, password

from settings import cms_url, form_url, checking_el_set, button_label, Feed_Back_Message, form_filling, total_rows







##############################################################################################################
#########################################  Setting That You can Alter with ###################################
##############################################################################################################


# username=""

# password=""



# url="https://cms.nust.edu.pk/psp/ps/?cmd=login&languageCd=ENG&"

# url='https://cms.nust.edu.pk/psp/ps/EMPLOYEE/PSFT_HR/c/STDNT_BIO_DATA.STDNT_BIO_DATA.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.STDNT_BIO_DATA_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder&cmd=login&errorCode=105'

# cms_url='https://cms.nust.edu.pk/'





# # iframe el url student teacher course evaluation form
# # multi_form_iframe_url='https://cms.nust.edu.pk/psc/ps/EMPLOYEE/PSFT_HR/c/QA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL?FolderPath=PORTAL_ROOT_OBJECT.FEED_BACK_FORMS.QA_FEEDBACK_FORMS.QA_STNDT_MANAGE_CO_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder&PortalActualURL=https%3a%2f%2fcms.nust.edu.pk%2fpsc%2fps%2fEMPLOYEE%2fPSFT_HR%2fc%2fQA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL&PortalContentURL=https%3a%2f%2fcms.nust.edu.pk%2fpsc%2fps%2fEMPLOYEE%2fPSFT_HR%2fc%2fQA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL&PortalContentProvider=PSFT_HR&PortalCRefLabel=Feedback%20Forms&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fcms.nust.edu.pk%2fpsp%2fps%2f&PortalURI=https%3a%2f%2fcms.nust.edu.pk%2fpsc%2fps%2f&PortalHostNode=HRMS&NoCrumbs=yes&PortalKeyStruct=yes'

# # 
# # single_form_url='https://cms.nust.edu.pk/psp/ps_3/EMPLOYEE/PSFT_HR/c/QA_FB_STD_ON_PG.QA_SCOE_FORM.GBL'



# # form url student teacher course evaluation form
# form_url='https://cms.nust.edu.pk/psp/ps/EMPLOYEE/PSFT_HR/c/QA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL?FolderPath=PORTAL_ROOT_OBJECT.FEED_BACK_FORMS.QA_FEEDBACK_FORMS.QA_STNDT_MANAGE_CO_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder'



# # set checking_el_set value below
# # Excellent = -1
# # Very Good = 0
# # Good = 1
# # Average = 2
# # Poor = 3

# #set this value to any of above to send to every row and every form
# checking_el_set=0





# # button_label
# # 'Submit' for  Student Teacher Evaluation Form
# # 'Save' for Other FeedBack Forms

# button_label="Submit"



# # set Feed_Back_Message that is to be send to every form
# Feed_Back_Message="...."




# # form_filling = 0 for single form
# # form_filling = 1 for Multi forms

# form_filling=0



# # set this for checking and pressing of submit etc button
# # 20 for student course evaluation

# total_rows=20








##############################################################################################################
#########################################  Other Code ###################################
##############################################################################################################



print("Opening CMS")



browser.get(cms_url)





def wait_for_el_by_id_present(el_id):
    ## timeout for finding element in browser  by their ids
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.ID, el_id))
        WebDriverWait(browser, timeout).until(element_present)

    except:
        print(f"Can't Find after Waiting for element with id {el_id}")



## login to nust cms

##############################################################################################################
#########################################  Logging in to Nust Cms  ###################################
##############################################################################################################


wait_for_el_by_id_present('userid')

user_input_box = browser.find_element_by_id('userid')
user_input_box.send_keys(username)

user_input_box = browser.find_element_by_id('pwd')
user_input_box.send_keys(password)

browser.find_element_by_class_name('psloginbutton').click()


print("Logging in to CMS")




##############################################################################################################
#########################################  Getting Iframe Url from Form   ###################################
##############################################################################################################



browser.get(form_url)
print("Opening the Form")



#find iframe element and url
iframe_el = browser.find_element_by_css_selector("iframe")

iframe_url=iframe_el.get_attribute('src')

print("Getting iframe Url")

# go to actual form
browser.get(iframe_url)






##############################################################################################################
#########################################  Single Form Filling Code  ###################################
##############################################################################################################


radio_button_in_each_row=5

# if the url of the form is single
def single_form_filling():
    rate=0  


    el_checked=checking_el_set


    print(f'Filled Text Area with {Feed_Back_Message}')

    TextBox_msg=Feed_Back_Message

    TextBox_el = browser.find_element_by_css_selector("textarea.PSLONGEDITBOX")

    TextBox_el.send_keys(TextBox_msg)


    while True:

        row_checked=0

        elements = browser.find_elements_by_css_selector(".PSRADIOBUTTON[type = 'radio']")

        # parentElements = browser.find_elements_by_class_name("PSRADIOBUTTON")
        
        try:

            for i,el in enumerate(elements):
                checked=el.get_attribute("checked")
                
                if checked:
                    print("Already Checked")

                    row_checked=row_checked+1

                else:
                    if(el_checked<i):
                        el_checked=el_checked+radio_button_in_each_row
                        el.click()
                        break


        except:
            pass





        print(f"{row_checked} Rows Filled")

        submit_button_clicked=False


        if row_checked >= total_rows:

            

            buttons = browser.find_elements_by_css_selector("input[type = 'button']")

            for i, button in enumerate(buttons):

                print(f'{button.get_attribute("value")} Button Found')

                # if button.get_attribute("value") == "Submit":
                if button.get_attribute("value") == button_label:

                    print(f'clicking {button_label} button')


                    button.click()
                    submit_button_clicked=True

                    break

        if submit_button_clicked:
            break



##############################################################################################################
#########################################  Multi to Single Form Filling Code  ###################################
##############################################################################################################



def multi_form_filling():


    i=0

    



    while(True):
        # win0divQA_FB_TEF_MT_VW_QA_FB_SUBMITTED$0
        submit_status_id= f"QA_FB_TEF_MT_VW_QA_FB_SUBMITTED${i}"



        # submit_status_id="win0divQA_FB_TEF_MT_VW_QA_FB_SUBMITTED$0"


        wait_for_el_by_id_present(submit_status_id)

        
        try:

            submit_status = browser.find_element_by_id(f'{submit_status_id}')

            # print(submit_status.text)

            if(submit_status.text=="Yes"):
                print("Form Already Filled")

            else:

                print("Form Not Already Filled")

                view_form_button_id=f'QA_FB_TEF_MT_VW_SSR_COMPONENT${i}'

                submit_button = browser.find_element_by_id(f'{view_form_button_id}')

                submit_button.click()

                single_form_filling()

        except:
            print('Cannot Find Any other Form to be Filled Closing...')
            break


                


        i=i+1






if form_filling == 0:
    single_form_filling()

elif form_filling == 1 :
    multi_form_filling()



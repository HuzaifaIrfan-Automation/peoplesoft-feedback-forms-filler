


##############################################################################################################
#########################################  CMS and Form Url ###################################
##############################################################################################################


cms_url='https://cms.nust.edu.pk/'

# iframe el url student teacher course evaluation form
# multi_form_iframe_url='https://cms.nust.edu.pk/psc/ps/EMPLOYEE/PSFT_HR/c/QA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL?FolderPath=PORTAL_ROOT_OBJECT.FEED_BACK_FORMS.QA_FEEDBACK_FORMS.QA_STNDT_MANAGE_CO_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder&PortalActualURL=https%3a%2f%2fcms.nust.edu.pk%2fpsc%2fps%2fEMPLOYEE%2fPSFT_HR%2fc%2fQA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL&PortalContentURL=https%3a%2f%2fcms.nust.edu.pk%2fpsc%2fps%2fEMPLOYEE%2fPSFT_HR%2fc%2fQA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL&PortalContentProvider=PSFT_HR&PortalCRefLabel=Feedback%20Forms&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fcms.nust.edu.pk%2fpsp%2fps%2f&PortalURI=https%3a%2f%2fcms.nust.edu.pk%2fpsc%2fps%2f&PortalHostNode=HRMS&NoCrumbs=yes&PortalKeyStruct=yes'


# mutli_form_url='https://cms.nust.edu.pk/psp/ps/EMPLOYEE/PSFT_HR/c/QA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL?FolderPath=PORTAL_ROOT_OBJECT.FEED_BACK_FORMS.QA_FEEDBACK_FORMS.QA_STNDT_MANAGE_CO_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder'


# 
# single_form_url='https://cms.nust.edu.pk/psp/ps_3/EMPLOYEE/PSFT_HR/c/QA_FB_STD_ON_PG.QA_SCOE_FORM.GBL'



# form url student teacher course evaluation form
form_url='https://cms.nust.edu.pk/psp/ps/EMPLOYEE/PSFT_HR/c/QA_STNDT_MANAGE_MENU.QA_STNDT_MANAGE_CO.GBL?FolderPath=PORTAL_ROOT_OBJECT.FEED_BACK_FORMS.QA_FEEDBACK_FORMS.QA_STNDT_MANAGE_CO_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder'






##############################################################################################################
######################################### Teachers Ratings ###################################
##############################################################################################################


# set checking_el_set value below
# Excellent = -1
# Very Good = 0
# Good = 1
# Average = 2
# Poor = 3

#set this value to any of above to send to every row and every form
checking_el_set=0






##############################################################################################################
#########################################  Set Button Label for auto submittion of the form ###################################
##############################################################################################################


# button_label
# 'Submit' for  Student Teacher Evaluation Form
# 'Save' for Other FeedBack Forms

button_label="Submit"





##############################################################################################################
#########################################  Feed Back Form Message ###################################
##############################################################################################################

# set Feed_Back_Message that is to be send to every form
Feed_Back_Message="...."





##############################################################################################################
#########################################  Form Filling Settings according to url given ###################################
##############################################################################################################

# form_filling = 0 for single form
# form_filling = 1 for Multi forms

form_filling=1




##############################################################################################################
######################################### Number of rows in a single Form ###################################
##############################################################################################################

# set this for checking and pressing of submit etc button
# 20 for student course evaluation

total_rows=20
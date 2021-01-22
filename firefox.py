



from selenium import webdriver      
  
# For using sleep function because selenium  
# works only when the all the elements of the  
# page is loaded. 
import time  



browser = webdriver.Firefox()

print("NUST CMS FeedBack Form Auto Filler")

print("Using Firefox As Web Driver!!")

from components.cms.open_cms import open_cms

open_cms(browser)





from components.cms.login_cms import login_cms

login_cms(browser)



from components.tables.open_forms_tables_view import open_forms_tables_view

open_forms_tables_view(browser)




from components.tables.process_tables import process_tables

not_all_filled=True

while not_all_filled:

    if process_tables(browser):
        not_all_filled = True
    else:
        not_all_filled = False



print('All Forms Filled!!!')







from ..wait_for import wait_for_id



from .feedback_values import Rate, Feed_Back_Message


def fill_form(browser):



    radio_button_in_each_row=5

    # if the url of the form is single

    wait_for_id(browser,'QA_SCE_FORM_DR_QA_SCE_Q_30')
    wait_for_id(browser,'QA_SCE_FORM_DR_QA_SCE_Q_28',2)



# win0divQA_SCE_FORM_DR_QA_FB_SCE_SAVE
# QA_SCE_HELPER_QA_BTN_TEF



    






    # textarea.PSLONGEDITBOX




    el_checked=0

    
    elements = browser.find_elements_by_css_selector(".PSRADIOBUTTON[type = 'radio']")

    total_radios=len(elements)
    total_rows=total_radios/radio_button_in_each_row

    print('Total Rows:', total_rows)

    


    while True:

        row_checked=0

        elements = browser.find_elements_by_css_selector(".PSRADIOBUTTON[type = 'radio']")


        # parentElements = browser.find_elements_by_class_name("PSRADIOBUTTON")
        
        try:

            for i in range(Rate,len(elements),radio_button_in_each_row):

                el= elements[i]
                checked=el.get_attribute("checked")
                
                if checked:
                    print("Already Checked")

                    row_checked=row_checked+1

                else:
                    el_checked=el_checked+radio_button_in_each_row
                    el.click()
                    break


        except:
            pass





        print(f"{row_checked} Rows Filled")

        submit_button_clicked=False

        
        if row_checked >= total_rows:



            try:

                TextArea = browser.find_element_by_css_selector("textarea")



                TextArea.send_keys(Feed_Back_Message)
                print(f'Filled Text Area with {Feed_Back_Message}')



            except:
                
                print('Text Area Not Found')

            

            # buttons = browser.find_elements_by_css_selector("input[type = 'button']")

            # for i, button in enumerate(buttons):

            #     print(f'{button.get_attribute("value")} Button Found')

            #     # if button.get_attribute("value") == "Submit":
            #     button_label="Submit"
            #     if button.get_attribute("value") == button_label:

            #         print(f'clicking {button_label} button')


            #         button.click()
            #         submit_button_clicked=True

            #         break



            ## save button for student course evaluation

            try:
                save_button=browser.find_element_by_css_selector("a#QA_SCE_FORM_DR_QA_FB_SCE_SAVE")

                save_button.click()

                submit_button_clicked=True

            
            except:
                print('student course evaluation save button not found')
                pass


            try:
                save_button=browser.find_element_by_css_selector("input[value = 'Submit']")

                save_button.click()

                submit_button_clicked=True

            
            except:
                print('Teacher Evaluation Form save button not found')
                pass


            

        if submit_button_clicked:
            return True
            





def form_status(browser,row):

    

    cols = row.find_elements_by_css_selector("td")

    not_submitted=False

    for col in cols:

        col_text=col.text

        if (col_text == 'Yes'):
            print('Form Submitted : Yes')
        
        elif (col_text == 'No'):
            print('Form Not Submitted : No')

            not_submitted=True

            

        else:
            print(col_text)

        
    if not_submitted:

        view_form_button=row.find_element_by_css_selector("input[type = 'button']")
        view_form_button.click()

        from ..forms.fill_form import fill_form

        print('Viewing Form')

        return fill_form(browser)

    else:
        return False

        

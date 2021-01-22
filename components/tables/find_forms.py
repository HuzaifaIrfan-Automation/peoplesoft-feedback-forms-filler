

from .form_status import form_status

def find_forms(browser,table):

    rows = table.find_elements_by_css_selector("tr")

    print('Number of Rows:' ,len(rows))

    rows.pop(0)

    print('Number of Forms in this Table:' ,(len(rows)))

    for i,row in enumerate(rows):

        print('Looking at Row ',i+1)

        if form_status(browser,row):
            return True


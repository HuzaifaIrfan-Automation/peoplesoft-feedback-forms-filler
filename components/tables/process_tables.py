

from .find_forms import find_forms

def process_tables(browser):

    tables = browser.find_elements_by_class_name("PSLEVEL1GRID")

    print("Total Tables ",len(tables))

    if len(tables) > 0:

        for n, table in enumerate(tables):

            print('Looking at Table ',n+1)

            if find_forms(browser,table):
                return True
    else:
        return True







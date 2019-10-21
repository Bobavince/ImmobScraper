from Parameters import (page_add_leboncoin, page_add_seloger, url_leboncoin,
                        url_seloger)
from scraper_leboncoin import LebonCoin_Scraper
from scraper_seloger import SeLoger_Scraper

if __name__ == "__main__":
    scraper_1 = LebonCoin_Scraper(url_leboncoin, page_add_leboncoin)
    list_appt_1 = scraper_1.get_full_list_appt()

    scraper_2 = SeLoger_Scraper(url_seloger, page_add_seloger)
    list_appt_2 = scraper_2.get_full_list_appt()

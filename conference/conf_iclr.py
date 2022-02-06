from conference.base_conference import BaseConference
import time


class ICLR(BaseConference):
    def url(self):
        return f"https://openreview.net/group?id=ICLR.cc/{self.__year__}/Conference"

    def retrieve(self):
        try:
            time.sleep(15)
            self.__driver__.find_element_by_partial_link_text('Oral').click()
            time.sleep(1)
            element_list = self.__driver__.find_elements_by_tag_name('h4')[1:]
            for i, element in enumerate(element_list):
                if self.ignore(element_list[i].text):
                    continue
                self.__titles__.append(element_list[i].text)
                self.__links__.append(element_list[i].find_elements_by_xpath('a')[1].get_attribute('href'))
        except Exception:
            print("[ERR] ICLR retrieve exception!")

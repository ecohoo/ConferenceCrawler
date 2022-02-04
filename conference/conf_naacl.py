from conference.base_conference import BaseConference


class NAACL(BaseConference):
    def url(self):
        return f"https://aclanthology.org/events/naacl-{self.__year__}/#{self.__year__}-naacl-main"

    def retrieve(self):
        element_list = self.__driver__.find_elements_by_tag_name('strong')[1:]
        for i, element in enumerate(element_list):
            if len(element_list[i].find_elements_by_xpath('a')) == 0:
                break
            link = element_list[i].find_elements_by_xpath('a')[0].get_attribute('href')
            link = link[:-1] + ".pdf"
            if "main" not in link:
                break
            if self.ignore(element_list[i].find_elements_by_xpath('a')[0].text):
                continue
            self.__titles__.append(element_list[i].find_elements_by_xpath('a')[0].text)
            self.__links__.append(link)

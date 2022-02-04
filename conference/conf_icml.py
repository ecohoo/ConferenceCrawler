from conference.base_conference import BaseConference


class ICML(BaseConference):
    def url(self):
        if self.__year__ is 2020:
            return "http://proceedings.mlr.press/v119/"
        return "http://proceedings.mlr.press/v139/"

    def retrieve(self):
        element_list = self.__driver__.find_elements_by_class_name('title')
        url_element_list = self.__driver__.find_elements_by_link_text('Download PDF')
        for i, element in enumerate(url_element_list):
            if self.ignore(element_list[i].text):
                continue
            self.__titles__.append(element_list[i].text)
            self.__links__.append(url_element_list[i].get_attribute('href'))

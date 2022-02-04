from conference.base_conference import BaseConference


class NeurIPS(BaseConference):
    def url(self):
        return f"https://papers.nips.cc/paper/{self.__year__}"

    def retrieve(self):
        element_list = self.__driver__.find_elements_by_tag_name('h3')
        for i, element in enumerate(element_list):
            if len(element_list[i].find_elements_by_xpath('a')) == 0:
                break
            link = element_list[i].find_elements_by_xpath('a')[0].get_attribute('href')
            newlink = link.split("doi")[0] + "doi/pdf" + link.split("doi")[1]
            if self.ignore(element_list[i].find_elements_by_xpath('a')[0].text):
                continue
            self.__titles__.append(element_list[i].find_elements_by_xpath('a')[0].text)
            self.__links__.append(newlink)
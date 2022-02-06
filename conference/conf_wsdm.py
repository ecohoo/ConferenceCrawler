from conference.base_conference import BaseConference


class WSDM(BaseConference):
    def url(self):
        if self.__year__ == 2020:
            return "https://www.wsdm-conference.org/2020/acm-proceedings.php"
        return "http://www.wsdm-conference.org/2021/proceedings.php"

    def retrieve(self):
        if self.__year__ == 2020:
            pdf_url_list = []
            element_list = self.__driver__.find_elements_by_tag_name('h3')
            for i, element in enumerate(element_list):
                if len(element_list[i].find_elements_by_xpath('a')) == 0:
                    break
                if self.ignore(element_list[i].find_elements_by_xpath('a')[0].text):
                    continue
                self.__titles__.append(element_list[i].find_elements_by_xpath('a')[0].text)
                pdf_url_list.append(element_list[i].find_elements_by_xpath('a')[0].get_attribute('href'))
            for i, link in enumerate(pdf_url_list):
                new_link = link.split("_doi_abs_")[1].split("&")[0]
                link = "https://dl.acm.org/doi/pdf/" + new_link.split("_")[0] + "/" + new_link.split("_")[1]
                self.__links__.append(link)
        else:
            element_list = self.__driver__.find_elements_by_tag_name('h3')
            for i, element in enumerate(element_list):
                if len(element_list[i].find_elements_by_xpath('a')) == 0:
                    break
                link = element_list[i].find_elements_by_xpath('a')[0].get_attribute('href')
                new_link = link.split("doi")[0] + "doi/pdf" + link.split("doi")[1]
                if self.ignore(element_list[i].find_elements_by_xpath('a')[0].text):
                    continue
                self.__titles__.append(element_list[i].find_elements_by_xpath('a')[0].text)
                self.__links__.append(new_link)

from conference.base_conference import BaseConference
import time


class SIGIR(BaseConference):
    def url(self):
        if self.__year__ == 2020:
            return "https://dl.acm.org/doi/proceedings/10.1145/3397271"
        return "https://dl.acm.org/doi/proceedings/10.1145/3404835"

    def retrieve(self):
        element_list = self.__driver__.find_elements_by_class_name('accordion-tabbed')[1].find_elements_by_class_name(
            'toc__section')
        for i, section in enumerate(element_list):
            if 'Session' not in section.text.split('\n')[0]:
                continue
            section.click()
            time.sleep(3)

            for j, paper_element in enumerate(section.find_elements_by_class_name('issue-item__content')):
                paper_name = paper_element.find_element_by_xpath('div/h5').text
                pdf_url = paper_element.find_element_by_xpath(
                    'div/div/div/div/ul[contains(@class,"right")]/li/a[contains(@href,"/pdf/")]').get_attribute('href')
                if self.ignore(paper_name):
                    continue
                self.__titles__.append(paper_name)
                self.__links__.append(pdf_url)

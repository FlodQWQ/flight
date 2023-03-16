import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Spider:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/111.0.0.0 " \
                     "Safari/537.36 "
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.page_load_strategy = 'eager'
        options.add_argument('--user-agent=%s' % user_agent)
        # options.add_argument('--proxy-server=127.0.0.1:7890')
        self.driver = webdriver.Chrome("./chromedriver.exe", options=options)
        self.wait = WebDriverWait(driver=self.driver, timeout=30)

    def run(self):
        self.driver.get("https://www.jal.co.jp/cn/zhcn/")
        self.driver.find_element_by_xpath("//p[contains(text(), '始发地')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//label[contains(text(), '单程')]").click()
        self.driver.find_element_by_xpath("//input[@placeholder='城市或机场']").send_keys("大连")
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        self.driver.find_element_by_xpath("//input[@placeholder='城市或机场']").send_keys("东京")
        time.sleep(1)
        actions.perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='days sun' and text()='2']").click()
        self.driver.find_element_by_xpath("//span[contains(text(), '搜索航班')]").click()

        while 1:
            try:
                price = self.driver.find_element_by_id("sidebarPriceSummaryTotalPrice").text
                break
            except:
                time.sleep(1)

        price = ''.join(num for num in price if num.isdigit())
        print(price)
        return price

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
    spider.close()

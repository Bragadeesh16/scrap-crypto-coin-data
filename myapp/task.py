from celery import shared_task
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

@shared_task
def getting_the_data(currency):
    website = 'https://coinmarketcap.com/'
    chromedriver_path = "/home/bragadeesh/Documents/chromedriver-linux64"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.binary_location = chromedriver_path

    data = {
        "coin_name": "",
        "price": "",
        "price_change": "",
        "market_cap": "",
        "market_cap_rank": "",
        "volume": "",
        "volume_rank": "",
        "volume_change": "",
        "circulating_supply": "",
        "total_supply": "",
        "diluted_market_cap": "",
        "official_links": [],
        "socials": []
    }

    results = []

    driver = webdriver.Chrome(options=options)
    driver.get(website)
    menu_div = driver.find_elements(By.CLASS_NAME,'container')
    for index, menu_div in enumerate(menu_div):
        try:
            svg_element = menu_div.find_elements(By.CSS_SELECTOR,'.kNerue')

            for index,svg_element in enumerate(svg_element):
                search_elements = svg_element.find_elements(By.CSS_SELECTOR,'.dMwnWW')
                search = search_elements[0]

        except Exception as e:
            print(f"Error finding SVG element in menu_div {index}: {e}")

    search.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ctOzuc')))
    search_bar = driver.find_elements(By.CSS_SELECTOR,".ctOzuc")
    search_input = search_bar[1]

    for currency in currency:
        search_input.clear()
        search_input.send_keys(currency)
        time.sleep(8)
        search_input.send_keys(Keys.RETURN)

        coin_name = driver.find_element(By.XPATH,'//span[@data-role = "coin-name"]')
        price = driver.find_element(By.XPATH,'//span[@class="sc-d1ede7e3-0 fsQm base-text"]')
        price_change = driver.find_element(By.XPATH,'//p[@class="sc-71024e3e-0 sc-58c82cf9-1 bgxfSG iPawMI"]')
        market_cap = driver.find_element(By.XPATH,'//dd[@class="sc-d1ede7e3-0 hPHvUM base-text"]')
        market_cap_rank = driver.find_element(By.XPATH,'//p[@class="sc-71024e3e-0 sc-58c82cf9-1 bgxfSG iPawMI"]')
        volume = driver.find_element(By.XPATH,'//dd[@class="sc-d1ede7e3-0 hPHvUM base-text"]')
        volume_rank = driver.find_element(By.XPATH,'//span[@class="text slider-value rank-value"]')
        volume_change = driver.find_element(By.XPATH,'//div[@class="sc-4c05d6ef-0 sc-58c82cf9-0 dlQYLv dTczEt"]')
        circulating_supply = driver.find_element(By.XPATH,'//dd[@class="sc-d1ede7e3-0 hPHvUM base-text"]')
        total_supply = driver.find_element(By.XPATH,'//dd[@class="sc-d1ede7e3-0 hPHvUM base-text"]')
        diluted_market_cap = driver.find_element(By.XPATH,'//dd[@class="sc-d1ede7e3-0 hPHvUM base-text"]')



        data['coin_name'] = coin_name.text
        data['price'] = price.text
        data['price_change'] = price_change.text
        data['market_cap'] = market_cap.text
        data['market_cap_rank'] = market_cap_rank.text
        data['volume'] = volume.text
        data['volume_rank'] = volume_rank.text
        data['volume_change'] = volume_change.text
        data['circulating_supply'] = circulating_supply.text
        data['total_supply'] = total_supply.text
        data['diluted_market_cap'] = diluted_market_cap.text

        social_divs = driver.find_elements(By.XPATH,'//div[@class="sc-d1ede7e3-0 sc-7f0f401-0 gRSwoF gQoblf"]')

        if len(social_divs) > 0:
            official_div = social_divs[0]
            name = official_div.text
            a_tags = official_div.find_elements(By.TAG_NAME, 'a')
            if a_tags:
                href = a_tags[0].get_attribute('href')
                data['official_links'].append({"name": name, "link": href})

            for parent_div in social_divs[1:]:
                name = parent_div.text
                a_tags = parent_div.find_elements(By.TAG_NAME, 'a')
                for link in a_tags:
                    href = link.get_attribute('href')
                    data['socials'].append({"name": name, "url": href})
        results.append(data) 

    return results
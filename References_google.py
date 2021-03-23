from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://scholar.google.com')

searchbar = driver.find_element_by_class_name('gs_in_ac')
searchbar.click()
time.sleep(1)
searchbar.send_keys("('machine learning' OR 'ML') AND ('Re-admission' OR 'Re-hospitalisation' OR 'Readmission' OR 'Rehospitalisation')")
time.sleep(5)

searchbutton = driver.find_element_by_id('gs_hdr_tsb')
searchbutton.click()
time.sleep(3)

year_range = driver.find_element_by_xpath('/html/body/div/div[10]/div[1]/div/div[1]/ul/li[5]')
year_range.click()
time.sleep(1)

fromyear = driver.find_element_by_xpath('/html/body/div/div[10]/div[1]/div/div[1]/form/div[1]/div[1]/input')
fromyear.click()
fromyear.send_keys('2017')

searchyear = driver.find_element_by_xpath('/html/body/div/div[10]/div[1]/div/div[1]/form/div[2]/button/span')
searchyear.click()
time.sleep(3)

unmatched_articles = []

for i in range(863):
    article_titles = driver.find_elements_by_tag_name('h3')
    x = 1
    for article_title in article_titles:
        if (('Machine Learning' in article_title.text) or ('machine learning' in article_title.text) or ('deep learning' in article_title.text) or ('deep-learning' in article_title.text)or ('Machine Learning-Based' in article_title.text)or ('Predictive' in article_title.text)or ('predictive' in article_title.text)or ('prediction' in article_title.text)or ('' in article_title.text)) \
                and (('readmission' in article_title.text) or ('Readmission' in article_title.text) or ('Re-admission' in article_title.text) or ('re-admission' in article_title.text) or ('Rehospitalisation' in article_title.text) or ('Re-hospitalisation' in article_title.text) or ('re-hospitalisation' in article_title.text) or ('rehospitalisation' in article_title.text)):
            cite = driver.find_element_by_css_selector(
                '#gs_res_ccl_mid > div:nth-child({0}) > div.gs_ri > div.gs_fl > a.gs_or_cit.gs_nph'.format(x))
            time.sleep(3)
            cite.click()
            time.sleep(3)
            endnote = driver.find_element_by_link_text('EndNote')
            endnote.click()
            time.sleep(3)
            back = driver.find_element_by_id('gs_cit-x')
            back.click()
            print('the {0} citation is done!'.format(x))
            time.sleep(3)
        else:
            print('the {0} cannot be done!'.format(x))
            unmatched_articles.append(article_title)
            time.sleep(3)

        x = x + 1
    nextpage = driver.find_element_by_css_selector('#gs_n > center > table > tbody > tr > td:nth-child(12)')
    nextpage.click()
    time.sleep(3)


driver.close()
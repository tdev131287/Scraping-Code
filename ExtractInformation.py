from selenium import webdriver
import time
import os
import pandas as pd

def getLinks():
    # url='https://www.ukas.com/find-an-organisation/browse-by-category/'
    dfInfo = pd.DataFrame()
    url='https://www.enac.es/entidades-acreditadas/buscador-de-acreditados'
    # url='https://services.accredia.it/accredia_labsearch.jsp?ID_LINK=1734&area=310&dipartimento=L&submit1=Everybody'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    
    driver.find_elements_by_css_selector("[class='btn btn-grey text-center']")[0].click()
    time.sleep(3)
    selectList = driver.find_elements_by_id('empresas')[0]
    
    opt = selectList.find_elements_by_tag_name('option')[0]
    for opt in selectList.find_elements_by_tag_name('option'):
        # import ipdb;ipdb.set_trace()
        Cname= opt.text
        print(Cname)
        opt.click()
        time.sleep(5)
        # info = driver.find_elements_by_id('detalleDireccionEntidad1651')[0]
        info = driver.find_elements_by_css_selector("[class='CompletaInfo']")[0]
        try:
            add = info.find_elements_by_tag_name('p')[0].text
        except:
            add='NA'
        try:
            phnumber= info.find_elements_by_css_selector("[class='row-fluid']")[0].find_elements_by_tag_name('div')[0].text
        except:
            phnumber='NA'
        try:
            email= info.find_elements_by_css_selector("[class='row-fluid']")[0].find_elements_by_tag_name('div')[1].text
        except:
            email='NA'
        try:
            website= info.find_elements_by_css_selector("[class='row-fluid']")[1].find_elements_by_tag_name('div')[0].text
        except:
            website='NA'

        dfInfo = dfInfo.append({'Name':Cname,'Address':add,'PhoneNumber':phnumber,'E-Mail':email,'Website':website},ignore_index=True)
        dfInfo.to_excel('WebInfo.xlsx',index=False)

def Ireland_Scraper():
    urldict={
        'Testing Laboratories':'https://www.inab.ie/inab-directory/laboratory-accreditation/testing-laboratories/',
        'Calibration Laboratories':'https://www.inab.ie/inab-directory/laboratory-accreditation/calibration-laboratories/',
        'Management System Certifications':'https://www.inab.ie/inab-directory/certification-bodies/management-systems-certification/',
        'Product Certification':'https://www.inab.ie/inab-directory/certification-bodies/product-certification/',
        'Inspection Bodies':'https://www.inab.ie/inab-directory/inspection-bodies/inspection-bodies/'
        #'Compliant Test Facilities':'https://www.inab.ie/inab-directory/good-laboratory-practice/good-laboratory-practice-compliant-test-facilities/',
    }
    dflinks = pd.DataFrame()
    driver = webdriver.Chrome()
    for key in urldict.keys():
        url = urldict[key]
        driver.get(url)
        time.sleep(5)
        tbl = driver.find_elements_by_tag_name('table')[0]
        for tr in tbl.find_elements_by_tag_name('tr'):
            try:
                import ipdb;ipdb.set_trace()
                name = tr.find_elements_by_tag_name('td')[0].text
                link = tr.find_elements_by_tag_name('td')[0].find_elements_by_tag_name('a')[0].get_attribute('href')
                dflinks = dflinks.append({'Name':name,'Website':link,'Type':key,'Source':url},ignore_index=True)
                dflinks.to_excel('AllLinks.xlsx',index=False)
                
            except:
                pass

def Ireland_Information():
    dfDetails = pd.DataFrame()
    url='https://www.inab.ie/inab-directory/certification-bodies/management-systems-certification/business-quality-assurance-international-ltd-.html'
    driver = webdriver.Chrome()
    driver.get(url)
    info = driver.find_elements_by_css_selector("[class='cms-content']")[1]
    add = info.find_elements_by_tag_name('p')[0].text
    contact = info.find_elements_by_tag_name('p')[1].text
    website = info.find_elements_by_tag_name('p')[2].text
    dfDetails = dfDetails.append({'Address':add,'Contact':contact,'Website':website},ignore_index=True)
    
    import ipdb;ipdb.set_trace()
if __name__=="__main__":
    # getLinks()
    # Ireland_Scraper()
    Ireland_Information()
    
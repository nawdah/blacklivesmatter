import requests
import json
import re
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import numpy as np

from selenium import webdriver
from splinter import Browser
from selenium.webdriver.common.keys import Keys

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def eat_the_rich(first, last, street, city, state, state_abbreviation, country, zipcode, email, phone, prefix):

    #working...
    black_lives_matter = ['https://blacklivesmatter.com/demand-racial-data-on-coronavirus/', 
                        'https://blacklivesmatter.com/coronavirus-demand-more-from-the-government/']
    #working...
    every_action = ['https://secure.everyaction.com/eR7GA7oz70GL8doBq19LrA2']

    #ERROR
    amnesty = ['https://www.amnesty.org/en/get-involved/take-action/george-floyd-police-violence-usa/']

    #working...
    action = ['https://actionnetwork.org/forms/2005_email_blm_defund']

    #working...
    actionnetwork = ['https://actionnetwork.org/letters/we-demand-the-peoples-budget?source=twitter&' ,
                    'https://actionnetwork.org/petitions/increase-our-communities-defund-the-philly-police-budget?source=direct_link&',
                    'https://actionnetwork.org/petitions/driscolls-hold-your-supplier-rancho-laguna-farms-accountable-for-mistreating-workers?source=direct_link&']

    #working...
    encryption = ['https://actionnetwork.org/petitions/dont-let-congress-kill-encryption']

    #ERROR
    support_naacp = ['https://support.naacp.org/onlineactions/HTLjqYG940WATTV_Y_SUUQ2']

    #ERROR
    petition_site = ['https://www.thepetitionsite.com/707/191/811/fire-jared-yuen-4362/',
                    'https://www.thepetitionsite.com/960/515/911/hold-harris-county-and-walmart-accountable-for-killing-alleged-shoplifter/']

    #working...
    docs = ['https://docs.google.com/forms/d/e/1FAIpQLSf1NrIJleLHjT3F5t2qMaoiRNTsZI5KQgihpcsgGp_lASz0Pw/viewform?fbclid=IwAR0tbdDUn1aZbpMxGOTErYZdFszcRBkoknntz35amBizhE32UEpDYoq4NdE']

    #working...
    action_aclu = ['https://action.aclu.org/petition/al-repealhfoa?fbclid=IwAR2dO_rU5DVvFtNN8Hz620OPa2IZTQ3ZSi6tl6LH_iYO3bSKNAupQIAT2hY']

    #CAPTCHA BLOCK
    peticao = ['https://peticaopublica.com/?pi=PT100402']

    #working...
    ipetition = ['https://www.ipetitions.com/petition/justice4CK']

    #working...
    campaigns = ['https://campaigns.organizefor.org/petitions/take-the-pledge-we-are-the-movement-for-black-lives',
                'https://campaigns.organizefor.org/petitions/justice-for-jamee-johnson',
                'https://campaigns.organizefor.org/petitions/take-the-pledge-we-are-the-movement-for-black-lives?share=2eb797bd-9756-4c00-b0a8-be90af8a638b&source=twitter-share-email-button&time=1591071476&utm_source=twitter',
                'https://campaigns.organizefor.org/petitions/3-years-without-justice-for-desmond-phillips-1?bucket=&source=twitter-share-button&utm_campaign=&utm_source=twitter&share=d96c01e9-b664-4d5a-85aa-a4640aeaef17',
                'https://campaigns.organizefor.org/petitions/fire-lapd-officers-ryan-lee-and-martin-robles-for-the-murder-of-grechariomack']

    #working...
    your_voice = ['https://act.colorofchange.org/sign/demand-justice-ahmaud?source=yourvoice_ctabutton']

    #working...
    color_of_change = ['https://act.colorofchange.org/sign/justiceforfloyd_george_floyd_minneapolis/?source=dm_sms_optin_5-26-20']


    #working...
    moveon = ['https://sign.moveon.org/petitions/justiceforbre-police-officers-who-killed-breonna-taylor-must-be-fired']

    #working...
    white_house = ['https://petitions.whitehouse.gov/petition/arrest-other-three']


    #CAPTCHA BLOCK
    change_org = ['https://www.change.org/p/mayor-jacob-frey-justice-for-george-floyd',
                'https://www.change.org/p/change-org-the-minneapolis-police-officers-to-be-charged-for-murder-after-killing-innocent-black-man',
                'https://www.change.org/p/federal-bureau-of-investigation-justice-for-george-floyd',
                'https://www.change.org/p/mayor-jacob-frey-justice-for-george-floyd-2',
                'https://www.change.org/p/andy-beshear-justice-for-breonna-taylor',
                'https://www.change.org/p/julius-jones-is-innocent-don-t-let-him-be-executed-by-the-state-of-oklahoma',
                'https://www.change.org/p/hennepin-county-attorney-mike-freeman-prosecute-the-murderers-who-killed-george-floyd',
                'https://www.change.org/p/justice-for-tony-mcdade',
                'https://www.change.org/p/us-senate-hands-up-act',
                'https://www.change.org/p/prefeitura-do-rio-de-janeiro-justice-for-jo%C4%81o-pedro',
                'https://www.change.org/p/alabama-governor-kay-ivey-willie-simmons-has-served-38-years-for-a-9-robbery',
                'https://www.change.org/p/federal-bureau-of-investigation-disbarment-of-george-e-barnhill',
                'https://www.change.org/p/justice-for-regis-korchinski-paquet',
                'https://www.change.org/p/governor-brian-kemp-justice-for-ahmaud-arbery',
                'https://www.change.org/p/ron-desantis-free-anthony-wint-fbc27c7c-920d-4104-9960-a234f45cbe20',
                'https://www.change.org/p/kim-ogg-after-the-smoke-clears-arrest-juan-delacruz-for-the-murder-of-pamela-turner-right-now',
                'https://www.change.org/p/reform-alliance-freejeffersonelie',
                'https://www.change.org/p/kansas-state-senate-exoneration-of-albert-wilson-00180b91-68bf-4c0c-9a12-732119e57dc9',
                'https://www.change.org/p/white-house-justice-for-sean',
                'https://www.change.org/p/united-states-supreme-court-justice-for-kendrick-johnson',
                'https://www.change.org/p/department-of-justice-investigate-the-killing-of-tamir-rice',
                'https://www.change.org/p/justice-for-tamir-rice-appoint-a-special-prosecutor',
                'https://www.change.org/p/gouvernement-fran%C3%A7ais-refus-de-la-loi-visant-%C3%A0-emp%C3%AAcher-la-diffusion-des-images-de-violences-polici%C3%A8res',
                'https://www.change.org/p/nypd-fire-racist-criminal-michael-j-reynolds-from-the-nypd']

    #working
    naacp_org = ['https://www.naacp.org/campaigns/we-are-done-dying/']

    #working
    m4bl = ['https://m4bl.org/join-our-movement/']

    #BLACK LIVES MATTER 

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}

    browser = Browser('chrome', incognito=True)

    for blm in black_lives_matter:

        browser.visit(blm)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        em = '//*[@id="form-email"]'
        zip_code = '//*[@id="form-zip_code"]'
        submit = '//*[@id="form_col2"]/input'

        try:
            browser.find_by_xpath(em).first.fill(email)
            browser.find_by_xpath(zip_code).first.fill(zipcode)

            button = browser.find_by_xpath(submit)
            for i in button:
                i.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
            
        #EVERY ACTION
        
    for ev in every_action:

        browser.visit(ev)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="NVPetitionForm618600"]/section/form/fieldset/div/div[1]/label[1]/input'
        last_name = '//*[@id="NVPetitionForm618600"]/section/form/fieldset/div/div[1]/label[2]/input'
        zip_code = '//*[@id="NVPetitionForm618600"]/section/form/fieldset/div/div[4]/label[1]/input'
        city_xpath = '//*[@id="NVPetitionForm618600"]/section/form/fieldset/div/div[4]/label[2]/input'
        state_xpath = '//*[@id="NVPetitionForm618600"]/section/form/fieldset/div/div[4]/label[3]/select'
        em = '//*[@id="NVPetitionForm618600"]/section/form/fieldset/div/div[5]/label[1]/input'
        phone_xpath = '//*[@id="NVPetitionForm618600"]/section/form/fieldset/div/div[5]/label[2]/div/input'
        submit = '//*[@id="NVPetitionForm618600"]/section/form/div[2]/input'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            browser.find_by_xpath(city_xpath).first.fill(city)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(phone_xpath).first.fill(phone)     

            time.sleep(10)

            button = browser.find_by_xpath(submit)
            for i in button:
                i.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
    #ACTION

    for act in action:

        browser.visit(act)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="form-first_name"]'
        zip_code = '//*[@id="form-zip_code"]'
        em = '//*[@id="form-email"]'
        submit = '//*[@id="new_answer"]/ul/li[5]/input'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(10)

            button = browser.find_by_xpath(submit)
            for i in button:
                i.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()

    #ACTION NETWORK

    for net in actionnetwork:

        browser.visit(net)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="form-first_name"]'
        last_name = '//*[@id="form-last_name"]'
        zip_code = '//*[@id="form-zip_code"]'
        em = '//*[@id="form-email"]'
        phone_xpath = '//*[@id="form-phone"]'
        submit = '//*[@id="new_delivery"]/ul/li[8]/input'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(phone_xpath).first.fill(phone)

            time.sleep(10)

            button = browser.find_by_xpath(submit)
            for i in button:
                i.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()

    #ENCRYPTION

    for en in encryption:

        browser.visit(en)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="form-first_name"]'
        last_name = '//*[@id="form-last_name"]'
        zip_code = '//*[@id="form-zip_code"]'
        em = '//*[@id="form-email"]'
        submit = '//*[@id="new_signature"]/input[4]'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(10)

            button = browser.find_by_xpath(submit)
            for i in button:
                i.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
    #DOCS

    for gdoc in docs:

        browser.visit(gdoc)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        name = '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
        em = '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input'
        zip_code = '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div[1]/div[2]/textarea'
        submit = '//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div'

        try:
            time.sleep(3)

            browser.find_by_xpath(name).first.fill(first + ' ' + last)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
            #ACLU

    for aclu in action_aclu:

        browser.visit(aclu)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="edit-submitted-sbp-first-name"]'
        last_name = '//*[@id="edit-submitted-sbp-last-name"]'
        em = '//*[@id="edit-submitted-mail"]'
        zip_code = '//*[@id="edit-submitted-sbp-zip"]'
        submit = '//*[@id="edit-submit"]'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
            #iPETITION

    for ipet in ipetition:

        browser.visit(ipet)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        name = '//*[@id="Submissions_name"]'
        em = '//*[@id="Submissions_email"]'
        submit = '//*[@id="sign_now"]'

        try:
            time.sleep(3)

            browser.find_by_xpath(name).first.fill(first + ' ' + last)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
    #CAMPAIGNS

    for camp in campaigns:

        browser.visit(camp)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="signature_first_name"]'
        last_name = '//*[@id="signature_last_name"]'
        zip_code = '//*[@id="signature_postcode"]'
        em = '//*[@id="signature_email"]'
        submit = '//*[@id="new_signature_button"]'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(10)

            button = browser.find_by_xpath(submit)
            for i in button:
                i.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
    #COLOR OF CHANGE 

    for color in color_of_change:

        browser.visit(color)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '/html/body/div/div/div/div/div/section/div/div[1]/div/div[1]/form/div[1]/div/div[2]/div/ul/li[1]/input'
        last_name = '/html/body/div/div/div/div/div/section/div/div[1]/div/div[1]/form/div[1]/div/div[2]/div/ul/li[2]/input'
        em = '//*[@id="id_email"]'
        zip_code = '//*[@id="id_zip"]'
        radio_button = '//*[@id="id_action_video_no"]'
        submit = '//*[@id="content"]/div/div/section/div/div[1]/div/div[1]/form/div[3]/button'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            radio = browser.find_by_xpath(radio_button)

            for r in radio:
                r.click()

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()

    #VOICE OF CHANGE 

    for voice in your_voice:

        browser.visit(voice)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '/html/body/div/div/div/div/div/section/div/div[1]/div/div[1]/form/div[1]/div/div[2]/div/ul/li[1]/input'
        em = '//*[@id="id_email"]'
        zip_code = '//*[@id="id_zip"]'
        radio_button = '//*[@id="id_action_video_no"]'
        submit = '//*[@id="content"]/div/div/section/div/div[1]/div/div[1]/form/div[3]/button'

        try:
            time.sleep(3)

            browser.find_by_xpath(name).first.fill(first + ' ' + last)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            radio = browser.find_by_xpath(radio_button)

            for r in radio:
                r.click()     

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
            #MOVEON 

    for move in moveon:

        browser.visit(move)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="signature_first_name"]'
        last_name = '//*[@id="signature_last_name"]'
        em = '//*[@id="signature_email"]'
        zip_code = '//*[@id="signature_postcode"]'
        submit = '//*[@id="new_signature_button"]'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
    #WHITE HOUSE 

    for supremacists in white_house:

        browser.visit(supremacists)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="edit-first-name"]'
        last_name = '//*[@id="edit-last-name"]'
        em = '//*[@id="edit-email"]'
        submit = '//*[@id="edit-submit"]'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()

    #NAACP ORG 

    for org in naacp_org:

        browser.visit(org)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")

        first_name = '//*[@id="NVSignupForm619391"]/section/form/fieldset/div/div[1]/label[1]/input'
        last_name = '//*[@id="NVSignupForm619391"]/section/form/fieldset/div/div[1]/label[2]/input'
        zip_code = '//*[@id="NVSignupForm619391"]/section/form/fieldset/div/div[2]/label/input'
        em = '//*[@id="NVSignupForm619391"]/section/form/fieldset/div/div[3]/label[1]/input'
        phone_xpath = '//*[@id="NVSignupForm619391"]/section/form/fieldset/div/div[3]/label[3]/div/input'
        submit = '//*[@id="NVSignupForm619391"]/section/form/div[2]/input'

        try:
            time.sleep(3)

            browser.find_by_xpath(first_name).first.fill(first)

            time.sleep(3)

            browser.find_by_xpath(last_name).first.fill(last)

            time.sleep(3)

            browser.find_by_xpath(zip_code).first.fill(zipcode)

            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(3)

            browser.find_by_xpath(phone_xpath).first.fill(phone)

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()
            
    #M4BL 

    for m4 in m4bl:

        browser.visit(m4)

        timeout = 5
        try:
            myElem = WebDriverWait(browser, timeout)
        except TimeoutException:
            print("Timed out waiting for page to load")


        em = '//*[@id="wpcf7-f477-p378-o1"]/form/p[1]/span[2]/input'

        submit = '//*[@id="wpcf7-f477-p378-o1"]/form/p[3]/input'

        try:
            time.sleep(3)

            browser.find_by_xpath(em).first.fill(email)

            time.sleep(5)

            deliver = browser.find_by_xpath(submit)
            for k in deliver:
                k.click()

            print("Thanks for signing!")
        except:
            raise
            browser.quit()




    return print("Thanks for sticking it to the man!")
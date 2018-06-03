from selenium import webdriver
from selenium.webdriver.support.select import Select

from tqdm import tqdm

from bs4 import BeautifulSoup

import re

# Config
BASE_URL = ""
BM_USER  = ""
BM_PASS  = ""
BM_ID    = ""

GET_EARNINGS = False
GET_BALANCE  = True

DEBUG = True

def debug(x):
    if DEBUG:
        print("[DEBUG] {}".format(x))

def create_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(chrome_options=options)

    return driver

def login(driver, username, password):
    driver.get(BASE_URL + "/login")

    user_elem = driver.find_element_by_name("usermail")
    user_elem.send_keys(username)

    pass_elem = driver.find_element_by_name("password")
    pass_elem.send_keys(password)

    pass_elem.submit()

    driver.implicitly_wait(10)

def get_contracts(driver):
    driver.get(BASE_URL + "/contracts")

    num_contracts = Select(driver.find_element_by_name("xtable_length"))
    num_contracts.select_by_index(3)

    contract_soup = BeautifulSoup(driver.page_source, "html.parser")

    return contract_soup

def parse_contracts(contract_soup, do_print=False):
    table = contract_soup.find("table")

    rows = table.findAll("tr")[1:] # first tr is headers

    if do_print:
        print("Printing reported contracts")

    issue_links = []

    earnings = []

    if do_print:
        print("----------------------------")
        print("Issue\t\tEarning")

    for row in rows:
        data = row.findAll("td")

        issue_links.append(data[0].find("a")["href"])

        earnings.append(float(data[-1].text))

        if do_print:
            print("{}\t{}".format(data[0].text, data[-1].text))

    if do_print:
        print("----------------------------")

        print("Total Reported Earnings: {}".format(sum(earnings)))

    return issue_links, earnings

def parse_issue(driver, link):
    driver.get(BASE_URL + link)

    issue_soup = BeautifulSoup(driver.page_source, "html.parser")

    issue_name = issue_soup.find("h2").text

    b_elems = issue_soup.findAll("b")

    status_elem = list(filter(lambda x: x.text == "Status:", b_elems))[0]

    issue_status = status_elem.nextSibling

    offer_table = issue_soup.find("table")

    offers = offer_table.findAll("tr")[1:]

    tot_earning = 0

    for offer in offers:
        funder, _, worker, _, _, _, _ = map(lambda x: x.text, offer.findAll("td"))

        if funder == BM_ID and worker != "EXPIRED" and issue_status == "closed":
            tot_earning += 5

        elif worker == BM_ID:
            tot_earning += 10

    return issue_name, tot_earning

def parse_issues(driver, issue_links):
    names, cal_earnings = [], []

    for link in tqdm(issue_links):
        name, cal_earning = parse_issue(driver, link)

        names.append(name)
        cal_earnings.append(cal_earning)

    return names, cal_earnings

def get_balance(url):
    driver.get(url)

    account_soup = BeautifulSoup(driver.page_source, "html.parser")

    bal = 0
    AC_BAL = "Account Balance"

    find_bal = lambda x: AC_BAL in x.text

    table = next(filter(find_bal, account_soup.findAll("table")))

    row = next(filter(find_bal, account_soup.findAll("tr")))

    elem = row.findAll("td")[1]
    bal = float(re.search("[0-9]*", elem.text).group(0))

    return bal

if __name__ == "__main__":
    debug("Setting up browser")
    driver = create_browser()

    debug("Logging in")
    login(driver, BM_USER, BM_PASS)
    debug("Login done")

    if GET_EARNINGS:
        debug("Get contracts")
        contract_soup = get_contracts(driver)

        debug("Parse contracts")
        issue_links, rep_earnings = parse_contracts(contract_soup)

        debug("Parse issues")
        names, cal_earnings = parse_issues(driver, issue_links)

        print("")

        for n, r, c in zip(names, rep_earnings, cal_earnings):
            print("{}\t{}\t{}".format(n, r, c))

        print("")
        print(sum(cal_earnings))

    if GET_BALANCE:
        debug("Getting balance")
        bal = get_balance(BASE_URL + "/account")

        print("Your balanc: {} tokens".format(bal))

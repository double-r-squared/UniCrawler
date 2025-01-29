import time
import re
import requests
from bs4 import BeautifulSoup
from string import ascii_uppercase as auc

az_url = "https://ucs.admin.uw.edu/UWOD/UWOD/OfficeListing?searchText={A_Z}&isAlphabetSearch=Y" #input("a-z directory url highlight the changing variable with {A_Z}: ")

## NON-REQUEST FUNCTIONS
def az_find(az_url): #input look for point
    az_list = []
    for letter in auc:
        az_list.append(az_url.format(A_Z = letter)) #no requests made here
        print(az_list[0])
    return az_list[0]
def crawl_delay():
    time.sleep(1)
    print("slowing down sorry!!! :3")
def get_total_pages(faculty_url, faculty_soup):
    #pagnation method
    page_IDs = list(set([a['href'] for a in faculty_soup.find("ul", class_='pagination').find_all('a', href=True)]))

    print("sub pages to Navigate", len(page_IDs))
    return page_IDs


## CRAWLER REQUEST FUNCTIONS

def dir_crawl(dir_url):
    department_list = []

    dir_response = requests.get(dir_url)
    directory_soup = BeautifulSoup(dir_response.text, "html.parser")

    list_items = directory_soup.find_all("li") #list of all urls containing the departments
    list_items = list_items[72:258] #specific location of department start and end
    for item in list_items:
        dep = item.text.strip() #TODO: fix name
        link = item.find("a", href=True)
        if link:
            link = link['href']
            dep_item = (dep, link) #TODO: use this in prod
            department_list.append(link)
    crawl_delay()
    return department_list

def dep_crawl(department_list): #falculty url list
    faculty_list = []

    faculty_url = department_list[0] + 'people' #test BUILD OUT MORE CASESESSESEESESS
    print(faculty_url)
    faculty_response = requests.get(faculty_url)
    faculty_soup = BeautifulSoup(faculty_response.text, "html.parser")
    pages = get_total_pages(faculty_url, faculty_soup)
    faculty_links = list(a['href'] for a in faculty_soup.find("tbody").find_all('a', href=True))

    print(faculty_links)

    # TODO: Navigating pages
    #if page_index < pages:
    #    dep_crawl(faculty_url + )
    crawl_delay()
    return faculty_list

dep_crawl(dir_crawl('https://www.washington.edu/about/academics/departments/'))

def faculty_crawl(faculty_list): #frontier
    #PUBLICATION/Papers/THesis AND SEARCH THESIS
    #OPEN LOOK FOR ADVISOR(S), ADVISOR
    #PULL NAME

    #parse and return these attributes:
    #return
    # {
    #   University: ,
    #   Department: , #Macro
    #   Name: , #Micro
    #   Website: , #Nano
    #   Students: , #Nano
    #   Advisor: , #Nano
    # }
    #append data with entry



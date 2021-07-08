import pandas as pd 
from selenium.webdriver import Firefox
from time import sleep

path = "C:/geckodriver.exe" #path
driver = Firefox(executable_path= path)
url = 'https://maharerait.mahaonline.gov.in/Login/Login' #website to scrap info from
driver.get(url)
sleep(2)
#form selections
driver.find_element_by_xpath('/html/body/section/div/div/form/div[1]/div[3]/div/div/div[2]/div[2]/a').click() #Registered Agents
sleep(5)
driver.find_element_by_xpath('//*[@id="Agent"]').click()
driver.find_element_by_xpath('//*[@id="btnAdvance"]').click()
driver.find_element_by_xpath('/html/body/section/div/div/form/div[2]/div[2]/div[4]/div/div[2]/select/option[4]').click() #Maharashtra
driver.find_element_by_xpath('/html/body/section/div/div/form/div[2]/div[2]/div[5]/div[1]/div[2]/select/option[18]').click() #Mumbai City
driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
sleep(5)

#initializing empty lists that will be appended later
master_contact = [] 
master_past_exp = []
master_member = []
master_project = []
master_branch = []

#the total number of entries were 3931 on the portal
for i in range(3931):
    c = i+1 #the index of each row is between 1 and 50
    c = c % 50 #to make sure the index remains under 50
    if c == 0: #50 is included, no index 0
        c = 50
    rera = driver.find_element_by_xpath('/html/body/section/div/div/form/div[3]/div/div[2]/div[1]/div/table/tbody/tr[%d]/td[3]' %c).text 
    driver.find_element_by_xpath('/html/body/section/div/div/form/div[3]/div/div[2]/div[1]/div/table/tbody/tr[%d]/td[4]/b/a' %c).click() #view button opens in new tab
    sleep(3)
    driver.switch_to.window(driver.window_handles[1]) #going to new tab
    sleep(3)
    info = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[1]/div[2]/div[1]/div/div[2]').text 
    all_df = pd.read_html(driver.current_url) #reads all the tables in the html
    
    for j in range(len(all_df)): #since not all entries have all the 5 tables so to fix that issue
        if 'Member Name' in all_df[j].columns:
            member_df = all_df[j]
            member_df['Agent Rera ID'] = rera # adding a rera column 
            master_member.append(member_df) #appending the df to a list
        if 'Project Type' in all_df[j].columns:
            exp_df =  all_df[j]
            exp_df['Agent Rera ID'] = rera # adding a rera column 
            master_past_exp.append(exp_df) #appending the df to a list
        if 'Branch Name' in all_df[j].columns:
            branch_df = all_df[j]
            branch_df['Agent Rera ID'] = rera # adding a rera column 
            master_branch.append(branch_df) #appending the df to a list
        if 'Certificate Number' in all_df[j].columns:
            project_df = all_df[j]
            project_df['Agent Rera ID'] = rera # adding a rera column 
            master_project.append(project_df) #appending the df to a list
            
    if info == 'Individual':
        name = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[1]/div/div[2]').text
        org = 'na' #individual agents do not have an organization 
        desc = 'na' # or desc value
        exp = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[4]/div/div[2]').text
        block = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[8]/div/div[2]').text
        building = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[8]/div/div[4]').text
        street = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[9]/div/div[2]').text
        local = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[9]/div/div[4]').text
        landmark = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[10]/div/div[2]').text
        state = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[10]/div/div[4]').text
        div = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[11]/div/div[2]').text
        dist = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[11]/div/div[4]').text
        taluka = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[12]/div/div[2]').text
        village = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[12]/div/div[4]').text
        pin = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[13]/div/div[2]').text
        web = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[17]/div/div[2]').text
        no = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/div[3]/div/div[2]/div[16]').text
#     elif info == 'Other Than Individual': 
    else:  
        name = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[2]').text
        org = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div/div[2]').text
        desc = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]').text
        exp = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[4]/div/div[2]').text
        block = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[7]/div/div[2]').text
        bulding = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[7]/div/div[4]').text
        street = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[8]/div/div[2]').text
        local = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[8]/div/div[4]').text
        landmark = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[9]/div/div[2]').text
        state = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[9]/div/div[4]').text
        div = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[10]/div/div[2]').text
        dist = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[10]/div/div[4]').text
        taluka = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[11]/div/div[2]').text
        village = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[11]/div/div[4]').text
        pin = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[12]/div/div[2]').text
        no = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[14]/div/div[2]').text
        web = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[1]/div[1]/div[3]/div[1]/div[2]/div[15]/div/div[3]').text
    li_contact = [rera, info, name, org, desc, exp, block, building, street, local, landmark, state, div, dist, taluka, village, pin, no, web] #stores the above data in a list
    master_contact.append(li_contact) #appends the above list to another list to be made into a df
    driver.close() #closes the new tab
    sleep(3)
    driver.switch_to.window(driver.window_handles[0]) #switches back to the first tab
    print(i,c, name) #counter
    if i % 49 == 0: #one page has 50 entries, so to switch pages when the end of page is reached
        driver.find_element_by_xpath('//*[@id="btnNext"]').click()
        sleep(5)
#end of for loop

final_past_experience_df = pd.concat(master_past_exp) #making the list of dataframes into a dataframe
final_branch_df = pd.concat(master_branch) #making the list of dataframes into a dataframe
final_project_df = pd.concat(master_project) #making the list of dataframes into a dataframe
final_members_df = pd.concat(master_member) #making the list of dataframes into a dataframe
final_contact_df = pd.DataFrame(
    master_contact, columns = ['Rera ID','Information Type', 'Name', 'Organization Type','Description for Other Type Organization','Do you have any Past Experince?','Block Number','Building Name','Street Name','Locality','Land Mark','State/UT','Division', 'Division','District','Taluka',
    'Vilage', 'Pin Code', 'Website URL'] ) #making the list of lists into a dataframe

#checking the dataframes
final_past_experience_df.head()
final_branch_df.head()
final_members_df.head()
final_project_df.head()
final_contact_df.head()

#writing to ..csv
final_past_experience_df.to_csv('Agent Past Experience.csv')
final_branch_df.to_csv('Agent Branch.csv')
final_members_df.to_csv('Agent Member.csv')
final_project_df.to_csv('Agent Project.csv')
final_contact_df.to_csv('Agent Contact.csv')

#This script will move all projects from one Snyk Organization to another.

import requests

print("This script will move the projects from one Snyk Organization to another.")
current_org = input("Enter the org ID your where your current projects are:")
move_org = input("Enter the org ID your where you would like to move your projects:")
auth_token = input("Enter your Snyk API token:")
url = "https://snyk.io/api/v1/org/"+ current_org + "/projects"

payload={}
headers = {
  'Authorization': 'token '+auth_token
}

response = requests.request("POST", url, headers=headers, data=payload)


response_dict = response.json()

proj_count=0
while response_dict['projects']:
  project = response_dict['projects'].pop()
  current_project=project['id']
  current_proj_name=project['name']
  url = "https://snyk.io/api/v1/org/"+current_org+"/project/"+current_project+"/move"
  payload={
    "targetOrgId": move_org
  }
  print("Moving project "+current_proj_name+"...")
  #print(url)
  requests.request("PUT", url, headers=headers, data=payload)
  proj_count+=1
print("Project move complete. "+str(proj_count)+" projects moved.")
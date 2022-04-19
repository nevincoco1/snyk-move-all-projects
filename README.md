# move_projects.py
This is a script to move all projects from one Snyk org to another. 

## Before you begin:
Ensure you are running a current version of Python.  You can get the latest version [here](https://www.python.org/downloads/). <br>


Open Notepad or similar app and copy the following strings to use later:

**Current Org ID**

1. Get the Org ID of the Organization where your projects currently reside.

![image](https://user-images.githubusercontent.com/89480245/163906048-3f016794-44ca-44e1-8d87-f16e6272fa43.png)



**Destination Org ID**

2. Switch to the destination Orgainization and repeat Step 1 to get the Org ID of the Organization where your projects will move to.


**Snyk API Token**

3. Finally, copy your Snyk API token.

![image](https://user-images.githubusercontent.com/89480245/163907259-a39994a0-8bf4-4fd1-b451-aad1a0edad22.png)
![image](https://user-images.githubusercontent.com/89480245/163908715-97ef86dc-e267-4b2b-9394-b524fa50f66f.png)


## How to use:
1. Copy the file **move_projects.py** to your python environment. 
2. Run the file by typing **`python move_projects.py`** or **`python3 move_projects.py`** depending on the command to run Python 3 in your environment.
3. You will be asked to input your **Current Org ID**, **Destination Org ID**, and **Snyk API Token**. (You can just paste these in)
4. The script will move all projects to the new org and remove them from the current org.  It should look similar to this:

![image](https://user-images.githubusercontent.com/89480245/163911529-59f55e52-21e9-4011-8628-9a31a84067eb.png)

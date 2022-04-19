# move_projects.py
This is a script to move all projects from one Snyk org to another.

## Before you begin:
Ensure you are running Python 3.6 or above.

Open the example configuration file to add your information for the script to use.

**Current Org ID (from_org)**

1. Get the Org ID of the Organization where your projects currently reside.

![image](https://user-images.githubusercontent.com/89480245/163906048-3f016794-44ca-44e1-8d87-f16e6272fa43.png)

**Destination Org ID (to_org)**

2. Switch to the destination Orgainization and repeat Step 1 to get the Org ID of the Organization where your projects will move to.

**Snyk API Token**

3. Finally, copy your Snyk API token.

![image](https://user-images.githubusercontent.com/89480245/163907259-a39994a0-8bf4-4fd1-b451-aad1a0edad22.png)
![image](https://user-images.githubusercontent.com/89480245/163908715-97ef86dc-e267-4b2b-9394-b524fa50f66f.png)

## How to use:
1. Clone the repo.
2. Create a virtual environment in your preferred manner (e.g. virtualenv venv -p $(which python3))
3. Rename `config.env.sample` to `config.env` and enter the values for the three variables in the file.
4. Run the file by typing `python3 move_projects.py` after the virtual environment is activated.
5. The script will move all projects to the new org and remove them from the current org as long as both orgs have the same integrations. It should look similar to this:

![image](https://user-images.githubusercontent.com/89480245/163911529-59f55e52-21e9-4011-8628-9a31a84067eb.png)

Login to Snyk and go to the org you have moved your projects to. Congratulations. You did it. Go get some ice cream. You're a hero.

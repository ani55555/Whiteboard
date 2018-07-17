Yo! Welcome to my whiteboard. If you're looking to mess around with the source code, there are a few things you need to download first. 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



1. Download and Python 3.6 
	link to download from  - https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
	check the box to include in path
	click the customized install
	check all boxes on the options screens
	check all boxes on the advanced screen
	click disable path length limit

To verify that python installed correctly:
	open a command prompt
		enter >python --version
			you should get a response such as "Python 3.6.6"
To verify that pip installed correctly:
	open a command prompt
		enter >pip --version
			you should get a response such "pip 10.0.1 from c:\program files\python36\lib\site-packages\pip (python 3.6)"

2. Install Django - This is the web framework used to design the website
	open an elevated command prompt
		enter pip install Django
		When complete you will get a confirmation or an error message

3. Install Jinja2 - This is a template engine
	open an elevated command prompt
		enter pip install Jinja2
		When complete you will get a confirmation or an error message


4. Install gitbash - This is a git tool needed to push and pull dev
	Download and run the installer from https://git-scm.com/download/win
	During the install take all defaults except the following:
		choose gitbash only
		choose enable symbolic links

5. Prepare the environment for first use
open the gitbash prompt
	change into the documents directory with "cd Documents"
	create a new directory (I called mine whiteboard) "mkdir whiteboard"
	change into the directory where your local git repo will live. 
		cd whiteboard
		Enter the following command> git init
		Enter the following command> git remote add origin https://github.com/ani55555/Whiteboard
		Enter the following command> git pull origin master
6. Run the server for the first time
you need to be using a standard command prompt for this
	change directory to where the project lives
		(for me this is c:\users\ssanders\documents\whiteboard)
	Enter the following command> python manage.py runserver
	To test if the above worked open a browser and navigate to http://127.0.0.1:8000

7. Some editor/IDE that can process Python. Use Atom, its amazing imo
	https://atom.io/

NOTES:
(Optional) ---> If you wanna pull from Git, navigate to a desired directory and use git pull origin master on the Git command line. 
You can download the Git command line here ---> https://git-scm.com/downloads
Full documentation on how to use Git here ---> https://git-scm.com/docs

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



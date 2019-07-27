TO BE COMPLETED!


# **DumpDinners Recipe App**
 
This project is my 3rd Milestone Project for Full-Stack Diploma in Software Development. It is the second last project for completion of this course. It is a Data Centric Project, using Python, Flask, MongoDB, HTML5, CSS3, Materialise CSS and some Bootstrap. I found the recipes from websites and added them to database, as well as registered users. 


## **UX Design**

Dump and Bake Idea originated from looking on this website - https://www.amazon.com/Dump-Dinners-Perfect-Cookbook-Delicious-ebook/dp/B01AV6T4DG

Used materialise css and added buttons (add recipe) to make the UI intuitive. 


**Garret's 5 Planes of UX design are as follows:-**

### **Strategy (The goal)**


### **Scope (What tasks can be done)**



### **Structure (Plan or Flow of Interactions)**




### **Skeleton**



### **Surface**


 


## **Features**
 
### **Existing Features**

### **Features Left to Implement**


## **Tech Used**

### **Technologies used includes:**


## **Testing**

User doesn't exit flash message - if incorrect username entered (image to be attached). Case sensitive, so if using uppercase letter instead of lower for password, won't be able to login.





## **Version Control (GitHub)**


As I had to switch from using Cloud9 to AWS Student Educate IDE at the end of June, I therefore created a new repository for my DumpDinners Project. However, due to the fact that AWS were using an email which I registered with initially, which isn't the same as my email or username on my GitHub account, therefore commits to this project were not recorded in my username from the period 29/6/19 to 25/7/19. The following is a list of about 30 commits that were not showing in my contribution stats, and it was only when I realised what was happening and how to fix it, that my contributions started showing again in my correct username/email. I used the following command to rebase my GitHub account with AWS, and was able to fix this issue. 

Git Commands to use to rebase username and user email:-
git commit -m --amend --author="username <name@example.com>"

Initially I referred to this article from Stack Overflow, and although it only referred to rebasing a single commit, I was at least able to rebase my author name correctly - https://stackoverflow.com/questions/3042437/how-to-change-the-commit-author-for-one-specific-commit

I later enquired on Stack Overflow how to go about rebasing all the other commits that were commited under a generic name 'Ubuntu', and posted this question (which recieved answers). However I did not have time to look further into interactive rebasing and the first answer was author change, which seemed to carry some risk, so will rebase my commits at a later time - https://stackoverflow.com/questions/57229016/trying-to-rebase-rename-30-commits-on-github/57229154

List of commits under name of 'Ubuntu' instead of my username (29/5/19-25/7/19):-

Commits on Jul 25, 2019
changes to styles.css, base.html, recipe.hmtl
Ubuntu committed 2 days ago
 
removed some code commented out in edit_recipe and add_recipe.html, r…  …
Ubuntu committed 2 days ago
 
fixing issues with updating recipe - cateogry name and date added isu…  …
Ubuntu committed 2 days ago
 
Commits on Jul 24, 2019
removal of extra photo, changes to base.html and recipe.html, added m…  …
Ubuntu committed 3 days ago
 
changes to README, as pushed wrong README (from another project) by m…  …
Ubuntu committed 3 days ago
 
Commits on Jul 21, 2019
changes to register page, fixing footer and button
Ubuntu committed 7 days ago
 
Commits on Jul 20, 2019
changes to allrecipes.html, allrecipes1.html, base.html
Ubuntu committed 7 days ago
 
Commits on Jul 17, 2019
adding recipes
Ubuntu committed 10 days ago
 
Commits on Jul 15, 2019
changes to recipe page layout, centered headings
Ubuntu committed 12 days ago
 
changes to base.html, adding comments
Ubuntu committed 12 days ago
 
added further changes to recipe page
Ubuntu committed 12 days ago
 
changes to color scheme and buttons across templates, modified social…  …
Ubuntu committed 12 days ago
 
Commits on Jul 14, 2019
added social icons to footer, fixed add and update category issues bu…  …
Ubuntu committed 13 days ago
 
Commits on Jul 12, 2019
centered some nav bar items
Ubuntu committed 15 days ago
 
added orange gradient colored background to home page to compliment blue
Ubuntu committed 16 days ago
 
changes to footer, added social icons and links, re-added favicon
Ubuntu committed 16 days ago
 
Commits on Jul 11, 2019
added recipes, modified addrecipe, base, editrecipe, recipe html file…  …
Ubuntu committed 16 days ago
 
Commits on Jul 7, 2019
metadata changes to tabs
Ubuntu committed 20 days ago
 
changes to templates
Ubuntu committed 20 days ago
 
Commits on Jul 6, 2019
centered login or register text on top of navbar
Ubuntu committed 21 days ago
 
added 404 page, amended templates and app.py. Got search working
Ubuntu committed 21 days ago
 
Commits on Jul 1, 2019
updated search bar in main body
Ubuntu committed 26 days ago
 
modified requirements.txt
Ubuntu committed 26 days ago
 
solved issues with views, as must be a numerical value and included '…  …
Ubuntu committed 26 days ago
 
Commits on Jun 29, 2019
updated all files and migrated from cloud9
Ubuntu committed 28 days ago 


## **Deployment**



## **Information**



## **How to run the code in this project**

Commands used to install dependencies:-


- installing virtual environment: sudo yum install python-virtualenv (on aws, otherwise use sudo apt-get install python-virtualenv)
- installing flask: pip install flask/pip3 install flask
- upgrading pip:sudo pip install --upgrade pip
- installing flask_pymongo: pip install flask_pymongo --user/pip3 install flask_pymongo --user
- pip install flask_pymongo --user


## **Credits**

http://cookbook-pierce.herokuapp.com/get_home

https://github.com/pierceoneill/code-institute-milestone-project-04

https://recipe-glut.herokuapp.com/index

https://github.com/5pence/recipeGlut



Dump recipe websites:

https://tasty.co/article/melissaharrison/vegetarian-dump-dinners
https://www.theseasonedmom.com
https://parade.com/843958/kristanroland/20-dump-it-and-forget-it-crock-pot-meals/#gallery_843958-4
https://myheavenlyrecipes.com
https://www.bettycrocker.com/menus-holidays-parties/mhplibrary/recipes/dump-and-go-dinners-to-save-your-crazy-days?esrc=18010&utm_medium=cpc&utm_source=pinterest&utm_campaign=omp_display_ompbc_td_eff&pp=1
https://parade.com/843958/kristanroland/20-dump-it-and-forget-it-crock-pot-meals
http://bargainbriana.com/bourbon-chicken/
http://bargainbriana.com/one-hour-8-chicken-freezer-meals/
https://damndelicious.net/2013/09/22/5-ingredient-white-chicken-chili/
https://www.tasteofhome.com/recipes/cherry-pudding-cake/


	
	
	
	
	
	
	
	




### **Content**

### **Code**


### **Acknowledgements**



> Written with [StackEdit](https://stackedit.io/).
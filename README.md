# **DumpDinners Recipe App**
 
This project is my 3rd Milestone Project for Full-Stack Diploma in Software Development. It is a Data Centric Project and the second last project for completion of this course. The project consists of Flask, MongoDB, Python, HTML5, CSS3, Materialise CSS, javascript and some Bootstrap vendor is also included, although I mainly used Materialise CSS to create it. I created a registered users and recipes collections in DumpDinners database using MongoDB. Initially I had another collection for 'categories' but as there was an issue with this being updated when a recipe was added, I omitted using this collection but kept categories as user-input field. 

## **UX Design**

The initial idea of creating DumpDinners website originated from looking at a cooking websites and specifically found this one interesting, and so followed on from that by creating this project -[Original Idea for DumpDinners website](https://www.amazon.com/Dump-Dinners-Perfect-Cookbook-Delicious-ebook/dp/B01AV6T4DG).

I wanted to show the various recipes which Dump and Bake includes, and included recipies in the following categories (Chicken, Meat, Vegetarian, French Cuisine, Desert). There are many more categories and the list is extensive. The idea behind Dump and Bake is that all you have to do is prepare the meal ahead of time (ie) in freezer, then simply dump it in a slow cooker and wait. For this reason dump meals are easy to prepare, as they don't involve a lot of time standing over a cooker. In addition they are very nutricious and healthy meals for all the family. In a nutshell, a dump dinner is a crock pot recipe you've prepared ahead of time. This article explains perfectly the concept of what a dump meal is about -[Descibing what a Dump dinner or meal is](https://blog.thatcleanlife.com/why-you-need-dump-dinners-in-your-life/).

I used materialise CSS [Materialise](https://materializecss.com/). I used materialise buttons (which are similar to what Google uses) for functions such as viewing, adding, editing and deleting recipes. The buttons have a 'wave' effect when clicked. An example of code for a 'submit' button with wave effect is:- 

		<button class="btn waves-effect waves-light" type="submit" name="action">Submit
			<i class="material-icons right">send</i>
		</button>
		
I also used materialise cards for the recipes, and font-awesome icons to style buttons and other features - [Font Awesome](https://fontawesome.com/v4.7.0/).

**User Stories**
First and foremost, the user is the primary focus of creating a website. The type of user I would expect to use DumpDinners website would be as follows:-

- Someone who likes food and cooking good healthy nutricious meals, easy to cook. 
- A student
- Stay-at-home mum
- Working mum with kids
- Anyone else who is interested in preparing and cooking dump meals and deserts. 

From researching what a user story is, I realised it is "a tool used for Agile software development to capture a description of a software feature from an end-user perspective. The user story describes the type of user, what they want and why. A user story helps to create a simplified description of a requirement." - [What is a User Story?](https://searchsoftwarequality.techtarget.com/definition/user-story).
As per previous projects I completed, for direction in UX design I referred to what I learned in the Code Institute tutorials, and also referred to this website about user experience, [Red Rocket Web Specialist](https://www.redrocketmg.com/5-planes-UX-design-great-website/), who consider that the two most important aspects of designing a good website are (1) the Abstract aspect (idea, goal, etc) and (2) the Concrete aspect (how to get a user to click on a link, etc). The transition from Abstract to Concrete should remain linear to ensure a smooth transition, with each phase being fluid and overlapping. 

**Garret's 5 Planes of UX design are as follows:-**

### **Strategy (The goal)**

The strategy is concerned with the goal of the project, which was to create a user friendly, interactive recipe website for dump recipes. As a user I wish to interact with the recipe website, by being able to login, logout, add, delete and update recipes.  
CRUD functions are demonstratable throughout the project. 

### **Scope (What tasks can be done)**

The tasks that can be accomplished on DumpDinners website involve all CRUD functions - therefore the user will be able to interact by viewing, adding, editing and deleting recipes. Users must login using their 'username' or register, if they haven't already done so. The website uses Flask to redirect to appropriate urls, so that users will know where to go. The user should have a good and smooth experience of using the website. CRUD is an acrynom standing for (create, read, update and delete) - [What is CRUD?](https://www.codecademy.com/articles/what-is-crud).

CRUD functions are detailed further in the **Testing** section showing screenshots of 'flash' messages on successfully implementing CRUD functions, for example, whenever a user adds a recipe or logout. Flash messages also show errors (ie) if users input incorrect password or if username was incorrect.

### **Structure (Plan or Flow of Interactions)**

This is the plan or flow of interactions users will take to navigate and understand DumpDinners website. I considered my database structure and detail below the structure of tables used for the DumpDinners website. Mainly just 2 tables were used (register and recipes). There was a 3rd table for categories, but due to having experienced issues with updating categories using materialise select dropdown menu, I changed this field to an input field. I therefore no longer required the categories table and deleted it. Within each table is a collection and within each collection a document. I used mLab to create my database from the backend. 

[MongoDB Schemata showing collections and user (register) collection](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/Mock-ups/Mock-up%20DumpDinners-MongoDB%20Tables%20Schema%20and%20Register%20collection.pdf)

[MongoDB showing collection for Recipe](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/Mock-ups/Mock-up%20DumpDinners%20-%20MongoDB%20Recipe%20collection.pdf)

### **Skeleton**

In this section, I tried to place the elements in appropriate places, and in a logical order – such as navbar, then heading, then brief explanation of the project using unordered listing.  I used Baslamic to create wireframes. I visualised in my mind and sketched the layout, and instead of using the sketch tools (and also due to time limitations) which Baslamic provides, I created blobs using Baslamiq with screenshots of different views on website, giving explanation for each. 

I took screenshots of the various views for user logged in, add recipe, edit recipe, recipe, login, register and home/index - [Wireframes/Mock-up Blobs using screenshots and Baslamiq](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/Mock-ups/Mock-ups%20DumpDinners.pdf)

I also tested the search button for recipes, which users can search by inputting Recipe Name, Username, Category. Ingredients, Calories or Cooking Time. The results are as follows and when the user clicks on 'More', they're shown the recipe page - [SEARCH FEATURE](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/Mock-ups/Mock-ups%20DumpDinners-Search%20button.pdf)

### **Surface**

https://www.shutterstock.com/

The surface, or the skin – is the interface for which visitors will engage with the dashboard. I kept the color scheme congruent, using complimentary colors such as blue and organge through the various website views, and used an orange gradient scheme throughout to add color to all areas of the website to enhance the look and feel of the website. I referred to this article - [CSS Background Gradient](https://www.quackit.com/css/codes/patterns/css_background_stripes.cfm)
 
I used a pencil art image for my main background image on the Home/Index page, referring to this article - [Pencil Art Theme](https://www.shutterstock.com/search/pencil+drawing)

All typography was in English but as Google has a translator, can be easily translated. I particularly choose a congruent colour scheme (purple for navbar and footer and lighter shades for body and drop down menus in the dashboard), which I felt gave an appropriate overall appearance.

## **Features**
 
### **Existing Features**
- Congruent Color Scheme (Blue and Orange - which are complimentary colours) with white font used as and when was more appropriate to highlight a link. 
- User login and register features. Flash messaging for incorrect password or username. 
- Routing to relevant pages, after a user undertakes an action/task (ie) when a user logs out, they're thanked with a flash message and redirected to login page (if they wish to login again). 
- Adding recipes feature, users (once logged in) can add recipes under their username. Once added they can view, edit and delete any recipe added under their username. 
- Users (logged in or otherwise) can view the first 4 recipes, on the Home (allrecipes1.html) page. To review all other recipes, they must login or register. 
- Website is responsive across all mobile devices and extensive testing done (see **Testing** section below). 
- Search bar to search for recipes using 'keyword' or 'ingredients' or 'recipe name'. This feature is responsive across all mobile devices. 
- I added a favicon feature to DumpDinners website, referring to this article - [Favicon](https://www.flaticon.com/)
- Users can 'Like' a recipe and likes are incremented, in the same way as user views. 'Likes' are not specific to any username but users does need to be logged in, to 'Like' all recipes (allrecipes.html). Anyone can 'Like' the first 4 recipes, however, as this is the Home page and does not require user login. 
- Users can search a recipe by Recipe Name, Username, Ingredients, Category, Calories and Cooking Time. Search navigation is easy. I have just recently added 2 further categories (Calories and Cooking time - as these are important factors for users).
- Users can share on social media (Facebook, Twitter, Pinterest, Google+) once they get to the recipe page. They can also see on how many users viewed the recipe or liked it, and also the categories. Unfortunately I wasn't able to 'increment the number of social media shares, despite trying very hard to do so. I downloaded ssk files (from social share kit), which had very good buttons but there was no 'count of shares, despite a lot of css code being used, so I disregarded this idea and went with what I understood and what worked, even if there was no increments of shares. It is possible for users to share recipes however, regardless if they are incremented or not (and I have tested this myself).
- Throughout the website there are links to home/index page, and a back-button on recipe, add recipe and edit recipe pages. 
- Due to time restraints, I did not have time to create a function for 'danger' message when user goes to delete a recipe. I therefore added a heading (in red) across all recipe pages. 

### **Features Left to Implement**
- Unfortunately I did not get time to add a user dashboard, for example showing all recipes 'Liked' or recipes viewed. I had hoped possibly to be able to get this done but unfortunately I ran out of time. 
- I had hoped to add flask messaging for users who want to delete a recipe they added, with a 'danger' message (ie) "Do you really want to delete this message, as this action is irreversible?". Unfortunately I did not get time to do this. 
- Recipes are displayed showing ingredients and methods in paragraph format, separated by bullet points, rather than on single lines. I used - 'pre-wrap': 'normal' for this. Ideally I would've preferred that the contents of the recipe were listed singularly but I had a lot of work to do developing the website, and I didn't focus too much on this aspect. My main purpose was to build a website that looked and felt good to use, and was functional, even if only basic functions. The important thing I remembered was that functions like CRUD could be carried out with minimum of ease. 
- Login security features was handled by importing 'from werkzeug.security import generate_password_hash, check_password_hash'. However I did not install flask bycrypt, so users could create any password and didn't have to be composed of numbers/special characters/letters, etc. 
- I did not get to use Pagination for the recipes (12 in total). As I focussed on other parts of the project more and was also under time pressure for submitting, so I could not implement this feature. 

### **Flask**

- What is Flask?
Flask is often referred to as a micro framework. Flask is a web application framework written in Python. It is developed by Armin Ronacher, who runs Pocco (International group of Python Enthusiasts). Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects. Flask uses a collection of libraries and modules that enables a web application developer to write applications without having to bother about low-level details. 

- WSGI
WSGI is a Web Server Gateway Interface (WSGI) for a universal interface between the web server and the web applications. It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.

- Jinja2
Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages. It aims to keep the core of an application simple yet extensible. 

To understand more about Flask, WSGI and Jinja2, click here -[FLASK](https://www.tutorialspoint.com/flask/flask_quick_guide)

## **Tech Used**

### **Technologies used includes:**
- **HTML5**, **CSS3**, **Javascript**, **JQuery**, **Materialise CSS**, **Python**, **Flask** **Flask Py_Mongo**, **MongoDB** 

Base languages used to create website.

Used **HTML5** to handle page routing and to build custom directives - [HTML5](https://www.html5rocks.com/en/)

Used **Font Awesome** icons to give our project an intuitive 'google style'look and feel - [FONT AWESOME 4.7.0](https://fontawesome.com/v4.7.0/)

Used **CSS3** for styling and enhancing the look of the website - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)

Used **Javascript** (minified versions) added end of document - [JAVASCRIPT](https://developer.mozilla.org/bm/docs/Web/JavaScript)

Used **JQuery** to trigger ready() functions for datepicker, collapsible side nav bar and materialise selection functions - [JQUERY](https://jquery.com/)

Downloaded **Bootstrap** vendor files but did not make use of bootstrap developing the project. At the start, I was unsure whether to use Bootstrap or Materialise CSS, but choose and stayed with using Materialise CSS and UI throughout the project - [BOOTSTRAP](http://getbootstrap.com/getting-started/)
 
Materialise CSS UI was used throughout this project. I liked the look and feel of this UI, which is the same style Google use -[MATERIALISE CSS](https://materializecss.com/)
 
Used Python 3.6.7 for developing this project - [PYTHON](https://docs.python.org/3/)

Used Flask 1.0.2 for developing this project - [FLASK](https://flask.palletsprojects.com/en/1.0.x/)

Used Flask_Pymongo 2.2.0 for developing this project -[FLASK_PYMONGO](https://flask-pymongo.readthedocs.io/en/latest/)

Used Pymongo 3.7.2 for developing this project - [PYMONGO](https://pypi.org/project/pymongo/)

Used Jinja2.10 for developing this project - [JINJA2](http://jinja.pocoo.org/docs/2.10/)

Used Werkzeug 0.14.1 for developing this project - [WERKZEUG](https://www.palletsprojects.com/p/werkzeug/)

Used Mongo DB (mLab) for this project - [MONGO DB](https://mlab.com/)

## **Testing**

Flask uses 'flash' messaging' for messages to appear when the user performs a task (such as adding a recipe or logging out). The following flask messages were tested, as was the underlying function (adding recipe, logging out) to ensure CRUD functions worked properly and the user was able to perform these functions. When a user first views DumpDinners website they can only view 4 recipes on the home page. Those recipes can be viewed further by clicking the 'More' button and the recipe ingredients and methods shown. The user can 'Like' any or all of the 4 recipes. The 'Likes' will be incremented in the registered user collection in MongoDB, and shows on the recipe summary (ie) the view the user sees before clicking on 'More'. Any user can view only 4 recipes (and 'Like') without having to login or register. However to view the full range of recipes, and be able to add their own recipe (as well as edit and delete), users MUST login or register. The website is correctly routed using Flask (app.py) routing to correctly route users to whichever page they wish to view. User and non-user views were tested across many pages and functions to ensure they worked correctly, and fellow student from Code Institute was asked also to test, which they did. 

In addition, I tested all links to make sure they redirected correctly and worked, such as url for home page and all recipes page. I also tested responsiveness on mobile versions by clicking on links in responsive view. I tested search feature, to make sure the search button functions correctly and it does. I also tested this across mobile versions and works correctly. 

Flash messages were shown for the following:-

- Wrong password - [INCORRECT PASSWORD MESSAGE](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/static/flash%20messages/login%20password%20error%20-%20incorrect%20password.PNG)

- Wrong or non-existent Username - [USER DOESN'T EXIST MESSAGE](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/static/flash%20messages/user%20login%20error%20-%20user%20doesn't%20exist.PNG)

- Logged Out - [LOGGED OUT MESSAGE](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/static/flash%20messages/log%20out%20message%20-%20thank%20you%2C%20etc.PNG)

- Registered - [THANK YOU FOR REGISTERING MESSAGE](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/static/flash%20messages/thank%20you%20for%20registering%20message.PNG)

- Recipe Added - [RECIPE ADDED MESSAGE](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/static/flash%20messages/thank%20you%2C%20you're%20recipe%20has%20been%20inserted!.PNG)

- Login - [WELCOME BACK MESSAGE](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/static/flash%20messages/welcome%20back%20message%2C%20when%20on%20successful%20login.PNG)

I also tested features such as 'Search' function to ensure it worked correctly and my findings are that it does work successfully (on both large and small screens). Using can search using Recipe Name, Username, Category, Ingredients, Calories or Cooking Time. These are the results of tests using Search - [RECIPE SEARCH](https://github.com/Deirdre18/dumpdinners-recipe-app/blob/master/Mock-ups/Mock-ups%20DumpDinners-Search%20button.pdf)

I've also tested responsiveness on both mobile and desktop, in a variety of screen sizes using Google Chrome Developer tools. I tested responsiveness across small, large and medium screens. 

- Google Chrome (version 68)
- Opera (version 55)
- Mozilla Firefox Developer (version 63)
- Internet Explorer (version 11)

**Testing across desktop/large laptop (using developer tools) and mobile browsers**
I have tested DumpDinners website on the above desktop browsers. On Firefox developer tools, I tested mobile responsiveness for Apple iPad Air2, Apple iPad Mini2, Apple iPad iPhone 6s, Google nexus 4,5,6,7, Laptop (1280px x 720px and 1366px x 768px), Nokia Lumia 520, Samsung Galaxy Note 3, Samsung Galaxy S5 and S7. On Chrome developer tools, I tested responsiveness for mobile small (320px), Mobile medium (375 x 840 px), Mobile large (425 x 960 px), tablet (768px x 2152px), laptop medium (1024px x 2241px), laptop large/medium (1440 x 3586px), laptop large (2138px x 5977px). 

Further testing has not been carried out at this stage, due to time limitations. 

## **Version Control (GitHub)**

I used version control (GitHub) on an ongoing basis to back-up my code to a remote repository at regular intervals throughout development of the DumpDinners website project. 

In managing commits on GitHub however, I encountered some issues, which I tried to resolve, but as submission of this project is soon, I have left the issues as they are (as they do not affect the code used or the number of commits, etc). In addition, I have detailed the issues I encounterd and what went wrong and why. 

**Explanation of commits which were commmited under the generic name of 'Ubuntu' rather than my username and steps I took to resolve the issue.** 

As I had to switch from using Cloud9 to AWS Student Educate IDE at the end of June, I therefore created a new repository for my DumpDinners Project. However, due to the fact that AWS were using an email which I registered with initially, which isn't the same as my email or username on my GitHub account, therefore commits to this project were not recorded in my username from the period 29/6/19 to 25/7/19. The following is a list of about 30 commits that were not showing in my contribution stats, and it was only when I realised what was happening and how to fix it, that my contributions started showing again in my correct username/email. I used the following command to rebase my GitHub account with AWS, and was able to fix this issue.

Git Commands to use to rebase username and user email:- git commit -m --amend --author="username name@example.com"

Initially I referred to this article from Stack Overflow, and although it only referred to rebasing a single commit, I was at least able to rebase my author name correctly -[Changing Commit Author](https://stackoverflow.com/questions/3042437/how-to-change-the-commit-author-for-one-specific-commit/) 

In addition, I posted this article on Stack Overflow asking how to resolve the issue - [Rebasing commits](https://stackoverflow.com/questions/57229016/trying-to-rebase-rename-30-commits-on-github/57229154)  

This is a **list of commits under name of 'Ubuntu'** instead of my username from 29/5/19 to 25/7/19:-

**Commits on Jul 25, 2019**
changes to styles.css, base.html, recipe.hmtl Ubuntu committed 2 days ago --
removed some code commented out in edit_recipe and add_recipe.html, r… … Ubuntu committed 2 days ago
fixing issues with updating recipe - cateogry name and date added isu… … Ubuntu committed 2 days ago
**Commits on Jul 24, 2019** removal of extra photo, changes to base.html and recipe.html, added m… … Ubuntu committed 3 days ago
changes to README, as pushed wrong README (from another project) by m… … Ubuntu committed 3 days ago
**Commits on Jul 21, 2019** changes to register page, fixing footer and button Ubuntu committed 7 days ago
**Commits on Jul 20, 2019** changes to allrecipes.html, allrecipes1.html, base.html Ubuntu committed 7 days ago
**Commits on Jul 17, 2019** adding recipes Ubuntu committed 10 days ago
**Commits on Jul 15, 2019** changes to recipe page layout, centered headings Ubuntu committed 12 days ago
changes to base.html, adding comments Ubuntu committed 12 days ago
added further changes to recipe page Ubuntu committed 12 days ago
changes to color scheme and buttons across templates, modified social… … Ubuntu committed 12 days ago
**Commits on Jul 14, 2019** added social icons to footer, fixed add and update category issues bu… … Ubuntu committed 13 days ago
**Commits on Jul 12, 2019** centered some nav bar items Ubuntu committed 15 days ago
added orange gradient colored background to home page to compliment blue Ubuntu committed 16 days ago
changes to footer, added social icons and links, re-added favicon Ubuntu committed 16 days ago
**Commits on Jul 11, 2019** added recipes, modified addrecipe, base, editrecipe, recipe html file… … Ubuntu committed 16 days ago
**Commits on Jul 7, 2019** metadata changes to tabs Ubuntu committed 20 days ago
changes to templates Ubuntu committed 20 days ago
**Commits on Jul 6, 2019** centered login or register text on top of navbar Ubuntu committed 21 days ago
added 404 page, amended templates and app.py. Got search working Ubuntu committed 21 days ago
**Commits on Jul 1, 2019** updated search bar in main body Ubuntu committed 26 days ago
modified requirements.txt Ubuntu committed 26 days ago
solved issues with views, as must be a numerical value and included '… … Ubuntu committed 26 days ago
**Commits on Jun 29, 2019** updated all files and migrated from cloud9 Ubuntu committed 28 days ago

## **Deployment**

This project is developed on Heroku Platform - [DumpDinners](https://dumpdinners-recipe-app.herokuapp.com/)

I used Heroku to deploy my project -[Heroku](https://dashboard.heroku.com)
I set the following Configuration Variables in Heroku:-

IP - 0.0.0.0
PORT- 5000
MONGO_DBNAME
MONGO_URI
SECRET_KEY

Sign up to Heroku platform is free and there is extensive documentation for developers. If developing a python app using Heroku, it is necessary to for the app to be detected by Heroku when deploying and the command "web: python app.py
" is used, which is incorporated in a Procfile (P must be capitalized).

## **How to run the code in this project**

Below is a list of some of the technologies I installed to run DumpDinners project. I started the project initially using Cloud9 IDE for education. However, at the end of June 2019, I could no longer use Cloud9, as the service was stopped and I commenced using AWS Cloud9 Student Start Education. I therefore created a new repository in AWS and cloned the previous one. 

To run DumpDinners website:-

1. Clone the repository url link to your workspace- [DumpDinners](https://github.com/Deirdre18/dumpdinners-recipe-app.git)
2. Install Flask - $pip install flask
3. Install Python - $sudo apt-get install python3.6 (or python 3.7)
4. Install Flask_Pymongo - $pip install flask_pymongo (in some instances, depending on what IDE is being used, it might be necessary to append --user to the end of the command.
5. Install requirements.txt file by using $pip freeze > requirements.txt

Other installments which maybe required:-
installing virtual environment: sudo yum install python-virtualenv (on aws, otherwise use sudo apt-get install python-virtualenv)
upgrading pip:sudo pip install --upgrade pip

**Note: PIP means means Package Manager for Python packages. To check which version of PIP you are using, use pip --version (in Ubuntu). Refer to PIP documentation for further guidance - [PIP](https://pypi.org/project/pip/)

## **Credits**

I give credit to viewing fellow students recipe websites, who have completed this project, and looking on GitHub to view their code.
I used some of the code from two students in particular. I found two projects particularly helpful for understanding coding issues I ran into doing my project (Carribean Recipe and RecipeGlut), and helped me understand more by referring to their code. I found also this project inspired me to use materialise css in my project (Daddy Does Dinner). I have listed the project links below and credited the authors for code used in my source code on my GitHub repository. I also found looking at the other projects listed below very helpful, and seeing the source code used. For this project I did it mainly on my own, with guidance from research and resources online, as well as referring questions to fellow students on Slack at times. 

## **Recipe Websites of fellow students I referred to:-**

[Carribean Recipe App] -(https://recipe-app-flask-mongo.herokuapp.com/)
[RecipeGlut] -(https://recipe-glut.herokuapp.com/)
[Daddy Does Dinner] -(https://cookbook-pierce.herokuapp.com/)
[Surfing Europe] -(https://surfingeurope.herokuapp.com/)
[Desert Search] -(https://dessert-search-ms3ag.herokuapp.com/)
[Cuisine] -(https://recipe-app-python.herokuapp.com/)

## **Recipe Websites I referred to:-**

[The Seasoned Mom] - (https://www.theseasonedmom.com) 
[My Heavingly Recipes] - (https://myheavenlyrecipes.com)
[Betty Crocker] - (https://www.bettycrocker.com)
[20 Dump it and forget it crockpot meals] - (https://parade.com/843958/kristanroland/20-dump-it-and-forget-it-crock-pot-meals) 
[Taste of Home] - ( https://www.tasteofhome.com)
[Damn Delicious] - (https://damndelicious.net/)
[Bargain Briana] - (http://bargainbriana.com/)

### **Content**
The content contained in the project is mainly my own and anywhere I've used any outside references, I've made reference to them (as in this README document). I've carefully referenced all sources of code and websites referred to, as well as my own research. 

### **Code**
- I based the project on code I learned throughout the course from the tutorials of [Code Institute](https://www.codeinstitute.net/) and by referring to the lessons. I also referred to [W3Schools](https://www.w3schools.com/) and also on occasion I referred to [Stack Overflow](https://stackoverflow.com/).

- I posted my own question on Stack Overflow regarding issue with Git commits and rebasing/changing author name for prior commits, which were under 'Ubuntu', instead of my username - [Question on Stack Overflow] - (https://stackoverflow.com/questions/57229016/trying-to-rebase-rename-30-commits-on-github/57229154)

- I referred to these websites for furhter guidance on issues encountered developing this project:-

Referred to this article for help understanding how to set secret key - [SECRET_KEY)(https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key)

Referred to this article for understand how to store flask sessions in dictionary - [FLASK SESSIONS)(Referred to this article for help understanding how to set secret key - [SECRET_KEY)(https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key))

To understand how Flask Login works, referred to this - [FLASK SESSIONS)(Referred to this article for help understanding how to set secret key - [FLASK LOGIN)(https://flask-login.readthedocs.io/en/latest/)

### **Acknowledgements**

I received inspiration for this project from many suurces, from looking at recipe websites, to my own interest in food and cooking, to the brillian websites my fellow course mates created, some of which were truly outstanding. Also to the Slack Community of fellow students at Code Institute for anyways being there in times of need to help each other.


Written with [StackEdit](https://stackedit.io/)
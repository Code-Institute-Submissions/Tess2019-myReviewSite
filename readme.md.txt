Board games for two

The goal for this project is to provide a structured information list with board games for two people, main focus on adults. The website list will show cards with pictures of the game, a short text and a link that opens in a new tab for easy acess to buy the game.


Ux
  As a adult user i want:
? I want to easily find and read about fun board games.
? Easy see and access to navigate the menu.
? To see images of the game and description about the game.
? Want to find out where to buy games.
? Want to read about more game tips.
? As a user I have the opportunity to be able to share my game tips with others.
? Visual feedback when using interactive forms or buttons.
? As a user I want to be able to contact the developer with questions.

Existing features that helps users in website:
? The main page of the website directs the user from start to see the the focus point of the site, which displays in a list of board games.
? Search engine input field at the top for users to find games by typing in the name of the game they are looking for. 
? Connected to search engine, game shows or a Sorry not found as flash messages.
? Big image and text about each of the games with a  link underneath the text section.
? The link opens in a new tab for the conveniens to be able access it later on if the user wants to stay on site for more reading.
? An interactive Navbar for easy navigation of content in the website, with Home, About, registration and contact.
? The website provides a member list, where the user can read game tips from other users.  
? Information about adding a game, a user needs to be registered.
? Registration page for users to be able to create a profile by filling in a registration input field form and  clicking  the easy to see Registration button.
? Required implements in forms to show red alert lines and messages on each row that's not adequately filled in by the user.
? Flash messages when Registration or LogIn form sessions come through, either valid or invalid.
? When successfully logged In, redirect  the user to their profile page and they get access to the Add Your Game Form  in the Navbar.
? Provides a fill out form for users to add their game they want to suggest.

? Edit and delete buttons in the profile page for the user to fix in their game suggestions.
? A Log out, when clicked, the user will be directed back to the main page.
? The website shows contact with email address in the footer
Existing feature for developer
? As a registered administrator, allowed to edit text or delete or add Games.

Features left to implement
? Add more games. 
? Additional more games in the numbers of players categories.
? A category dropdown suggestion in the form to apply a new game according to the numbers of players(2-4players, 4-6players etc.)
? Different game lists for the different numbers of players.Implement a game rating system for users.
? Implement a game rating system for games.
? Affiliate links for the developer to earn money from the site. For this project it's only a url to where to buy the games.
? For the users to get some kind of bonus, news and/or discount on games if they register for this website.
? Maybe a term of service or rules for the use of the site. The existing text is not a legal agreement but a disclaimer text for this project only. 
? Function displayed as an Arrow to the right of site, that redirects to the top of the page when the user is far down the page.

Wireframes
Balsamiq were used in the designing and planning of this project. I have a copy in my repository in github.
Click Here to see my ideas. 

Technologies Used
This project uses the CRUD mechanisms and database access functionality. I Use a static file (style.css) to apply custom styles. I created a custom Javascript directory and called It script.js.
Materialize- responsive front-end framework based on Material Design. Relies on jquery.
JQuery- use this to simplify DOM manipulation
Font-Awesome- more icons to select from, complement to materialize icon library.
Flask- is a lightweight Web Server Gateway Interface (WSGI) web application framework. It depends on the Jinja template engine and the Werkzeug WSGI toolkit.
Werkzeug- is a comprehensive WSGI web application library. Has become one of the most advanced WSGI utility libraries.
Jinja template engine- is simply a text file. A template contains variables and/or expressions.Any file can be loaded as a template, regardless of file extension. 
MongoDB- stores data in flexible, JSON-like documents.The document model maps to the objects in application code. Ad hoc queries, indexing, and real time aggregation provide powerful ways to access and analyze my data.
Balsamic- wireframing tool, where I sketch my UI idea.
Github- Version control system that keeps the revisions straight, storing the modifications in a central repository. Git is a command-line tool, but the center around which all things involving Git revolve is the hub—GitHub.com—where developers store their projects and network with like minded people.
Heroku- is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps. Heroku provides services, tools, workflows, and polyglot support—all designed to enhance developer productivity.
RandomKeygen - The Secure Password & Keygen Generator, used in the env.py.
w3schools.com -  is a site for web developers, covering all the aspects of web development, example html, css, jquery, python as I use in this project.
Google Chrome Devtools- can help edit pages on-the-fly and diagnose problems quickly, which ultimately helps you build better websites, faster.

Markdown - to write this readme with markdown syntax.It’s a plain text format for writing structured documents, based on formatting conventions from email and usenet. Markdown-formatted text can be opened using virtually any application. 

Testing 

Testing website code:
html validator
css validator
javascript validator
Python validator
Google Chrome Devtools- to inspect DOM or CSS. Right Click the elements panel and select Inspect.


Testing
Testing of the functions in the project website.
This section is divided into main dots in action and under explains the expected effect.
	 
? Click on the pages in Menu
? Redirect to the wanted page
? Have the Navbar in every page that’s linked

? Writing in search with valid game names from existing data and press button
? The game that’s search and found shows at the top of page



? Writing in search with invalid game names from existing data and press button
? Flash message “Sorry not found”
	
? Writing the user register  form with valid data and a click button.
? Green coloured lines when all inputs filled in
? Flash message:” You are Successfully Registered” and redirected to profile page
? Username now added in mongo dB.
? The user can use any syllable and or number to register

? Writing the user Login form with valid data.
? Redirects to profile page.

? Writing the user Login form with invalid data.
? Required implements in forms to show red alert lines and messages on each row that is not adequately filled in by the user.

? Add game for user in a input form
? Added data to MongoDB
? The games data shows in members game list
? And shows up in Profile page

? Click on the Logout in menu.
? User gets directed back to the Login page
? Gets a flash message “You have been Logged out”



Issues

Data display problem
when it was time to get the list of data from the members suggestions i was stuck for a while. what i did was that i forgot to add a new html the member_list.html to display the data from Mongodb. Instead I tried to put the for loop in the boargames.html. I couldn't understand why I didn't get the information from the mongodb, though each game I put in the input form from the add_game.html worked. I could see the data go through to Mongodb. I added the app.route and the member_list.html and I got the data display where i wanted it to go. 
@app.route("/member_list")
def member_list():
    game = list(mongo.db.add_game.find())
    return render_template("member_list.html", add_game=game)



{% for game in add_game %}
                    <!--{{ game.category }} additional feature -->
                    <!--<div class="divider"></div>-->
                            <div class="section.list member-list-img">
                                <h5><b>{{ game.category_name }}</b></h5>
                                <h6>Description:</h6>
                                <p>{{ game.game_description }}</p>
                                <h6>My review:</h6>
                                <p><b><q>{{ game.user_note }}</q></b></p>
                                <p><em>by:{{ game.created_by }}</em></p> 
                            </div>   
                {% endfor%}




Footer problem- did not stick on the bottom of page:
MY CODE:					
.footer{
  display: absolute;
  left:0;
  padding-bottom: 16px;
  padding-top: 16px;
  width: 100%;
  background-color: #117A65;
  color:white;  
}


Fixed with code from freecodecamp
.footer{
  position: absolute;
  bottom:0;
  width: 100%;
  height: 2,5rem;
  background-color: #117A65;
  color:white;  
}


Color issues
When adding colors by name in css the colors would not  always show in html.
To solve this I switched using color names to hex.

Deploy project without showing the SECRET_KEY value



Deployment

Start by signing up, read more here Github account.

Here is a short step by step how to deploy your project to Github

Create a new repository.
- The repository name has to be unique to your account.



 You can set up your GitHub Pages to deploy every one of your repositories in addition to <username>.github.io. This will allow you to ensure all of your sites are deployed automatically whenever you push to GitHub.

In GitHub, navigate to your <username>.github.io repository and click Settings.
Within Settings, navigate to the Source section within the Github Pages section. From the dropdown menu, select master branch and then click Save.
Now, all of your repositories can be found at 
https://github.com/USER/PROJECTNAME.git?
Deploying New Changes
Now that your GitHub Pages site is set up, deploying new changes is easy. Every time you make a change to your site, use the normal GitHub flow. That is, use git commit and git push to send your changes to GitHub. Read more Here about git commands.
How to connect your local project
On your local machine, create a new project folder with the command:
mkdir myproject
Change into that newly-created directory with the command:
cd myproject
Initialize the repository with the command:
git init
Now let's create a readme file with the command:
touch readme.txt
Add the new file to the staging area with the command:
git add .
Now we're going to create our first commit. If you're not sure what a commit is, it's simple: A commit adds the latest changes to the source code to the newly-created repository. These changes will then be part of the head revision of the repository.
To create the commit, issue the command:
git commit -m "added readme"
You can change the text in quotes to be whatever you want, such as "my first commit." Make sure the text in quotes describes what's been done for the commit.
The next step will make use of the GitHub repository address. What we need to do is add the local repository to the origin (the name of the remote repository where you want to publish your commits) of the remote repository. This is done with the command:
git remote add origin https://github.com/USER/PROJECTNAME.git
Where USER is your GitHub username and PROJECTNAME is the name you gave your new project. 
At this point you can then push your work to the remote with the command:
git push -u origin master
When you run this command, you'll be asked for your GitHub username, followed by your GitHub user password. Upon successful authentication, your local repository will be connected to the remote GitHub repository and the readme.txt file pushed to the remote.



Heruko
The Heroku platform uses Git as the primary means for deploying applications (there are other ways to transport your source code to Heroku, including via an API).
When you create an application on Heroku, it associates a new Git remote, typically named heroku, with the local Git repository for your application.
 As a result, deploying code is just the familiar git push, but to the heroku remote instead:
 git push heroku master
Before you create Heroku applications, set up the Procfile so Heroku knows which file runs the app.
Use the echo command in the terminal:
“echo web: python app.py > Procfile”
The Procfile might add a blank line at the bottom, and sometimes this can cause problems
when running our app on Heroku, so just delete that line and save the file.
Check the requirement.txt that the files were created successfully.
In Heroku:
?  Login and click “Create a New App” Use a unique Name for your app using “dash” or “minus” example: “flask-board game-project”
? Select the region closest to you, the click “Create App”
? To connect the app I used the Automatic Deployment from Github repository. Added my repository name and clicked Search. Once it find my repo I clicked connect to this app.
? Click on “settings” tab and click Reveal Config Vars”    
? Here you write which variables are required. Check your env.py file for variables. Don’t use any “quotes” for key or the value.
? · In the first Config Vars input you write the variable IP, vith the value of 0.0.0.0
? Next variable PORT , which is 5000
? Next you copy the SECRET_KEY from the env.py file and past in it in value.
? Write the MONGO_URI for the next variable but leave the value line for the string empty for now.
? Last is the MONGO_DBNAME that is the name of the database you have, so game _manager for me.
? ·Now you have to go back to your terminal and confirm that you see the changes. Type “git status”
? Add the requirements file: “git add requirements.txt”
? Then commit the file: git commit -m “ Add requirements.txt”
? Now add the Procfile: “git add Procfile”
? Commit that file: “git commit -m “Add Procfile”
? Finally do: “git push origin master” (if you have the project in only the main branch)
? Head back to Heroku and go to the “Deploy” tab.
? Now you can “Enable Automatic Deployment”
? Click “Deploy Branch”
? Whenever you now push changes  to github repository, Heroku will receive the code.
? It takes a little while to build so wait until you see a confirmation “ Your app was successfully deployed.
? Click “view” to launch your new app.
? You're done!

Credits

Code credits

? Code for base.html, app.py and env.py files was copied by tutorials provided by Code Institute  tutorials.The code was then modified to suit the website needs and layout.

? Code for the forms for registration, login and adding game functions are copied templates from Materialize and modified to suit the site needs.

? Template code for Navbar and collapsible navbar was copied from Materialize. So was code for the Card template and buttons, and then edited to fit project needs.

? Code for the hex colors used are copied from Color-picker.

? Code for the icons are copied from Font-Awesome.

? Some text for the section Heroku in used was copied from heroku.com

? Text about Github technologies used comes from howtogeek.com 

? Major of the text of the deployment to Github is from easy to read from techrepublic

? Background colors in about page form Css Gradient Generator
? How to deploy without exposing secret_key The Coding Train

? Fixed footer with css from freecodecamp

Media
The photos used in this site are from Unsplash
The Photos of the Games are copied from Amazon. Links are provided to each game on the website. 

Acknowledgments
Inspiration to this project comes from 
Code institutes tutorials
The Strategist
gamesradar


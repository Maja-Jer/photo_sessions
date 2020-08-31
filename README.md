SECRET KEY: 'p@ei#69*b*zz3u4yie-$()@cy^l(+x9&@6ypx+r0lm(3%_9hr7'


https://github.com/AJGreaves/familyhub/blob/master/README.md
https://guides.github.com/features/mastering-markdown/
Started with VSC but decided to go back to Gitpod due to familiarity of the IDE
# UX
## Goals
### Visitor Goals
The central target audience for Photo Sessions are:
People who want to purchase prints for their house or business
Bloggers or web developers who want copyrighted photos for their sites or blogs (future development)
Business owners who want photos for their business, be those digital (next level fof teh site) or prints
 
 
### User goals are:
Purchase photos/prints
Navigate the site in an intuitive manner and complete the purchase
See what is available on the page and decide if any of the photos work for they need it for
 
 
 
A few of the possible goals users might have:
 
 
 
The design of this site fits the conventions of similar sites, and lays out the information in a user friendly and accessible way.
 
<!--The Photo Sessions page allows users to search by location, category, rating -->
 
### Business Goals
 
Business user goals are:
 
A well thought-out, well designed, user-friendly platform that will benefit my business.
 
A user interface that is user friendly for me to input my data easily and efficiently.
 
Value for money (at the moment the website is a student project, but eventual planning is to monetise this site, so it is worth adding this important goal here now.)
 
Photo Sessions is a great way to meet these user needs because:
 
The user interface for inputting activity data has been carefully controlled to validate input and make sure what is provided fits the needs of the database structure. Setting input field types to ------- etc makes sure the user is prompted when the data they provide is incorrect.
 
The edit photo page is clearly structured and laid out in a simple and easy to understand
 
 
The account page for the admin user shows all their existing products and gives them the option to view, edit or delete them from this location.
 
The users needs on each page have been thought about and buttons provided for these paths through the site, to make navigating easy.
 
### Photo Sessions Goals
Provide an effective, easy to use site for the users wishing to purchase prints
 
So that I can learn and practice frontend and backend programming together for the first time. To combine the use of HTML, CSS, Bootstrap and JavaScript with Python, Django....
 
While this is currently a student project, the idea is to transform this site into a site that sells prints of my personal photos and print of my friends' artwork (check Features to implement)
 
# User Stories
## Visitor Stories
As a visitor to Photo Sessions I expect/want/need:
 
To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.
 
The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.
 
The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.
 
As a user who is interested to find photos from a particular country, I want to be able to find them easily. I also want to be able to filter them by rating, category(country) and price
 
The site to provide easy access to the photo, rating, description, pricing and reviews.
 
As a user on a budget, I want to be able to filter results by pricing. I also want to know what photo has the best rating from the customers that have already purchased the prints.
 
As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices.
 
 
 
As a regular user of the Photo Sessions website, I expect to be able to connect to the social media channels, to keep up to date with new entries on the site.
 
As a user of Photo Sessions, I expect to be able to easily get in contact via a contact form, register, create an account
 
As a registered user, I expect to be able to
view my past orders
Rate and review photos I already purchased earlier
 
As a user I expect feedback from the website I am using when I interact with it, I expect notifications informing me of actions completed,whether they were successful or not.
 
## admin Stories
As an Admin of Photo sessions the goal is:
 
To be able to log in to access my existing entries, and for the photos to only be editable with my account.
 
To create, edit and delete entries in my account.
 
A user interface that is simple and easy to use, that is laid out in a logical way with clear indications where necessary about the type and format of the data I need to provide.
 
Forms for inputting my data to make the process easy, that there is no wasting my time or making the process difficult or slow.
 
My data is not accessible by anyone but myself and the other Photo Sessions administrators.
 
In Django Admin, to be able to edit, delete, access profiles, orders, categories, photos.
 
 
# Design Choices
The Photo Sessions website has an overall friendly feel. The following design choices were made with this in mind:
 
## Fonts
The primary font Lato was chosen for the main text of the site because it is easy to read and complements the fonts chosen for titles very well. An extra reason for picking this font is that it is still easy to read when printed small.
 
Social media icons for facebook, instagram and twitter are used in the footer of the site.
 
In the footer, to link to the social media outlets for Photo Sessions. these links do not yet exist, so currently the icons link to the main pages for each social media network.
 
On each photo page for any links provided by the organizers to their events and activities.
 
## Colours
### Photo Sessions Brand Colours
 
The brand colours for this project were chosen because they reference travel well, while still choosing tones and shades that worked well together without overwhelming the eyes.
 
A black was chosen for the main text as it contrasts with the white background clearly.
 
The navbar background colour is a clean white colour, light enough to provide contrast with the headings, while still setting itself apart from the photo background in the main content.
 
In the footer a white, provides the background colour, which is a good contrast to 
 
## Styling
 
All buttons on the site fit the same bootstrap button styling in size and shape.
Bootstrap cards were utilized on Photo Sessions to display short information about each photo, with a link to each photo page on it.
 
Css effects to all text links on the site (other than the Categories under the photos.cause them to animate to a darker shade when hovered over(other than the Categories)
# Wireframes
These wireframes were created using Balsamiq during the Scope Plane part of the design and planning process for this project.
P
UT WIREFRAMES IN A SEPARATE DOC
 
# Features
## Existing Features
Elements on every page
Navbar
Banner for free delivery
Return to top button
Footer
 
The navigation bar features the Photo Sessions logo in the top left corner.
 
For visitors to the site who are not logged in,they can view the products
All photos
Japan, Philippines, Portugal
Account
Bag
 
For users who are logged in, the list items are as follows:
All photos
Japan, Philippines, Portugal
My account (this option is a dropdown menu)
Admin login
On top of everything what logged in users have, admin has the option of Product Management where it’s possible to add the photo.
 
At every photo, admin has an option to 
Add new
Edit or Delete
 
Python determines if the user is logged in or not by checking if 'user' in session and passes this data to Jinja to display the correct navbar for the user.
 
The navbar is collapsed into a burger icon on small screens. 
 
The practical design choice was made not to fix the navbar to the top of the page as the user scrolls. This was because I wanted as much screen height as possible to display the website information on and I did not want to take up precious space with a fixed navbar. To get around the problem of having to scroll up a long way to reach the navigation, I added a scroll to top button above the footer as well.
 
Return to top button: 
 
A floating button appears on the lower right of the screen when the user starts to scroll downwards. Clicking this moves the view back up to the top of the page. I added this feature because some pages can be quite long and the navbar is not fixed to the top of the page.
 
## Footer
 
### The footer features:
Links to social media locations (Which will eventually be linked up to the Photo Sessions social media platforms, once they exist).
 
 
## Home Page
Photo Sessions homepage on all major screen sizes
Background Image: https://www.desktopbackground.org/wallpaper/high-resolution-beach-pictures-widescreen-hd-wallpapers-341566
 
The Photo Sessions homepage features a photo that is interesting to lovers of good photos and travel. I chose this image because it is eye catching and striking. The tagline for the website is laid over the image. This image was coded as a background-image in css and set to background-size: cover; so that it is responsive while never getting stretched or distorted.
 
Photo Cards
 
Each photo card on the Photos page gives the user some brief and useful information about each of the photos displayed. The photo image, price, rating and the category. Every card is clickable to go to the main photo page for that photo, so that if the user wishes to learn more the information it is only one click away.
 
Each card has three buttons next to it: Edit and Delete.
 
The edit button takes the user to the Edit photo Page where they can update the data for this photo in the database.
 
The delete button simply deletes the photo
 
 
Search
 
At the moment the filters available are:
 
By name (A-Z) and (z-A)
By price (low to high and high to low
By Rating
By Category (A-Z and Z-A)
 
 
 
As soon as the user clicks on one of these options a request is sent to pull the relevant data and display it for the user, without having to reload the page.
 
The user is also provided with a clear All Photos option under All Photos tab in the Photos page if they wish to return to looking at all the available photos.
 
On tablet and desktop size screens the filters navbar sits in a fixed position on the right side of the screen.
 
### photo Page
Photo Sessions photo page on all major screen sizes is responsive and ajusts to the screen size by rearranging the order of photos
Each photo page for an entry in the database displays that information in clearly laid out and easy to digest way. 
 
The image for the photo, in the photo page the dimensions of this image are not altered, so that the photo can have their entire picture on the website.
 
A category that the photo applies to is provided under the photo in the main photo page and when a specific photo is opened. I chose not to have the category in the photo page after the photo has been openend.
 
The photo description is displayed on the right of the photo in the photo page, for the user who has already scanned all the relevant data and wants to know more.
 
### Sign Up Page
The Sign Up page features a simple form, where the user can input an account name and password. The form was kept deliberately simple so that signup has minimum barriers.
 
 
If the user does not already exist in the database then the account is created, and a notification informing the user of successful creation of their account appears. 
 
### log In Page
The log in page also features a simple form where the user can enter their username and their password.
 
If the user inputs incorrect data a notification responds with various messages depending on what was incorrect.
 
When the user logs in with a correct username success notification appears 
When the admin logs in with a correct username success notification appears and admin can see Product Management in My account and will also have the option to edit or Delete photos
 
 
### Product Management Page
 
When logging in as Admin, Product management page appears. In there the Admin is able to add photos by inputting the name, SKU, description, photo searchable from the computer
 
### Account Page
Photo Sessions account page on all major screen sizes is responsive
 
 
 
### Add New photo Page
Photo Sessions add new photo page on all major screen sizes
The Add New Photo Page is where the admin provides the data for the Photo Sessions activities database.
 
The form is broken into sections, and laid out on a clean white background
 
The admin user is asked to enter the following data for their new photo:
 
Name
Category
price
rating
photo itself
friendly name
 
 
Categories - dropdown to indicate what categories the photo applies to.
Japan
Portugal
Philippines
architecture
beach
City
Nature 
Sailing
 
 
### Edit photo Page
The Edit photo Page is identical to the Add New Page, except that the heading on the page says "Edit" and data for the activity to be edited has been pulled from the database. 
 
 
### Admin account
 
Give myself (or any other administrator of Photo Sessions) special permissions to access / change data in the database from a Photo Sessions interface, rather than having to access the data directly in Django.
 
Give admin the ability to view, edit and delete any photo from database.
 
Have Order History on the users account page so they can see which of the photos have been purchased
 
## Features Left to Implement
Fix the option when a non-registered user buys the photo, to create the account for them
 
 
# Information Architecture
 
## Database Choice
Flask and then later got pushed to Heroku
 
# Technologies Used
 
## Tools
Gitpod is the IDE used for developing this project.
Flickr to store all external images for this project.
PIP for installation of tools needed in this project.
Git to handle version control.
GitHub to store and share all project code remotely.
Am I Responsive to test the responsiveness
 
 
## Libraries
JQuery to simplify DOM manipulation.
 
Bootstrap to simplify the structure of the website and make the website responsive easily.
FontAwesome to provide icons for Photo Sessions.
Google Fonts to style the website fonts.
Flask to construct and render pages.
Jinja to simplify displaying data from the backend of this project smoothly and effectively in html.
 
## Languages
This project uses HTML, CSS, JavaScript and Python programming languages.
 
# Testing
Testing was done across multiple browsers, laptops and phones. The responsiveness and features were tested and they were all working correctly

# Code checkers

Pep8 for python
W3 for HTML and CSS
CodeBeautify for JS
 
# Deployment
## How to run this project locally
To run this project on your own IDE follow the instructions below:
 
Ensure you have the following tools:
 
An IDE such as Gitpod
The following must be installed on your machine:
 
PIP
Python 3
Git
 
 
## Instructions
Save a copy of the github repository located at https://github.com/Maja-Jer/photo_sessions by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
git clone: https://github.com/Maja-Jer/photo_sessions
If possible, open a terminal session in the unzip folder or cd to the correct location.
 
A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
 
python -m .venv venv
NOTE: Your Python command may differ, such as python3 or py
 
Activate the .venv with the command:
.venv\Scripts\activate 
Again this command may differ depending on your operating system, please check the Python Documentation on virtual environments for further instructions.
 
If needed, Upgrade pip locally with
pip install --upgrade pip.
Install all required modules with the command
pip -r requirements.txt.
In your local IDE create a file called .flaskenv.
 
You can now run the application with the command
 
python3 manage.py runserver
You can visit the website at -------
 
### Heroku Deployment
To deploy Photo Sessions to heroku, take the following steps:
 
Create a requirements.txt file using the terminal command pip freeze > requirements.txt.
 
Create a Procfile with the terminal command echo web: python app.py > Procfile.
 
git add and git commit the new requirements and Procfile and then git push the project to GitHub.
 
Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
 
From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
 
Confirm the linking of the heroku app to the correct GitHub repository.
 
In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
 
Set the following config vars:
 
Key Value
DEBUG   FALSE
IP  0.0.0.0
 
 
# Credits
## Content
I wrote all the descrptions
 
### Images
 
The photographs are my personal photos taken on differnt trip in the recent year
 
Background photo: https://www.desktopbackground.org/wallpaper/high-resolution-beach-pictures-widescreen-hd-wallpapers-341566
 
 
 
## Code
I was inspired by the boutiqueAdo project, but I have added my own twist in the code when it suited me.
Template code for navbar and dropdown is taken from Bootstrap and modified to suit the sites needs.
I have taken the footer from one of my previous projects
 
 
## Acknowledgements
Special thanks to:
my mentor
tutors 
my Croatian group, specifically Igor
 
# Disclaimer
The content of this website is educational purposes only.



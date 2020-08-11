# UX

## Goals

### Visitor Goals

The central target audience for Photo Sessions are:

### User goals are:

A few of the possible goals users might have:

The design of this site fits the conventions of similar sites, and lays out the information in a user friendly and accessible way.

<!--The Photo Sessions page allows users to search by location, category, rating -->

### Business Goals

Business user goals are:

A well thought-out, well designed, user-friendly platform that will benefit my business.

A user interface that is user friendly for me to input my data easily and efficiently.

Value for money (at the moment the website is a student project, but eventual planning is to monetise this site, so it is worth adding this important goal here now.)

Photo Sessions is a great way to meet these user needs because:

The user interface for inputting activity data has been carefully controlled to validate input and make sure what is provided fits the needs of the database structure. Setting input field types to email, number, url etc makes sure the user is prompted when the data they provide is incorrect.

<!--????? The editor page is clearly structured and laid out in a simple and easy to understand -->

The editor has a preview page in it so the user can see how their activity will look on the site before it has been published, and gives them the opportunity to go back and make changes if they wish.

The account page for the admin user shows all their existing products and gives them the option to view, edit or delete them from this location.

The users needs on each page have been thought about and buttons provided for these paths through the site, to make navigating easy.

### Photo Sessions Goals

<!-- Provide an effective, easy to use site for .......-->

So that I can learn and practice frontend and backend programming together for the first time. To combine the use of HTML, CSS, Bootstrap and JavaScript with Python, Django....

While this is currently a student project, the idea is to transform this site into a site that sells prints of my personal photos and print of my friends' artwork (check Features to implement)

# User Stories

## Visitor Stories

As a visitor to Photo Sessions I expect/want/need:

To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.

The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.

The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.

<!--> As a user who is interested to find photos from a particular country, I want to be able to find them easily. I also want to be able to filter them by rating and price... ADD MORE!!!! -->

The site to provide easy access to the photo, rating, description, pricing.

As a user on a budget, I want to be able to filter results by pricing. I also want to know what photo has the best rating from the customers that have already purchased the prints.

As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices.

<!--As a user searching for ...-->

As a regular user of the Photo Sessions website, I expect to be able to connect to the social media channels, to keep up to date with new entries on the site.

As a user of Photo Sessions, I expect to be able to easily get in contact via a contact form, register, create an account

<!--As a registerd user, I expect to be able to....-->

<!--As a user I expect feedback from the website I am using when I interact with it, I expect loading spinners when pages are taking a while to load, I expect pop ups and modals to inform me when my forms have been completed and sent correctly.-->

## Business Stories

As a Business advertising on Photo Sessions I expect/want/need:

To see that various methods of contacting my business are available to users using Photo Sessions.

To be able to log in to access my existing entries, and for my data to only be editable with my account.

To create, edit and delete entries in my account.

A user interface that is simple and easy to use, that is laid out in a logical way with clear indications where necessary about the type and format of the data I need to provide.

Forms for inputting my data to make the process easy, that there is no wasting my time or making the process difficult or slow.

<!--?????My data is not accessible by anyone but myself and the Photo Sessions administrators.

????? Protections have been put in place to prevent me from accidentally deleting a photo.-->

# Design Choices

The Photo Sessions website has an overall family friendly feel, with emphasis on providing complex information in a bite size, learnable format. The following design choices were made with this in mind:

## Fonts

The primary font Lato was chosen for the main text of the site because it is easy to read and complements the fonts chosen for titles very well. A extra reason for picking this font is that it is still easy to read when printed small.

The secondary font

The tertiary font

<!--????? Social media icons for facebook, instagram and twitter are used in 3 places on the site.-->

In the footer, to link to the social media outlets for Photo Sessions. these links do not yet exist, so currently the icons link to the main pages for each social media network.

On each photo page for any links provided by the organizers to their events and activities.

## Colours

### Photo Sessions Brand Colours

The brand colours for this project were chosen because they are colorful, which references to travel well, while still choosing tones and shades that worked well together without overwhelming the eyes.

<!--Colorful highlights that draw the eye to headings are provided by _______, which is accented with the ????? in horizontal lines and links.-->

A dark navy blue was chosen for the main text as it contrasts with the white background clearly.

The navbar background colour is a clean white colour, light enough to provide contrast with the navy blue headings, while still setting itself apart from the photo background in the main content.

In the footer a darker shade of blue, provides the background colour, setting the footer apart from the rest of the content and making it dark enough that the text can be in white and still have enough contrast to be easily readable.

<!--????? The same darker blue is used for the filters bar on the activities page. Blue is a colour for travel, so was a good choice for the feeling of this website.-->

## Styling

<!--????? A loading spinner was added to Photo Sessions, to run while the page or data loads. The spinner chosen resembles a wind spinner toy. I picked it because it is colorful and fits well with the overall feel and demographic for the site.-->

All buttons on the site fit the same bootstrap button styling in size and shape, but I added my own brand colours to them so they fit in with the rest of the content.

<!--????? Bootstrap cards were utilized on Photo Sessions to display short information about each photo, with a link to each photo page on it. The cards were styled with curved corners, a theme repeated around the entire website in images, input boxes, buttons, pagination links etc.-->

A bootstrap

hover effects

<!--????? Some subtle shadows have been added to photo cards, modals and smaller form boxes, to give them depth on the page. This shadow is made larger on hover, giving the user a positive user experience in highlighting the section of the site they are hovering over.

????? Css effects on buttons cause them to animate to a darker shade when hovered over, this same effect is also applied to all text links on the site.-->

# Wireframes

These wireframes were created using Balsamiq during the Scope Plane part of the design and planning process for this project.
P
UT WIREFRAMES IN A SEPARATE DOC

????? PDF
Photo Sessions development planes PDF
This document was created during the planning phase of this project. The final website has some slight differences from what was planned. But I included this document in the project to provide insight into the original planning and direction of the site during the planning stages.

# Features

## Existing Features

Elements on every page
Navbar

The navigation bar features the Photo Sessions logo in the top left corner.

For visitors to the site who are not logged in, list items links are available for them to use.

Home
Activities
Create Account
Log in
Contact
For users who are logged in, the list items are as follows:

Home
Activities
Contact
My account (this option is a dropdown menu)
My photos
Add new
Settings
Log out
Python determines if the user is logged in or not by checking if 'user' in session and passes this data to Jinja to display the correct navbar for the user.

<!--The navbar is collapsed into a burger icon on small screens. On the photos page, where the activities filter takes up some of the width of the screen, the navbar is collapsed on medium screens as well, so that menu items did not start overlapping content.-->

<!--The practical design choice was made not to fix the navbar to the top of the page as the user scrolls. This was because I wanted as much screen height as possible to display the website information on and I did not want to take up precious space with a fixed navbar. To get around the problem of having to scroll up a long way to reach the navigation, I added a scroll to top button and essential links in the footer as well.-->

## Footer

### The footer features:

Contact information for Photo Sessions, currently an email address
Brief description of the purpose and mission for the site.
Copyright information.
Links to social media locations (Which will eventually be linked up to the Photo Sessions social media platforms, once they exist).

<!--Floating to top button:

A floating button appears on the lower right of the screen when the user starts to scroll downwards. Clicking this moves the view back up to the top of the page. I added this feature because some pages can be quite long and the navbar is not fixed to the top of the page.
Adding the class .active to the #to-top-button changes it's opacity from 0 to 0.5, which gave me the ability to animate the change gently. The opacity is increased again to 1 on hover.
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        $("#to-top-btn").addClass('active');
    } else {
        $("#to-top-btn").removeClass('active');
    }
}-->

## Home Page

Photo Sessions home page on all major screen sizes
Background Image

<!--The Photo Sessions home page features a colorful ??????I chose this image because it is eye catching and striking, and it features ????? The tagline for the website is laid over the image. This image was coded as a background-image in css and set to background-size: cover; so that it is responsive while never getting stretched or distorted.

Photo Cards

Each event card on the home page gives the user some brief and useful information about each of the photos displayed. The photo image, price, rating. ???? Every card is clickable to go to the main photo page for that photo, so that if the user wishes to learn more the information is only one click away.

The images on the cards are set to background-image using css, which ensures that no matter what dimensions the original image provided was, all card images have equal size, making for a much more attractive site and user experience.-->

Filters

At the moment the filters available are:

<!--fill this in-->

As soon as the user clicks on one of these options JavaScript sends a fetch request to pull the relevant data and display it for the user, without having to reload the page.

The user is also provided with a clear Sort By button if they wish to return to looking at all the available photos.

<!--On tablet and desktop size screens the filters navbar sits in a fixed position on the left side of the screen.-->

<!--To save space on mobile devices, the filters navbar can be slid out by pressing a show filters button.-->

<!--Pagination

Pagination is included on the activities page when the number of results to display is over 12. Each page contains up to 12 photos. This was done to make loading times faster and a smoother experience for the user.-->

### photo Page

Photo Sessions photo page on all major screen sizes
Each photo page for an entry in the database displays that information in clearly laid out and easy to digest way.

The image for the photo, in the photo page the dimensions of this image are not altered, so that the photo can have their entire picture on the website.

On large size screens and up the <!--image takes up 50% width of it's container. On medium and small size screens it takes up 100% width and the other content is displayed below it.-->

<!--The open times for the activity are displayed in a table that is easy to read and understand.

The dates section is visible for activities and events that have a start and end date. If the business has selected "ongoing" when creating the entry then the dates section does not appear in the photo page.

A list of categories that the activity applies to are provided above the description and below the photo.

The photo description is displayed underneath all the other information, for the user who has already scanned all the relevant data and wants to know more.

The email business button opens a modal with an email form to send to the admin directly from the Photo Sessions website. This feature was chosen to protect the businesses email addresses from being scraped from the website if they were set to mailto:. The email address is inserted from the data into the the contact html using JavaScript. The email form is sent using EmailJS.-->

At the bottom of the photo pages there is a Return to Top button, which takes the user (back) to the activities page.

### Create Account Page

<!--The create account page features a simple form, where the user can input an account name, email address and password. The form was kept deliberately simple so that signup has minimum barriers.

Once the form is complete the data is sent to the backend using JavaScript fetch() and then a request is made to MongoDB to check if the user name or email address already exists in the the database.

If it does then a response is returned to JavaScript so that a response can be given to the user via modal.

If the user does not already exist in the database then the account is created, and a modal informing the user of successful creation of their account appears. In the modal a button link to the log in page is provided.

This Account and Log In Pages Flowchart fully explains the behavior of the forms, data checks and modal messages on this page and the Log In Page.

(see Features Left to Implement for additional features to be included on this page in future releases)-->

### log In Page

<!--The log in page also features a simple form where the user can enter either their username or their email address, and their password.

This form also uses JavaScript fetch() to pass the input data from the user to Python. The reason for this use is that I wanted to provide the user with a modal once they were logged in, rather than reloading the page.

If the user inputs incorrect data a modal responds with various messages depending on what was incorrect.

When the user logs in with a correct email and password a success modal appears with links to their personal account page and editor page to add a new activity to the database.

This Account and Log In Pages Flowchart fully explains the behavior of the forms, data checks and modal messages on this page and the Account Page.-->

### Account Settings Page

<!--The account settings page includes two small forms for the user to update their email address or password.

Each form requires the user to input their current email/password and then their new one.

If the current data is not correct the user is informed of this via modal.-->

### Account Page

<!--Photo Sessions account page on all major screen sizes
At the top right of the account page a cog icon for access to the Account Settings Page is displayed. The positioning of this is the convention for links to settings, which is why it was chosen for this page as well.

Underneath the cog icon on the account page a clearly visible green Add New button has been added so that the user can easily access the Edit photo Page.

The user account page displays a card for each of the photos in the database that they have created.

Each card has three buttons underneath it: View, Edit and Delete.

The view button takes the user to the photo on Photo Sessions as visitors to the site see it.

The edit button takes the user to the Edit photo Page where they can update the data for this photo in the database.

The delete button activates a modal, asking the user to confirm that they want to delete this photo by typing "DELETE" into an input field.

Once the field value is equal to "DELETE" the confirm delete button on the modal becomes active to the user can click it to remove the activity entry from the database.

This feature was included to prevent accidental deletion of a complex data entry.-->

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

Categories ????? check-boxes to indicate what categories the activity applies to.
Japan
Portugal
Philippines
Tokyo
Osaka
Nara
Volcano
Palawan
Boracay
Lisbon
Porto
Sailing

Validation of the <input> fields is handled in variety of ways.

<!--????? The input type attributes are set to text, email, url and number where appropriate.-->

<!--Check-boxes for much of the data to be stored as simply true or false in the database.

Limits are placed on the length of input accepted, in order to protect from buffer overflows (hacking attempts).

At the bottom of the page the user is given a button to preview their data in the photo page, before it is published to the website. When this button is pushed the data is put into the database with the additional key value pair of {"published": false} applied to it. Then the preview page is loaded.-->

### Preview photo Page

<!--The preview photo page is where the admin can preview their new photo photo and see what it will look like on the Photo Sessions website.

The page is identical to the photo Page, except for three changes:

????? A preview bar along the top reminds the user that they are in preview mode, and need to click the publish button at the bottom of the page in order to make the photo live on the Photo Sessions website.

????? At the bottom left of the page the "share this page" icons do not work, as we do not want the user to accidentally share the preview page. If these icons are clicked a modal pops up to inform the user of this and tell them they can share the page once the photo has been published.

On the bottom right of the page, the "search more activities" button has been replaced with Edit and Publish buttons.

The Edit button takes the user to the Edit photo Page.

The Publish button updates the photo with {"published": false} so that the data can now be displayed on the Photo Sessions home page and All Photos page.-->

### Edit photo Page

<!--The Edit photo Page is identical to the Add New Page, except that the heading on the page says "Edit" and data for the activity to be edited has been pulled from the database and each <input>, <select>, <checkbox> and <textarea> values have been populated with the correct data.-->

### Contact Page

<!--???? The Contact Page features an email contact form, which is wired up to my email address with EmailJS.????

The contact page also features the contact information for Photo Sessions as displayed in the footer.-->

<!--### ????? Permission Denied page
The custom permission denied page features a humorous surprise for the user who attempts to access pages you must be logged in to access, while being logged out.

Two buttons on this page give the user a choice to either go to the log in page or go back one item in their browser history to whatever page they were on before this one.-->

### Admin account

<!--Give myself (or any other administrator of Photo Sessions) special permissions to access / change data in the database from a Photo Sessions interface, rather than having to access the data directly in MongoDB.????

Give admin the ability to view, edit and delete any photo from database.

Give admin the ability to add/remove "recommended" field on any photo from database, so that only businesses that have paid for this feature will see it effected on the site.-->

<!--Have separate sections on the users account page so they can see which of the photos have been purchased-->

## Features Left to Implement

# Information Architecture

## Database Choice

<!--A SQL database structure would have suited this project better, however this website is a student project and the current point that I am in the course is my only opportunity to use NoSQL as the final piece of coursework (the next one) required SQL. In order to get experience with using NoSQL this project utilizes the NoSQL database MongoDB.

To have easy access to relational data, inner objects were used inside the data structure so that they could be accessed and looped through where needed.

The shortDescription in the database is generated using Python, taking the first 100 characters from the description provided by the user. This short description is displayed on the activity cards on the home page and search results.

Example JSON from the activities collection-->

# Technologies Used

## Tools

Gitpod is the IDE used for developing this project.
Flickr to store all external images for this project.
PIP for installation of tools needed in this project.
Git to handle version control.

<!--MongoDB Atlas is the database for this project-->

GitHub to store and share all project code remotely.

<!--Browserstack to test functionality on all browsers and devices.
Am I Responsive to create the images in this readme file of each page displayed on different screen sizes.-->

## Libraries UPDATE!

JQuery to simplify DOM manipulation.

<!--Jasmine to run automated tests on JavaScript and jQuery code.
Jasmine-jQuery to make it possible to test jQuery code using Jasmine.-->

Bootstrap to simplify the structure of the website and make the website responsive easily.
FontAwesome to provide icons for Photo Sessions.

<!--Gijgo provided bootstrap styled date and time pickers.-->

Google Fonts to style the website fonts.

<!--PyMongo to make communication between Python and MongoDB possible.
Flask to construct and render pages.
Jinja to simplify displaying data from the backend of this project smoothly and effectively in html.-->

## Languages

This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing

<!--Testing information can be found in separate testing.md file-->

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools:

An IDE such as Gitpod
The following must be installed on your machine:

PIP
Python 3
Git

<!-- An account at MongoDB Atlas or MongoDB running locally on your machine.
How to set up your Mongo Atlas account here.-->

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

<!--Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database Photo Sessions, with 2 collections called users and activities. You will find example json structures for these collections in the schemas folder.-->

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
DEBUG FALSE
IP 0.0.0.0
MONGO_URI mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT 5000
SECRET_KEY <your_secret_key>
To get you MONGO_URI read the MongoDB Atlas documentation here
In the heroku dashboard, click "Deploy".

In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".

The site is now successfully deployed.

# Credits

## Content

Text for the Photo Sessions

All other text on Photo Sessions was written by me.

## Media

<!--### Animations
Animated spinner was provided by icons8
Hide and seek bot for 404 page was provided by dribbble.com-->

### Images

The photographs are my personal photos taken on differnt trip in the recent year

Background photo:

## Code

<!--Template code for navbar and dropdown is taken from Bootstrap and modified to suit the sites needs.
UPDATE THIS"-->

## Acknowledgements

Special thanks to:
my mentor
tutors
my Croatian group, specifically Igor

# Contact

To contact me feel free to email

# Disclaimer

The content of this website is educational purposes only.

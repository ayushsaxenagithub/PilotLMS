<h1>A fully responsive Learning Management System with models for Organisation, Teacher and Student. </h1>


## Description

The project is a web application built using Django, a high-level Python web framework. It provides a comprehensive platform for managing user profiles, organizations, teachers, students, courses, and related entities. The application facilitates collaboration, learning, and progress tracking in an educational setting.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Users Functionality](#users)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [Screenshots](#screenshots)

## Features

- User registration and login system.
- Creation and management of user profiles with personal information and social media links.
- Creation and management of organizations with descriptions, locations, websites, and founding years.
- Creation and management of teachers with associated profiles, organizations, qualifications, and research interests.
- Creation and management of students with associated profiles and departments.
- Categorization of courses using tags.
- Creation and management of courses with associated organizations, teachers, tags, descriptions, and course content.
- Enrollment of students in courses.
- Creation and management of modules within courses with associated videos and notes.
- Uploading and management of videos with associated modules and courses.
- Commenting and sub-commenting on videos and courses.
- Creation and management of notes on videos, modules, and courses.
- Tracking user progress in courses and overall course progress.
- Creation and management of quizzes associated with videos.
- Creation and management of quiz questions and answers.
- Monitoring user quiz attempts.

## Installation

We need to Download a number of libraries and also create an environment before running the site.

Step 1: Create an environment outside the PilotLMS folder to keep the settings local to this project, Then activate it.. reference below
> > https://docs.python.org/3/library/venv.html

Step 2: Create the Folder and clone the project, now Change directory into FOLDER_NAME
> > git clone (https://github.com/ayushsaxenagithub/PilotLMS.git)
> > cd FOLDER_NAME

Step 3: Install the requirements for the project using the command...
> > pip install -r requirements.txt

Step 4: To activate the server 
> > python manage.py migrate

Step 4: To collectstatic files
> > python manage.py collectstaicfiles

Step 6: To activate the server 
> > python manage.py runserver
Step 7 : Open your web browser and visit http://localhost:8000 to access the application.

## Usage
<ul>
  <li>Register a new user account or log in with an existing account.</li>
  <li>Create a profile and fill in the necessary details.</li>
  <li>Create organizations and add descriptions, locations, websites, and founding years.</li>
  <li>Add teachers and students, linking them to their respective profiles and organizations.</li>
  <li>Categorize courses using tags.</li>
  <li>Create courses, specifying the associated organization, teacher, tags, descriptions, and course content.</li>
  <li>Enroll students in courses.</li>
  <li>Create modules within courses and add videos and notes.</li>
  <li>Upload videos, specifying the associated module and course.</li>
  <li>Interact with videos and courses by leaving comments and sub-comments.</li>
  <li>Create notes on videos, modules, and courses.</li>
  <li>Track user progress in courses and monitor overall course progress.</li>
  <li>Create quizzes associated with videos and add questions and answers.</li>
  <li>Monitor user attempts and quiz results.</li>
</ul>



<br>

## Users Functionality

<h3>Student</h3>
<ul>
<li> Login/Signup using tokens and cookies</li>
<li> Dashboard to view courses and their progress</li>
<li> Quiz popups within videos</li>
<li> Doubt section</li>
<li> Personal Notes</li>
</ul>

<h3>Teacher</h3>
<ul>
<li> Teacher Dashboard for administering student progress and analytics</li>
<li> Teacher domain within his Organization</li>
<li> Setup quizes for students</li>
</ul>
<h3>organization</h3>


<ul>
<li> Has the power to appoint a user as an instructor</li>
<li> Has a domain specific to itself only accesible to its teachers</li>
<li> Every teacher should belong to an onganisation</li>
</ul>

## Technologies
<p>The project is built using the following technologies:</p>
<ul>
  <li>Python</li>
  <li>Django - Web framework</li>
  <li>Django REST Framework - Web API framework</li>
  <li>SQLite - Database</li>
</ul>
<p>Front-end:</p>
<ul>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ul>
<p>Authentication:</p>
<ul>
  <li>Django Authentication - User authentication and authorization</li>
</ul>
<p>File Storage:</p>
<ul>
  <li>Amazon S3 (or any other storage service)</li>
</ul>

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request.

<h2>Screenshots</h2>

![IMG-20230501-WA0016](https://user-images.githubusercontent.com/84840415/235439314-5e89c455-bf77-4fc1-a65f-7696db537d47.jpg)
![IMG-20230501-WA0010](https://user-images.githubusercontent.com/84840415/235439315-5479c46a-d783-4574-bcd8-a33729ff3164.jpg)
![IMG-20230501-WA0012](https://user-images.githubusercontent.com/84840415/235439322-0d3a80b9-de96-40af-b752-7defdaba308a.jpg)
![IMG-20230501-WA0013](https://user-images.githubusercontent.com/84840415/235439325-7ca92fa6-f17e-4dcd-a1bd-b93e18cf3280.jpg)
![IMG-20230501-WA0015](https://user-images.githubusercontent.com/84840415/235439328-b27fe4b3-061a-408b-bdcd-d5a96cc9304f.jpg)


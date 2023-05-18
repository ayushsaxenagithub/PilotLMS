<h1>A fully responsive Learning Management System with models for Organisation, Teacher and Student. </h1>

### Functionality Overview

The web application provides the following functionality:

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

This project aims to provide a comprehensive platform for managing user profiles, organizations, courses, and related entities, while also enabling collaboration, learning, and progress tracking.

<h2>Tech Used</h2>

'Python'
'PHP'
'Django'

<h2> Getting Started </h2>

We need to Download a number of libraries and also create an environment before running the site.

Step 1: Create an environment outside the PilotLMS folder to keep the settings local to this project, Then activate it.. reference below
> > https://docs.python.org/3/library/venv.html

Step 2: Create the Folder and clone the project, now Change directory into FOLDER_NAME
> > cd FOLDER_NAME

Step 3: Install the requirements for the project using the command...
> > pip install -r requirements.txt

Step 4: To run the code 
> > python manage.py runserver

<br>

<h2>Features</h2>

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



<h2>Screenshots</h2>

![IMG-20230501-WA0016](https://user-images.githubusercontent.com/84840415/235439314-5e89c455-bf77-4fc1-a65f-7696db537d47.jpg)
![IMG-20230501-WA0010](https://user-images.githubusercontent.com/84840415/235439315-5479c46a-d783-4574-bcd8-a33729ff3164.jpg)
![IMG-20230501-WA0012](https://user-images.githubusercontent.com/84840415/235439322-0d3a80b9-de96-40af-b752-7defdaba308a.jpg)
![IMG-20230501-WA0013](https://user-images.githubusercontent.com/84840415/235439325-7ca92fa6-f17e-4dcd-a1bd-b93e18cf3280.jpg)
![IMG-20230501-WA0015](https://user-images.githubusercontent.com/84840415/235439328-b27fe4b3-061a-408b-bdcd-d5a96cc9304f.jpg)


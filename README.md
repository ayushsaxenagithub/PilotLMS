<h1>A fully responsive Learning Management System with models for Organisation, Teacher and Student. </h1>

<h2>Tech Used</h2>

Python
PHP
Django

<h2> Getting Started </h2>

We need to Download a number of libraries and also create an environment before running the site.

Step 1: Create an environment outside the PilotLMS folder to keep the settings local to this project, Then activate it using the command...
> > env\scripts\activate

Step 2: Change directory into PilotLMS
> > cd PILOTLMS

Step 3: Install the requirements for the project using the command...
> > pip install -r requirements.txt

Step 4: To run the code 
> > python manage.py collectstatic
> > yes 
> > python manage.py runserver

<br>

<h2>Features</h2>

<h3>Student</h3>
<ul>
<li>* Login/Signup using tokens and cookies.</li>
<li>* Dashboard to view courses and their progress.</li>
<li>* Quiz popups within videos</li>
<li>* Doubt section</li>
<li>* Personal Notes</li>
</ul>

<h3>Teacher</h3>
* Teacher Dashboard for administering student progress and analytics
* Teacher domain within his Organization
* Setup quizes for students

<h3>organization</h3>
* Has the power to appoint a user as an instructor
* Has a domain specific to itself only accesible to its teachers.
* Every teacher should belong to an onganisation

<h2>Screenshots</h2>



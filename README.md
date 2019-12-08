# Project
To create a CRUD application using the topics covered during the training and also be able to demonstrate the usability of python, linux and continuos intergration servers within the project development. 

#index 
[Brief] (#brief)

* [Solution](#solution)

[Testing] (#testing)
* [Report] (#report)

[Deployment](#Depl)

[Improvements for the future](#improve)

<a name="brief"></a>
## Project Brief
To create a CRUD application using the topics covered during the training and also be able to demonstrate the usability of python, linux and continuos intergration servers within the project development. 

<a name="solution"></a>
### Solution
After drafting a few ideas, I decided to create a event listing app that would allow users to sign up and create events to manage. The one to many relationship was working very well as it created a relation between the two tables by having user_ID to take full control of the both tables. 

###Delievered Solution 
![ERD](/documentation/erdiagram.png

The ER diagrams show a relation between the two tables, although this is functional the user is able to navigate between the account page, events and home page. The user_id is also foreignkey in the event table as it triggers the creation and of events in the table, users are not able to use this feature unless they log in or are registered. 

<a name="mla"></a>
### CI Pipeline Diagram
Please click on the diagram for a high resolution version:
![CID](/documentation/cipipeline.png

This is a diagram demonstrating the architure of the application it includes a view of what was implemented and what technology was used for each stage of the development of the project. 

<a name ="testing"></a>
## Testing
Pytest was used for unit testing, Gunicorn was also iniated to support some of the testing and deployement from vm to server and i managed to create a webhook to git that would trigger a test-run on jenkins for each push made to the repo which allowed the automation of tests. The application itself can now be deployed on virtual machines and also local host. 

<a name="tech"></a>
### Technologies Included

* Microsoft Visual Code
* SQL Virtual machine on GCP - Database 
* Jenkins - CI Server - Automated Testing 
* Pytest Cov - Unit Testing Coverage 
* [Git](https://github.com/devops-cohort/leeroy/tree/feature)- Version Control System
* [Trello](https://trello.com/b/fpC9DHKx/individual-project) - Project Tracking
* GCP -Live Environment and hosting VMs

<a name="improve"></a>
## Improvements For Future Use

Currently User_id are required to gain access to the events page and view information on the home page. Users are only able to use the CRUD functionality on their accounts but only use half of those functions on events, I would like to simplyfy the process of making an event and also add delete and update functions on the event. I would also like to add bootsraping to allow a more appealing structure of the application. Adding another table would help to make more room for other features that will boost usability of the application for the users. In later sprints all these changes can be made and also some names need changing on the columns as they are slowing down the process of inputing data in the event table. 

<a name="auth"></a>
## Authors

Leeroy Chiweshe

<a name="ack"></a>
## Acknowledgements

* The rest of the cohorts on the programme
* QA Consulting team and instructors leading the way for us

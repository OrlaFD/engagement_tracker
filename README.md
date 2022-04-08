# Engagement Tracker Application

## Description

The Engagement Tracker application aims to streamline and simplify the way employees track the tasks of customer engagements they are aligned to. Each Engagement has one or more Tasks. These are then assigned to a single user. Within the application, users can view the list of engagements within the master details page, with integrated search functionality. When an engagement is clicked on, its associated tasks can be viewed with the option to add or delete tasks. Selecting a specific Task on an Engagement will open a Details page, where Task attributes can be updated and set as complete. Completed Tasks are striked-through and are indicated by a green circle, whereas incomplete tasks have greyed-out circles.

## Framework

To begin development, a framework was chosen to accelerate progress. Django was selected as it is high-level, follows the model–template–views (MTV) architectural pattern, and has an out-of-box admin interface. This contrasts to other frameworks such as Flask, a micro-framework, which provides less front-end and administration functionality.

Note that an application (‘base’) was created to break down the project (‘engagement_tracker’) into manageable components.

## Installation 

First, ensure that you have Python 3.5+ installed. You can download the latest version here: https://www.python.org/downloads/. Once that’s installed, you’ll have Python’s package manager, pip, included by default.

Install Django using: ```pip install django```

Install Factory Boy: ```pip install factory_boy```

To run the application: ```python manage.py runserver``` 


## Technologies Used
* Django: Version 4.0.2
* SQLite
* Factory Boy: Version 2.4.0
* Class-Based Views and Mixins


### References 

Views.py contains the references used in this project's source code.
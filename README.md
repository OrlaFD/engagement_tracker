# engagement_tracker

The Engagement Tracker application aims to streamline and simplify the way employees track the tasks of customer engagements they are aligned to. Each Engagement has one or more Tasks. These are then assigned to a single user (employee). Within the application, users can view the list of engagements within the master details page, including search functionality. When an engagement is clicked on, its associated tasks can be viewed with the option to add more tasks. Selecting a specific Task on an Engagement will open a Details page, where Task attributes can be updated and set as complete. Completed Tasks are striked-through and are indicated by a green circle, whereas incomplete tasks have greyed-out circles.

To run the app:

python manage.py runserver
 
Current Issues:
"When an engagement is clicked on, its associated tasks can be viewed" - I cannot get this to work. For example, if an engagement is clicked on it should open up the list of tasks that are associated with it. At the moment, if an engagement is clicked on it opens up a list of all tasks instead of its associated ones. 

I have created tasks that are associated with a specific engagement (via the django admin panel) and know that these associations exist as I am able to display these tasks directly next to their engagement name using the commented out code on lines 32-34 in engagement_list.html. However I would like to see the list of associated tasks in the tasks page when the engagement is clicked on.

This may be something to do with dynamic filtering in class-based views: https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/#dynamic-filtering

In engagement_list.html I have included an engagementID (line 30) so that when each engagement is clicked on it has a unique key in the url. However I am unsure how to use this so that its associated tasks appear in the list of tasks (task_list.html), or if this is even needed.

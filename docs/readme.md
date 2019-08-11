# This program gets two dates and finds the difference between the two.
## whats inside
A command line tool that receives two numbers can calculates number of days between two dates.
Basics tests, and stress random test.
## to run
To manually test the program, go to the root directory and type:
python3 commandLine.py
## To test;
There are three static tests in test_basics.py contains three basic secnaiors;
The one test in test_random_stress.py runs 1000 randomly selected dates and checks against python datetime module.
To see the test; go to /tests/ with command line and type:
py.test
you will need to have installed pytest;
## The web app
### Description
The web app consists of a GUI where user can enter two dates; a javascript handler script makes a "POST" request to the app with information in the form and the webserver responds.
### to run
You will need to have Flask installed; by doing sudo pip3 install Flask; go the webapp directory and enter:
python3 application.py
You will be able to see the printed values; I could have redirected output to logs but ran out of time.

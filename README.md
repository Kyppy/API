# API
iReporter webapp API
This API contains several resources for the iReporter webapp these include:

-A resource that allows users to their post 'red-flag'incidents records as well as edit the location and their comments for eachc case.

-A resource that allows users to fetch their records.This can be a specific record or all of them at once.

-A resource for users to delete their posts.

This repo also includes configuration files that enable continuous integration on Travis CI as well as cloud-based app hosting on Heroku.

Each resource is an application of the HTTP verbs GET,POST,PATCH and DELETE.
To use them,an appropriate request must be made to the app using a url.
For instance to post a incident a post request must be made using http://localhost:5000/api/v1/red_flag/<incident_id>.The 'incident_id' is the unique identifier for each user post and ensures each user's post is never confused with other users.

[![Build Status](https://travis-ci.org/Kyppy/API.svg?branch=develop)](https://travis-ci.org/Kyppy/API)

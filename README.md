# iReporter API #
This API contains request resources for the iReporter webapp.This repo also includes configuration files that enable continuous integration on Travis CI as well as cloud-based app hosting on Heroku.

## Endpoint Documentation ##

## Get All Redflag Incidents ##
Returns a list of 'red-flag' records as dicts.

* URL
   * /api/v1/red_flags
* Method:
   * GET
* URL Params
   * Required: None 
* Data Params
   * None
* Success Response
   * Code: 200 
   * Content: {"status":200, "data":[list of dicts}
   
* Error Response
   * If no red-flag records exist will return empty list.

## Get A Specific Redflag Incident ##
Returns a dict of a single 'red-flag' record. Record is specified by its 'id' field.

* URL
   * /api/v1/red_flag/<int:red_flag_id>
* Method:
   * GET
* URL Params
   * Required: red_flag_id =[integer] 
* Data Params
   * None
* Success Response
   * Code: 200 
   * Content: {"status":200, "data":[redflag record]}
   
* Error Response
   * Code: 404
   * Content: {"status":404, "message":"An incident with id '<red_flag_id>' does not exist."}

## Post A Redflag Incident ##
Posts a dict of a single 'red-flag' record. Record is specified by its 'id' field.

* URL
   * /api/v1/red_flag/<int:red_flag_id>
* Method:
   * POST
* URL Params
   * Required: red_flag_id =[integer] 
* Data Params
   * None
* Success Response
   * Code: 201
   * Content: return {"status":201, "data":{"id":<red_flag_id>, "message":"created red-flag record"}}
   
* Error Response
   * Code: 400
   * Content:<p> {"message":"A red-flag with id '<red_flag_id>' already exists."}<br> 
                  OR<br>
                 {"message":"'id '<red_flag_id>' of request body and 'id' '<url_input>' of url do not match"<p>
 
## Edit The Location Field Of A Redflag Incident ##
Edits the 'location' field of a single 'red-flag' record. Record is specified by its 'id' field.

* URL
   * /api/v1/red_flag/<int:red_flag_id>/location
* Method:
   * PATCH
* URL Params
   * Required: red_flag_id =[integer] 
* Data Params
   * None
* Success Response
   * Code: 200
   * Content: return {"status":200, "data":{"id":'<red_flag_id>', "message":"Updated red-flag record's location"}}
   
* Error Response
   * Code: 400,404
   * Content:<p> {"message":"A red-flag with id '<red_flag_id>' already exists."}<br> 
                  OR<br>
                 {"message":"'id '<red_flag_id>' of request body and 'id' '<url_input>' of url do not match"<br>
                  OR<br>
                 {"message":"Location update data was not provided."}<p>

## Edit The Comment Field Of A Redflag Incident ##
Edits the 'comment' field of a single 'red-flag' record. Record is specified by its 'id' field.

* URL
   * /api/v1/red_flag/<int:red_flag_id>/comment
* Method:
   * PATCH
* URL Params
   * Required: red_flag_id =[integer] 
* Data Params
   * None
* Success Response
   * Code: 200
   * Content: return {"status":200, "data":{"id":'<red_flag_id>', "message":"Updated red-flag record's comment"}}
   
* Error Response
   * Code: 400,404
   * Content:<p> {"message":"A red-flag with id '<red_flag_id>' already exists."}<br> 
                  OR<br>
                 {"message":"'id '<red_flag_id>' of request body and 'id' '<url_input>' of url do not match"<br>
                  OR<br>
                 {"message":"Comment update data was not provided."}<p>
  
## Delete A Specific 'red-flag' Incident ##
Removes the dict of a single 'red-flag' record. Record is specified by its 'id' field.

* URL
   * /api/v1/red_flag/<int:red_flag_id>
* Method:
   * DELETE
* URL Params
   * Required: red_flag_id =[integer] 
* Data Params
   * None
* Success Response
   * Code: 200 
   * Content: {"status":200, "data":{"id":'<red_flag_id>', "message":"red-flag record has been deleted"}}
   
* Error Response
   * Code: 404
   * Content: {"status":404, "message":"An incident with id '<red_flag_id>' does not exist."}
   
### Continuous Integration Badges ###
[![Build Status](https://travis-ci.org/Kyppy/API.svg?branch=develop)](https://travis-ci.org/Kyppy/API)

[![Coverage Status](https://coveralls.io/repos/github/Kyppy/API/badge.svg?branch=develop)](https://coveralls.io/github/Kyppy/API?branch=develop)

[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/Kyppy/API)

### Heroku App Link ###
https://redflag-ch2-api.herokuapp.com/api/v1/red_flags

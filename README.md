# iReporter API #
This API contains request resources for the iReporter webapp.This repo also includes configuration files that enable continuous integration on Travis CI as well as cloud-based app hosting on Heroku.

## Endpoint Documentation ##

## Get All 'red-flag' Incident Records ##
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
   * Method will always return list. If no data present will return empty list.

## Get Specific 'red-flag' Incident Record ##
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

## Post Redflag Incident ##
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
  
[![Build Status](https://travis-ci.org/Kyppy/API.svg?branch=develop)](https://travis-ci.org/Kyppy/API)

[![Coverage Status](https://coveralls.io/repos/github/Kyppy/API/badge.svg?branch=develop)](https://coveralls.io/github/Kyppy/API?branch=develop)

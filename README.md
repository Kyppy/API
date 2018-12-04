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
   * Required: red_flag_id =[integer] 
* Data Params
   * None
* Success Response
   * Code:200 
   * Content:{"status":200, "data":[list of dicts}
   
* Error Response
   * Method will always return list.If no data present will return empty list.

[![Build Status](https://travis-ci.org/Kyppy/API.svg?branch=develop)](https://travis-ci.org/Kyppy/API)

[![Coverage Status](https://coveralls.io/repos/github/Kyppy/API/badge.svg?branch=develop)](https://coveralls.io/github/Kyppy/API?branch=develop)

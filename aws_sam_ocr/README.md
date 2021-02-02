# Extraction Core Utils
	 - This is a set of utils infra that supports extracion core workflows.
	 - This persently has an AWS SAM app that validates model data for NPI in the client accounts 

## Things to be finalized
	- To which bucket should sam filed be uploaded ?
    - 

## Project structure
Here is a brief overview of what we have generated for you.
```bash
.
├── README.md                   <-- Notes and Playbooks
├── src                         <-- Source code for the app
│   ├── __init__.py
│   ├── app.py                  <-- Lambda handler code
|   └── validate.py             <-- Code for the validator
├── tests                       <-- Contains testingcode
│   │── test_validate.py        <-- Unit tests for validator
│   │── test_event.json         <-- S3 event data for integration testing
│   └── *.csv                   <-- Sample data for testing
├── template.yaml               <-- SAM template
├── deploy                      <-- Deployment shell script
├── run_unit_tests              <-- Shell script to run unit tests
└── run_integration_tests       <-- Shell script to run integration tests
```


## Requirements
* AWS CLI
* Python 3.8
* Docker
* pytest package

## Notes
```
# creates a sample event for given s3 bucket
sam local generate-event s3 put --bucket aws-sam-one --key test > event_file.json
```

## CLI Commands to deploy and test the application
**WIP**

For deploying
```
./deploy
```
For running unit tests
```
./run_unit_tests
```

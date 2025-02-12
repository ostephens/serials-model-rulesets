# README
This repository contains some common serial publication patterns expressed as model rulesets that can be loaded into the FOLIO Serials Management application.

To load a file, POST the content of the file to the /serials-management/modelRulesets endpoint

The repository also contains python code for merging the indiviual files into a single JSON file (structured as a JSON array) to allow easy processing by other software (e.g. using Postman collection runner to load each model ruleset)
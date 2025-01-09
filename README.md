# createOpenEveEvent

Helper script for the WELCOME team to create an event from a .md file

Script parses the date from openeve.md. Simply change the date and run the script. 

A new event plus corresponding calendar entry will be created. Without an upcoming 
OpenEvening event in the calendar, SLMSChimp will not be inviting new members from
the survey list.

### .env file

Please make sure to have that in .gitignore

~~~
#.env for createOpenEveEvent.py | save as ".env"

# Discourse
USER_API_KEY="discourse_user_api_key"
USER_API_CLIENT_ID="client_id"
~~~

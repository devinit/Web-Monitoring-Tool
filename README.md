# Web-Monitoring-Tool
Monitoring tool for html servers, db services and ssh ports on preconfigured hosts for Development Initiatives on preconfigured hosts at regular intervals and store their status based on whether they respond or not, speed of the response and the status of their associated services.
On failure, it will send an email to the tool’s administrators and a Twitter update as well.
The tool will feature both an authentication based private area and a public dashboard.

Private app
------------
The private app will allow adding/removing/editing hosts to check and which services they also offer. It’s going to be a SPA (React possibly) app that shows also detailed information about up/downtime, response time, disk usage if possible. A simple User section can be considered if time allows, otherwise the default Django admin provided one will suffice.

Public page
------------
The public page will simply list our monitored hosts and show an icon based on whether the tool is online and all its services are as well, the tool and services are offline or the status of the monitored services if they are experiencing difficulties. This page will not be under authentication and can be seen by anyone at any point in time.


###### MAIN FEATURES
These are the main metrics the monitor will want to check
- Does the server respond?
- Does it respond with HTML for a GET request?
- What is the server’s uptime?
- What is the server’s response time?
- What classes as downtime?:
- does the web app respond with 200/300 status codes?
- is-ready for databases?
- are the cron jobs running?
- is SSH and SSL enabled?
- Save into database downtime stats

###### ADMIN INTERFACE
These are requirements for the administrator interface
- Should be behind authentication
- The list view should be a single page application
- CRUD should happen inline dynamically
- It should have a Users management section
- If time allows, another single page application
- Start with Django admin interface
- It should have a metrics page “Dashboard” (example)
- x/y servers are up
- avg response time
- avg uptime per month
- server stats if we have time
- performance
- stats
- disk usage
- uptime
- Should allow exceptions to be configured
- during planned downtimes, Tweets and Slack notifications should pause

###### PUBLIC PAGE
This section defines the basic requirements for the public page
- Should list of services and status (without showing any other info)
- up
- down
- difficulties
- Should allow to filter by service’s namespace (all/IATI/DI)
- Basic


###### NOTIFICATIONS
This section defines the basic requirements for the notification app
- Twitter (Spotify’s example):
- Should create a Twitter account per monitoring “namespace” (DI/IATI)
- Should automatically notify (once) when
- A service goes offline
- A service comes back online
- Every 4 hours if the service is still offline
- Twitter status accounts examples
- Planned downtime communicated automatically through exceptions
- Slack integration:
- Metrics as a JSON api
- commands to check all tools statuses

###### FUTURE DEVELOPMENTS
- Make it generic and share it as a Django package

###### NICE TO HAVE
- Brainstorm a name for this tool - Web Monitoring Tool seems too generic
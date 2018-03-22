## LOG ANALYSIS - SQL

This is the first project for Udacity's _The Backend: Databases & Applications_ section as part of the **Full Stack Web Developer Nanodegree**.

### Project Description
#### Pre-requisites for this project:
- Python3
- Vagrant
- VirtualBox
- Access to the **news** database in your virtual machine

#### Setup
1. Install Vagrant and VirtualBox
2. Download the [Virtual Machine configuration](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
3. Download or Clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
4. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Starting up the Virtual machine
1. Open terminal and go to the folder where you saved the fullstack repository then `cd vagrant`.
2. Launch Vagrant and then log into the machine:
`vagrant up`
`vagrant ssh`
3. cd into the vagrant volder with `/vagrant`
4. Set up the database then load connect to the database:
`psql -d news -f newsdata.sql`
`psql -d news`

### Questions to Answer:
- What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
- Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
- On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

### Python Query Run
This project requires access to the _news_ database, which has been run on a virtual machine using Vagrant and VirtualBox. By this stage you should be set-up to run the queries, but if not review the set-up.

Run `python udacity_logs.py | ~tee logs_analysis.txt` in your terminal screen to run the queries, print to screen, and simultaneously save to the text file.

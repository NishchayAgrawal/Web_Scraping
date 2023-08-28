# Running Python Script as a Cron Job on EC2

This Project will help you how to set up and run a Python script as a cron job on an EC2 instance. This is useful for automating tasks at scheduled intervals.

## Prerequisites

- An Amazon EC2 instance with SSH access.
- Basic knowledge of the Linux command line.
- Your Python script and any required dependencies.

## Steps

1. **SSH into EC2 Instance:** Connect to your EC2 instance using SSH.
   
2. **Create Python Script:** Write the Python script you want to run.
   ```
   i.) Create your python script and uploaded to s3 bucket.
   
   ii.) Create directory Cron(I have created cron directory) and then copy code to you'r currect directory
        aws s3 cp s3://{Bucket_Path}/cron_job.py ./cron/cron_job.py

   Note :- Also create one more directory to store logs for running jobs
   
   iii.) Go the Cron directory Install virtual env. and activate that
   Commands :-
    sudo apt-get update
    sudo apt-get install python3-venv
    python3 -m venv venv
    source venv/bin/activate
   

3. **Install Required Dependencies:** If your script requires additional packages, install them using `pip`(Here I have created virtual env. inside that Directory).
   ```
   pip install fsspec
   pip install requests
   pip install pandas
   ```

4. **Edit Crontab:** Open your crontab for editing:

   ```bash
   crontab -l :- This command will show you all cron jobs
   crontab -e :- This command will help you to edit the cron jobs.

   crontab -e

   * * * * * PYTHONPATH=/home/ubuntu/cron/venv/lib/python3.x/site-packages /home/ubuntu/cron/venv/bin/python3 /home/ubuntu/cron/cron_job.py >> /home/ubuntu/logs/cron_log.txt 2>&
   

5. **Test the Script:** Run your Python script manually to ensure it works as expected.

   ```bash
   PYTHONPATH=/home/ubuntu/cron/venv/lib/python3.x/site-packages /home/ubuntu/cron/venv/bin/python3 /home/ubuntu/cron/cron_job.py

## Note :-
1.) **stdin  :- 0 , stdout :- 1 , stderr :- 2**

here 2>&1 :-  This redirects standard error (stderr) to the same log file as stdout. This ensures that both standard output and standard error are captured in the log file.
log.txt >> 2>&1 :- It will store Stderr and stdout to log.txt file

2.) **Cron Schedule Expression :** https://crontab.guru/

# SpeedTestLogger

This is a simple python script that calls the Ookla Speedtest utility from command line.

## Prerequisites
- Python 3.9 or above
- Ookla SpeedTest-CLI ( [https://tnkr.in/5ok](https://tnkr.in/5ok) ) installed on your *nix based system (Linux, Mac, Windows with WSL installed)
- A MariaDB database. SQL scripts to create the tables are located in the [mariadb_sql](./mariadb_sql/) folder.
- a task scheduler, like CRON to run this script at an interval.


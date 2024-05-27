#!/usr/bin/python3
import mariadb
import json
import subprocess
import random
import time
import secrets

print("Start time ", time.ctime())
delay = random.randint(1,1740) # Delay ranging from zero to 29 minutes
print("Delaying test for {0} seconds".format(delay))
time.sleep(delay)

r=None
results = None
error = None
sql = None


try:
    r = subprocess.run(['/usr/bin/speedtest', '-fjson'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    results = json.loads(r)
except Exception as e:
    error = "Error While Executing SpeedTest:\nError:({0}){1}\nR:{2}".format(type(e), e, r)
    print(error)

if results:
    # Stack Overflow article about converting bps in json to Mbps shown in the UI
    # https://stackoverflow.com/questions/71490927/understand-ookla-speedtest-json-values
    download = results['download']['bandwidth'] / 125000
    upload = results['upload']['bandwidth'] / 125000

    packetLoss = 0.00
    try:
        packetLoss = resuls['packetLoss']
    except:
        print("packetLoss not returned in results")


    print("Up {0}, Down {1}, Packet-loss {2}".format(upload, download, packetLoss))

    sql = "INSERT INTO SpeedTestResults (download_bandwidth, download_jitter, externalIP, packetLoss, ping_latency, " \
            "server_location, upload_bandwidth, upload_jitter, server_ip, server_sponsor) " \
            "VALUES ('{0:.2f}', '{1:.2f}', '{2}', '{3:.1f}', '{4:,.2f}', '{5}', '{6:.2f}', '{7:.2f}', '{8}', '{9}')".format(
                download,
                results['download']['latency']['jitter'],
                results['interface']['externalIp'],
                packetLoss,
                results['ping']['latency'],
                results['server']['location'],
                upload,
                results['upload']['latency']['jitter'],
                results['server']['ip'],
                results['server']['name'])
    
else:
    sql = "INSERT INTO Errors (errorText) VALUES ('{0}')".format(error.replace("'","''"))

#print(sql)

db = mariadb.connect(
        host = secrets.MARIADBHOST,
        user = secrets.MARIADBUSER,
        passwd = secrets.MARIADBPWD,
        db = secrets.MARIADBDB )
db.autocommit = True
cursor = db.cursor()
cursor.execute(sql)
print("End Time ", time.ctime())
# Change working directory to /tmp
cd /tmp

# Create monitoring log
touch .monitoring

# timestamp
date > .monitoring
echo "===== DISK SPACE =====" >> .monitoring

# Disk space
df  / >> .monitoring
echo "===== MEMORY =====" >> .monitoring

# Memory usage
free >> .monitoring
vmstat >> .monitoring
echo "===== CPU UPTIME=====" >> .monitoring

# CPU uptime
uptime >> .monitoring
echo "===== CPU INFO =====" >> .monitoring

# CPU usage
cat /proc/cpuinfo >> .monitoring
echo "===== PROCESSESS =====" >> .monitoring

# Process alive
names='python nginx docker postgres apache2'
for name in $names
do
    echo $name $(ps aux |  grep "$name" | grep -v "grep" | awk '{print $2}') >> .monitoring
done
echo "===== DOCKER =====" >> .monitoring


# Docker
docker -v >> .monitoring
echo "===== DOCKER IMAGES =====" >> .monitoring

# Docker images
docker image list --quiet --filter dangling=false >> .monitoring
echo "===== CRON SCHEDULE =====" >> .monitoring

# Cron schedule
cronusers='root'
for cronuser in $cronusers
do
    crontab -u $cronuser -l >> .monitoring
done
echo "===== OS INFO =====" >> .monitoring

# OS info
lsb_release -a >> .monitoring
echo "===== END =====" >> .monitoring

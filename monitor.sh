# Change working directory to /tmp
cd /tmp

# Create monitoring log
touch .monitoring

# timestamp
date > .monitoring
echo "=====" >> .monitoring

# Disk space
df  / >> .monitoring
echo "=====" >> .monitoring

# Memory usage
free -h >> .monitoring
echo "=====" >> .monitoring

# CPU uptime
uptime >> .monitoring
echo "=====" >> .monitoring

# CPU usage
cat /proc/cpuinfo >> .monitoring
echo "=====" >> .monitoring

# Process alive
names='python nginx docker postgres apache2'
for name in $names
do
    echo $name $(ps aux |  grep "$name" | grep -v "grep" | awk '{print $2}') >> .monitoring
done
echo "=====" >> .monitoring


# Docker
docker -v >> .monitoring
echo "=====" >> .monitoring

# Docker images
docker image list --quiet --filter dangling=false >> .monitoring
echo "=====" >> .monitoring

# Cron schedule
cronusers='root'
for cronuser in $cronusers
do
    crontab -u $cronuser -l >> .monitoring
done
echo "=====" >> .monitoring

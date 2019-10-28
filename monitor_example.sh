# Change working directory to /tmp
cd /tmp

# Create monitoring log
touch .monitoring

# Disk space
df  / > .monitoring
echo "=====" >> .monitoring

# Memory usage
free -h >> .monitoring
echo "=====" >> .monitoring

# CPU usage
cat /proc/cpuinfo >> .monitoring
echo "=====" >> .monitoring

# Process alive
names='python nginx kdkdkdkd'
for name in $names
do
    echo $name $(ps aux | grep "$name" ) >> .monitoring
done
echo "=====" >> .monitoring

# Docker
docker image list --quiet --filter dangling=false >> .monitoring
echo "=====" >> .monitoring

# Cron schedule
cronusers='root'
for cronuser in $cronusers
do
    crontab -u $cronuser -l >> .monitoring
done
echo "=====" >> .monitoring

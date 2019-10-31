#!/bin/bash
CRON_CONTENTS="* * * * * ./monitor.sh"
declare -A SERVERS=( []=root )
for server in "${!SERVERS[@]}"
do
	scp monitor.sh ${SERVERS[$server]}@$server:/root
	ssh ${SERVERS[$server]}@$server /bin/bash << EOF
		(crontab -u root -l; echo "$CRON_CONTENTS") | crontab -u root -
EOF
done

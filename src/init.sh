#!/bin/bash 

echo -e "export TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN\nexport TELEGRAM_GROUP_CHAT_ID=$TELEGRAM_GROUP_CHAT_ID\n" > $TELEGRAM_ENV_FILE

cron && tail -f /var/log/ip_checker.log

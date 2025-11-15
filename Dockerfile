FROM debian:12-slim

RUN apt-get update && apt-get -y install cron python3

ENV CRON_FILE=/crontab_ip_checker
ADD src/crontab.txt $CRON_FILE
RUN crontab $CRON_FILE

ENV TELEGRAM_ENV_FILE=/telegram.env

COPY src/cronjob.sh /cronjob.sh
RUN chmod +x /cronjob.sh
RUN sed -i "s|TELEGRAM_ENV_FILE|${TELEGRAM_ENV_FILE}|" /cronjob.sh

RUN touch /var/log/ip_checker.log

VOLUME /data

WORKDIR /app

CMD ["./init.sh"]

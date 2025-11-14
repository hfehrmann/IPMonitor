FROM debian:12-slim

RUN apt-get update && apt-get -y install cron python3

ADD src/crontab.txt cron_ip_checker

RUN crontab cron_ip_checker

RUN touch /var/log/ip_checker.log

WORKDIR /app

CMD ["cron", "&&", "tail", "-f", "/var/log/ip_checker.log"]

# IP Monitor

This project runs a cron job every hour to check if your public IP has changed or not. If it has changed, it sends a telegram message to a group to notify the new ip. It just uses a single file as storage under `src/data`.

## Requirements

1. You will need a telegram bot. Follow [this guide](https://core.telegram.org/bots#how-do-i-create-a-bot)
2. You will need to get the group id you want to post a message [stackoverflow response](https://stackoverflow.com/a/32572159/7282071). Essentially, you need to get the id from the [getUpdates API](https://core.telegram.org/bots/api#getupdates)
3. Configure the variables in the `.env` file.
4. Profit

# Discord-Message-Logger

This Discord server message logger is intended for educational and research purposes only. 
**Please only use this bot with the permission of the server owner or administrator.**

### Rationale
This bot was originally created for the purpose of data collection for the [CussNet Project](https://github.com/AdrielAmoguis/Cuss-Net). This is meant
for use in servers with a majority Filipino population in order to collect sentiment data for a neural network as training and testing data.

### Privacy Concerns
This bot operates discreetly. It will show itself as offline and does not send any messages. Data that is collected is purely message text. No user data or IDs will be collected.

### How does it work?
The bot listens on its main on_message handler. This handler is called whenever a message is sent to a channel that the bot has direct access to. Hence,
private channels that the bot does not have explicit access permissions to will not be logged. The bot outputs the data as a CSV file for persistent storage.
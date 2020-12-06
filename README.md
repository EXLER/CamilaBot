<p align="center">
    <img src="logo.png" width="400">
    <p align="center">🦸 Discord music/helper bot for managing small and private servers</p>
</p>

## Requirements
* Python 3.6
* ffmpeg

## Usage
* Create a new bot on [Discord Developer Portal](https://discord.com/developers/applications) and generate a bot token
* Rename `.env.example` to `.env` and fill out the empty fields

### PM2 setup
Run the installation script to setup dependencies and `pm2` for process management

```bash
$ sudo scripts/setup-pm2.sh
```

### Docker setup
Create a container using `docker-compose`

```bash
$ docker-compose up -d
```


## Available commands
```
Miscellaneous:
  format       Format message of given ID with given syntax.
Music:
  join         Join the room occupied by the person invoking the command
  leave        Leave the current voice channel
  pause        Pause the current playing video
  play         Play music from a YouTube video
  skip         Skip the current playing video
  unpause      Unpause the currently paused video
Plan:
  changeplan   Change the lesson plan for a given group with attached image
  plan         Display the lesson plan for the group represented by user's role
Randoms:
  randommember Choose a random member of given Discord role
  randomrange  Choose a random integer between given lower and upper bounds
​No Category:
  help         Shows this message

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```

## License

Copyright (c) 2020 by ***Kamil Marut***

`SuperCamila` is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), following all clarifications stated in the [license file](LICENSE).
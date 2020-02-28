![Streamelopers Dev](https://streamelopers.org/assets/img/logos/logo-white-bg.png)

# Streamelopers CLI - [Config File Generator] ⚙️🚀

![Build and Upload package STOBS.](https://github.com/DarkCode01/streamelopers-cli/workflows/Build./badge.svg)

This project is to provide to all dev for streamer from dominican republic all cofig or tools tha we are using when we create a stream, this project is to collaborate for all users can stream whatever conference, panel, activity in Dominican Republic or from the other country, without have to configurate all OBS for you.

## Getting Started

You have to install [`stcli`](https://pypi.org/manage/project/stcli/releases/) library from [Pypi](https://pypi.org/).

### Installing

```
python3 -m pip install -U stcli
```
Run `stcli` to test if library was installed.
```
stcli --help
```

#### Create a simple config file with scenes collection of a speaking.
```
stcli generate --type speaking --ouput test
```
That command generate a new file config with yours scenes collection, in the folder `stcli` Home on your computer.

## Built With

* [Click](https://click.palletsprojects.com/) - The library to manage all arguments.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Jose Segura** - *Initial work* - [Darkcoder](https://github.com/Darkcode01)


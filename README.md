![Streamelopers Dev](https://streamelopers.org/assets/img/logos/logo-white-bg.png)

# Streamelopers CLI - [Config File Generator] ⚙️🚀

![Build](https://github.com/DarkCode01/streamelopers-cli/workflows/Build/badge.svg?branch=master)

This project is to provide to all dev for streamer from dominican republic all cofig or tools tha we are using when we create a stream, this project is to collaborate for all users can stream whatever conference, panel, activity in Dominican Republic or from the other country, without have to configurate all OBS for you.

## Getting Started

You have to install [`sdcli`](https://pypi.org/manage/project/sdcli/releases/) library from [Pypi](https://pypi.org/).

### Installing

```
python3 -m pip install -U sdcli
```
Run `sdcli` to test if library was installed.
```
sdcli --help
```

#### Create a simple config file with scenes collection of a speaking.
```
sdcli generate --name test
```
That command generate a new file config with yours scenes collection, in the folder `sdcli` Home on your computer.

## Built With

* [Click](https://click.palletsprojects.com/) - The library to manage all arguments.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Jose Segura** - *Initial work* - [Darkcoder](https://github.com/Darkcode01)


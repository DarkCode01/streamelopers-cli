![Streamelopers Dev](https://streamelopers.org/assets/img/logos/logo-white-bg.png)

# Streamelopers CLI - [Config File Generator] ⚙️🚀

This project is to provide to all dev for streamer from dominican republic all cofig or tools tha we are using when we create a stream, this project is to collaborate for all users can stream whatever conference, panel, activity in Dominican Republic or from the other country, without have to configurate all OBS for you.

## Getting Started

You have to install [`stobs`](https://pypi.org/manage/project/stobs/releases/) library from [Pypi](https://pypi.org/).

### Installing

```
python3 -m pip install -U stobs
```
Run `stobs` to test if library was installed.
```
stobs --help
```

#### Create a simple config file with scenes collection of a speaking.
```
stobs generate --type speaking --ouput test
```
That command generate a new file config with yours scenes collection, in the folder `stobs` Home on your computer.

## Built With

* [Click](https://click.palletsprojects.com/) - The library to manage all arguments.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Billie Thompson** - *Initial work* - [Darkcoder](https://github.com/Darkcode01)


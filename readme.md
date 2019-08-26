## Model Tuner

### Intro

This is a web app which enables you to tune your model through PC and Mobile simutaneously. It is powered by Flask and Vue.js. Back-end is responsible for handle model trials and results and front-end provides interface to start/stop your model with different config and visualize trial results.

### Framework

<img src="framework.pdf"></img>

Some key point if you want to apply this framework to your work:
- Choose your matric for your model and write them into to one .csv file at each print time where can be read by flask.

- Expose your model trial with one interface say `start_trial()`.
    ```python
    num_runs = 10
    def start_trial(config):
        data_config = load_config() # return value is a dict
        data_config.update(config)
        for i in range(num_runs):
            model.run(data)
    ```
    
- Call your `start_trial` function at `back_end/app/run.py`.

- Customize your format of results shown in the front-end and rewrite function `data()`,`table()` and class `Data` in `back_end/app/run.py`. You may also need to change some files in Vue.js project. :)


So actually this project probably used by myself. If you want your own model tuner, I strongly suggest you write one on your own. It will only take you one night :).

### About
The whole framework is quite simple since the motivation of this application is to enable me to choose different parameters and check results and then choose again on the phone. I don't need to sit in front of table and watch my screen: epoch 1, epoch 2, epoch ....
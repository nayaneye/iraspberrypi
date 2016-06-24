Signup with plot.ly website:
---------------------------

- [Plotly Website](https://plot.ly)
- After creating account, login with your credentials.
- Go to Settings, Note your api-key and token.
- If token not generated, Click Add new token.

Install the required modules and dependencies:
---------------------------------------------
```
-  sudo apt-get install python-dev
-  wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
-  sudo easy_install -U distribute
-  sudo apt-get install python-pip
-  sudo pip install rpi.gpio
-  sudo pip install plotly
```

Create a new folder for your project. Create a config.json file in said folder and input your plotly API key, and your plotly streaming tokens.
--------
Example config.json:
```
{
  "plotly_streaming_tokens": ["your_stream_token", "another_stream_token"],
  "plotly_api_key": "7dd3p73ljs",
  "plotly_username": "satyadev"
}
```

Script:
------
Now, we're going to pull in our config file, and use them to initialize our Plotly object.

```
  with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

    py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])
```

Now, we create a shell for our graph, and prepare it for streaming. 
This is where you first include your streaming_token, to tell Plotly's 
servers to expect a stream from that particular stream_token!
```
  url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Example Values')

  print "View your streaming graph here: ", url
```

Sample Terminal Output:
----------------------
```
  pi@raspberrypi ~/PRJ/plotly $ python tmp.py
  High five! You successfuly sent some data to your account on plotly. View your plot in your browser at https://plot.ly/~satyadev/0 or inside your plot.ly account where it is named 'Raspberry Pi Streaming Temp Values'
View your streaming graph here:  https://plot.ly/~satyadev/0
```

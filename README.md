# PySaver

![alt text](https://www.guidomascia.blog/wp-content/uploads/2024/01/sample_screenshot.png)

PySaver is an applet you can run on your system tray icon indicator based on PyQt and <code>power-profiles-daemon</code>. 

The latter allows you to choose between three different power profiles:
- power-saver
- balanced
- performance

To manage and switch throughout such profiles, you should always run a command in the terminal. As far as I like it as I feel like Elliot Alderson, this is annoying on the long run, especially if you have to switch from watching a Youtube video to run MATLAB. 

## Install
### Dependencies

You need <code>power-profiles-daemon</code> for the applet to work. For Debian-based distros, run under administrator privileges:

```
apt install power-profiles-daemon
```

This applet depends on PyQt5. Install it by running:

```
pip install PyQt5
```

### Install the applet

Clone the repository and move into its root directory:

```
git clone https://github.com/Maskul93/PySaver.git
cd PySaver/
```

Under administrator privileges:

```
cp PySaver.py /usr/bin/PySaver.py
```

For running it:

```
python3 /usr/bin/PySaver.py
```

If you wish to run it automatically on session login, add the previous line of code to the Session and Startup.

# Credits
The code is released with GNU/GPL 3.0 License, meaning that you can do whatever you want with it. 

Every suggestion is encouraged! If you wish, <a href="https://www.paypal.com/donate/?business=FTGEV3H8Z7Y7W&no_recurring=0&item_name=If+you+are+buying+me+a+coffee%2C+remember+the+inflation%21&currency_code=EUR">offer me a coffee</a>!

Keylogger Project

Description:

This project is a simple keylogger developed in Python using the pynput library. It captures keystrokes and logs them to a text file, allowing for the demonstration of basic keylogging techniques and file handling in Python.

⚠️ Important: This project is intended for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Please use this knowledge responsibly.



Features

-Records all keystrokes and logs them to a file (key_log.txt)
-Custom handling for special keys:
        *Enter key: Starts a new line in the log file
        *Backspace key: Logged as --
        *Space key: Logged as a regular space
Stops logging when the Esc key is pressed

Requirements:

-Python 3.x
-pynput library

Setup Instructions:

1.Clone this repository:
 git clone https://github.com/your-username/keylogger-project.git

2.Navigate to the project folder:
 cd keylogger-project
 
3.Install the pynput library:
 pip install pynput
 
4.Run the keylogger script:
 python keylogger.py
 
Code Overview:

*on_press(key): Captures and logs each keystroke. Custom behavior for special keys:
*Enter: Adds a newline in the log file
*Backspace: Logs -- to represent a backspace action
*Space: Adds an actual space in the log file
*on_release(key): Stops the keylogger when the Esc key is pressed.
*Listener: Listens for key events and triggers on_press and on_release.

Ethical Disclaimer

This keylogger is intended strictly for educational purposes. Unauthorized use to capture keystrokes on any device is illegal and unethical. Always obtain consent before testing or using this tool on any system.

License

This project is licensed under the MIT License. See the LICENSE file for more details.


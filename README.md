# JSON Escaper Burp Suite plugin
Version 1.2

The JSON Escaper Burp Suite plugin simplifies the process of escaping JSON payloads for pentesters, as there is no built-in option for this in Burp. This is especially true when working with JSON payloads and trying to ensure that they are properly escaped to prevent errors. It eliminates the need for manual escaping and ensures proper formatting for testing. With its simple interface, the plugin enables you to enter your payload, escape it, and display the result in a JTextArea where you can select and copy the text

## How to Use
1. Download the plugin [JSON-Escaper.py](https://raw.githubusercontent.com/akashc99/JSON-Escaper-Burp-Suite-Python-plugin/main/JSON-Escaper.py)
2. Set up Jython in Burp Suite by going to the Extender tab and selecting the Options subtab. Under the "Python Environment" section, select "Use existing Jython standalone JAR" and browse to the location of the Jython standalone JAR on your computer
3. In Burp Suite, go to the Extender tab and click on the "Add" button.
4. Select "Python" as the extension type and select the JSON-Escaper.py file from your computer.
5. The JSON Escaper tab will be added to the Burp Suite UI.
6. Enter the payload in the text field and click on the "Escape" button.
7. The escaped payload will be displayed in the JTextArea, where you can select and copy the text.

OR

Install from BApp store.

![POC](https://github-production-user-asset-6210df.s3.amazonaws.com/23627154/246598374-57f92290-73fb-4403-949e-b2230e93bd2e.gif)


Please note that it is necessary to have Jython installed in order to use this plugin. If you do not have Jython installed, you can download it from the official website (http://www.jython.org/) and follow the instructions for installation.

## Feedback
If you have any feedback or suggestions, feel free to open an issue on this Github repository.

## License
This plugin is licensed under the MIT License.

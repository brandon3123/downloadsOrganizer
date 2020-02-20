# Directory Organizer

This project will allow you to keep any directory of your choosing organized by file type/date.

## Instructions

1. Install Python 3.x
    * https://www.python.org/downloads/

2. To monitor a directory for changes, simply run the **directoryOrganizer.py** file with a command line argument of the directory to monitor.

        python3 directoryOrganizer.py /Users/you/Downloads
        
## Run On Mac Startup

1. Create .plist file similar to the following template.

        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>directory.organizer.script</string>
            <key>ProgramArguments</key>
            <array>
                <!-- Full path to python 3.x -->
                <string>/usr/local/Cellar/python/3.7.6_1/Frameworks/Python.framework/Versions/3.7/bin/python3.7</string>
                <!-- Full path to directoryOrganizer.py -->
                <string>/directory-organizer/directoryOrganizer.py</string>
                <!-- Full path of directory you wish to organize -->
                <string>/Users/you/Downloads</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
            <key>StandardErrorPath</key>
            <string>/var/log/directory_organizer.error</string>
            <key>KeepAlive</key>
            <true/>
        </dict>
        </plist>
        
2. Set permissions as root for the .plist file you have created.

       sudo chown root /path/to/plistCreate
3. Move the created .plist file to your launch agents directory.

       mv /path/to/plistCreated ~/Library/LaunchAgents/plistCreated
4. Load the .plist created to launchctl.

       sudo launchctl load ~/Library/LaunchAgents/pListCreated
5. Enjoy! Your script should now be running and will continue to run on startup.
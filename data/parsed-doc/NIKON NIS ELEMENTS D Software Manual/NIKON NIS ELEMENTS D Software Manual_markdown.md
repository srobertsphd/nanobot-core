## NIS-Elements D

## Manual

Publication date 12.05.2014

v. 4.30.00

No part of this publication may be reproduced or transmitted except with the written permission of Laboratory Imaging, s. r. o. Information within this publication is subject to change without notice. Changes, technical inaccuracies and typographical errors will be corrected in subsequent editions.

LABORATORY IMAGING, spol. s.r.o. Za Drahou 171/17 102 00 Praha 10 Czech Republic

Table of Contents

| 1. Command Line Startup Options ........................................................................................... 1          |     |
|----------------------------------------------------------------------------------------------------------------------------------------|-----|
| 2. Installation and Settings .....................................................................................................     | 5   |
| 2.1. Installation and Updates ..........................................................................................               | 5   |
| 2.2. User Rights ..........................................................................................................            | 11  |
| 2.3. NIS-Elements Preferences ...................................................................................... 19                |     |
| 3. User Interface .................................................................................................................    | 23  |
| 3.1. Main Window Components ..................................................................................... 24                   |     |
| 3.2. Image Window ...................................................................................................... 27            |     |
| 3.3. Arranging User Interface ........................................................................................                 | 28  |
| 3.4. Layouts ...............................................................................................................           | 29  |
| 3.5. Layout Manager .................................................................................................... 30            |     |
| 3.6. Modifying Tool Bars ............................................................................................... 31            |     |
| 3.7. Modifying Menus ................................................................................................... 33            |     |
| 3.8. Running a Macro Upon Layout Change ..................................................................... 34                       |     |
| 3.9. Appearance Options .............................................................................................. 34              |     |
| 3.10. Simplified User Interface ...................................................................................... 35              |     |
| 4. Cameras &amp; Devices .......................................................................................................... 39     |     |
| 4.1. Basic Workflows .................................................................................................... 39           |     |
| 5. Image Acquisition ............................................................................................................      | 55  |
| 5.1. Introduction to Image Acquisition ............................................................................                    | 55  |
| 5.2. Shading Correction ...............................................................................................                | 56  |
| 5.3. Camera ROI .........................................................................................................              | 57  |
| 5.4. About ND Acquisition ............................................................................................. 59             |     |
| 5.5. Time-lapse Acquisition ...........................................................................................                | 60  |
| 5.6. Multi-point Acquisition ...........................................................................................               | 63  |
| 5.7. Z-series Acquisition ................................................................................................ 66          |     |
| 6. Displaying Images ............................................................................................................ 69   |     |
| 6.1. Opening Image Files .............................................................................................. 69             |     |
| 6.2. Image Layers ........................................................................................................ 71          |     |
| 6.3. Navigation in ND2 Files .........................................................................................                 | 74  |
| 6.4. ND Views .............................................................................................................            | 76  |
| 6.5. Large Images .......................................................................................................              | 77  |
| 6.6. LUTs (Look-Up Tables) ............................................................................................ 79             |     |
| 6.7. Organizer .............................................................................................................           | 84  |
| 6.8. Database .............................................................................................................            | 88  |
| 6.9. Saving Image Files ................................................................................................               | 91  |
| 6.10. Closing Images ...................................................................................................               | 93  |
| 6.11. Supported Image Formats .................................................................................... 94                  |     |
| 7. Image Analysis ................................................................................................................. 97 |     |
| 7.1. Preprocessing .......................................................................................................             | 97  |
| 7.2. Histogram ............................................................................................................            | 97  |
| 7.3. Thresholding ....................................................................................................... 100          |     |
| 7.4. Binary Layer .......................................................................................................              | 108 |
| 7.5. Mathematical Morphology Basics .......................................................................... 109                     |     |
| 7.6. Regions of Interest - ROIs .....................................................................................                  | 112 |

| 8. Measurement ...............................................................................................................     | 117   |
|------------------------------------------------------------------------------------------------------------------------------------|-------|
| 8.1. Calibration .........................................................................................................         | 117   |
| 8.2. Units .................................................................................................................       | 118   |
| 8.3. Rough Measurement ........................................................................................... 119             |       |
| 8.4. Manual Measurement .........................................................................................                  | 120   |
| 8.5. Object Count ......................................................................................................           | 122   |
| 8.6. Automated Measurement ..................................................................................... 127               |       |
| 8.7. Measurement Options .........................................................................................                 | 129   |
| 8.8. Measurement Features .......................................................................................                  | 129   |
| 8.9. Measurement on Graph ....................................................................................... 143              |       |
| 8.10. Pixel Classifier ..................................................................................................          | 143   |
| 8.11. Exporting Results ..............................................................................................             | 146   |
| 9. Creating Reports ...........................................................................................................    | 149   |
| 9.1. Report Generator ................................................................................................             | 149   |
| 9.2. Report Objects ...................................................................................................            | 150   |
| 9.3. Report Templates ................................................................................................ 153         |       |
| 9.4. Creating Reports from Database ........................................................................... 153                |       |
| 10. Macros ....................................................................................................................... | 155   |
| 10.1. Creating Macros ................................................................................................ 155         |       |
| 10.2. Running a Macro ............................................................................................... 157          |       |
| 10.3. Macro Language Syntax ..................................................................................... 157              |       |
| 10.4. Controlling Cameras by Macro ............................................................................                    | 164   |
| 10.5. Interactive Advanced Macro (API) ........................................................................ 165                |       |
| 10.6. Macro Preferences ............................................................................................               | 165   |
| 11. Movies ....................................................................................................................... | 167   |
| 11.1. Capturing AVI Movie ........................................................................................... 167          |       |
| 11.2. Save ND2 as AVI ...............................................................................................              | 167   |
| 11.3. About Video Compression ..................................................................................                   | 167   |
| 12. Additional Modules ......................................................................................................      | 169   |
| 12.1. Automatic Measurement .................................................................................... 169               |       |
| 12.2. Database .........................................................................................................           | 169   |
| 12.3. Extended Depth of Focus ................................................................................... 169              |       |
| 12.4. Filters Particle Analysis ......................................................................................             | 169   |
| 12.5. HDR ................................................................................................................         | 169   |
| 12.6. Industrial GUI ...................................................................................................           | 169   |
| 12.7. Interactive Advanced Macro (API) ......................................................................... 170               |       |
| 12.8. Live Comparisons .............................................................................................. 170          |       |
| 12.9. Local Option .....................................................................................................           | 170   |
| 12.10. Metalo - Cast Iron Analysis ................................................................................ 170            |       |
| 12.11. Metalo - Grain Size Analysis .............................................................................. 170             |       |
| General Index ...................................................................................................................  | 171   |

## 1. Command Line Startup Options

See also 2.1.3. Command Line Installation Options [9].

When starting NIS-Elements from the command line (or when editing the desktop shortcut properties), you may append some switches with parameters to the main command and thereby modify the startup behavior.

Note

Some switches do not have parameters.

Example 1.1. Command line switches syntax

- ' NIS-Elements executable' switch#1 parameter#1 switch#2 parameter#2 etc.

For example, to run NIS-Elements D and open the starting\_image.jp2 at straight away, run.:

"c:\Program Files\NIS-Elements D\nis\_d.exe" -f "C:\Images\starting\_im-age.jp2"

## Startup Switches

- -? Displays a help screen with the description of switches (basically this page).
- -c 'Command' The application runs the specified NIS-Elements D macro Command .
- -f 'Filename' The application tries to open the image pointed to by the Filename parameter.
- -g 'Grabber Name' The image grabber (driver) of the specified Grabber Name will be used and no camera-selection window will show at startup. Set the parameter value to 'last' and the most recently used grabber/camera will be loaded. As the grabber name, you must use internal name of the grabber, not the one you see in the startup dialog window.

Either use one of the following names or search the application log file for the phrase 'Grabber Name' (see Fixed Grabber Startup [2]).

-gn No grabber (camera) driver will be loaded. Image acquisition will not be possible.

- -h 'HW Unit Name' The specified HW Unit will be used. When using this option you must also specify the Grabber Name. Two HW Units (e.g. two DS-U2 cameras) can be run by one grabber/driver. The available HW Units are listed in the Acquire &gt; Select *Camera Name* window. Set the parameter value to 'select' and the selection box will be shown. When using this option you must also use the -g switch. To find the HW Unit Name, please search through the application log file for 'HW Unit Name'.
- -cam 'Camera Name' The specified Camera will be used. When using this option you must also specify the Grabber Name and the HWUnit Name . To find the camera name, search the application log file for 'Camera Name'. It is also possible to use only a part of the Camera Name, but the part of the name must be unique among all the available cameras.
- -i 'Config Name' A user can specify the configuration to be used by NIS-Elements . The default configuration is saved in the 'C:\ProgramData\Laboratory Imaging\Platform' folder. If you want to create a custom configuration, use the -i switch, e.g.: nis\_ar.exe -i "My\_Configuration" . The config-

uration of this instance will be saved to the 'C:\ProgramData\Laboratory Imaging\My\_Configuration' folder.

This is useful when using two cameras on one microscope for example. You can create a separate program shortcut which uses the -i switch to load a different configuration.

- -s 'Settings File' The application will use the specified Settings File to load and save its settings. The settings file can be created from MS Windows Start menu by the NIS Settings Utility .
- -l 'Language' The application will run in the specified language (if available). Use three-letter language codes according to the ISO 639 [http://en.wikipedia.org/wiki/List\_of\_ISO\_639-2\_codes] standard.
- -m 'Macro File' Application will execute the macro file (*.mac) pointed to by the Macro File parameter.

-passive The application will not connect to any device on startup ( NIS-Elements D will start with blank Device Manager). Camera selection is not affected by this option.

- -p 'Command' ['Param'] The application window will be placed according to the Command . Possible values are:
- · left , right , top , bottom -the window is placed on the corresponding monitor screen.
- · monitor N -the window is placed on the Nth monitor.
- · rectangle (x0,y0,x1,y1) -the window is placed in the specified rectangle (in workspace coordinates). The coordinates must be in parenthesis without any spaces.

-q A new instance of the application will run. By default, only one instance of NIS-Elements is allowed to run.

## Fixed Grabber Startup

Each time NIS-Elements D is run or the grabber / camera / HW unit is changed, four parameter values are written to the application log file (C:\ProgramData\Laboratory Imaging\Platform\Logfiles).:

- · Grabber Name
- · HW Unit Name
- · HW Unit Connection String
- · Camera Name

Let's say we want to set the last used configuration for every NIS-Elements D start:

- 1. Lookup the parameters in the most recent log file. E.g.:

Grabber Name CLxGrabberDriverSim

HWUnit Name

SimGrabber

HWUnit Connection String (empty)

Camera Name Sim\_Camera\_Color

- 2. Modify the shortcut, E.g.:

- "c:\Program Files\NIS-Elements\nis\_d.exe" -g CLxGrabberDriverSim -h SimGrabber -cam Sim\_Camera\_Color
- 3. Double-click the shortcut. NIS-Elements will start without asking for grabber selection

## 2. Installation and Settings

## 2.1. Installation and Updates

## 2.1.1. The Installation DVD-ROM Content

- · NIS-Elements software setup file
- · Drivers and utilities for the HASP Key
- · Drivers for selected cameras
- · User's Guide in the PDF file format
- · Sample image database
- · Sample ND2 image sequences

## 2.1.2. NIS-Elements Installation Steps

## Caution

You have to possess the administrator rights to your computer to be able to install NIS-Elements D successfully.

## Quick Guide

- · Insert the installation DVD in the DVD-ROM drive. A window automatically appears.
- · Install the selected NIS-Elements software version, additional modules and device drivers.
- · Plug the provided HASP key into the USB port of your PC.
- · Run NIS-Elements .

## Step by Step

- 1) When the installation DVD is inserted, a selection window appears automatically.

<!-- image -->

Select the software package to be installed. Select the one you have got the license for and which is properly coded in your HASP key. The installation wizard welcome-window appears. Click Next to continue.

## 2) Install Local Options

Figure 2.2. Local Options installation

<!-- image -->

Select whether to install Local Option or not. Define the folder where NIS-Elements D should be installed. We recommend to use the predefined directory. If you want to change the directory anyway, press the Browse button and select a new one. Otherwise click Next .

Note

The Local Option installation provides some advanced features which did not pass the quality assurance procedure yet. We recommend to wait until they are released officially.

4)

<!-- image -->

Now, select the cameras which will be used with NIS-Elements D .

<!-- image -->

If your licence contains some additional modules besides the NIS-Elements D core software, please select them in this window.

## Note

Any module selected will be installed along with NIS-Elements D automatically. However, you might not be licensed to use it. The module will run after you get the corresponding code registered in your HASP key.

6)

<!-- image -->

Select the devices which will be used with NIS-Elements D . Finish the installation by clicking the Install button.

Note

NIS-Elements may not be connected to devices after installation depending on the PC status at installation. If so, execute the Modify installation command of the Windows Start menu (see the next step) to perform Repair that corrects the previously installed status.

## Warning

For Windows7 users: Some devices do not work correctly after recovery from Sleep mode. Please turn off the Windows 7 Sleep Mode to prevent possible problems:

- · Run the Start &gt; Control Panel command on the main Windows tool bar.
- · Click Hardware and Sound
- · Select Change when the computer wakes
- · In the Put the computer to sleep option, select Never
- · Confirm the settings by the Save changes button.

<!-- image -->

The setup creates a new program group in the Start menu containing the following items: NISElements D application shortcut, the HASP key information shortcut, the Modify Installation shortcut (for adding hardware drivers, modules, etc.), the Uninstall procedure, and the Send Info Tool. A shortcut to NIS-Elements D is created on the desktop too. These changes affect all user profiles of your local Windows operating system.

Figure 2.7. Start menu

<!-- image -->

Note

Clicking the Uninstall command deletes all installed files from disk, and removes the NISElements D program group from the Start menu as well as it removes the desktop icon.

## 2.1.3. Command Line Installation Options

See 1. Command Line Startup Options [1] for details about how to use command line switches. The following switches are to be used with the NIS-Elements installation file to modify behavior of the installation wizard.

-all This parameter unhides options in the setup which are hidden by default. It concerns mainly drivers of devices which were formerly supported but are no longer available.

-new If this command line parameter is appended, the setup checks if any other setup has already been installed. If so, the setup restarts and runs in an independent mode. The update mode is disabled. This enables to install two or more builds together on one operating system.

-xp This parameter enables the user to install NIS-Elements on Windows XP even though this operating system is NOT supported officially.

## 2.1.4. Additional Module/Device Installation

You may need to install a device or an additional module after the NIS-Elements D main system installation.

- · Go to [Start menu &gt; Programs &gt; NIS-Elements D ] program group.
- · Select the Modify Installation command.

- · Follow the installation wizard instructions. Select the check-boxes by the items you would like to add.
- · Finish the installation.

## 2.1.5. Sample Database Installation

If you chose to install the Sample Database, a new subdirectory 'Databases' is created inside the NISElements D installation directory (e.g. C:\Program files\ NIS-Elements D \Databases\...). The 'Sample\_Database.mdb' file is copied to there along with database images (stored in subdirectories). An administrator username/password to access this database is set to:

- · Username: "sa"
- · Password: "sa"

## 2.1.6. Software Copy Protection

The NIS-Elements D software is delivered with a hardware key (also called HL = hardware licence).

Figure 2.8. Hardware key

<!-- image -->

The key contains information about the software licence and allows users to run the corresponding software. A warning message is displayed when user starts NIS-Elements with incorrect HASP. Please connect the USB HASP after the NIS-Elements D installation is finished. The utility called HASPinfo is installed to the NIS-Elements D directory. It enables the user to view information about the software licence and is accessible via the Help &gt; HASP Info menu command.

## 2.1.7. Device Updates

The main goal of the Device Updates setup is to add new devices/cameras or to fix problems that are localized in the drivers only and do not affect any other NIS-Elements functionality.

Device Update setup requires installation of the corresponding NIS-Elements version. The setup contains only .dll files supporting a new device or some corrections and upgrades of already existing drivers. This update form keeps NIS-Elements stable and the update file size small.

Device Update numbering is consecutive and appropriate to its NIS-Elements version until a new full setup of NIS-Elements is released (Major version, Service Pack or HotFix) - then the numbering starts from the beginning.

Device Updates are cumulative and contain all the changes from the previous updates. Also full NISElements setups (Major versions, Service Packs and HotFixes) will contain all the changes from the previously released Device Updates.

## 2.1.8. Fixes

Fixes represent driver changes which serve for testing purposes or for correcting problems occurring only under special conditions. Fixes are packed into a zip file containing modified driver files. Fixes are usually user requested, therefore they are not considered as Device Update candidates.

## 2.1.9. Installing the Database Module on 64-bit Systems

The NIS-Elements installation file contains 64bit MDB drivers which improve the speed of the database module on 64bit systems. However, 32bit version of MS Office 2010 cannot be used along with these 64bit drivers. You can install these drivers, if:

- · you run 64bit version of MS Office 2010
- · you use other version of MS Office such as Office 2013
- · you do not use MS Office at all

Find the drivers in the NIS-Elements folder, typically: 'C:\Program Files\ NIS-Elements D \Drivers\Data-base\_MDB\'

## 2.2. User Rights

User management is very useful when a single workstation is shared by number of users. Some user accounts may have administrator rights to NIS-Elements while other's privileges are quite restricted. A per-person system may be established or user accounts may be shared. The following principles are utilized within NIS-Elements D :

MSWindowsaccountssupport NIS-Elements D can assign privileges to MS Windows accounts. Whoever is logged in the operating system and runs NIS-Elements obtains a default set of privileges. System administrator can then further restrict or extend the user's rights.

NIS-Elements D password protection It may be not comfortable enough to log the current user off from MSWindows when a user change is required in NIS-Elements . For such case a completely independent list of user accounts, which is not connected with MS Windows users, can be created. Then just restart of NIS-Elements is needed to switch the user.

Private vs. Shared storage Every user-created item (setting) important in the work-flow can be protected from unwanted change in two levels. First, the creator of the item (optical configuration, layout, objective, etc.) can save it as private . Unless its status is changed to shared , no other user will even see this item within the lists throughout the application. The second level of protection concerning all shared items is provided by assigning users to Groups and Privileges groups.

Groups Every user is a member of a group. The group enumerates shared items (optical configurations, objectives, etc.) which will be visible for its members. NIS-Elements administrators can create any number of groups and select the items to be visible.

Privileges There are basic groups of privileges which allows users or restrict them to perform certain actions. This concerns for example modifying macros, reports, selecting cameras, etc. There are four levels of privileges by default, but further can be created by an administrator:

- · Admin
- · Common
- · Guest
- · Default

## 2.2.1. NIS-Elements authentication

If you have chosen ' NIS-Elements (Password protected)' user authentication method, a login dialog window appears at every start-up of NIS-Elements . Enter a user name and a password for existing user account. If the option Allow to Create a New User at Start-up is enabled, you can create a new user account without needing an administrator. This account is assigned to the Default group of users and Default group of privileges automatically.

## 2.2.2. Creating a Shared Layout

Please read the following example on user management. Step by step, we describe the creation of a shared layout which can not be modified by members of the Common and Guest groups.

- 1) Run the View &gt; Layout &gt; Layout Manager command. Set at least one of the defined layouts as Shared . (see 3.3. Arranging User Interface [28])
- 2) In the left column of the window, select User Rights .

<!-- image -->

- 3) Make sure you are logged as a user with the Privilege to Modify user rights . If not, use the Log As... button to log in under a different account which has the privilege.

<!-- image -->

## 4) Set layout visibility

Select the Groups tab. Here you can see at least one group of items called Default . Either select one a group or create a new one by the New button and choose Layout within the list of items. All layouts set as shared will be listed on the right side within the Accessible items field. Make sure the check boxes next to the layouts which you allow to be used by the group are selected.

## 5) Disable layout modification

Select the Privileges tab. Select the group of privileges which should have not the permission to modify the selected shared layouts. In the Privileges field on the right, make sure you de-select the Modify Shared Layouts option.

## 6) Apply the new policies

Select the Users tab. In the list of users, select the ones which you would like to apply the policy to (users can be selected one by one or by multi-selection with the Shift or Ctrl key pressed). Then, assign the appropriate Group and Privileges by selecting them from a pull-down menu on the right side of the window.

- 7) Confirm the changes by the Apply button.

## 2.2.3. Closing Another Instance of NIS-Elements

When more users want to work with NIS-Elements on the same computer and one of them did not close his NIS-Elements running copy, other users cannot use the program, because only one NIS-Elements copy can be running at a time. The possibility to close the running program started by a different user during a new NIS-Elements launch is available in the following dialog window. This applies only if there are no experiments running.

Figure 2.9. Another instance running

<!-- image -->

## 2.2.4. User Rights Options

User Authentication The Windows authentication utilizes Windows accounts to automatically log in to NIS-Elements D .

The NIS-Elements D (Password protected) authentication utilizes application user accounts and passwords at the start-up of NIS-Elements D . Check the Allow to Create a New User at Start-up option to enable creating of a new user in the Login dialog window.

Current user Displays currently logged in user.

Log As Opens the Login As dialog which enables you to login as a different user e.g. an administrator with more user rights for the purpose of changing User rights settings.

Figure 2.10. Login As

<!-- image -->

Select the user name you want to log-in as. Enter a valid password and press OK . The new user identity is available only while the User manager is opened.

Statistics Edit path and file name of a database file for saving statistics.

Export/Import user rights These buttons enable anyone to save/load complete settings of user accounts and their privileges to/from an external XML file. Standard Open and Save As windows appear. Having the data exported may be useful when copying the settings to other computers.

## 2.2.5. Users Tab Options

New Enables to create new NIS-Elements D user account. You have to posses the privilege Modify User Rights.

Figure 2.11. Creating new user

<!-- image -->

Enter a new user name, assign him to one of the existing Groups and group of Privileges and set the password. Check the Enforce user to change his password at start-up option to make the user change his password at his first login into the NIS-Elements D .

## User name and password properties

Length of the user name and password is limited to 50 characters. You can use any combination of characters, symbols or numbers (except the Windows ones: " , :, *, ?, ", \, /, &lt;, &gt;, |" ).

Remove Removes selected user account. You can select multiple accounts and delete them at once.

Copy To Choose a user from the pull down menu whose group and group of privileges will be changed according to settings of a selected user.

Duplicate You can easily create a new user by duplicating the existing. This preserves all account settings under a different name. If you have selected to duplicate more then one user, enter a name prefix, which is added in front of the original name for all selected duplicated accounts. User which was created as a duplicate has an empty password and is forced to change his password at next application startup.

User Accounts List This table displays all existing user accounts. You can sort them according to any of four columns. The first column displays type of the account. The second one shows user names. The third one displays assigned group of users. The fourth one displays assigned group of privileges. Select one or more users whose settings needs modification.

Set password To change password of a selected NIS-Elements D user account, press the Set password button. You have to posses the Privilege Modify User Rights. Otherwise you can change only password of the current user. Following window appears:

Figure 2.12. Reset of password

<!-- image -->

Name of the user is displayed. Enter and confirm new password. When done, press the Change button.

Enforce user to change his password at start-up Check this option to make the user change his password at his first login into the NIS-Elements D .

Enumerate All Windows Users This button starts copying MS Windows accounts to NIS-Elements D . The accounts are assigned to user groups (admin, common, guest) according to their Windows permission settings.

## 2.2.6. Groups Tab Options

Figure 2.13. Groups tab

<!-- image -->

New Enables to create new group of users. You have to posses the privilege Modify User Rights. Enter a name of new group.

Remove Removes selected groups. You can select multiple groups and delete them at once.

Copy To Choose a group from the pull down menu which settings will be changed according to selected group.

Duplicate You can easily create a new group of users by duplicating the existing. This preserves all group settings under a different name.

List of Groups All defined groups are listed in this window. Each group contains subsets. If you click on a subset, its items appear in the Accessible items list.

Accessible items This list shows items of a selected subset. Every item has its own check box. If the check box is checked, all users assigned to the corresponding group will see the item. Otherwise they will not see the item.

Optical Configuration Displays all shared optical configurations.

Objectives Displays all shared objectives.

Cameras Displays all installed cameras. From the pull down menu below select a camera which is used as default for users without the privilege Select Camera.

Devices Displays all installed devices.

Layouts Displays all shared layouts.

Macros Displays all shared macro commands. Check a macro to make the content of it visible to this Group.

Reports Displays all shared reports and report templates.

## 2.2.7. Privileges Tab Options

Figure 2.14. Privileges tab

<!-- image -->

New Enables to create new group of privileges. You have to posses the privilege Modify User Rights. Enter a name of new group.

Remove Removes selected groups. You can select multiple groups and delete them at once.

Copy To Choose a group from the pull down menu which settings will be changed according to selected group.

Duplicate You can easily create a new group of privileges by duplicating the existing. This preserves all group settings under a different name. If you have selected to duplicate more then one group of privileges, enter a name prefix, which is added in front of the original name for all selected duplicated accounts.

Groups of Privileges A list of all groups of privileges is displayed.

Privileges A list of privileges is displayed. Every item has its own check box. If the check box is checked, it grants all users assigned to the corresponding group relevant privilege to access, change, modify, etc.

Note

Users that do not have the privilege "Modify Shared Optical Configuration" can temporarily change the brightness settings (e.g. exposure time, gain, etc.) in a shared optical configuration and use such adjusted optical configuration for example in Multichannel acquisition. But all such modifications will not be stored and they will disappear when the application is restarted.

## 2.3. NIS-Elements Preferences

## 2.3.1. Adjusting Program Preferences

- 1) Run the Edit &gt; Options command. The Options dialog window appears.
- 2) Select a tab which contains requested options. Options are sorted into several groups:

General Options concerning basic image operations. See 2.3.2. General [20].

Appearance Options concerning the graphical user interface. See 3.9. Appearance Options [34].

Open Next Options concerning the File &gt; Open/Save Next &gt; Open Next menu command. See 6.1.2. Options for the Open Next Command [70].

Save Next See 6.9.2. Save Next Options [92] for more information.

Macro Configures key shortcuts to macros and sets macros to run automatically on startup See 10.6. Macro Preferences [165].

Measurement See 8.7. Measurement Options [129] for more information.

Data export See Data Export Options [147] for more information.

User rights See 2.2. User Rights [11] for more information.

Layout Manager See 3.5. Layout Manager [30] for more information.

- 3) Make any changes you need in preferences and use the following buttons to manage them:

Defaults for this Page Restores default settings of the currently displayed options tab.

OK Confirms and saves changes made to the preferences. The dialog window is closed afterwards.

Cancel Cancels all changes made to the preferences. The dialog window is closed afterwards.

Apply Applies changes made in preferences but keeps the Options dialog window open. You can apply changes individually on each tab.

Help Displays relevant help page.

## 2.3.2. General

## Documents and History

(requires:Local Option)

Use fix path for images The defined directory is always used when using the File &gt; Open or File &gt; Save As command.

Limit number of opened documents When this options is checked, the user is limited to a single opened image at one time.

Capture always creates a new document If checked, every acquisition creates a new image.

Use last LUTs on image open When a new image is opened, this option turns the look up tables automatically on, and copies the settings from the current or the last opened image. Some image formats (jp2, ND2) can contain the LUTs settings. If such image is opened, the saved LUTs are loaded instead of the most recently used.

Use AutoLUTs on image open for images without LUTs information This option keeps the AutoLUTs feature of the File &gt; Open window always ON, and it applies AutoLUTs to the image after opening. This option is ignored if LUTs settings are saved in the image, or if the Use last LUTs on image open option is applied.

Show mapping dialog in organizer after drag and drop Displays the Mapping window every time an image is inserted to a database table. It enables you to check/modify mapping of the image info values to the database table fields.

Open new ND views to new window Displays each newly generated ND view in a separate window.

Showimageinfo window on save Displays the File &gt; Image Properties window every time an image is saved via the Save As command.

Detect sequence on image open Whenyouselect to open an image that is a part of image sequence such as 001.jp2, 002.jp2..., it is recognized automatically and you are offered to convert it to an ND2 file.

Show binary layers' contours Check this item to display contours of binary layers.

Use zero based time scale for ND documents (requires:Local Option) Select this option to ensure that the first frame of a time sequence will always start at 0.0s.

State of saturation indicator after start Select what to do with the saturation indicator settings ( ) after NIS-Elements D is restarted. Turn it ON, OFF, or remember the last setting.

## Rotation Flips and Shifts

Apply to overlaid binary layer If checked, in overlay mode both binary and color images are rotated, shifted and flipped.

## Optical Configuration

Save all camera settings to optical configuration automatically If the currently selected optical configuration contains Camera Settings and this option is checked, any change of the settings is written to the optical configuration immediately.

Save brightness to optical configuration automatically If the currently selected optical configuration contains Camera Settings, the Brightness setting is being updated continuously according to the current state. Also functionality of saving confocal brightness setting(laser power, detector gain and scan frame rate) is contained in this option.

Select corresponding optical configuration when filter changed... (requires:Local Option) Enabled if 'Unselect' in the option below is chosen. Allows NIS-E to automatically change the optical configuration based on the filter selected on the microscope.

## When Optical Configuration setting changed

Keep Selected The Opt. configuration name is marked by the "*" sign and the change is offered to be saved.

Unselect Every change of Optical configuration setting results in its deselecting and switching to user settings.

Save all changes All changes regarding the Opt. configuration settings are updated automatically according to the current state.

Temp NIS-Elements D uses the Temp directory for storing temporary data when there is not enough RAM available. You can redirect the system to use a directory on another harddisk, which may speed up the whole system.

Defaults for this Page Restores the default setting for General Options.

## 3. User Interface

Figure 3.1. The NIS-Elements Main Window

<!-- image -->

## 3.1. Main Window Components

## 3.1.1. Main Menu

All basic NIS-Elements functions are accessible from the main menu at the top of the screen. Menu commands are grouped according to their purpose.

## 3.1.2. Tool Bars

There is a default set of tool bars, each tool bar containing number of buttons. There is also one fully customizable tool bar - the main left tool bar - to which any button can be added. Every button or whole tool bar can be hidden by user. Please see 3.3. Arranging User Interface [28] for further details.

## 3.1.3. Status Bar

The status bar at the bottom of the screen displays the following information:

Figure 3.2. The application status bar

<!-- image -->

- 1. This part of the status bar displays available layouts.

Note

The layout Tabs may be hidden when the Show Layout Tabs option in the 3.3. Arranging User Interface [28] window is deselected.

- 2. This status bar section displays the type of the currently selected camera.
- 3. Here you can get information about the most recently performed command. The FPS / Exposure / Focus info is shown in case of live image. The black bar indicates the focus rate. Longer black bar represents more of the image in focus.
- 4. This section show the name of the current objective.
- 5. Current coordinates of XY (Z) stage are shown in this part of the status bar.

## 3.1.4. Docking Panes

Docking panes are square spaces inside the application window, where you can place (dock) any of the control panels. There is one docking pane available at the Right, Bottom, and Left side of the application screen.

## To Display a Docking Pane

1. Go to the View &gt; Docking Panes sub-menu and select the pane you would like to display.

<!-- image -->

Note

The Docking Panes sub-menu can be also displayed by right-clicking into the empty application screen.

- 2. The docking pane appears, either empty or with some window(s) docked inside.
- 3. Repeat this procedure to display more docking panes.

## Handling Control Panels

Various control panels can be displayed docked within the docking panes or they can be floating. See the following picture:

Figure 3.4. The Docked Control Panel Caption

<!-- image -->

To handle the control panels (CPs), you can:

Open recently closed CP Locate the button on the main left tool bar. When you click it, the list of recently closed CPs appears. Pick one to display it again.

Add CP to a docking pane Right click inside a docking pane (3) to display the context menu. Select the control panel to be displayed. If the window is already opened somewhere else (in another docking pane or floating), it closes and moves to the new destination.

Close CP Click the cross button (2) in the right top corner of the tab.

Drag CP Drag any CP by the tab and drop it somewhere. If you drop it by the edge of a docking pane, it will create another column of this pane. If you drop it over the caption of another CP, it will be docked in the same pane as a new tab. If dropped somewhere else, the CP will be floating.

A color frame appears when you place the mouse cursor dragging a CP over the edge of a docking pane or a caption of another CP. It indicates that if you drop it, its placement will be handled automatically.

Minimize the docking pane Click the arrows in the top left corner. The pane minimizes to a stripe by the edge of the screen. It can be restored to its original position by double clicking this stripe or by clicking the arrows again.

Close the docking pane Click the cross button (4) in the docking pane caption. Or you can right click the pane and unselect the Docking View option.

Dock/undock CP To dock (and undock) a CP, double click its tab.

Display CP Another way to display a CP is to go to the View menu and select the desired control panel. After that, the CP appears on the screen - floating or docked. Positions of the windows are being saved by the system so that each control panel appears in the same position as it was before it being hidden. The controls are sorted to several groups.

<!-- image -->

Shrink/Expand dockers Having more docking panes opened, a situation where there is not enough room for the control panels can occur. In such case, the Shrink and Expand commands shall be used.

<!-- image -->

- 1. Right click the pane you would like to shrink/expand. A context menu appears.
- 2. Select the Expand Shrink / command.Whenoneofthepanesshrinks, the neighbouring pane expands to the emptied corner and vice-versa.

## 3.2. Image Window

Tools affecting the appearance of the current image are gathered within the image window tool bars (the top image tool bar and the right image tool bar) . There are the following buttons by default:

<!-- image -->

Enable LUTs Applies LUTs to the image. See 6.6. LUTs (Look-Up Tables) [79].

- Keep Auto Scale LUTs Applies the AutoScale command to the image continuously.
- Auto Scale Performs automatic setting of LUTs.
- Reset LUTs Discards the LUTs settings.
- Show LUTs window Opens the window with LUTs.

Pixel Saturation Indication Turns on / off pixel saturation indication without setting on / off LUTs. Select the highlighting color from the nearby pull-down menu for Oversaturated and / or Undersaturated pixels. See 6.2.3. Displaying Image Layers [72].

- Fit to screen Adjusts zoom to view the whole image within the NIS-Elements D screen.
- Best Fit Adjusts zoom to fit the NIS-Elements D image window in one direction but to fill the screen.
- 1:1 Zoom Adjust zoom so that one pixel of the image matches one pixel of monitor.
- Zoom In Increases magnification of the image.
- Zoom Out Decreases magnification of the image.
- Show Probe This button activates the probe. The probe affects histograms, auto exposure and auto white balance functions.
- Show Grid Displays the grid for rough measurements.
- Show Scale Displays the image scale.
- Show Frame Displays and applies the measurement frame. (requires:Automatic Measurement)
- Turn ROI On/Off Displays the Measurement Region Of Interest. (requires:Automatic Measurement)
- Show Profile Displays the Measure &gt; Intensity Profile control panel. It allows you to specify a linear section in the image of which the pixel intensities graph will be created.
- View LUT Intensity Displays the scale of intensities used inside the image. It works on monochromatic images or a single image channel.
- ShowAnnotations Displays the vector layer which typically consists of annotation objects (text labels, arrows) and measurement objects.
- View Binary Displays the binary layer of the image. (requires:Automatic Measurement)

<!-- image -->

<!-- image -->

- View Color Displays the color layer of the image.
- View Overlay Displays the color layer and the binary layer in overlay. (requires:Automatic Measurement)

Tip

Right click the icons to invoke a context menu where properties of each tool can be modified.

## Channel Tabs

<!-- image -->

Channel tabs at the bottom left corner of the image window enable switching between image channels. You can also edit their properties using commands available via a context-menu. See also 6.2. Image Layers [71].

## Status Bar

The status bar at the bottom of the image window displays the following information:

<!-- image -->

- 1. The first field of the image window status bar Image displays the calibration. See also 8.1. Calibration [117] , 8.2. Units [118].
- 2. Image bit depth (8bit, 12bit, 16bit, etc.) followed by Image size. You can change the displayed units from the context menu.
- 3. Pixel coordinates of the mouse cursor along with channel intensities, Binary layer value (0 or 1) and the Color mode (RGB, Monochromatic, etc.).

## 3.3. Arranging User Interface

Having a well organized application layout can help you make the work with NIS-Elements D very effective. There are the following options on customizing the appearance of NIS-Elements D :

Custom window placement All control panels (Camera Settings, Measurement, Histogram, LUTs, etc.) can be arranged inside or outside of the main application window.

Compact window or multiple windows The control panels as well as tool bars can be floating or docked on sides of the application screen.

Multiple monitor support The NIS-Elements D window can be stretched to occupy two monitors. When you switch from different application, NIS-Elements D will be activated on both monitors.

Customized tool bars Tool bar buttons may be added and removed from tool bars. See 3.6. Modifying Tool Bars [31].

Maximizing the Image Area You can hide some of the GUI elements which are displayed by default:

- · The channel tabs and the layout tabs may be hidden to save some screen-space. Display the 3.9. Appearance Options [34] window and de-select the Show Channel Tabs and the Show Layout Tabs options.
- · Image controls and the image status bar may be hidden. Use the Auto hide bottom toolbar option of the 3.9. Appearance Options [34] window.
- · When an image is displayed in great magnification, scroll bars automatically appear by the sides of the image window. You can hide them by de-selecting the Show Scrollbars context menu option.

## 3.4. Layouts

A layout in the context of NIS-Elements D is a set of options describing the arrangement of control panels, tool bars, and menu items. Blue tabs representing active layouts appear in the application status bar. The following layouts are placed there by default:

- · Full Screen
- · Docked Controls
- · Measurement

Other layouts can be added and managed via the Layout Manager. To hide/show the layout tabs within the status bar, go for View &gt; Layout &gt; Layout Manager and (de)select the Show Layout Tabs option.

## To Create a New Layout

<!-- image -->

- 1. Modify the current layout so that it suits your concept of work.
- 2. An asterisk * appears next to the layout name (to indicate it has been modified).
- 3. Right click the layout tab and select the Save Current Layout As or Save As Default command. If you do not need to create a new layout but would like to save the changes made, just right click the current (asterisk-marked) tab and select the Save command from the menu.
- 4. Write the new layout name and confirm it by OK.
- 5. A new tab appears and the layout is saved to the list of layouts.

## To Reload Previous Layout Settings

You may want to undo the changes made to the layout. Mostly, it can be done by the Reload command. Or by selecting the Load Default command.

- · Right click the asterisk-marked (recently modified but not saved) tab and choose the Reload command. The application restores the last saved state of the layout.
- · Right click the asterisk-marked tab and choose the Load Default command. The application loads the previously saved default layout.

## 3.5. Layout Manager

Run View &gt; Layout &gt; Layout Manager to display the Layout Manager. The list of currently available layouts is placed on the left side of the layout manager. Each layout may contain information about controls, tool bars, menu, and commands to be performed when switching between layouts.

Figure 3.10. List of Layouts

<!-- image -->

## Modifying the Layout Settings

- 1. Select items within the Global Layout list which you want to be shared by all layouts.
- 2. The check marks on the left of the layout names indicate the layout visibility. Select the ones you want to display in the application status bar.
- 3. If an item within some particular layout is not selected, it means you do not want to customize it and the global settings - if selected within the Global Layout -will be used. If the item is not selected within the Global Layout either, the settings of the most recently active layout will be used.
- 4. Set whether the layout is Private or Shared . If set Private , it will not be visible for other users. See 2.2. User Rights [11].
- 5. Customize each item according to your needs (see below).

## Layout Manager Tools

<!-- image -->

New Adds a new layout to the list of layouts.

- Remove Deletes the selected layout. The first two layouts cannot be deleted.
- Activate Makes the selected layout active.
- Load Default Loads original settings of the selected pre-defined layout ( Full Screen , Docked Controls , Measurement ) so that it looks just like after the program installation.
- Lock Layout Select a layout component and click this button to lock these elements so that they cannot be moved or closed. To unlock these components, click the button again or right-click the locked layout tab at the bottom and click Unlock Layout .

<!-- image -->

- Apply to All Ensures that the executed changes will be applied to all layouts.
- Import Enables to load a previously saved set of layouts from an XML file. When you try to import a layout with already existing name, you will be prompted to choose whether: the imported layout replaces the existing colliding layout, or is not imported, or is imported and renamed.
- Export Layouts The settings of layouts can be saved to an external XML file. Use this Export button. In the windows that appears, define the destination file name and check which layouts will be included in the exported xml file.

## 3.6. Modifying Tool Bars

## Hiding Toolbar Buttons

<!-- image -->

- 1. Display Layout Manager by the View &gt; Layout &gt; Layout Manager command.
- 2. Select the Toolbars item within the list of layouts. The right-side part of the window changes.
- 3. Choose one of the tool bars which you would like to modify from the Toolbar pull-down menu.
- 4. If selected, de-select the Use Default option on the right.
- 5. Any button of the tool bar may be hidden by de-selecting it. No buttons can be added to any of the tool bars except the Main Left Tool Bar .
- 6. The whole tool bar can be hidden by de-selecting the Show Toolbar check box.
- 7. There are two sizes of buttons available. Select the Large Buttons option to use the larger one. This setting is shared by all tool bars.

## Adding Buttons to the Left Tool Bar

Custom user buttons can be added to the main left tool bar. You can define your own buttons which run single macro functions or execute macros . Select the Main Left Toolbar from the pull-down menu.

<!-- image -->

Let's say that we very often use the Image &gt; Contrast command. It is useful to add a shortcut button to the tool bar.

- 1. Press the Add button, and choose Command from the pull-down menu:
- 2. A new command Command0 -is added to the list.
- 3. Now, assign a macro command: Open the pull-down menu on the right side of the Command edit box and click Command List .
- 4. A list of commands appears. Choose \_Contrast() .
- 5. Confirm the selection by OK .

Note

It is possible to assign a sequence of commands to a single button by repeating this procedure.

If you are not satisfied with the default icon, you can change it by pressing the Change... button. A window for selecting the icon appears. You can select the image from the NIS-Elements D icon set or load some other from any file containing icons (ico, dll). You can define another icon for the command in a disabled state, too.

It is handy to define a tool-tip (a text that appears when the mouse cursor is placed over the icon) for your command. Simply write the text into the Tooltip box. You can change the position of the command in the tool bar using the arrow buttons. The Default button discards your changes and inserts the default set of commands to the tool bar.

## 3.7. Modifying Menus

The Main Menu and some of the Context Menus within the application window may be modified. Items of the context menus can be hidden by de-selecting them similarly to the tool bars. The main menu can be modified as follows:

## Modifying the Main Menu

- 1. Display Layout Manager by the View &gt; Layout &gt; Layout Manager command.
- 2. Select the Main Menu in the topmost pull-down menu.

<!-- image -->

- 3. Any item may be added to the main menu - a Separator , a Menu Command , a sub-menu ( Menu Popup ), and even a new menu ( Main Menu Popup ) - by the Add button.
- 4. Select the existing menu item under which you would like to place the new item.
- 5. Click the Add button and select the item to be added from the pull-down menu.
- 6. Edit the Item Properties .

<!-- image -->

Text This is the text which appears in the pull-down menu. You may add '&amp;' before any letter such letter will be considered a keyboard shortcut when browsing the menu.

Hot key One or more hot key shortcuts may be assigned to the command. Just press the Add button and press the key combination. Press Remove to remove the selected hot key.

Enabled/Disabled bitmap, Command These fields serve for assigning a bitmap image and a macro function to the menu command. It works the same way as when modifying the Main Left Tool Bar (described above).

## Note

The Default button discards all changes and loads the main menu original configuration. The Remove button deletes the selected item. The arrow buttons move the selected item up/down. The Use Default check box, when selected, applies the default settings to the menu.

## 3.8. Running a Macro Upon Layout Change

A macro command or a macro can be run upon layout change.

- 1. Display the layout manager by the View &gt; Layout &gt; Layout Manager command.
- 2. Select the layout by displaying of which the macro function will run and select the Commands check box.
- 3. The following box appears on the right side:

<!-- image -->

- 4. Select the timing. The 'before' option will run the command when you click on the layout tab, but before actually changing the layout. The 'after' option runs the command right after the layout is changed.
- 5. When the field is enabled, type the command or insert it via the pull-down menu.

## 3.9. Appearance Options

General appearance adjustments can be made in the Options window. Run the Edit &gt; Options command and switch to the Appearance tab.

Background Background of the main screen may use default tiles or custom color.

Color scheme There are the following color schemes predefine within the application: Light scheme, Dark scheme, Black scheme.

Language Select the language to be used in GUI. The language pack is a part of the 12.9. Local Option [170] feature set.

Prompts on Image Save dialog Actual words used on buttons of the window which appears if an image has been modified and is about to be closed.

The Z value displayed in statusbar Having two Z devices, select whether to display Z1, Z2 or both on the main status bar.

Close ND Acquisition window after Run (requires:Local Option)

The View &gt; Acquisition Controls &gt; ND Acquisition window will be closed automatically upon acquisition start.

Image window tool bars You can decide whether the image tool bar is integrated to the main tool bar or whether each image has its own. You can also decide the buttons appearance. See 3.2. Image Window [27].

Auto hide bottom toolbar This option hides the image status bar and the ND2 control bar (6.3.1. Control Bar [74]) automatically. It is displayed only when the mouse cursor rolls over the bottom part of the image picture.

Show channel tabs Show channel names and colors in the image window status bar.

Show Layout tabs Show layout tabs in the main status bar.

Show Task Bar If unselected, the Windows taskbar will be hidden.

Default vertical docker on the (requires:Local Option)

Select the preferred side for the default vertical docking pane.

Keep text size while zooming When selected, text annotations will not be zoomed with the image. See View &gt; Analysis Controls &gt; Annotations and Measurements .

Allow zoom factors lower than best fit When selected, the image can not be resized to be smaller than displayed using Best fit command.

Lock camera magnification If you are used to switch between two camera modes (resolutions), this option ensures that the scene observed does not change its size or position.

Keep picture window aspect If checked, the image window respects the image size while zooming.

Initial Zoom You can select the zoom factor of the newly opened images. The options are Best Fit, 200, 100, 50, 25%.

Initial zoom 100% for Live and Capture Whenever a new Live or Captured window is opened, the zoom will be automatically set to 100%.

## 3.10. Simplified User Interface

After the Industrial GUI module is installed, a simple layout intended to be used in industry imaging applications is added to the application. Switch to the layout by the Simple button in the top right

corner in the top right corner. Return to the main layout by the same button (which is changed to NIS-D ).

Note

This button corresponds to the View &gt; SimpleControl menu choice.

A Nikon-manufactured digital camera (DS-U1/U2/U3, DXM1200C, 1QM) must be connected to NIS-Elements D in order to display the View &gt; SimpleControl command.

## 3.10.1. Behavior

- · The 'Live' and 'Captured' images can be switched between the main image area and the preview window on the right.
- · The number of control panels displayed within the docking panes is reduced. The following controls appear:

3.10.5. Preview Control Panel [38]

View &gt; Acquisition Controls &gt; *Camera* Settings

<!-- image -->

View &gt; Analysis Controls &gt; Annotations and Measurements

3.10.3. Camera Control Panel [37]

3.10.4. Save Control Panel [37]

View &gt; Acquisition Controls &gt; *Microscope* Pad

View &gt; Acquisition Controls &gt; Auto Capture Folder

No other control panels can be displayed.

- · The main tool bar is reduced, some buttons are added. See 3.10.2. Tool Bar Buttons [36].

## 3.10.2. Tool Bar Buttons

The following tool bar buttons are added to the layout:

<!-- image -->

Print This button sends the current image (the large one) to the default printer. Invoke the nearby pull-down menu to set printing properties. See File &gt; Print .

ChangeView This button swaps the Live and the Captured images between the main image window and the preview window in the right-side docking pane.

Show Graticule This button has been moved here from the right image tool bar of the main view and provides the same functionality. See 3.1. Main Window Components [24].

Show Scale This button has been moved here from the right image tool bar of the main view and provides the same functionality. See 3.1. Main Window Components [24].

<!-- image -->

## 3.10.3. Camera Control Panel

This control panel contains a single button. Behavior of this button change according to the Auto Capture (Auto Save) option of the Save control panel. It either captures a single image ( Capture) or captures a single image and saves it to the Auto Capture Folder automatically ( Auto Capture).

<!-- image -->

## 3.10.4. Save Control Panel

This control panel enables the user to specify image saving options. Most of the settings only applies when the Auto Capture option is checked.

<!-- image -->

Directory Press the ... button and select the Auto Capture Folder where images will be saved by default.

Prefix, Digits Type the prefix intended for the files being saved automatically. Specify how many digits shall be used for numbering the images.

File Format, Compression Select the file format to save the images in. Some formats enable you to set the Compression parameter. It is recommended to use either 'none' or 'lossless' in order to preserve good image quality.

Ex. The path and file name of the next image to be saved is displayed here.

Auto Capture Check this option and the a new image will be created and saved to the Auto Capture Folder each time you press the Auto Capture button.

Annotation This option determines whether the annotations created by the tools of the Annotations and Measurements window will be included in the saved file.

Warning

The separate annotation layer will be merged with the image data.

## 3.10.5. Preview Control Panel

The Live or Captured image is displayed within this window. Use the Change View button of the main tool bar to select which one.

<!-- image -->

## 4. Cameras &amp; Devices

## 4.1. Basic Workflows

## 4.1.1. Camera Selection on Startup

Let's assume the camera works properly, is connected to the PC with proper system drivers installed and running (if required by the camera).

## Setting Up the Camera

1)

## Select Camera Driver

You will be asked to select the camera driver every time you launch NIS-Elements D . You can change the driver later using the Acquire &gt; Select Driver command. Choose the driver that matches your camera:

<!-- image -->

## Selecting a Camera

Color cameras can be used in a monochromatic mode. The actual camera type (color/mono) can be selected by the Acquire &gt; Select *Camera Name* command.

Note

The emulated monochromatic mode is optimized for use with fluorescence specimen where often only a single-color signal is being captured. The following formula is used to compute intensity of the emulated mono image:

<!-- formula-not-decoded -->

Where: W is channel weight calculated from the channel histogram and I is channel intensity. Wensures, that channels containing some signal are accentuated while channels without signal are suppressed. As a result, depending on conditions, the brightness of a monochrome image might not change even if the lamp light intensity is changed.

2)

3)

## Adjust the Camera Settings

Exposure time, camera resolution, and other camera-specific features are adjustable from the Camera Settings window. To invoke it, use the Acquire &gt; Camera Settings command.

## 4.1.2. Optical Configurations

Typically, a laboratory computer image analysis system consists of a computer, a camera, and a microscope equipped with certain accessories (objectives, filters, shutters, illumination, rotary changers, etc). Most of the mentioned microscopic hardware can be motorized and therefore can be controlled via NISElements D . In addition, it is possible to integrate single settings of all these devices into one compact set called Optical Configuration . It is recommended to create several optical configurations containing particular devices settings. Then a single click can completely change the current hardware configuration.

## Creating New Optical Configuration

- 1) Please check that all the devices (microscopes, cameras, etc.) which you want to associate with the new optical configuration are properly attached to the system and working.
- 2) Choose the Calibration &gt; New Optical Configuration command. In the window which appears, adjust the settings of the devices to match the intended state which will be saved to the optical configuration.
- 3) Type the name of the new optical configuration to the Name field. Use a short descriptive name, the name is used on the button in the main tool bar when you select the Show on toolbar option.
- 4) In the left column, select which device settings to associate with the Optical configuration.

Camera setting A list of the current camera properties appears on the right. It is being updated dynamically.

If you want to use stored ROIs for Camera ROI setting (turn ROI on/off and use the stored ROI value), tick "Use Stored ROI" checkbox in the Camera features box.

Channel setup These settings determine how channels of newly captured images will be named and what color will be assigned to them. The available properties depends on the current camera setup (color/mono). In the mono camera mode, you can either assign the name, the emission length and color to the channel Manually , or leave this task to NIS-Elements D (the Automatically option). In such case, information of the light path (emission wavelength) will be used to determine the channel name and color.

Microscope setting If there is more than one shutter available and you would like to associate a shutter with the optical configuration, select which one is the Active Shutter from the pull-down menu. Select which parts of the microscope shall be included in the configuration by checking them in the Used devices dialog box.

## Note

Active shutters remember their aperture setting and display it in the Microscope setting section.

Objective An objective mounted to a motorized nosepiece can be included in the configuration. Select the objective from the pull-down menu. Objectives which are currently assigned to any position of the nosepiece are listed. See 4.1.3. Objectives [42].

## Note

The objective must be assigned to a nosepiece position via the microscope control pad or the nosepiece control panel beforehand.

- 5) If some of the device settings still need to be adjusted, click the Camera &amp; Devices Controls button and select the appropriate control panel from the pull-down menu. Adjust the settings within the control panel, the optical configuration will be updated automatically.
- 6) Click Finish to save the new optical configuration and to close the window.
- 7) You can create more optical configurations by repeating the procedure. The optical configurations are saved to registry immediately. A backup of optical configurations can be made by running the Calibration &gt; Optical Configurations command and clicking the Export button.

## Managing Optical Configurations

To display the optical configurations manager window, run the Calibration &gt; Optical Configurations command. You can make the following actions from the window:

- · Create, duplicate, rename, delete, copy settings and switch between optical configurations.
- · Modify optical configuration properties.
- · Import and export optical configurations to/from an XML file.

## Operations with Optical Configurations

Once created, the configuration appears in the list and can be shared with other users by changing the Private option to Shared (see 2.2. User Rights [11]). The following operations can be performed on the selected configuration:

- · It can be deleted by pressing the Remove button. A confirmation dialog box appears.
- · Its name can be changed by the Rename button. A button with the configuration name appears in the tool bar (if the Show on toolbar option is selected).
- · The configuration settings may be transferred to another optical configuration by the Copy to button. Press the button and select the optical configuration to be overwritten with the current one.
- · A copy of the configuration can be made via the Duplicate button.

- · The configuration can be applied to by the Set As Active button.
- · The settings of all optical configurations can be exported to an external XML file using the Export button.
- · The previously exported optical configurations settings can be loaded from the XML file via the Import button.
- · The list of optical configurations can be ordered manually using the arrow-up and arrow-down buttons.
- · Each configuration can be arbitrary modified within the right-side portion of the window.

The optical configuration buttons are available in the main tool bar when Show on toolbar option was selected during the setting process.

## 4.1.3. Objectives

If you want to perform measurements on captured images it is wise to calibrate all objectives used to capture images. Whenever an image is captured through a calibrated objective, the image inherits its calibration.

## 4.1.3.1. Managing Objectives

Run the Calibration &gt; Objectives command. The Objectives window appears:

<!-- image -->

A list of used objectives can be created within the Objectives window. For each objective, the objective name, position in the changer, storage status and the calibration are displayed. A Calculator icon next to the calibration value indicates that the calibration has been calculated from objective properties.

If the calculator icon is missing, the calibration has been performed manually. Use the buttons on the right side to manage the objectives:

Insert Click the button and select one of the objectives from the database (ordered by magnification). Custom objectives can be added to the database via an INI file.

New Press this button to create a custom objective. The new objective will be added to the list. Then, define the Main properties and the Physical properties of the objective.

Duplicate If zoom is used, the objective calibration must be re-calculated accordingly. Use this button to make a copy of the objective and define the zoom factor in the window which opens.

Remove This button deletes the selected objective.

Recalibrate Starts the calibration of the selected objective. See 4.1.3.3. Objective Calibration [43].

Export Enables you to export the complete list of objectives to an XML file. The standard Save As window appears.

Import This button enables you to import a complete list of objectives from an external XML file previously created by the Export button.

Current Unit This button invokes a pull-down menu where units for the whole application can be selected.

<!-- image -->

Help Displays a help page to the Calibration &gt; Objectives command.

Edit the properties of the selected objective in the bottom part of the window. Press the Close button to finish this window.

## 4.1.3.2. Assigning Objective to a Nosepiece Position

- 1. To assign an objective to a position or to change an attached objective assignment, click the setup button in the nosepiece section of the microscope control pad.
- 2. A window appears which enables you to select one of the available objectives to the corresponding position.
- 3. Each objective has its specifications displayed in the table. These specifications are not editable.

## 4.1.3.3. Objective Calibration

After you press the Recalibrate button in the Objectives window or when creating a new custom objective, the following window appears:

<!-- image -->

Select one of the calibration methods:

- · The Manual calibration lets you draw a distance into a picture and assign real length to it (see below).
- · If a motorized XY stage is available, the Auto and 4 points automatic methods appear.

Press OK to continue...

## Manual Calibration

- 1) When performing a manual calibration, the live image starts automatically and the following window appears:

<!-- image -->

- 2) Select one of the icons to draw a distance to the image. If you know the precise calibration value (px/unit), press the Pixel Size button to enter the real size of one pixel:

<!-- image -->

Enter the calibration value, select units, and confirm the calibration by OK . If you do not know the pixel size, you will have to continue with the calibration on live image:

- 3) Insert a calibration slide to the microscope stage.
- 4) The distance is defined by placing lines (Horizontal, Vertical, Parallel) to the image. Choose the orientation of the lines by pressing the appropriate button.

## Note

If you are sure the camera angle is 0, 90, 180, or 270º, it is recommended to select either vertical or horizontal lines. Otherwise, select the parallel lines.

- 5) Click into the image to place the first line. Place the second line in the intended position by another click.

## Note

You can modify the line position while holding the mouse button. After you release the button no further changes can be made. When 'Parallel lines' were selected, draw the first line by clicking twice inside the image. The line can be moved and adjusted arbitrary by mouse. When satisfied, finish the first line by right-click. The second line can be placed by another click to the image, this time only to adjust the distance from the first line. The process is completed by right-click.

- 6) The following dialog box appears:

<!-- image -->

- 7) Enter the distance between the two lines and select correct units.
- 8) Press OK . The objective is calibrated now.

## Automatic Calibration

The automatic calibration requires a motorized stage. Select one of the following methods:

Auto The Auto method is fully automatic. Calibration is performed on a part of the live image marked by red square that is shown before the calibration is launched. You can also choose the channel to be used by auto-calibration.

Figure 4.7. Auto-calibration window

<!-- image -->

NIS-Elements D moves the motorized stage, acquires two images, and calculates the calibration from the shift of the images. The auto-calibration performs an estimation of the real relay lens zoom factor. If the estimation does not match the value specified within the optical path window, a warning appears.

<!-- image -->

It is recommended to cancel the auto calibration (click No ), check the real zoom factor of your relay lens and check and correct the relay lens settings within the Acquire &gt; Camera Light Path command window.

Note

The success of this method depends on the texture of the specimen, its contrast, illumination, etc. If the combination of these factors is unsuitable, the auto calibration may fail. If it fails, try the following:

- · Move the stage to another area of the specimen to get a better texture.
- · Improve contrast by setting LUTs.
- · Check focus, re-focus if needed.
- · Turn on the Acquire &gt; Shading Correction &gt; Shading Correction command ON.

4 points If you select the 4 points method, the system draws four points on the screen (subsequently) and asks user to move one significant part of the specimen to each position. After all four steps are completed, the calibration is calculated from the moves of the stage.

## Superresolution Calibration

This type of calibration is available after successful manual or automatic calibration. It triples the camera's resolution and uses fine stage movements to improve the resulting objective calibration. Click the Run SR Calibration button and wait till the objective calibrates.

## Calibrate Using Objective

When you have an uncalibrated image, you can use an already calibrated objective to calibrate it. Rightclick the Uncalibrated field on the image status bar and choose one of the objectives from the Calibrate using Objective sub-menu. Of course, the same objective which was used to capture the image shall be selected.

## 4.1.4. Connecting a Device to NIS-Elements

Before you get to work with NIS-Elements D , all hardware accessories should be connected properly to the system. In most cases, the following basic procedure is sufficient to connect a device successfully:

- 1. Install NIS-Elements D , and select the appropriate device(s) during the installation.
- 2. Connect the device to the PC and switch the device ON.
- 3. Run NIS-Elements D , and run the Devices &gt; Manage devices command to open the Device Manager.
- 4. Use the Add button to add the device to NIS-Elements D .
- 5. Select the device from the list of installed devices and press the Connect button.
- 6. Select logical devices to be activated.
- 7. Configure device-specific settings using the Configure (physical) Device and the (logical) Device Parameters buttons.
- 8. Close the Device Manager.

Note

MULTIZOOMAZ100M,ECLIPSELVseries, ECLIPSE MA200, or ECLIPSE L200N/300N microscopes can not be connected from NIS-Elements D while the setup tool of each microscope is active. To

connect any of these microscopes to NIS-Elements D, exit the setup tool and then run the NISElements D.

## Renaming of devices

Either logical or physical device can be renamed by user. Just right-click the device name and select the Rename Device command from the context menu. The user-defined names can be handy in two cases:

- · You are using two logical devices having matching names, but you need to uniquely identify them (e.g. from macro).
- · You are used to call a device with another name and would like to rename it in order not to be confused by the predefined name any more.

## 4.1.5. What are 'Logical Devices'?

NIS-Elements D handles hardware accessories using the concept of logical devices. There are features of different hardware devices which equal and therefore can be controlled equally. Such features are called 'logical devices'. A typical logical device is Stage XY . Different microscopes can be equipped with different XY motorized stages, although - regarding the user interface - they behave equally. One physical device (a piece of hardware) can contain one or more logical devices the list of which appear in the Device Manager after the connection is established.

## Available Logical Devices

Analyzer The analyzer is a polarizing filter placed in the optical path between the specimen and the lamp. The logical device offers two states: ON (inserted) and OFF (extracted).

Aperture This logical device is used for controlling apertures in the light path. It is used in complex microscopes rather than as a standalone device. Two parameters can be typically set for aperture devices, the state (ON/OFF) and aperture size.

Condenser A condenser is a two-lens combination located next to the illumination source in the optical path. Its purpose is to collect light and direct it to the specimen being examined. The corresponding logical device relates to a changer of different condensers.

Filter This logical device controls filter changer movements. There can be several filter changers connected to NIS-Elements D at a time. Each filter changer needs to be set up - filter types shall be assigned to positions of the changer:

- 1. Display the filter changer control panel ( Devices &gt; Filters and shutters or Devices &gt; Microscope Control Pad ).
- 2. Click the settings button , a window appears.
- 3. Select one of the available positions which the filter will be assigned to.
- 4. Click the ... button, a list of available filters appears.

- 5. Select the filter name from the list and confirm it by OK.
- 6. The filters can be moved within the already defined positions using the Up/Down arrow buttons.

## Note

When browsing the list of filters, details about the currently selected filter are displayed on the right side of the window.

Illuminator This logical device is used for controlling the specimen illumination remotely. There is no standard dialog box for the illuminator control. Each device handles this logical device via a user interface specially designed for it - typically containing one button for switching it ON/OFF and a slider for regulating intensity.

Light Path Some microscopes have more than one port where it is possible to attach a light source or a camera. This logical device can switch the illumination between these ports.

Microscope This logical device is used to group standalone logical devices used in certain microscopes. To control the logical devices of a microscope from one control panel, select the Devices &gt; Microscope Control Pad command.

Nosepiece This logical device serves for controlling microscope objective changers. There can be three nosepiece types attached to a microscope:

- · Manual -it can not be controlled via the software.
- · Intelligent -the current nosepiece position is read by the application, but can not be controlled.
- · Motorized - such nosepieces can be fully controlled via the Microscope Control Pad or the Nosepiece control panel.

See 4.1.3.2. Assigning Objective to a Nosepiece Position [43] .

ND Filter A neutral-density filter is a light absorbing filter whose absorption spectrum is moderately flat. It is used to reduce the illumination intensity within the optical path. The logical device offers two states: ON (inserted) and OFF (extracted).

PFS Perfect Focus System - this logical device corresponds to the PFS physical device available with Nikon TE2000/TI microscopes.

Shutter This logical device can control shutters installed in your system. This device is handled via the Devices &gt; Filters and shutters control panel or straight from the microscope control pad. You can select the type and rename the shutter by running a contextual menu command either within the Filters &amp; Shutters control panel, Device Manager window, or in the main tool bar.

## Note

There was a restricted number of shutters which could be connected to the system in previous releases of NIS-Elements D and they were identified by Type (DIA, EPI, Aux1, etc...). The current version supports identification of shutters by custom Names, but the Type attribute can be still found in some windows (or used in some macro functions). This is to ensure backward compatibility.

Zoom This logical device is used for controlling the zoom factor. Run the Devices &gt; Zoom Configuration command to adjust the zoom settings.

Stage XY Stage XY enables the movement of specimen within X and Y axes. The system offers user to control stage movements.

Stage Z The Z Drive device enables movement throughout the Z axis direction.

## 4.1.6. XY Stages and Z Drives Tips

Please read the following tips for using motorized XY Stages and Z Drives.

## Motorized Stage Initialization

A motorized stage being initialized could strike the objective. Before initializing the stage, make sure that the objective is away from the stage. If a motorized Z drive is available, use the Devices &gt; Objective Clearance command to prevent this.

## Setting Software Limits to Stage Movement

Some microscopes enable you to reduce the range of movement of the motorized stage by setting limits within the configuration window.

- 1) Display the configuration dialog window (within the Devices &gt; Manage devices window).
- 2) Move the stage to the position where the limit shall be set.
- 3) Click the appropriate button.
- 4) Set all the limits by repeating this procedure.

Caution

This procedure can not be used if you already set some limits and would like to broaden them at the same time. NIS-Elements D will not allow you to move the stage to any out-oflimits position. What you need to do is to reset the limits within the configuration window beforehand.

## Using two independent Z Drive devices

Workstations can be equipped with two independent Z drive systems, one coarse (slow) and the other fine (fast). Typically, the first one is used for specimen manipulation in Z axis, when changing objectives, etc. , the second one is used for auto-focusing. The following text explains how NIS-Elements handle the two Z drives.

Absolute Z The current positions of both Z drives (Z1, Z2) and the absolute Z position (sum of Z1 and Z2) are displayed in the main status bar. If there is not enough space to display all these values, only the absolute Z value is displayed (Z1 and Z2 still appear in a tool-tip). The absolute Z value appears in the Z Series Setup.

## Active Z

The concept of Active Z enables user to select the preferred Z drive:

- · The active Z drive is used when performing auto-focus.
- · The Devices &gt; Enable Mouse Joystick Z in Live (*current value* µm) command applies to the active Z.

You can select the Active Z device in the Devices &gt; Mouse Joystick and Auto Focus Z: *Z Drive Name* menu.

## Regular Z drive + Piezo Z drive

If you have a regular Z drive and a Piezo Z drive installed, some functionality is added:

- · The Move Piezo Z to button is added to the Z Series Setup window when Piezo Z is selected.
- · The Devices &gt; Keeps Z position and centers Piezo Z and the Devices &gt; Move Piezo Z to Home Position commands appear in the Devices menu

The button and the Devices &gt; Keeps Z position and centers Piezo Z command provide corresponding functionality. They move the Piezo Z device to its home position, and compensate this shift by moving the second Z drive in order to maintain the absolute Z position.

## 4.1.7. Camera Settings

A digital camera mounted to a microscope port or a macro-scope stand records images of the observed scene on a light-sensitive sensor, and transfers them to a computer. NIS-Elements D supports various cameras differing from each other in resolution, frame-rate, sensor type, etc. Despite these differences, controlling different cameras is similar. The following features are included in the View &gt; Acquisition Controls &gt; *Camera* Settings window depending on a particular camera type.

## Note

The complete list of cameras and devices supported by NIS-Elements is available in a separate document.

AE Compensation In automatic exposure modes, the compensation affects how optimum exposure settings (Exposure time and Gain) are calculated. The Compensation value is expressed in Exposure Values (EV). Setting the compensation to + 1.0 EV makes the image twice brighter (e.g. doubles the Exposure time or Gain).

AELock This option makes the automatic exposure mode to lock the current exposure settings (Exposure time and Gain).

Analog Gain Controls strength of the camera analog signal before it is digitized). This setting affects image brightness.

Auto White Balance (AWB) The AWB button performs an automatic white balancing. It adjusts the red, green, and blue image components in order to get a neutral white color.

Averaging Averaging is a commonly used technique of decreasing noise in the image. In this method 2, 4, 8 or 16 consecutive frames are averaged together.

Binning The binning mode provides considerably enhanced camera chip sensitivity by integrating more elements (pixels) together. E.g.: binning x4 integrates the signal from the area of 4x4 chip elements to one pixel of the resulting image. Smaller resolutions and faster frame rates are achieved using the binning modes.

Contrast Affects dynamics of how the luminosity is rendered. There are several modes for different illumination (contrast) scene situation.

Exposure Mode, Exposure Exposure or Exposure time is the time of charge accumulation in a camera chip between two adjacent frames. Prolonging the exposure time increases brightness of the image as well as its quality (there will be less noise).

Exposure mode determines how the Exposure time is calculated. Generally, automatic and manual modes are used:

Auto Exposure, AE Calculates Exposure time and Gain in order to achieve optimal brightness of the scene. Image quality is the priority, therefore longer exposure times are being preferred. In most cases, the auto exposure can be run once by pressing the Auto Exposure button, or continuously by selecting the nearby check box.

Note

Depending on particular light conditions, the result of Auto Exposure may not be optimal for image acquisition.

## Warning

You can use one optical configuration when working with live image and switch to another optical configuration just for the image acquisition, very often, this is performed automatically i.e. by a macro command. If the 'on-acquisition' optical configuration has the Auto Exposure camera mode turned ON, it may produce over- or under-saturated images. Since the Auto Exposure algorithm estimates the optimal exposure time by analyzing several last frames, it is not able to make the estimation correctly if the change of optical configurations would cause significant change in image brightness. To prevent this, we recommend to use Manual Exposure mode in the optical configuration used for capturing.

Manual Exposure User selects both Exposure time and Gain manually.

Format - Fast (Focus), Format - Quality (Capture), Resolution Usually, cameras can provide several image resolutions. NIS-Elements D enables to create two presets of the resolution settings Fast and Quality . The formats then differ in image size, and consequently in frame rate (number of frames per second - fps). The higher the resolution is, the lower frame rate can be achieved. Available resolutions depend on the camera type.

## Note

When switching between the formats while observing the live image, the size of the image on the screen is maintained - the zoom setting is changed instead. Only in some special cases, the behavior changes and the image size is changed instead of the zoom setting which is maintained.

Gain Controls the sensitivity of a camera. Increasing the gain increases brightness of the image, but decreases quality (the more random noise, the more streaky noise and color unevenness), and increases the frame rate indirectly by enabling shorter exposure times.

Gamma The gamma correction maps the intensity of live signal exponentially to the gamma parameter. For gamma &lt; 1, dark portions of the image are enhanced whereas for gamma &gt; 1, image parts of higher intensities are enhanced.

Hue Hue shifts image colors across the rainbow.

Live Acceleration Would you like to increase the frame rate of the live signal? Move the slider to a desired multiplier. The system then automatically shortens the exposure time (so the frame rate rises), and the loss of intensity is compensated by gain (software multiplication).

Maximum Exposure This is a safeguard of the time of the Auto Exposure. For quick exposure, it is convenient not to set this value too high.

Metering Mode If this option is available, auto exposure can be calculated with an emphasis on overexposed peaks ( Peak ) or average pixel intensity ( Average ).

Offset Sets the brightness of the image. It is a constant additive (positive or negative) changing all pixel values of the image. With negative offset value the dark image areas become pure black. Considering fluorescence microscopy, an appropriate offset setting can create continuous black background and thus help to enhance (together with gain or illumination enhancement) the contrast.

Overillumination Tolerance Sets how many pixels should be white after the Auto exposure is performed. Use lower values (0.01%) for very bright (shining) objects (fluorescence). For common bright field, even 1% may be a good value. Optionally, you can define the absolute number of white pixels.

Saturation The amount of saturation determines how colors are rendered. More saturation produces richer colors. Less saturation makes the colors gray.

Scene Mode/Preset There are presets of camera settings optimized for the specific usage. You can reset the settings by the Reset button.

Asbestos Asbestos.

## Bioscience/Biological microscopy:

- B Bright field.
- D (DIC/PH) DIC or phase contrast.

E Enzyme labeled antibody method,

F (DF/FL) Dark-field fluorescence.

H Hematoxylin and Eosin stain.

HAL-Bright Field Halogen illuminated bright field.

HAL-ELA Halogen illuminated enzyme labeled antibody method.

HAL-HE Halogen illuminated Hematoxylin and eosin stain.

LED-Bright Field LED illuminated bright field.

## Industrial microscopy:

C Circuit boards.

FPD Flat panel displays.

M(Metal) Metal or ceramic.

W(Water/IC) Wafer IC-Chip.

Neutral Neutral preset.

Separate Channel Settings Having a color camera, influence of the settings described above on each color channel can be adjusted. In such case, three edit boxes with the default values set to 1.0 are displayed below the feature setting. These values determine the influence of the feature on each color channel.

Sharpness Some camera settings provide the sharpness control which affects how sharp edges in the image appear. Too much sharpness leads to over-saturated edges.

Target Maximum Intensity Restricts the maximum of image intensity after the auto exposure was applied. The value represents a percentage of the whole camera dynamic range.

Trigger Mode Sets the exposure method.

Bulb The exposure time and frames timing are controlled by external signal connected to the camera.

Internal The exposure time and the beginning of each frame acquisition is controlled by the settings in NIS-Elements .

Strobe In this mode, the beginning of each frame exposure is being controlled by external signal.

Use Current ROI The currently defined region of interest, set by the Define ROI command, can be switched ON/OFF by checking this item.

Using Probe The probe enables you to determine a small image area that serves as the data source area for LUTs, histogram etc. It also affects the AWB (auto white balance) and the AE (Auto Exposure) features of the cameras which support it. When the probe functionality is not supported, the AWB and AE algorithms are computed from the whole image.

White Balance There are usually Red, Green and Blue Gain properties that control how colors are rendered. It is used to eliminate a color cast from white areas.

## 4.1.8. Controlling Illumination Devices

<!-- image -->

The substance of an illumination device is the light source. The light emission is produced mainly by a laser, diode or a light bulb. NIS-Elements D does not distinguish between wavelength modules of these light sources and all are controlled in a similar manner. Basically you select which wavelength(s) you want to use for illumination and set its light intensity. The selected wavelength modules are turned off until you activate the shutter button usually placed in the bottom left corner of the control panel.

## 5. Image Acquisition

## 5.1. Introduction to Image Acquisition

Having NIS-Elements D installed and all hardware accessories set up, you can start capturing images. Let's begin with the simplest case.

## How to capture a single image

- 1) Turn the connected camera and other devices ON and start NIS-Elements D .
- 2) Run Acquire &gt; Camera Settings to display the Camera Settings control panel.
- 3) Switch camera to the Live-Fast mode ( Acquire &gt; Live - Fast )
- 4) Adjust resolution of the Live Fast mode to get a continuous Live image. It is recommended to set a low resolution in order to achieve high frame rates. This is good when searching the specimen or when focusing manually.
- 5) Adjust Exposure time to get a nice image of the scene.
- 6) Focus on the scene.
- 7) Optionally, turn on the camera ROI. The Define ROI button appears on the tool bar if the camera ROI function is supported by your camera. See also 5.3. Camera ROI [57].
- 8) Capture the image by running the Acquire &gt; Capture command
- 9) A new image is opened automatically and named 'Captured'.

## Tools for Handling the Live Image

Live - Quality, Ctrl + + If a high frame rate is not crucial or if you would like to view the live image exactly as it will be captured, run the Acquire &gt; Live - Quality command. It displays the live image in the Quality (Capture) resolution. This resolution is used whenever an image is captured.

- Capture, Ctrl + -When pressed, the camera exposure runs till the end of the current frame, and the next frame is captured and displayed on the screen (it is the first frame with the complete exposure after you have pressed the Capture button).

If you are using the Live-Fast mode and click Acquire &gt; Capture , NIS-Elements will automatically switch to the quality mode to capture the image. When the image is captured, it is opened on the screen in a new image window.

Freeze, The Freeze button interrupts the camera exposure, and displays the very last complete frame.

## 5.2. Shading Correction

Shading correction is a method which can correct illumination inhomogenities of the captured images. How does this work? First of all, a 'correction image' must be captured. It is an image which represents illumination intensities within the field of view. Such image is created by capturing a blank scene and can look like this:

Figure 5.1. Inhomogeneous illumination

<!-- image -->

As you see in the image, the illumination intensity is 100% in the center but gets darker near the edges. This can be corrected by applying the shading correction which will - based on the correction image equalize intensities of the resulting image:

Figure 5.2. Image acquired without the shading correction

<!-- image -->

Figure 5.3. Image acquired and corrected

<!-- image -->

The shading correction can minimize the illumination and background inhomogenities by subtracting a blank scene from the current image.

## How to setup a shading correction

- 1) Decide whether to use just a single shading correction image or different image for each optical configuration. Make the selection via the Acquire &gt; Shading Correction &gt; Shading per Optical Configuration commands.
- 2) Get the correction image. You can either acquire a new image by the Acquire &gt; Shading Correction &gt; Capture Correction Image command or use an existing one. To use some existing image, open it and call the Acquire &gt; Shading Correction &gt; Use Current Image As Shading Correction command. In both cases the correction image will be kept in memory. To view the correction image, run Acquire &gt; Shading Correction &gt; Show Correction Image .
- 3) In case of 'per optical configuration' shading correction, repeat this procedure for with each optical configuration turned ON.
- 4) The Acquire &gt; Shading Correction &gt; Shading Correction is enabled if only the correction image is available for the current acquisition settings. For example, if the Shading per Optical Configuration is chosen but the correction image for the current OC has not been captured yet, the Acquire &gt; Shading Correction &gt; Shading Correction stays disabled.

## 5.3. Camera ROI

You can specify a camera ROI on a live image by selecting the Acquire &gt; Camera ROI &gt; Define ROI command. The live image is then restricted to the defined area whenever the ROI button is pressed.

Figure 5.4. Turn Camera ROI ON/OFF

<!-- image -->

The camera ROI can be also saved to a file for later use. This can be done by the Acquire &gt; Camera ROI &gt; Save ROI command. When the time comes, load the saved camera ROI by the Acquire &gt; Camera ROI &gt; Load ROI command. The current ROI will be overwritten.

The same Define ROI button appears in the toolbar of a captured image too. It does not matter whether you define the ROI on the captured or live image, the setting is shared.

## Camera ROI Definition

- 1) Run Acquire &gt; Camera ROI &gt; Define ROI . The following window appears:

<!-- image -->

- 2) A ROI frame appears in the image at the same time. You can either change ROI dimensions or/and position using a mouse cursor, or you can enter precise numerical values in the dialog window.
- 3) If you would like the ROI to be placed in the center of the camera chip, click Center ROI . The ROI will move to the center of the live image.
- 4) Confirm the action by the OK button.

Note

NIS-Elements may adjust the ROI size automatically after the user sets it. Such automatic adjustment is needed in order for the ROI to work in different resolutions of the Live Fast and Quality Capture formats.

Caution

Nikon DS cameras have fixed-sized camera ROI, therefore width and height of the ROI cannot be changed. Only its position can be adjusted within this window.

## Predefined Camera ROI

If you are using Andor Neo/Zyla or Hamamatsu Flash 4.0, 2.8, you can choose the Predefined Camera ROI in the ROI pull down menu, offering several predefined frame sizes.

<!-- image -->

## 5.4. About ND Acquisition

NIS-Elements D being a multi-purpose imaging system can be used as a handy tool to study objects, live organisms, processes, etc. The universal ND2(N-dimensional) file format is what makes this possible. One ND2 file can contain multiple images organized according to what type of acquisition they came from. There are the following acquisition types:

## Note

Each acquisition type gives a name to the corresponding dimension of the resulting ND2 file. For example, we can speak about two-dimensional TZ ND2 file, which means the file contains the Timelapse dimension and the Z-series dimension.

Time-lapse - T A sequence of images can be captured over a period of time and create a time-lapse image. See 5.5. Time-lapse Acquisition [60].

Multi-point - XY Images from different areas of the slide can be acquired. See 5.6. Multi-point Acquisition [63].

Z-series - Z Several techniques utilize Z-stacks of images. Such Z-stack can be for example converted to a 3D model of the specimen. See 5.7. Z-series Acquisition [66].

- · Single-dimensional documents can be created automatically (using motorized accessories) or manually using commands from the Acquire menu.

## Common ND Experiment Options

The following options can be applied to all types of ND experiments:

Experiment You can enter a custom name of the experiment. Also name of the phase is editable.

Path Browse to a folder where your ND2 images will be stored.

## Custom Metadata (requires:Local Option)

Check this option to add custom metadata. The created metadata can be changed after acquisition. Display image properties ( File &gt; Image Properties ), display the Custom Metadata tab and click the Modify Description button.

Auto Focus Automatic focusing can be used during the experiment. You can select the auto-focus method that best meets your needs. The Define button shows a window where you can define parameters of the selected focusing method.

## Note

If the auto-focus is set to be performed Before each Phase and the ND Experiment contains just a single time phase, the automatic focus will not be performed. To run auto focus, use the At the Beginning option.

Closing Shutter The active shutter can be closed between single image acquisitions. Just select the Close active Shutter... option in the experiment window.

Running Macro Commands You can define a command (or a macro) to be run in various stages of the experiment. Select the timing in the Advanced section of the experiment window and enter the command to be run.

Load Use this button to for a configuration XML file to be loaded. The file with the current configuration can be created by the Save button.

Save Click this button to save the current configuration of this dialog to an XML file. A standard Save As window appears.

## ND Sequence Options

The following options can be applied to time, multipoint and multichannel sequences in ND experiments:

- New This button adds new step into the sequence.
- Select All Use this button to select all steps in the sequence.
- Clear Selection Use this button to clear all steps selection.
- Move Up, Move Down These buttons moves the current step up/down in the sequence.
- Remove Current This button removes current step from the sequence.
- Remove All This button removes all steps from the sequence.

## 5.5. Time-lapse Acquisition

Detailed studying of long-lasting processes is enabled by the time lapse acquisition mode of NIS-Elements D . The achievable experiment duration is limited by the hardware abilities of your PC only. Invoke the Acquire &gt; Capture Timelapse &gt; Capture Automatically command to set the experiment up:

<!-- image -->

The Time schedule table enables you to define one time phase where duration, interval between single images, and number of images of the phase can be adjusted. The Interval , Duration , and Loops settings are bound together, so you just need to set two of these parameters. The remaining parameter is calculated automatically.

The flag mark indicates the Duration/Loops priority. For example: if the camera exposure time exceeds the defined Interval between frames, than the experiment settings are not achievable - only the marked column will be pushed to be correct. You can set the priority column by clicking on its caption.

## Special Options

The following options can be used with this type of ND acquisition. Options common to all types are described here.

Switch Transmitted Illuminator off When Idle If this option is selected, the lamp is turned off whenever there is a long-enough gap between two acquisitions.

## Warning

It takes a little time for some lamps to reach the set intensity. In such case, we recommend to use the Wait(); macro function before the capture is performed.

Events Press the Events...

button to display the following window:

<!-- image -->

Define user hot keys which run user events during time-lapse acquisition. Simply click inside the Hot key field of the User events window and press any key combination you want to assign to the event. Then you can enter the event description. A macro command can be specified which will be executed when the event occurs (triggered by user). When the event occurs, the specified command is run and a marker is placed to the image sequence.

## 5.5.1. Timing Explanation

When performing fast Time-lapse acquisition (capturing images in short intervals), it is important to understand how the acquisition with digital camera works.

Case #1: No delay If the interval in the experiment is set to "No delay", the camera runs in "internal hardware trigger mode" (i.e.: Timed mode, Streaming mode). The camera sends maximum frames to the computer. This may result in a situation where the computer is not capable of receiving all the frames the camera sends. If so, depending on the camera type, the overflowing frames may be omitted.

Case #2: Interval is too short The time needed to receive one frame consists of three phases: exposure time, readout time and software overhead delay.

<!-- image -->

## Legend:

- 1. exposure time
- 2. readout time
- 3. camera sends data to PC
- 4. software overhead time
- 5. specified interval
- 6. resulting interval

The camera runs in a "software triggered mode" where it gives the frames much slower than in "no delay" because it is being synchronized with other events. In this case it is synchronized with timing of the timelapse acquisition. If the interval between frames is set to a shorter time than is the sum of the three phases (e.g. 50 msec), some latency will occur. As a result, the interval in the image sequence is prolonged to (exposure time + readout time + SW overhead).

Case#3: Interval is sufficient The camera runs in a "software triggered mode". If the interval is sufficient, the timing in the resulting image sequence will equal the timing specified within the acquisition window.

<!-- image -->

## Legend:

- 1. exposure time
- 2. readout time
- 3. camera sends data to PC
- 4. software overhead time
- 5. specified interval

## 5.6. Multi-point Acquisition

This window serves for defining XY(Z) points to be scanned during the multipoint capture experiment. This feature is available when a motorized stage XY(Z) is present in the system. Check the Include Z box to display the Z column. The list of defined points can be saved (and loaded later) to an XML file by the Save ( Load ) button. Run the Acquire &gt; Capture Multipoint &gt; Capture Automatically command.

## 5.6.1. Point by Point (Manual) Multi-Point

- 1. Move the stage to the first position.
- 2. Press the Add New button. A new line containing current coordinates of the stage appears in the list.
- 3. Move to the next position and repeat the steps until you have all the intended points defined.

## 5.6.2. Well Plate (Rectangular) Multi-Point

You can insert a pattern designed to cover a wellplate. Of course it can be used to create any rectangular pattern.

- 1) Click the Custom button. The following window appears
- 2) Select Manual if you know the distances between wells. Otherwise select the Interactive and continue.

Manual This method will create a pattern which will scan Rows x Columns fields. The Distance X and Y parameters specify distances between two fields. The scanning will begin at the current position.

Interactive The interactive method lets you specify the number of fields to be scanned and starts a wizard where you will specify the top-left and the bottom-right corner of the well plate. The distances between wells are calculated automatically.

## 3) Click Finish .

## 5.6.3. Large Image (Covering) Multi-Point

A Multi-point which will cover certain area can be created:

- 1) Click the Custom button and select the Large Image tab
- 2) Set the large image settings:

Scan Area Select whether to define the Scan Area by number of fields or the actual field size.

Camera Select the camera to be used. This field is enabled only if you have a dual-camera setup.

Objective Select the objective for which the multi-point will be calculated. The resulting number of fields / area size changes depending on the selected objective magnification.

Overlap Overlap of neighboring images in %.

- 3) Click Finish .

## 5.6.4. Random Multi-Point

(requires:Local Option)

Specify the area where a random set of points will be generated.

- 1) Click the Custom button and select the Random tab.
- 2) Select shape of the area to be filled with random points

Rectangle The area will be defined by a rectangle. Define X and Y coordinates of left top corner of the area, width and height of the area.

Radius The area will be defined by a circle. Define X and Y coordinates of center of the circle.

- 3) Specify Number of points in the multi-point set.
- 4) Click Finish .

## 5.6.5. To Change a Single Z Coordinate:

- 1. Make sure the Move stage to selected point is pressed. This button ensures that the motorized stage moves to the coordinates of the currently selected point.
- 2. Click inside the line you would like to change.
- 3. Move the Z drive to the new position.
- 4. Click the &lt;-button.

Note

The XY coordinates of one point cannot be adjusted (unless you delete it and add a new point).

## 5.6.6. Special Options

Autofocus None, Steps in Range, Steps in Continuous.

Custom Displays a tool for creating predefined multi-point patterns.

See 5.6.2. Well Plate (Rectangular) Multi-Point [63], 5.6.3. Large Image (Covering) Multi-Point [64], 5.6.4. Random Multi-Point [64].

Execute Command after Capture You can either Run Macro, or select a command from the Command list. The command is executed after capturing.

Execute Command before Capture You can either Run Macro, or select a command from the Command list. The command is executed before capturing.

Include Z If selected, also the Z coordinate will be taken into account during XY(Z) acquisition.

Note

This option is disabled if the Relative XY option is used.

Leave PFS offset ON between points Check this item to keep PFS on while moving between the points.

Move Stage to Selected Point This button ensures that the motorized stage moves to the coordinates of the currently selected point.

## Offset All

The offset all button can shift the XY coordinates of all points in the same way:

- 1. Make sure the Move stage to selected point is pressed. This button ensures that the motorized stage moves to the coordinates of the currently selected point.
- 2. Select one point of the list.
- 3. Move the XY(Z) stage to a new position (define the offset).
- 4. Press the Offset All button.
- 5. The coordinates of all points change - the same shift which you made with the stage is applied to them.

Optimize If the Optimize button is pressed, the system will re-order the defined points in order to minimize the XY stage trajectory.

Point name Displays the name of the point. You can change the name (default names are #1, #2 #3, etc.).

Redefine reference Z after Auto Focus/PFS Check this option to redefine reference Z position after performing autofocus or PFS (if AF or PFS is turned on).

Relative XY Check the Relative XY item to consider all coordinates as relative with respect to the current stage position. Any of the points may be used as the reference point, just right-click it and select Set this point as a reference position .

Use Focus Surface Uses Focus Surface for capturing.

X, Y, Z Displays X, Y and Z coordinates of the point. The arrow button assign current position of Z stage to the point. The Offset All Points item shifts the X and Y (Z) coordinate of all points in the same offset which is defined as a difference between current stage coordinate and coordinate of the current point.

## 5.7. Z-series Acquisition

Automatic capturing of images from different focal planes using a motorized Z drive can be performed. Run the Acquire &gt; Capture Z-Series &gt; Capture Automatically command to display the setup window. There are three different approaches of how to set the experiment:

## Top and Bottom, Step

<!-- image -->

- 1) Press the button, the cube turns blue.
- 2) Run the Live camera signal. In case you have two Z drives, select the Z device from the pull-down menu.
- 3) Set the Z range: move the Z drive to the top position and press the Top button, move it to the bottom position and press the Bottom button.

- 4) Define the Step size in µm or the number of steps to be captured.

Note

In this mode the Home position is assigned automatically to the middle step (e.g. the third step out of the whole 5 steps). The Reset button discards the Top, Home, and Bottom positions settings.

Depending on the direction of Z-acquisition, the last Z position (top or bottom) may slightly differ from the user setting. However, you can select which position will be preserved exactly. Right-click one of the Top/Bottom buttons and select Keep exact Bottom/Top Position. The setting is indicated by underlining the button text.

## Home Position, Range

- 1) Press one of the following buttons, the cube turns yellow. The range is defined by the home-position and the scanning range:

<!-- image -->

<!-- image -->

Symmetric mode Define the Range by inserting a value in µm.

Asymmetric mode The range is specified by two values, Below - the distance below the home position, and Above -the distance above the home position.

The Relative button resets the Home position value and the Z range is calculated relatively.

- 2) Run the Live camera signal. In case you have two Z drives, select the Z device from the pull-down menu.
- 3) Move the Z drive to the position which you would like the Z drive to move around. Press the Home button to define the home position.
- 4) Specify the scanning Range .
- 5) Define the Step size in µm or the number of steps to be captured.

Note

When you set the Home Position in the Top/Bottom or Symmetric mode, its value is kept after switching to the Asymmetric mode.

## Special Options

Piezo Z If a Piezo Z drive device is connected, the Piezo button appears in the panel. Use the pull-down menu to select the action which will be performed upon pressing the button:

<!-- image -->

Keeps Z position and centers Piezo Z This option moves the Piezo Z drive to the home position, but compensates the movement by the second Z drive in order to keep the original absolute Z position(sum of Z1 and Z2).

Move Piezo Z to Home position Moves the Piezo Z drive to the home position regardless of the absolute Z drive position.

Direction You can define the Z-stack scanning direction - either from Top to Bottom , or vice versa ( Bottom to Top ).

Two Z devices Two Z devices (Main Z + Piezo Z) can be used for Z-Series acquisition and Autofocus task in Jobs. Z device combination is used automatically if AF/Z-Stack range exceeds the range of Piezo Z. Combining two Z devices speeds up the Z stack acquisition, however the user can still decide whether or not to use the Z device combination. Only the Main Z device is used if it is selected in the Z device combo box. Only the Piezo Z device is used if it is selected in the Z device combo box and the defined Range is within the device range. Combination of both Main Z and Piezo Z is used if Piezo Z is selected in the Z device combo box and the defined Range is bigger than the device range.

## 6. Displaying Images

## 6.1. Opening Image Files

NIS-Elements D offers several ways to open an image file, using either:

The File &gt; Open command To invoke the Open dialog box where you can select the file to be opened, run the File &gt; Open command. This command is also called when you click the Open button on the main tool bar

Organizer An image can be opened by double clicking its filename within Organizer . Run the View &gt; Organizer Layout command F10 to switch to the Organizer. See the 6.7. Organizer [84].

Recent Files List You can quickly access the last opened images using the File &gt; Recent Files menu.

Open next/previous/first/last Commands These commands enable you to continuously open the subsequent images from a particular directory or a database table. The File &gt; Open/Save Next &gt; Open Previous , File &gt; Open/Save Next &gt; Open Next , File &gt; Open/Save Next &gt; Open First , File &gt; Open/Save Next &gt; Open Last commands may be used.

Auto Capture Folder The Auto Capture Folder is a control panel that can be displayed by calling the View &gt; Acquisition Controls &gt; Auto Capture Folder command. It displays images within a selected folder.

To change the folder click the button in the top left corner of the control panel and browse for another folder. Any image of this folder can be opened by a double-click.

Any File Manager During installation, NIS-Elements D creates file associations to files that are considered its native format for storing images (JPEG2000 , ND2). The JPEG2000 (JP2) and ND2 image files can be then opened in NIS-Elements D just by double clicking their names within any file manager or the desktop.

## 6.1.1. Switching Between Loaded Images

Commands for managing the opened images are grouped in the Window menu. The recently opened files are listed in its bottom part. The currently displayed image is indicated by the selected radio button. To change the current image, select it from the list or use the Next or the Previous commands (represented by Ctrl + Tab and Ctrl + Shift + Tab shortcuts).

<!-- image -->

## 6.1.2. Options for the Open Next Command

This window enables you to configure the File &gt; Open/Save Next &gt; Open Next command properties.

Run the Edit &gt; Options command and switch to the Open Next tab.

## Open from file

Directory Specifies the directory with files to open.

Files of Type Filters the files to open by the image format.

Order By This pull-down menu enables you to select one of the image properties as the ordering criterion. The button toggles the alphabetical order.

Prefix Filters the files to open by prefix. You can click to show advanced filtering options window.

The button turns the advanced filter on/off.

Next file Defines the name of the file that will be automatically opened after pressing OK. You can see its name on the right side of the box.

Open from Database These options equals the ones described above.

Limit Number of Image Limit the number of documents, which will be opened and accessible in the Opened Images tab. The maximum is 24 opened documents.

Defaults for this Page Pressing this button restores the default settings of this window. All your changes will be lost.

OK Confirms all the changes and closes the window.

Apply Saves the changes which are applied, bud the window remains opened.

Cancel Discards all the changes and closes the window.

Help Displays relevant help page.

## 6.2. Image Layers

## 6.2.1. Introduction to Image Layers

The following image layers can be saved within a NIS-Elements D image.

<!-- image -->

Annotation layer In this layer, vector objects are stored. The results of manual and automatic measurements, text labels and other annotations can be included.

Binary layer(s) The binary layer is usually the result of thresholding. By thresholding, you distinguish objects of interest from background. A picture of night sky can make a nice example - shining stars may be 'thresholded' and compose the binary layer. Then, by means of automatic measurement, you can e.g. count them. More than one binary layer can be placed over one image. (requires:Automatic Measurement)

ROI layer ROIs (regions of interest) is a strong tool for distinguishing objects from background similar to the binary layer. The advantage over the binary layer is that ROIs are vector objects and therefore provide different way of manipulation. See 7.6. Regions of Interest - ROIs [112].

Color layer The color layer contains the image data captured by a camera. It can handle images with the depth of up to 16 bits per color component. The dimensions of this layer determines the dimensions of the other layers.

Note

Whensaving an image, only some file formats are capable of saving all the layers. The other image formats will save the content of the color layer only. See 6.11. Supported Image Formats [94].

## 6.2.2. Image Types

## RGB Images

Images acquired by a color camera typically consist of three components that represent red, green and blue channel intensities. You can display a single color channel using the tabs located in the bottomleft corner of the image window. Or, an arbitrary combination of them can be selected while holding the Ctrl key down.

<!-- image -->

## Multi-channel Images

These documents usually arise from fluorescence microscopy. Instead of 3 color components (RGB), multichannel images can be composed of arbitrary number of user-definable color channels.

Note

If there is a image that contains more than 8 components, the tabs in the bottom left corner of the image are replaced by the wavelength dimension, similarly to how other dimension loops of nd2 files are displayed.

Please see 6.3. Navigation in ND2 Files [74], 5.4. About ND Acquisition [59]

## 6.2.3. Displaying Image Layers

- · Single channels and monochromatic images can be displayed using a predefined color scale. Right click the 'channel tab' in the bottom left corner of image window and select a color scale from the Channel Color for... sub-menu.

<!-- image -->

- · Over-saturated and under-saturated pixels may be highlighted in the image. Color of these pixels may be selected from the context menu of the Pixel Saturation Indication button. The button is placed on image tool-bar. Select one of the following options for each group of pixels referring to Oversaturated and Undersaturated pixels:

<!-- image -->

None The pixel saturation will not be indicated.

Take color from channel tab Color which has been assigned to each channel will be used for display. See 6.2.4. Assigning Colors to Channels [73].

Complementary color Colors complementary to the display color of each channel will be used in order to ensure good visibility of the highlighted pixels.

'Color Name' Several basic colors are pre-selected in the menu.

You can turn the saturation indication ON and OFF by clicking the button.

## 6.2.4. Assigning Colors to Channels

Despite the color in which a channel is displayed, other per-channel colors can be assigned to it. This regards colors for:

- · Indication of over-saturated pixels (the color will be used with the Take color from channel tab option).
- · Indication of under-saturated pixels (the color will be used with the Take color from channel tab option).
- · Display of a binary layer 'attached' to a particular channel. (the color will be used until the binary layer is detached from the channel).

To select these colors for each channel, right-click the channel tab and select it from the Colors for '...' sub-menu.

<!-- image -->

## 6.2.5. Copying Channels by Drag and Drop

Drag one of the channel tabs and drop it to the left portion of the image window in order to create a new image.

Note

- · Even the All and RGB tab can be copied.
- · When extracting a channel from Live image, it does not freeze the camera signal.

## 6.3. Navigation in ND2 Files

## 6.3.1. Control Bar

When an ND2 file is opened, its structure is pictured at the bottom of the image window. There is a time line with all captured images indicated by gray markers. The blue-highlighted marker indicates the currently observed image. Below the time line, loops of each dimension are indicated by rectangles. In case the multi-channel dimension is included and the number of channels does not exceed 10, the channels are indicated by the color tabs at the very bottom of the image window.

Browse the nd2 file by clicking inside the time line. You can also display a single loop by selecting the corresponding blue rectangle. There are some examples, how the nd2 file control bar can look like in different cases:

Figure 6.7. A T/Z/multi-channel image.Figure 6.8. A multi-channel image containing 11 channels

<!-- image -->

<!-- image -->

## Playing Controls

Play Sequence Plays all images of the dimension at selected speed. If a selection is applied, only the selected images will be included in the playback.

- Stop Playing Stops playing the sequence at the last displayed frame.

- Previous Position Displays the previous frame of the dimension.
- Next Position Displays the next image of the dimension.
- Decrease/Increase Playing Speed Changes the playback speed by one step down/up
- Real Time Playing Speed Sets the playing speed to real-time (as the image was captured).
- Maximum Playing Speed for Every Frame Sets the playing speed to maximum while the display of every frame is guaranteed (when the speed is set to maximum by the + button, some frames are usually omitted when playing the sequence depending on your graphic card).
- Home Position Displays the frame of the Z dimension that was set as 'home' during the acquisition.

## Tips

- · Right-click the selection to invoke a context menu. The selection can be adjusted, deleted, or the nd2 file can be cropped.
- · Detailed info about dimensions will be displayed after you click the leftmost button of the control bar (T&gt;, Z&gt;, ...).
- · Place the cursor over one of the dimensions. A tool-tip which displays statistics of the dimension appears.

## Playing options

Right click the speed bar to display the following context menu and select the playing mode.

<!-- image -->

Backward selects the direction of playing the image sequence. When you check the Stop on Events

option and then press the Play Sequence button, a dialog window appears once the first user event is reached. The dialog window displays information about the reached user event. Use the Continue button to continue playing to the next event, or press the Stop button to stop the playback at the current frame. Within the window, you can also select the Do not ask again in this session (Always stop) option, the playing will stop automatically on every user event but the window will not appear. Repeat command

sets the repetitive infinite playback. Fast Advance command corresponds to the Maximum Playing

Speed for Every Frame button described above. Real Time command corresponds to the Real Time Playing Speed button described above.

## 6.4. ND Views

There are several views which can display the nd2 files in various ways. Some views are available for some dimensions only. If a view is available for two or three dimensions of the nd2 file, a pull-down menu appears in the top image tool bar. There you can select the dimension to be displayed.

## Note

When you switch the view, a new image window opens by default. This behavior can be changed within the Edit &gt; Options command window so that only one view of an image will be opened at a time.

- Main View When you open an ND2 file, it opens in this view.

<!-- image -->

<!-- image -->

Slices View This view displays orthogonal XY, XZ, and YZ projections of the image sequence. (Requires Z or T dimension). (requires:Extended Depth of Focus)

Figure 6.10. Main View

<!-- image -->

Figure 6.11. Slices View (requires:Extended Depth of Focus)

<!-- image -->

## 6.4.1. ND2 Information

Information about current frame of an ND2 document or live image can be displayed using the Show NDInformation command from the image contextual menu. It displays information about current frame of the ND2 document or live image. All possible information (metadata) are displayed by default.

You can edit which information is displayed in the Label Properties dialog window: Right click the ND2 information field and select the ND Info Properties command. Use options and tools in this window to customize the display of the ND information - you can change text properties, type of displayed information, accuracy of the displayed number up to three decimal places, format of the information, duration of display and other.

## 6.5. Large Images

## 6.5.1. Opening Files in Progressive Mode

If a single image (or one ND2 frame) is too big and it can not be loaded to RAM in one piece - you will be asked whether to open it in a Progressive Mode . This means that only a thumbnail of the image will be loaded to the RAM. When zooming-in to view image details, the image data of the particular portion of the image will be loaded to RAM progressively (piece by piece).

Many image processing functions and commands are disabled in this mode. This problem usually occurs with Large Images created by stitching several frames together. In case you need to process such an image, a smooth solution is to split it into tiles and create a multi-point ND2 file out of it. Please see 6.5.2. Splitting Large Images [78].

## 6.5.2. Splitting Large Images

You can split an existing large image to tiles easily.

- 1) Open the large image to be split.
- 2) Run the Image &gt; Split Image command. A dialog window appears.
- 3) Set split options:

Split to separate files - output format Select the output format (ND2 or TIFF). A separate file will be saved for each tile. Define Output folder and Prefix where the files will be saved.

Create multipoint ND Document Only one multi-point ND2 file will be created and opened after the split.

Tile Size, Number of tiles Define width and height of a single tile in pixels or set the number of columns and rows to which to split.

Overlap Set overlap value of neighboring tiles either in % or the current calibration units (presumably µm). Overlap up to 50% of the tile size is allowed, higher values are reduced to the maximum

.

Fill background Select a color to fill empty spaces which will appear the total area of tiles exceeds the image. Use the Optimize button to prevent the empty spaces.

- 4) If you do not require the tiles to have exact size, click the Optimize button. The system will arrange/resize the tiles automatically so that the whole image is covered precisely.
- 5) Click OK.

## 6.5.3. Locating XY Positions Between Images

If two images have matching XY coordinates you can locate the exact position in one image inside the other. This would be the case especially after using the Image &gt; Split Image command. Right click the location within the first (multi-point) image and select Find this Point in Paired Document from the context menu.

If you do this right after splitting the large image (the two images are 'paired'), the system displays it and highlights the XY position by a flashing cross. If it is not clear to the system which images shall be paired (e.g. three or more images with matching coordinates are open), the user will be prompt to select the second image to the pair.

## 6.6. LUTs (Look-Up Tables)

LUTs is a useful tool for image color and brightness modifications. You can use LUTs to enhance images for observation purposes so the color modifications will be non-destructive to the image data. LUTs settings are saved along with the image file. If required, the LUTs settings can be applied to the image data by pressing the button. Use the Show LUTs window button in the image tool bar to display the LUTs window.

The following actions are available within the LUTs window:

- · Adjusting the Gamma parameter . The gamma curve is drawn in gray over each graph. You can drag the middle point and move it up or down, or enter an exact value to the G: field at the top of the graph area.
- · Adjusting the input intensity range. The input intensity range can be restricted by moving the black and white triangular sliders to the center. All pixels with values outside of the modified input range will be set to maximum/minimum values and the remaining pixels will be approximated in order to fill the output (full) range.

Note

This is the way how images can be equalized. For example, if the image is very dark and most of the histogram is located to the left while the right part of it is flat, you may move the white slider(s) to the position where the histogram line starts to rise. This will incredibly brighten the image and reveal details which were previously hidden in a dark.

- · You can adjust the histograms height non-proportionally by moving the slider on the left side of the window up and down.

## Tips

- · Right-click the graph area and (de)select Draw trend style . When ON, the LUTs curves will be smoothed to display the data trends rather then represent the actual image data values.
- · The position of the black, white and Gamma sliders can be reset by a double click.

Different controls will be available when applying LUTs to monochromatic, RGB, multi-channel or spectral image. When LUTs are active, the LUTs button in the top-left corner of the image window is highlighted red.

## 6.6.1. LUTs on RGB Images

<!-- image -->

There are 3 separate windows for each of the RGB channels. All channels are controlled at the same time by default. To control each channel separately, press and hold the Shift key while you drag the sliders or adjust Gamma.

## LUTs Tools

ON Enable/Disable LUTs This button applies LUTs to the current image.

Keep Auto Scale Press this button to run the auto scale procedure permanently (on the live image). When you turn this button OFF, the settings remain as if the Auto Scale button was pressed only once.

Auto Scale This button adjusts the white slider position of all channels automatically with the purpose to enhance the image reasonably. If you have selected the Use Black Level option from the Settings pull-down menu, the black slider will be affected too.

Reset All Components Discard all LUTs settings and turn LUTs OFF by pressing this button.

Settings Display the pull down menu and select one of the following commands:

- · Brightfield Opacity -You can change opacity of a brightfield channel. Define the opacity in the Brightfield Opacity dialog window that appears after you run this command.
- · Use Black Level -Check this item to ensure that the black slider will be affected by the auto scale functions .
- · Settings -opens the Auto Scale Settings window. See Auto Scale Settings [81].

Keep Auto White Balance Check Box Check this option to switch the Auto White Balance functionality permanently (on the live image).

AWB Press this button to perform the Auto White Balance operation once.

Auto White Balance Color (...) This button Opens the AWB Color window and enables you to select a color shade which the system shall eliminate (make white). See AWB [81].

Reset AWB Discard all AWB settings with this button.

Color Oversaturation Switch this button ON and the system highlights all pixels with values reaching maximal values. Select colors to highlight the pixels with in the pull-down menu. See also 6.2.3. Displaying Image Layers [72].

<!-- image -->

These buttons arrange histograms of single channels next to each other horizontally or vertically.

This button arranges histograms of single channels overlapped. Use sliders at the bottom of the graph window to amplify or reduce the green/red/blue component display in the view.

Save/Load LUTs This pull-down menu enables user to handle LUTs settings in various ways. They can be saved to a *.lut file and loaded later. Or, LUTs settings saved along with an image image can be loaded directly from this image by the Reuse LUTs from File command.Oryoucancopy/paste the settings within the documents opened in NIS-Elements D .

Modify Image Through LUTs Press this button to apply the LUTs settings to the image data - the original image will be overwritten. Until you press this button, no changes are made to the image data.

Reset Zoom Zooms the histogram to fit the preview window.

Auto Range zooms the histogram so that the 'high' and 'low' limits are distinguishable. For example, if a small intensity range is defined on a 16bit image the low and high lines are displayed as one-pixel line. Pressing this button will stretch the histogram in order to display the lines separately.

## Auto Scale Settings

Press the arrow next to the Reset LUTs button and a pull-down menu appears. Invoke the Settings command.

<!-- image -->

The Low and High fields determine how many of all pixels of the picture are left outside the sliders when Auto Scale is applied (0-10%).

## AWB

White color in some images may suffer from having a color tint. The AWB (Auto White Balance) mode adjusts the image to get pure white instead of this tint. Similarly to LUTs auto scale, the AWB function

can be used once, or permanently on the live image. If you know the tint your 'white' color has, you can select this color by the color picker that appears after pressing the ... button:

<!-- image -->

Choose the color by mouse. You can also enter the RGB values to the fields below. A preview of the chosen color appears in the rightmost rectangle.

## 6.6.2. LUTs on Monochromatic Images

<!-- image -->

All features mentioned above are also valid for monochromatic images, except that the AWB function is not available. There are some other features added when in 'mono' mode.

Gradient Mapping monochromatic images to pseudo-color gradients is often used to enhance details in the image which would otherwise not be obvious. This button indicates the currently selected gradient. When pressed, a pull-down menu appears where you can select the color scheme you would like to use. Try a few of the schemes to see which one suits best.

<!-- image -->

## Manage Custom LUTs (requires:Local Option)

The Manage Custom LUTs command in the pull down menu enables to define a custom LUTs gradient. Use the tools available in the dialog window to define your custom gradients. They then appear in the pull down menu ready to be applied. Please see View &gt; Image &gt; LUTs &gt; Create Custom LUTs for details about the custom LUTs definition.

## 6.6.3. LUTs on Multichannel Images

Figure 6.17. LUTs window on two-channel image

<!-- image -->

Most of features mentioned above are also valid for multi-channel images. There are some other features added when in 'multi-channel' mode. Each channel is controlled separately by default. To control all channels at the same time, press and hold the Shift key while you drag the sliders or adjust Gamma.

When the image contains up to three channels, all channels can be visible at one time and you can handle them similarly to the RGB mode. When there are more than three channels, only one channel is displayed at one time. A pull-down menu in the tool bar enables you to select the channel to be displayed.

<!-- image -->

Next to the channel selection pull-down menu, there is this Auto Scale button. By pressing it, the system will automatically adjust only the current channel settings.

## 6.7. Organizer

## 6.7.1. About Organizer

<!-- image -->

Apart from the main application layout used for capturing and image analysis, NIS-Elements D provides an extra layout called Organizer . Organizer makes the work with image files and databases as easy as possible. To activate it, run the View &gt; Organizer Layout command or click the button located in the top right corner of the application window. The screen opens divided into two identical panes. To

switch from one pane to the other, use the View &gt; Next Pane (F6) command. To copy files between the panes, simply drag the images from one side to the other side.

Figure 6.18. The organizer layout.

<!-- image -->

- · This button toggles the display of the directory tree. You can switch it off to get additional space to display images.
- · In the nearby pull-down menu, it is possible to set the file type and only the one will be displayed. Or, All Images can be displayed.
- · If the Subfolders check-box is selected, all images from included sub-folders are displayed.

## 6.7.2. Image Filter

You can define a filter which enables you to display only images which fit the defined conditions. One or two conditions may be applied.

- · Pressing this button invokes the filter setup window.
- · This button activates the filter.

## Basic Mode

This mode enables you to filter files according to one condition.

## Advanced Mode

This mode enables you to define two conditions with a relationship between them. Either select OR to display files matching at least one condition, or select AND to display files which match both conditions.

<!-- image -->

- 1. Search in field -select the field where NIS-Elements D should search for a given expression.
- 2. If the selected field is of a numerical type (e.g. Size, Calibration, File date etc.) you can specify, whether you want to find the exact value or a value in a given range . This is selected by the Condition type radio button.
- 3. If the field type is Text , the Occurrence setting determines the way of evaluating the expression:
- · Anywhere -If the given sequence of characters is found anywhere in the field, the system will evaluate it as a match. For example: you have entered 'set' to the Values field. The filter will select records with the following field values: 'set', 'reset', 'settings', 'preset', etc.
- · Exact - If the given sequence of characters exactly equals to the content of the field, it is evaluated as a match. Fields containing the 'set' value only will match.
- · Start - If the entered string is found at the beginning of a field, it passes the condition. For example: fields containing 'set', 'settings', 'setup' will match.
- · All letter strings - It is possible to search for more expressions. These should be entered separated by commas. If you want to enter an expression with a space, insert it quoted. If this option is selected, only records where all of those expressions appear (anywhere) will match.
- · Any letter string - This option is for entering multiple expressions as above, but this time every field with an occurrence of at least one from the given expressions is matched.

## 6.7.3. Operations with Images within Organizer

- · To open an image double click its thumbnail. NIS-Elements D will close Organizer and display it in the main window.

- · To select multiple images, either click on the first and the last image holding the Shift key (continuous group selection) or click individual images with the Ctrl key down.
- · You can copy one or more images from one folder to another by 'drag and drop'.
- · To delete selected images press the Delete key.

All these operations and some other can be invoked also from the context menu, which appears after you right-click on the image thumbnail:

<!-- image -->

## Thumbnail Displaying Options

You can adjust the way images are shown in the organizer.

Thumbnail View Press this button and select the size of displayed image thumbnails. Selecting the Details with preview option will display images below each other with all available information aside.

Rotating Images There is a possibility to rotate images from within the organizer. It affects not only the image thumbnails, but the image data too. Press the corresponding buttons.

Autocontrast Press this button to turn the Apply autocontrast to thumbnails option ON. It enhances the image thumbnails automatically. Dark images gain details.

## Sorting of Images

To order displayed images, right click anywhere in the pane - a context menu will appear. Move to the Sort by sub-menu which offers several ordering criteria. If the ordering is turned ON already, the icon is displayed on the left side of the applied criterion.

<!-- image -->

## Grouping of Images

To arrange the view of images efficiently, you can use the capability of grouping of images. Drag the column name bar to the grouping bar (right above the column name bars). All files with matching field values of the selected column will be grouped together. This can be undone by dragging the column caption back to the others. See Figure 6.18, 'The organizer layout.' [85] (the Calibration column is grouped).

Note

If you have the Database module installed, the Organizer becomes switchable between two modes: the Files View and the Database View. See description of the Database View.

## 6.7.4. Resizing the Organizer Panes

The pane size is adjustable. To resize it, you can either:

- · 1. Place the mouse cursor over the dividing line in the middle.
- 2. The cursor becomes an arrow with two tips.
- 3. Drag it left or right to the new position.
- · Resizes the panes to achieve the same size for both of them.
- · Resizes the pane to its maximal/minimal size (one pane is then displayed on the whole screen).

## 6.8. Database

After you install the 12.2. Database [169] module, the Database menu appears in the main tool bar.

Note

Viz. 2.1.9. Installing the Database Module on 64-bit Systems [11].

## 6.8.1. New Database

Before you can connect to a new database the structure of tables and fields, or at least the protection level shall be set:

- 1. Run Database &gt; New Database .
- 2. Specify the file to be created.

<!-- image -->

- 3. Select one of the database templates. Each template consists of several predefined tables. If you choose Blank , no tables will be created (later you will have to use the Database &gt; New Table command). Click Next .

- 4. Select the default protection of the database. The user accounts can be based on MS Windows accounts, or arbitrary number of database user accounts protected by password can be created. Or, the database can be fully accessible for all users - if the Not Protected option is selected. Click Finish

.

- 5. The database connection will be automatically created and connected. You can browse the database with the Organizer .

## 6.8.2. New Connection

If there is an existing database created by NIS-Elements D , you can connect to it via the Database &gt; New Connection command:

- 1. Run Database &gt; New Connection . A window appears.
- 2. Locate the database (*.MDB) file.
- 3. Confirm the action with OK .

Connections to databases can be managed via the Database &gt; Manage Connections command.

## 6.8.3. Database Tables

A new table can be added to an existing database. Every database must contain at least one table. If you have created a blank database or you would like to add a table to any of the connected databases, do as follows.

- 1. Run Database &gt; New Table . A window appears.
- 2. Select one of the connected databases to which the table will be added.
- 3. Select one of the table templates. Table templates can be imported from the other connected databases. If you choose Blank , you will have to create the table structure from scratch (in the next step). Click Next .
- 4. Define the field properties in the window that appears.
- 5. Finish the table creation.

## 6.8.4. User Permissions

Database access rights can be set for individual users. As we mentioned above, there are two types of protection:

Password protection Any number of database user accounts can be created. Then you can connect to a database by the user name and password.

Windows account protection User permissions to databases can be set for different MS Windows users. The access to a database is then granted if only the user is currently logged in Windows.

Both protection types can be combined in one database. To manage the user accounts and permissions of a connected database:

Note

You have to be connected to the database under an account with sufficient user rights.

- 1. Run Database &gt; User Accounts and Permissions . A window appears.
- 2. Select the database of your interest. All user accounts of the database will appear in the list below.
- 3. Create new or select an existing user account.
- 4. Use the buttons on the right to manage the account properties, duplicate it (along with the permissions settings), change the password, modify permissions ( Change properties ), or even delete it.

## 6.8.5. Database Backup

The capability to backup the database is essential for serious work. The Database Backup Scheduler enables to backup the MS Access database automatically once in a precisely specified time interval, so you do not have to be afraid to loose any data. The Database Scheduler uses the standard Windows Scheduled Tasks tool (Start &gt; Control Panel &gt; Scheduled Tasks). Once you schedule a backup, there is only one condition to perform it successfully: The computer must be turned ON at the scheduled time. Configure the backup via the Database &gt; Schedule Database Backup command.

## 6.8.6. Database View within Organizer

You can browse the database using the built-in Organizer . Use the View &gt; Organizer Layout command (or the to Press the button located in the top right corner of the screen) to display the Organizer . Here you can either browse images saved on the hard disk or browse the database. Switch between the two views by the following buttons:

Files This button switches the pane to show a directory tree and images from the selected folder (and optionally its sub-folders).

- Database This button switches the pane to show the database structure and lists images from the currently selected database table.

See 6.7. Organizer [84] for general information about how to use the Organizer.

## Features Available in the Database View

Figure 6.22. The Database View

<!-- image -->

- · This button displays the detailed information about the selected image. You can switch it off to get additional space to display images.
- · The nearby pull-down menu displays the database connection name and enables to switch between active connections.
- · The next pull-down menu enables you to select a database table to be displayed.

## Operating with Images

You can insert images to a database by 'drag and drop'. Simply drag the image from a folder and drop it onto the pane, where the database table is opened.

## 6.9. Saving Image Files

NIS-Elements D offers several ways to save an image file, using either:

The File &gt; Save As command The most common way of saving the current image. You can select image format in the Save as type pull-down menu. See also 11.2. Save ND2 as AVI [167].

The File &gt; Open/Save Next &gt; Save Next command This command saves the current image (live or static) automatically according to the settings defined within the general options window. See 6.9.2. Save Next Options [92].

During image-capturing experiments Images and image sequences can be saved automatically during experiments such as ND Acquisition (5.4. About ND Acquisition [59]).

## 6.9.1. Saving Images with UAC

Because of the security enhancement with the UAC (user account control) of Windows Vista and Windows 7 , it is not possible to save images in those folders that require Windows administrator user rights. Those folders are:

- · C:\Windows and subsequent folders
- · C:\Users and subsequent folders excluding C:\Users\[login-user-name]
- · C:\Program Files and subsequent folders excluding C:\Program Files\ NIS-Elements D \Images

## 6.9.2. Save Next Options

This window enables you to configure the File &gt; Open/Save Next &gt; Save Next command properties. Run the Edit &gt; Options command and switch to the Save Next tab.

## Save to File

Directory, Prefix, Digits, File Format, Compression Defines name of the file that will be automatically generated. Let's assume, that you have selected - Directory: c:\images; Prefix: seq; Digits: 4; File Format: JPEG2000. Then, by pressing Enter (calling the Save Next command), an automatic file named "seq0001.jp2" is generated and saved to the "c:\images" directory. When pressing Enter again, the file "seq0002.jp2" is saved to the same directory etc.

Define Image Info Displays a dialog box, where you can enter some description (jp2 meta-information), that will be saved with every image:

Overwrite/Skip already existing files Allow or deny rewriting of the images already existing in the default save directory.

Save to Database Whenselected, images are being saved to a chosen database table, instead of saving them directly onto disk.

Database If you are already connected to some database, select it from the pull-down menu. Else a dialog window appears, which enables you to connect to any database.

Table Select the database table which the images will be stored to.

Autoincremental field Choose which field of the database will be used to store the generated image descriptions.

The image descriptions are generated according to the Prefix, Digits, Number values. Let's assume, that you define - Prefix: seq; Digits: 4; Number: 20. Then, by pressing Enter , the current image is saved to the selected database table and the automatic image description is put into the Autoin-

cremental field of the table. Its name would be "seq0020" in our case. When pressing Enter again, the second record signed "seq0021" is created.

External mapping You may create an external *.txt or *.ini file containing mappings that assign table field names to some particular values. These values are automatically filled into the database records when the Save Next command is called. Please, see the comments below for an example.

Note

```
External mapping example - The *.ini file content may be:
```

```
[Table 1] Author=Jack Sparrow Experiment number=12 Sample=Malus silvestris
```

It means: When saving images to the database table named "Table 1", the fields of Author, Experiment number, and Sample will be filled with the specified values.

## Options

Show grabbing dialog before saving Before an image is saved the Grabbing dialog box is shown. Selecting this option enables you to define the way of grabbing (with/without a shading correction, averaged etc).

When saving, display Image Info dialog box You can change the default image information (jp2 meta-information) right before saving.

Sound Alert If checked, a short tone from your PC speaker is played every time the Save Next command is used.

Save with annotation and binary layers If checked, images are saved together with the binary and annotation layer.

Change to live after saving an image After saving a single image, a Live image is displayed immediately.

Defaults for this Page Pressing this button restores the default settings of this window. All your changes will be lost.

OK Confirms all the changes and closes the window.

Apply Saves the changes which are applied, bud the window remains opened.

Cancel Discards all the changes and closes the window.

Help Displays relevant help page.

## 6.10. Closing Images

- · The currently displayed image can be quickly closed by pressing the cross button in the top-right corner of the image window.

- · The image can be also closed by invoking the File &gt; Close command.
- · If you want to close all images, use the Window &gt; Close All command.
- · If you try to close an image that has been changed, NIS-Elements D will display a confirmation dialog box, offering to save the changes.
- · Use the Window &gt; Close All but Current commandtoclose all opened documents but keep the current one opened.

## 6.11. Supported Image Formats

NIS-Elements D supports a number of standard file formats. In addition, NIS-Elements D uses its own image file format (ND2) to fulfil specific application requirements.

JPEG2000 Format (JP2) An advanced format with optional compression rates. Image calibration, text descriptions, and other meta-data can be saved together with the image in this format.

ND2Format (ND2) This is the special format for storing sequences of images acquired during ND experiments. It contains various information about the hardware settings and the experiment conditions and settings. It also maintains all image layers of course.

Joint Photo Expert Group Format (JFF, JPG, JTF) Standard JPEG files (JPEG File Interchange Format, Progressive JPEG, JPEG Tagged Interchange Format) used in many image processing applications.

Tagged Image File Format (TIFF) This format can save the same amount of meta-data as JPEG2000. TIFF files are larger than JPEG2000 files but are loaded faster. TIFF files have several ways to store image data, therefore there are many versions of TIFF. NIS-Elements D supports the most common TIFF modalities. TIFF image format in NIS-E supports also floating point images.

CompuServe Graphic Interchange Format (GIF) This is a file format commonly used on the Internet. It uses a lossless compression and stores images in 8-bit color scheme. GIF supports single-color transparency and animation. GIF does not support layers or alpha channels.

Portable Network Graphics Format (PNG) This is a replacement for the GIF format. It is a full-featured (non-LZW) compressed format intended for a widespread use without any legal restraints. NIS-Elements D does not support the interlaced version of this format.

Windows Bitmap (BMP) This is the standard Windows file format. This format does not include additional image description information such as author, sample, subject or calibration.

LIM Format (LIM) Developed for the needs of laboratory image analysis software. Nowadays, all its features (and more) are provided by the JPEG 2000 format.

ICS/IDS image sequence ICS/IDS image sequences are generated by some microscopes and consist of two files: the ICS file with information about the sequence; the IDS file containing the image data. The ICS file must be stored in the same directory together with the IDS file.

Caution

ND Images containing multi-point XY dimension cannot be saved to a file in the ICS/IDS format. See also 5.4. About ND Acquisition [59].

## NanoZoomer files (NDPI, VMS) (requires:Local Option)

We can open these files produced by Hamamatsu devices and save the image information to an ND2 file.

## ShuttlePix files (requires:Local Option)

Nikon ShuttlePix Digital Microscopes produce standard TIFF and JPEG files and save the calibration info to a separate file. NIS-Elements recognizes the calibration file and loads it along with the image data.

## 7. Image Analysis

## 7.1. Preprocessing

## 7.1.1. Processing On: Intensity/RGB/Channels

You can decide whether to perform the processing on single RGB channels of the image, or on the intensity component of the image only. The RGB/Intensity setting is global so it is applied to all the other processing commands automatically. When processing a multichannel image, this option is disabled the operation is applied to channels automatically.

Note

In case the command does not open a window where it would be possible to make the choice, the setting from the last performed processing command (the global setting) is applied.

## 7.2. Histogram

A histogram displays frequencies of pixels of a certain intensity value. The intensity values range from 0 to 255 (on 8bit images). A separate curve is created for each color channel. Run the View &gt; Visualization Controls &gt; Histogram command to display the histogram control panel:

<!-- image -->

## 7.2.1. Source Data

Source data of the histogram can be viewed if you swap to the Data tab in the bottom-left corner of the window. The area from where the histogram is calculated can be restricted according to the selected histogram mode:

- The data are obtained from the whole image.
- The data are obtained from within the probe.
- The data are obtained from within the current ROI.
- The data are obtained from the image parts under the binary layer.

## 7.2.2. Export

<!-- image -->

The source data or the histogram image can be exported to an external file. Display the Export pulldown menu and select a suitable destination. Click the button to perform the export. The Export ND

histogram button enables to export histogram data of all frames of the current nd2 file. The same destination which is selected in the Export pull-down menu is applied.

Note

Please, see the 8.11. Exporting Results [146] chapter for further details.

## 7.2.3. Histogram Scaling

The histogram can be zoomed in and out using the zoom buttons on sides of the window. There are also other options to adjust the graph appearance:

Left slider There is a slider along the Frequency axis. Drag it in order to stretch the view of either lower or upper values of the axis.

Auto Scale Vertical Zooms the graph of each channel separately to fit the available area. When this function is ON, the histogram is not proportional.

Auto Scale Horizontal Zooms the graph so that the marginal zero frequencies, if there are some, are excluded from display.

Graph Linear Displays the linear scale on the Y axis.

Graph Logarithmic Displays logarithmic scale on the Y axis.

Show Grid Turns ON/OFF the grid in the background.

## 7.2.4. Overrun Indication

If certain amount of pixels with maximum/minimum intensity values (black/white pixels) are spotted in the image, color dots appears above the graph. The color indicates which channel is affected. When you place the mouse cursor over the dots, a tool tip message appears with details about the percentage of under/overexposed pixels. The percentage limit setting is loaded from the LUTs settings (the color dots do not appear unless the set percentage of black/white pixels is exceeded).

## Note

If the overrun concerns more than three channels (considering multi-channel images), only one white dot is displayed instead of many color dots.

## 7.2.5. Graph Memorizing

You can save the current graph to memory and display it later for comparison with another graph.

Displays memorized graph.

Memorizes the current graph. Only one graph can be memorized at a time. If any graph has already been memorized before, it will be overwritten by the current graph.

Clears the memory.

## 7.2.6. Histogram Options

## Drawing Style

There are two ways the histogram can be drawn:

- · Raw Data -tries to draw the source data precisely to the graph
- · Trend Style -interpolates the data so that the histogram lines appear smoother.

## Histogram Options Window

The graph appearance can be modified. Press the Options button - a window appears where the following settings can be adjusted:

Colors Graph background and axes colors can be selected.

Pen Width Set the width of the histogram(s) line to 1, 2, or 3 pixels.

Fill Graph Area The area below the histogram line can be filled with the channel color.

Graph Area Opacity Select the opacity of the Graph Area color in %.

Vertical/Horizontal AutoScale, Show Grid These options equals the corresponding buttons of the histogram tool bar.

Interpolation method Select the way of drawing the graph line. The Linear (smooth) and Quick (precise) options are available.

AntiAlias Smooths the edges of the graph line.

Horizontal axis always visible If checked, the axis does not leave the graph area while zooming in the graph.

## 7.3. Thresholding

(requires:Automatic Measurement)

Specifying correct threshold limits is a crucial procedure of the automated image analysis. The point is to determine which pixels will and which will not be included in the binary layer and thereby distinguish objects to be analyzed from background. Thresholding can be performed in the following modes:

Note

To display the thresholding control panel, run the View &gt; Analysis Controls &gt; Thresholding command.

## 7.3.1. RGB Mode

The RGB thresholding mode is available only if an RGB image is opened. There are two ways how to define the threshold limits, by choosing reference points within the image, or by defining the limit values for each color channel.

<!-- image -->

To threshold the image use the following tools:

- Reset This button erases the threshold settings (no binary objects are created).
- Single point threshold tool Select it and click inside the image to define the threshold. The threshold ranges will be adjusted so the selected pixel will fit inside.
- 3 point circle tool Picks threshold from the radius of 3 pixels.
- 6 point circle tool Picks threshold from the radius of 6 pixels.
- Undo Reverses the previous threshold operation.
- Redo Returns the threshold as it had been before the Undo button was used.
- Re-threshold image Use this button to update the binary layer according to the current settings. The purpose of this button is to obtain the original binary layer in case it has been modified e.g. by a command from the binary layer.
- Keep Updating Binary Press this button to keep the binary layer up-to-date all the time. You may find this function useful especially when thresholding is applied to the live image.
- Threshold ND image When an nd2 file is opened, this button appears. Define the threshold limits on the current frame and use the button to apply it on the whole nd2 file.
- Full Image/Use ROI If selected, threshold is defined only on the area of the Region Of Interest.

Save / Load Threshold Settings This button invokes a pull-down menu which enables to load/save the current threshold settings from/to an external file (*.threshold).

Zoom Zoom the histogram in/out.

Auto Zoom Zooms the histogram to fit the preview window.

Auto Range Zooms the histogram so that the 'high' and 'low' threshold lines are distinguishable. For example, if a small intensity range is defined on a 16bit image the low and high lines are displayed as one-pixel line. Pressing this button will stretch the histogram in order to display the lines separately.

## How to use the picker tool to threshold an image

1. Select one of the cross hair tools.

- 2. Left click on the image over a pixel of the image that should be considered part of the threshold/ binary layer. All pixels with similar intensity values of the image will also be highlighted. An outline will also display around the object(s) as well as the building solid colored threshold/ binary layer.
- 3. Continue to click on areas of the image that should be part of the threshold/ binary layer.

Note

Right-clicking inside the image can be used to swap between the color mode (without the definition window) and overlay mode (with the definition window).

## How to use the histogram to threshold an image

- 1. Move your mouse cursor over the histogram and hover over the vertical line labeled L (lower limit).Move the vertical line left or right to set the lower limit of the threshold. Use the image and its building threshold to provide feedback on whether the limit is set in the correct place. Accepted areas of the histogram for the threshold are colored gray.
- 2. Repeat first step with the vertical line labeled H (higher limit)
- 3. You can combine the histogram with picker tools to create the thresholded image.

## Threshold Adjustments

Thresholding parameters can be adjusted very precisely in the following way:

- · Threshold limits of each channel can be adjusted by rewriting the values in the top-left/top-right corner of each channel histogram.
- · Threshold range of each channel (the colored stripe) can be shifted by mouse. Place the cursor in the middle of the range (a circle appears) and drag it left or right.
- · Threshold limits of each channel can be adjusted by mouse. Place the cursor on the edge of the thresholding range and drag it left or right.

The two last behaviors can be further modified by pressing additional keys:

- · Move the threshold using the right mouse button - the binary layer in the image is not updated continuously, but is updated only once after the mouse button is released. Such operation saves some computing and therefore is quicker.
- · Hold Shift while moving the threshold limits - the threshold adjustment is performed on all channels together (RGB images only).
- · Hold Ctrl while moving the threshold limits - both the low and the high threshold limits move in opposite directions.

## Binary Operations

Four basic operations can be performed on the binary layer before it is displayed on screen. To turn the operation on, click on the up arrow button in order to define the number of its iterations:

Clean Removes small objects from binary image.

Smooth Smooths the binary image contours.

Fill Holes Fills holes within binary objects.

Separate Separates objects.

## Restrictions

Size Define size range using min/max value in the edit boxes or using the slider.

Circularity Define circularity range using min/max value in the edit boxes or using the slider.

## Thresholding Large Images

If thresholding images larger than 5000 x 5000 pixels, a new check box called Preview on selected area only is displayed. This feature enables to display the threshold preview just on a limited area to speed up the thresholding adjustment.

## Changing Appearance of the Threshold Layer

<!-- image -->

To change the color or transparency of the layer, right-click the Overlay button in the general controls toobar in the document window. A contextual menu appears, where you can select one of the predefined transparency levels, or run the Colorize Binary Objects command. This command displays the binary objects in several different colors. The algorithm ensures that two neighboring objects are never colored by similar colors.

See 7.5. Mathematical Morphology Basics [109].

## 7.3.2. HSI Mode

The HSI thresholding mode is available only if an RGB image is opened. The thresholding procedure works the same way as in the RGB mode except that the pixel values are displayed in the HSI (Hue, Saturation, Intensity) color space and that the Saturation and Intensity channels can be switched OFF.

Therefore you can threshold over the H HS , , or HI channels only. Switch the channel off by de-selecting the check box in the top-left corner of the channel histogram.

## 7.3.3. Intensity Mode

The thresholding procedure works the same way as in the RGB mode except that it is performed on the intensity pixel values.

## 7.3.4. MCH Mode

The MCH mode is not available when working with a monochromatic (single channel) image. This mode is dedicated to perform threshold on multichannel images, but can be applied to RGB images as well.

- · If there are many channels, only one channel histogram is displayed. Switch between the channels by selecting their names from the bottom pull-down menu.
- · The binary layer(s) can be displayed in two modes:
- 1. Each channel can create its own binary layer
- 2. One layer can be created as an intersection of all channels binaries.

## 7.3.5. Thresholding Example

(requires:Automatic Measurement)

## Step by Step

- 1. Threshold the image using the Intensity Measurement option in the Thresholding control panel.

<!-- image -->

- 2. Clean the image to remove detected small non-nuclei areas.
- 3. Select features to be measured in the Automated Measurement Results control panel. Press the Options button and choose the Select Object Features command. An Object Measurement Setup window appears. Add or remove features you want to measure.
- 4. Press the Update measurement button in the Automated Measurement Results control panel to measure image features. Overview the results. Press the Store Data button to save the data for future reference.

<!-- image -->

- 5. Right click the Turn ROI On/Off button in the right document toolbar. Choose the ROI &gt; Move Binary to ROI command. Each binary object turns into separate ROI.

<!-- image -->

- 6. Threshold the cell nucleoli in the nuclei the same way as was already described above using the Thresholding control panel.
- 7. Measure the thresholded nucleoli using the Update measurement button in the Automated measurement Results control panel. Press the Store Data button to save the data.
- 8. Group results per ROI: drag the title of the column called RoiID into the grey area above the columns. You can drag and drop any combination of features as well. Results always group according to such selected features.

<!-- image -->

- 9. Turn on the graph using the Show Histogram button.

<!-- image -->

The histogram displays the selected feature of interest. If you want to display different feature - press the right mouse button over the data table on the left and open the Feature of Interest submenu. Select another feature. The histogram recalculates automatically.

- 1 0 . To get the information about area percentage, select the Field measurement option in the top toolbar of the Automated measurement Results control panel.

Figure 7.7. Example

<!-- image -->

Field 1 displays results of measurement when measured without ROI. That means % of nucleoli in the entire image.

Field 2 displays results of measurement when measure with ROI on. That means % of nucleoli within the nuclei.

- 1 1 . You can export the result to various locations using the Export command.

## 7.4. Binary Layer

(requires:Automatic Measurement)

## Working with the Binary Layer

There are the following buttons at the bottom of the right image tool bar.

View Binary This button displays the binary layer only of the image. It can be edited by hand using the binary editor ( Binary &gt; Binary Editor ).

View Overlay The binary layer can be displayed together with the color layer using an overlay mode.

Several binary layers can be created for one color image. Manage them using the View &gt; Analysis Controls &gt; Binary Layers control panel.

View Color This button switches to view the color image (only).

The binary layer, as a result of thresholding, can be modified by hand using the binary layer editor. It is a built-in application providing various drawing tools and morphology commands. Go for the Binary &gt; Binary Editor command or press Tab . New buttons appear on the tool bars:

## 7.4.1. Drawing tools

The binary image can be modified using various drawing tools. Although the way of use of some tools differs, there are some general principles:

- · Make sure you are in the right drawing mode (drawing background /foreground )
- · Drawing of any object which has not been completed yet can be canceled by pressing Esc .
- · The polygon-like shapes are drawn by clicks of the left mouse button. The right button finishes the shape.
- · The automatic drawing tools (threshold, auto detect) have a changeable parameter. It can be modified by + and -keys or by mouse wheel.
- · The scene can be magnified by the UP/DOWN arrows when mouse wheel serves another purposes.
- · You can drag a magnified image by right mouse button.
- · A line width can be set in the top tool bar.
- · Hints are displayed in the second top tool bar.

## Binary Layer Color and Transparency

When in overlay mode:

- · The Insert key switches between predefined overlay colors.

- · Ctrl + Up/Down increases/decreases the binary layer transparency.

## Erasing Single objects

Single binary objects can be erased in the following way:

- · Run View &gt; Analysis Controls &gt; Binary Toolbar .
- · Select the Delete Object tool from the toolbar.
- · Click inside the objects to be erased.

## Multiple Binary Layers

An arbitrary number of binary layers can be created within one image. Click this Create New Binary Layer button in the image tool bar to add a new binary layer. The binary layer that you are currently editing can be selected in the nearby pull-down menu. Binary layers can be managed from the View &gt; Analysis Controls &gt; Binary Layers control panel.

## 7.5. Mathematical Morphology Basics

(requires:Automatic Measurement)

The binary image as a result of thresholding often needs to be modified before a measurement is performed. Edges of the objects can be smoothed, holes in the objects filled etc. by using the mathematical morphology commands.

Note

'Image Analysis and Mathematical Morphology' by J. Serra (Academic Press, London, 1982) was used as a reference publication for the following overview.

The basic processes of mathematical morphology are: erosion, dilation, open, close and homotopic transformations.

<!-- image -->

Erosion After performing erosion, the objects shrink. Marginal pixels of the objects are subtracted. If an object or a narrow shape is thinner than the border to be subtracted, they disappear from the image.

Dilation After performing dilation, the objects enlarge. Pixels are added around the objects. If the distance between two objects is shorter than twice the thickness of the border to be added, these objects become merge together. If a hole is smaller than twice the thickness of the border, it disappears from the image.

Open Open is erosion followed by dilation so the size of the objects is not significantly affected. Contours are smoothed, small objects are suppressed and gently connected, particles are disconnected.

Close Close is dilation followed by erosion so the size of objects is not significantly affected. Contours are smoothed, small holes and small depressions are suppressed. Very close objects may be connected together.

<!-- image -->

Clean This transformation is also called geodesic opening. The image is eroded first so small objects disappear. Then, the remaining eroded objects are reconstructed to their original size and shape. The advantage of this algorithm is that small objects disappear but the rest of the image is not affected.

- Fill Holes Fills the holes inside objects. This transformation is handy when objects have a rich inner structure with intensities typical for background. After applying the Fill Holes transformation, objects become homogeneous.

<!-- image -->

<!-- image -->

<!-- image -->

Contour This transformation converts objects into their contours.

- Smooth Smooth affects rough edges of the objects makes them smooth.

MorphoSeparate Objects This transformation detects standalone objects that are connected together and isolates them.

## 7.5.1. Connectivity

Applying the above mentioned transformations has some limitations due to digital images rasterization.

Whenspeaking about binary image processing, a binary image is a set of pixels where values 1 represent objects and values 0 represent background. In the square grid of the image, two possible connectivities can be used for processing - the 8-connectivity or the 4-connectivity. Look at the picture below. If the 8connectivity is used, the two pixels represent one object. If the 4-connectivity is applied, there are two objects in the picture. NIS-Elements D works with the 8-connectivity model, so all pixels neighboring by the corner belong to one object.

<!-- image -->

## 7.5.2. Structuring Element = Kernel = Matrix

When applying Erosion, Dilation, Opening or Closing, one of the parameters which determines the transformation result is the selection of kernel (structuring element, matrix) type. There are the following kernels used in NIS-Elements D :

<!-- image -->

The bright pixel in the center or near the center of the kernel represents its 'midpoint'.

## Example 7.1. Erosion

Let's assume 1 and 0 represent object(1) and background(0) pixels of the binary layer. You can imagine the erosion as the following algorithm:

Move the midpoint of the kernel to every point of the image. Each time, look at the neighboring pixels of the kernel and make the following decision:

- · If there are object(1) pixels in all the positions of the kernel, set the midpoint to object(1).
- · If there is at least one background(0) pixel in the kernel, set the midpoint to background(0).

## Example 7.2. Dilation

You can imagine the dilation as the following algorithm:

Move the midpoint of the kernel to every point of the image. Each time, look at the neighboring pixels of the kernel and make the following decision:

- · If there is at least one object(1) pixel in any position of the kernel, set the midpoint to object(1).
- · If there are background(0) pixels in all the positions of the kernel, set the midpoint to background(0).

## Example 7.3. Open and Close

Openis performed by eroding the image and then applying a dilation to the eroded image. On the contrary, Closing is performed as a dilation followed by erosion.

## Repetition issues

If the midpoint is not in the center, applying erosions or dilations by odd number of iterations causes image to shift by 1 pixel. Normally, the total image shift would be determined by the number of Iterations (in pixels). NIS-Elements D eliminates this shift: it changes the position of the midpoint 1 pixel downrightwards within the kernel for even operations. For opening and closing it is possible to eliminate this shift totally. However, if you run the erode or dilate processes again and again using the kernel with even dimensions and odd number of iterations, then the shift becomes significant.

## 7.5.3. Mathematical Morphology Examples

Please see the following examples of some of the binary functions applied to an image. In the following sequence of images, the functions were applied subsequently:

Example 7.4. Functions applied subsequently

<!-- image -->

## 7.6. Regions of Interest - ROIs

In laboratory imaging experiments, users are often interested in just a part of the image. To define such an interesting part of the image we use one or more Regions of Interest (ROIs). These regions are used

later in analysis and measurements.

Note

Do not confuse image ROIs with Camera ROI which is used to reduce the active area to just a part of the camera sensor (CCD or CMOS). Such reduction usually results in higher frame rate. See 5.3. Camera ROI [57].

## 7.6.1. Types of ROI

Individual ROIs (ROI objects) are 2D objects. They can have different shape: rectangular, elliptical polygonal or bezier. One shape can be created with one or more tools. For instance polygon ROI can be defined using both 'Draw Polygonal ROI' and 'Autodetect ROI'.

In case of an ND file which has time axis (e.g. time-lapse) individual ROI objects can be defined as 'Global ' or as 'Changing over time'. Global objects do not change any of their characteristics over time. Objects that are defined as changing over time can change their position and shape in time (however objects cannot change their shape - e.g. from ellipse to polygon). This feature is useful for track moving or warping objects.

In case of Multi Point nd2 file there is one more option: ROI can be defined per Multi Point (which is the default). It means that ROIs from one point are completely independent of ROIs defined on the other point (even if they have the same number). This applies also to ROIs defined as 'Changing over Time' (in case the image has time axis too). On the other hand if the ROI is changed to a 'Global' it will be shared among all points of the Multi Point set.

Depending on the application purposes ROI objects can have different usage. NIS can handle 'Background ROIs', 'Reference ROIs', 'Stimulation ROIs' and 'Standard ROIs'.

## 7.6.2. Interaction with ROIs

ROIs can be manipulated anytime directly in the image window. Many of the following techniques work in ROI editors too. Objects cannot be moved or resized when they are Locked (some analysis tools or users may lock them to prevent accidental modification). They must be unlocked (from the ROIs' context menu) before any manipulation. Note that the mouse cursor changes over the ROI to indicate which action will be started after mouse button is pressed (it changes when modification keys like Alt and Ctrl are pressed).

Selection ROI objects can be selected by clicking on an unselected object (other previously selected are unselected). Clicking on a ROI object with Ctrl key pressed results in altering the selection state. More than one object can be selected in this way. Double-clicking on any object results in only that object being selected. All objects can be selected by pressing Ctrl+A or by choosing 'Select All ROIs' from the menu over any ROI. Alternatively, it is also possible to select a set of objects by dragging a rectangle around them with Ctrl key being pressed.

Moving Objects are moved by simply dragging them (cursor indicates that). When more objects are selected only the one under cursor is moved by default. This can be changed by pressing the Alt key and move all selected objects. When object is changing over time, any moving results in a new key-frame.

Individual dots representing the key-frames can be moved too. It is possible to duplicate existing objects by Shift dragging. It works on selected objects. In case of a key-framed object, object is duplicated with all its' key-frames unless Alt is pressed.

Resizing Resizing a ROI is done by dragging its' contour (the cursor changes accordingly). Note that resizing hit-zones extend towards outside of the object (as opposed to moving hot-zones which extend towards inside of the object). Resizing always affects only one object (selection is not taken into account). The behavior slightly varies depending on the object shape. By default resize does not hold aspect of the object - width and height can be changed independently. By holding Shift key aspect is maintained (useful for circles) and the center is not moved. Rectangle can be also rotated by using Alt key while dragging.

Exact values can be entered in 'ROI Properties' dialog which is accessible from the ROI context menu.

## 7.6.3. Simple ROI Editor

When creating more than one ROI, the Simple ROI editor is the tool of choice. With this tool it is possible to make all possible shapes with different methods. All interaction techniques work here as well.

Figure 7.12. Simple ROI Editor toolbar

<!-- image -->

Note that many actions have a hot-key (P for Pointing tool, R for Rectangle, E for ellipse, L for Polygon, Bfor Bezier , A for Auto detection, H for drawing holes and others) to speed up the process of interaction.

## 7.6.4. Auto-Detect Tool

Auto-detect tool is available from ROI menu, Simple ROI editor and some other places. It produces a Polygon ROI. Using the tool is two step process: The first click on an image structure results in preliminary object contour, that is drawn on the screen. After that, user can further tweak the object contour and then finish whole auto-detect by confirming with right mouse button. User can always cancel auto-detect by pressing Esc key.

The very first click is important, because these pixels under the cursor determine intensities from which the algorithm guesses the whole object. As a general rule it is better to choose brightest pixels in the bright objects (fluorescence) and dimmest in the dark object. It is also good to click near the center of the object.

After the click the algorithm presents its guess of the object contour and goes into the interactive phase. In this phase it is possible to:

Redefine the first point by clicking again in the image

Cancel auto-detect by pressing Esc key

Grow or shrink the object area (changes the intensity range of pixels making the object) by scrolling mouse wheel or pressing PageUp/PageDown (for finer steps use Ctrl + mouse wheel)

Erode or Dilate morphologically the object by 'E'/'D' or Down/Up keys

Open or Close morphologically the object by 'O'/'C' keys

Morpho-separate portions of the object by 'S' or 'P' key (if it is not possible to separate the key does nothing)

## 7.6.5. Using ROIs for analysis

ROIs are used mainly in Automated Measurement to measure ROIs features or number of binary objects inside each ROI , Object Count to restrict binary objects to areas of interest only, ROI statistics to measure intensities interactively. In all these cases ROI selection is taken into account as well as intersection options in Measurement Options.

## 8. Measurement

## 8.1. Calibration

Calibration of the image is of crucial importance to measurement. On calibrated images, realistic measurements can be performed and objects of different images could be compared to each other. A correct calibration has to be made before you begin to measure.

There are two ways how to obtain a calibrated image:

- · To capture images with a calibrated system (objective). Please see the 4.1.3.3. Objective Calibration [43] chapter which explains how to calibrate the NIS-Elements D system.
- · To calibrate an uncalibrated image manually:

## Calibrating an Uncalibrated Image

- 1) Run the Calibration &gt; Recalibrate Document command.

2)

<!-- image -->

- a) If you know the size of one pixel, click the Pixel size... button.
- b) If you do not know the pixel size, draw a distance to the image and set its real length. For this purpose, you should use an image of a calibration slide or a ruler captured with your system.

There are three modes: horizontal, vertical and parallel lines, select one of them. Click into image to place first line, then second line appears on your mouse cursor. Place this line and the following dialog box appears.

3)

4)

Figure 8.2. Pixel Size CalibrationFigure 8.3. Line-length Calibration

<!-- image -->

<!-- image -->

- 5) Click OK to finish the calibration.

## 8.2. Units

NIS-Elements D supports the following units:

pixels

nanometers

micrometers

millimeters

centimeters

decimeters

meters

kilometers

inches

mils

If the image is uncalibrated, pixels are the only units available. In case of a calibrated image, it is possible to select other units which are then used to display all values (e.g. measured length/area). There are two ways of how to select the desired units:

- · Right click the image status bar where the calibration is displayed. Select the units and precision from the context menu.

<!-- image -->

- · Or, click the Current unit button located in the Calibration &gt; Objectives command window and select the units.

## 8.3. Rough Measurement

Quick and approximate measurements can be performed utilizing graticules. They behave like adjustable floating rulers. User can simply align a graticule with the measured object and read the distance value (e.g. the diameter). To activate the graticule, press the Graticules button.

## 1) Select Graticule Type

The type of the graticule ruler is indicated by a picture on the Graticules button placed on the right image tool bar. To change the graticule type, click on the graticules button with the right mouse button and select the appropriate item from the context menu:

- Rectangular Grid
- Circle
- Simple Circle
- Cross
- Industrial Cross
- Simple Cross
- Vertical Ruler
- Horizontal Ruler

## 2) Define Graticule Properties

Right click the Graticules button and select the Graticules properties command from the pulldown menu. A window appears where display parameters (shape, color, line width, density of lines) of all graticules can be adjusted.

## Graticules Density

The density value - the closest distance between two line intersections of the graticule - can be set, or you can let NIS-Elements D adjust it automatically according to the current zoom factor. The units selection depends on the image calibration (calibrated/uncalibrated).

Note

Concerning the Cross graticule. The distance defined by Density is divided into smaller sections automatically. However, for odd density values greater than 10, the markings remain hidden because it is not possible to display them accurately.

## 3) Measure the Image

The graticule measurement provides the following options:

- · The graticule can be moved by mouse arbitrary.
- · The graticule position can be reset by using the Move Graticules to Center command from the context menu.

- · A binary layer can be created from the current graticule using the Copy Graticules to Binary command.
- · A Graticule Mask can be created from the current binary layer using the Copy/Add Binary to Graticule Mask command.
- · A Graticule Mask can be stored/loaded to/from an external file via the Save Graticule Mask As and Open Graticule Mask commands.
- · A new image containing graticules can be created by the Edit &gt; Create Full View Snapshot (8bit RGB) command.

## 8.4. Manual Measurement

<!-- image -->

Length, area, angles, taxonomy, counts, circle radius, and ellipse semiaxes can be measured manually over an image. The results are being recorded to a simple statistics table, which can be exported to a file or clipboard. Also, the data can be presented as a graph.

- · Run the View &gt; Analysis Controls &gt; Annotations and Measurements command. The manual measurement control panel appears.
- · Select a tool corresponding to the feature you are going to measure. There are several tools for measuring each feature.

- · Measure the objects in the image using mouse.
- · Select where to export results in the Export pull-down menu.
- · Export the results using the Export button.

## Example Procedure

Measurement of the image of a grain:

<!-- image -->

- 1) Select the Vertical parallel lines tool.
- 2) Place the first line on the top edge of the crystal by clicking into the image. The position of the line can be adjusted while you hold the left mouse button down. After you release it, the line is positioned.
- 3) Repeat this to place the second line on the bottom edge of the crystal.
- 4) When finished, an arrow is drawn between the lines, and the result of the measurement is attached. A record with the measurement type and the measured value is added to the results table.

## Working with the Measurement and Annotation Objects

There are two types of vector objects which can be placed over the image: annotation objects and measurement objects.

This button of the right image tool bar turns the visibility of annotation layer ON/OFF. Right-clicking the button displays a context menu with the following options:

- · Clear All Objects will delete annotation and measurement objects.
- · Clear Annotation Objects will delete all annotation objects.
- · Clear Measurement Objects will delete all measurement objects.
- · Select Annotation Objects will select all objects that are not the measurement ones.
- · Select Measurement Objects will select all measurement objects.
- · Select All Objects and Deselect will select/deselect all annotation and measurement objects.

Visibility of annotation/measurement objects In an ND document that contains time dimension, you can set visibility of any annotation object by the following rules:

- · object is visible globally means in all frames in all dimensions - select the option Object is always visible
- · object is visible in all T, Z dimensions, but only in current multipoint - select the option Object is always visible and check the Object belong only to Current Multi Point option
- · object is visible only in selected time frames in all multipoints - select the option Object is visible in range
- · object is visible only in selected time frames in current multipoint - select the option Object is visible in range and check the Object belong only to Current Multi Point option

Select one of these rules in the context menu that appears when you click with right mouse button on an annotation object in the ND document. Detailed definition of object visibility can be done using commands in the Visibility in Time sub-menu.

## 8.5. Object Count

(requires:Automatic Measurement)

The Object Count tool is designed for automated object detection and counting. It enables users to threshold the image, automatically measure the binary objects, and export the measured data to a file in a straightforward way. Object count can be performed even on Live image. Run the View &gt; Analysis Controls &gt; Object Count command to display the control panel.

The recommended workflow through the dialog is to move from left to right, starting with thresholding, then using restrictions and finally reviewing the result and export out of NIS-Elements D to a text file or an MS Excel spreadsheet.

## 8.5.1. Thresholding the Image

<!-- image -->

The threshold limits shall be defined by picking object-typical colors from the image. Select one of the following tools:

- · 1 point threshold tool
- · 3 points circle threshold tool
- · 6 points circle threshold tool

Click inside the image to define typical object areas. The system will detect similar parts of the image and highlight it by color. The threshold limits are indicated in the histogram and can be further modified by dragging the limit lines by mouse.

Please, refer to the 7.3. Thresholding [100] chapter for further details on thresholding.

## 8.5.2. Applying Restrictions

The number of objects that are included in the results table can be restricted by defining limits. Objects which do not fit these limits will be left out of the result table.

<!-- image -->

- · Right click to the restrictions field to select one or more of the available measurement features.
- · Select the restriction feature you would like to define.
- · Move sliders below the histogram to set the limits. The limit values are indicated next to the feature name, and can be modified by double clicking the indicated value.
- · Decide whether the defined interval will be excluded or included - this is done by setting the Inside/Outside option next to the feature name.
- · The nearby check box indicates whether the restriction is currently being applied or not. If applied, the histogram below is color, otherwise it is gray.

<!-- image -->

Note

Infinitude can be defined by entering 'oo' or 'inf'.

Reset The Reset button on the right side discards restriction settings of all features.

Bins This setting determines the number of columns in the histogram.

## Restrictions from the Image

A reference object can be picked from the image and used to set the limit values.

- · Select the restriction feature you would like to set by mouse. Let's assume you have selected Circularity .

- · Right click the thresholded object which is going to be used as source. A context menu appears.
- · Select whether to INCLUDE or EXCLUDE the selected object and all others with higher/lower circularity.
- · The restriction will be applied and indicated by colors within the image.

<!-- image -->

## 8.5.3. Results

The following results appear in the results table:

- · Total Area is the area of the ROI. It is shown in square pixels or square calibration units .
- · Measured Area is the area of the binaries inside the ROI.
- · Number of objects -number of objects after applying restrictions.
- · Table of results - measurement results for each object are displayed in this table. Select the columns to display/hide from the context menu which appears when you right-click one of the column captions.
- · # -number of selected objects is displayed in the left part of the tool bar. One or more objects can be selected by mouse while holding the Ctrl or the Shift key.

<!-- image -->

## Tool Bar

There is a tool bar above the results table which contains the following buttons:

Delete selected objects Removes the selected objects. The objects can be selected by mouse while holding Ctrl .

- Invert selection Deselects objects selected by mouse and vice versa.

<!-- image -->

- Generate binary Erases binary objects which do not meet the restrictions settings.
- Show Object Calatog Opens the Object Catalog control panel with data source automatically set to "Object Count".

Export The measured data can be exported to clipboard or a file using the Export button. Please refer to the 8.11. Exporting Results [146] chapter for further details.

- Save/Load Object Count configuration Invokes a pull-down menu which enables you to load/save the current object count settings from/to an external file (*.counting).

Use Standard EqDia Check this option to enable counting of objects using standard EqDiameter. Value of the standard EqDiameter parameter can be edited in the field nearby.

- Keep updating count Refreshes the measured results each time the binary layer changes (e.g. when the threshold is modified).

## 8.5.4. Object Count Procedure Example

- 1. Open the Object Count control panel. See 8.5. Object Count [122].
- 2. Threshold the image. Use the thresholding picking tools and click on the image to sample areas of interest. These pixels selected will determine what intensity/ part of histogram is considered accepted. The threshold will detect several specs or smaller objects such as noise or background. If desired, the Clean and Smooth filters will exclude smaller objects.
- 3. You can also measure using the defined region of interest (the button) or measurement frame ( the button). Check the options are properly set in the Measure &gt; Options dialog window.
- 4. Apply restrictions. Select Area from the list of available restriction features. Use the sliders in the histogram to specify the lower limit and the upper limit. The lower and upper limit will update in the display.

<!-- image -->

The green area of the histogram represents the accepted range areas. Any object with an area in the green range will be considered an object. Alternatively, any object with an area in the red ranges will not be considered an object.

The outlines of objects on the image differ according to whether the object is restricted or accepted. In this case, accepted objects have a green outline and restricted objects have a blue outline.

To ensure that that count is updating with any change, click the icon:

- 5. Remove any unwanted object from the object count by selecting the Delete Selected Objects icon from the Result section. The object will lose its thresholded overlay and will be excluded from the measurement.

Warning

You cannot Undo this action. To restore an object repeat the original threshold procedure or load a saved Object Count configuration.

- 6. View the result data and export them to a file or spreadsheet application. See 8.11. Exporting Results [146] for further information.

## 8.6. Automated Measurement

(requires:Automatic Measurement)

Automated measurement is the most powerful of image analysis features. In combination with user macros, NIS-Elements D can become a semi- or fully-automatic image analysis tool. There are several key procedures which a proper automated measurement should involve:

- · Optical system calibration (see the 4.1.2. Optical Configurations [40] chapter)
- · Image acquisition (see the 5. Image Acquisition [55] chapter)
- · Defining threshold, creating the binary layer (see the 7.3. Thresholding [100] chapter)
- · Performing the automated measurement
- · Results presentation

## Image Layers Involved in Measurement

The the binary layer and also the color image can get involved in the automated measurement:

- · Binary layer -is typically used for shape and size measurements (area, perimeter, surface fraction).
- · Color layer -intensity or hue measurements are carried out on this layer. The area covered with the binary layer is used as the source data.

## Object/Field Measurement

NIS-Elements D distinguishes two types of automated measurements: object and field.

Object Measurement Groups of neighbouring pixels of the binary layer are called objects. Results of the object measurement are usually the object data such as Length, Area, CentreX/Y (the X,Y position of the central pixel of an object), etc.

Field Measurement Field measurements produce information regarding the whole measurement area (measurement frame, ROI). Such information can be Area Fraction, Mean Brightness, Density Variation, etc.

Please see the complete list of measurement features in the 8.8. Measurement Features [129] chapter.

## Restricting the Area of Measurement

The area of measurement can be restricted by the measurement frame or by a user defined region of interest (ROI).

Region of Interest - ROI ROI is a user defined area of the image. Whenever the ROI is displayed (by the View &gt; Layers &gt; Measurement ROI command), it is also applied to restrict the area of measurement.

Measurement Frame The measurement frame is a re-sizable rectangular frame which serves for bounding the area accepted for measurement. Turn the measurement frame ON via the Measure &gt; Use Measurement Frame command.

Binary objects touching edges of ROI or the measurement frame can be treated differently (excluded from the measurement or included). This behavior can be specified within the Measure &gt; Options window.

## Statistics and Data Presentation

NIS-Elements D calculates basic statistics - mean value, standard deviation and distribution of all measured features. The features to be measured can be selected in the Measure &gt; Object Features and the Measure &gt; Field and ROI Features windows. Results of all automated measurements are

presented and can be exported from the View &gt; Analysis Controls &gt; Automated Measurement Results control panel.

## 8.7. Measurement Options

Run the Edit &gt; Options command and select the Measurement tab.

Rules for Excluding Objects This section regards automatic measurement. Select the options how to treat the objects touching the area borders when you are performing the automatic measurement:

Using Measurement Frame Pick up the option how to treat the object touching the measurement frame. Run the automatic measurement by the Measure &gt; Use Measurement Frame command.

Using ROI Pick up the option how to treat the object touching the ROI frame. Run the automatic measurement by the View &gt; Layers &gt; Measurement ROI command.

Without Measurement Frame and ROI Pick up the option how to treat the object touching the image border. Turn off the measurement frame and ROI and run the automatic measurement.

These options do not affect the field measurement results (field measurement is always applied inside the defined area without exceptions).

Object Colors After the automatic measurement is performed, all measured objects are highlighted by color borders. Here you can select colors for the objects excluded from measurement according to the ROI/measurement frame settings. The Out of limits color will be used to highlight objects which do not fit the applied restrictions ( View &gt; Analysis Controls &gt; Automated Measurement ).

## Manual Measurement

Automatically zoom in Length manual measurements This option zooms the image while placing the measurement points to the image. Only the indicated measurement tools are affected.

Copy manual measurement objects from live image to captured NIS-Elements D enables to

measure manually on live camera signal ( View &gt; Analysis Controls &gt; Annotations and Measurements ). After the Acquire &gt; Capture command is used, the measurement objects in the image are copied (or not) to the captured image according to this setting.

Label The manual measurement objects can be labeled. Select what information will be attached to every manual measurement object in an image.

## 8.8. Measurement Features

(requires:Automatic Measurement)

The following list describes all the features that can be measured within NIS-Elements D Measurements. Suitable type of measurement (object, field, manual) and the required image layer (binary, color/binary) are included in the description.

AcqTime Calling the Grab Sequence command, the AcqTime is set to zero at the beginning. Then, NISElements D assigns the AcqTime to every newly grabbed image file header, which denotes time elapsed

from the beginning of the grabbing. If the Grab Sequence command is not called, than the AcqTime is the time elapsed since the start of NIS-Elements D .

Measurement Type: object, field

Image Type: binary

Area Area is a principal size criterion. In a non-calibrated system, it expresses the number of pixels; in a calibrated one, it expresses the real area.

Measurement Type: object, field, manual

Image Type: binary

Figure 8.12. Area

<!-- image -->

AreaFraction AreaFraction is the ratio of the segmented image area and the MeasuredArea. It has a strong stereological interpretation: in the case of isotropic uniform random sections it is equal to the volume fraction.

AreaFraction = Area/MeasuredArea

Measurement Type: field

Image Type: binary

Figure 8.13. Area fraction

<!-- image -->

Blue Arithmetic mean of pixel intensities of the blue component.

Measurement Type: manual

Image Type: color

BoundsLeft, BoundsRight, BoundsTop, BoundsBottom These are distances (X or Y coordinates) of the left, right, top, and bottom edge of the object bounding rectangle. The units of calibration are used if the image is calibrated. Otherwise, the coordinate value is in pixels.

## Measurement Type: object

Image Type: binary

Figure 8.14. Bounds

<!-- image -->

BoundsAbsLeft, BoundsAbsRight, BoundsAbsTop, BoundsAbsBottom These are absolute distances (X or Y coordinates) of the left, right, top, and bottom edge of the object bounding rectangle within a motorized stage range. This feature can be measured only when a motorized stage is connected.

Measurement Type: object

Image Type: binary

Figure 8.15. BoundsAbs

<!-- image -->

BoundsPxLeft, BoundsPxRight, BoundsPxTop, BoundsPxBottom

These are distances (X or Y coordin-

ates) of the left, right, top, and bottom edge of the object bounding rectangle. Unlike the BoundsLeft,... distance, this value is always in pixels.

Measurement Type: object

Image Type:

binary

BrightVariation It is the usual standard deviation of brightness values.

Measurement Type:

object, field

Image Type:

color/binary

CentreX CentreX is the x co-ordinate of the center of gravity. The units of calibration are used if the image is calibrated. Otherwise, the coordinate value is in pixels.

Measurement Type: object

Image Type: binary

CentreY CentreY is the y co-ordinate of the center of gravity. The units of calibration are used if the image is calibrated. Otherwise, the coordinate value is in pixels.

Measurement Type: object

Image Type: binary

CentreXabs CentreXabs is the absolute x co-ordinate of the center of gravity within a motorized stage range. This feature can be measured only when a motorized stage is connected.

Measurement Type: object

Image Type:

binary

CentreYabs CentreXabs is the absolute y co-ordinate of the center of gravity within a motorized stage range. This feature can be measured only when a motorized stage is connected.

Measurement Type: object

Image Type: binary

CentreXpx CentreXpx is the x co-ordinate of the center of gravity. Unlike the CentreX coordinate, this value is always in pixels.

Measurement Type: object

Image Type: binary

CentreYpx CentreYpx is the y co-ordinate of the center of gravity. Unlike the CentreY coordinate, this value is always in pixels.

Measurement Type: object

Image Type:

binary

Circularity Circularity equals to 1 only for circles; all other shapes are characterized by circularity smaller than 1. It is a derived shape measure, calculated from the area and perimeter. This feature is useful for examining shape characteristics.

Circularity = 4* π *Area/Perimeter 2

Measurement Type: object

Image Type: binary

Class NIS-Elements D recognizes 12 classes (1-12). If you have selected class feature (function Object Features or Field Features), system automatically asks you to specify the class via dialog box. In field or scan objects measurements, the application asks for a class before measurement is performed on the current image. In single object measurement, NIS-Elements D asks for a class for every measured object. In the case you want to pass by, there is a possibility to run the SetClass function.

Measurement Type: object, field, manual

Image Type:

binary

Convexity Indicates convexity of the object edges.

Convexity = Area / Convex Hull Area

Measurement Type: object

Image Type: binary

DensityVariation density values.

## DensityVariation is derived from density values. It is a usual standard deviation of

Measurement Type: object, field

Image Type:

color/binary

EdfSurface EdfSurface is based on 3D model. It determines the surface area of an 3D object.

Measurement Type: object, field

Image Type:

binary, EDF

EdfRoughness EdfRoughness is based on 3D model. It indicates how much the 3D object is rough.

EdfRoughness = EdfSurface/Area

Measurement Type:

object, field

Image Type: binary, EDF

Elongation Elongation is determined as a ratio of MaxFeret and MinFeret features. This feature is useful for shape characteristics.

Elongation = MaxFeret/MinFeret

Measurement Type: object

Image Type:

binary

EqDiameter The equivalent diameter is a size feature derived from the area. It determines the diameter of a circle with the same area as the measured object:

Eqdia = sqrt(4*Area/ π )

Measurement Type: object, manual

Image Type: binary

Figure 8.16. EqDiameter

<!-- image -->

ExPurity This feature specifies the amount of white in the measured color, if the measured color can be composed of white and a pure spectral color.

Measurement Type: object, field, manual

Image Type: color

FillArea In case an object does not contain holes then the FillArea is equivalent to the Area. If an object contains holes, FillArea remains the same while Area is reduced by the area of the holes.

Measurement Type: object

Image Type: binary

Figure 8.17. FillArea

Figure 8.18. Calculation of Hue (H)

<!-- image -->

FillRatio FillRatio is the ratio of Area and FillArea:

FillRatio = Area/FillArea

If an object does not contain holes the FillRatio is equal 1. If an object contains holes, FillRatio is less than 1. This feature can distinguish objects with and without holes.

Measurement Type: object

Image Type: binary

IntensityVariation IntensityVariation is derived from an intensity histogram. It is an usual standard deviation of intensity values. This feature describes the inner structure of an object or a field.

Measurement Type: object, field

Image Type: color

Green Arithmetic mean of pixel intensities of the Green component.

Measurement Type: manual

Image Type:

color

HueTypical HueTypical is the hue value with maximum frequency in a hue value histogram. This feature describes the most frequent hue (color) in an object or field.

Measurement Type:

object, field

Image Type: color/binary

Measurement Type: object, field

Image Type: color/binary

Length Length is a derived feature appropriate for elongated or thin structures. As based on the rod model, it is useful for calculating length of medial axis of thin rods.

Length = (Perimeter + sqrt(Perimeter 2 -16*Area))/4

Measurement Type: object, manual

Image Type: binary

Figure 8.20. Length

<!-- image -->

LineLength Line length is defined as the length of the object with elongated shape.

Measurement Type: object

Image Type:

color/gray

Luminance Luminance is defined as a radiant power weighted by a spectral sensitivity that has characteristics of human vision.

Measurement Type: object, field, manual

Image Type: color

MaxFeret The MaxFeret is the maximal value of the set of Feret's diameters. Generally (for convex objects), Feret's diameter at angle α equals the projected length of object at angle α , α (0,180); NIS-Elements D calculates Feret's diameter for α =0, 10, 20, 30, ..., 180.

Measurement Type: object, manual

HueVariation HueVariation is the usual standard deviation of hue values. This feature describes hue (color) distribution of inner structure of an object or field.

Figure 8.19. Calculation of Hue (H)

<!-- formula-not-decoded -->

Image Type: binary

MaxFeret90 The MaxFeret90 is a length projected across the MaxFeret diameter.

Measurement Type: object, manual

Image Type: binary

Figure 8.21. MaxFeret

<!-- image -->

MaxIntensity MaxIntensity value is derived from the intensity histogram. It is the maximal of intensity pixel values.

<!-- formula-not-decoded -->

Measurement Type: manual

Image Type: color/gray

MeanBlue Arithmetic mean of pixel intensities of the Blue component.

Measurement Type: object, field, manual

Image Type: color/binary

MeanBrightness Arithmetic mean of brightness values of pixels.

Measurement Type: object, field, manual

Image Type: color/binary

MeanDensity Arithmetic mean of density values of pixels.

Measurement Type: object, field, manual

Image Type: color/binary

MeanIntensity MeanIntensity value is derived from the intensity histogram. It is the arithmetic mean of pixel intensities.

<!-- formula-not-decoded -->

Measurement Type: object, field, manual

Image Type:

color/binary

MeanGreen Arithmetic mean of pixel intensities of the Green component.

Measurement Type: object, field, manual

Image Type:

color/binary

MeanChord MeanChord is the mean value of secants in the 0, 45, 90 and 135 degrees directions. It is a derived feature and is calculated from the Area and mean projection according to the following formula.

MeanChord = 4*Area/(Pr 0 +Pr 45 +Pr 90 +Pr 135 )

Measurement Type: object, field

Image Type: binary

MeanRed Arithmetic mean of pixel intensities of the Red component.

Measurement Type: object, field, manual

Image Type:

color/binary

MeanSaturation Arithmetic mean of saturation values of pixels.

<!-- formula-not-decoded -->

Figure 8.25. Calculation of Saturation (S)

<!-- formula-not-decoded -->

Measurement Type: object, field

Image Type: color/binary

MeasuredArea MeasuredArea value is the area of the measurement frame or of a mask within the measurement frame, if the mask status is on.

Measurement Type: object, field

Image Type: binary

MinFeret The MinFeret value is the minimal value of the set of Feret's diameters. Generally (for convex objects), Feret's diameter at angle α equals the projected length of object at angle α , α (0,180); NISElements D calculates Feret"s diameter for α =0,10,20, 30, ..., 180.

Measurement Type: object, manual

Image Type: binary

MinIntensity MinIntensity value is derived from the intensity histogram. It is the minimum of intensity values of pixels.

<!-- formula-not-decoded -->

Measurement Type: manual

Image Type: color/gray

NumberObjects NumberObjectsvalue returns the number of objects in the measurement frame. Exclusion rules for counting objects are taken into account.

Measurement Type: field

Image Type:

binary

Orientation Orientation is the angle at which Feret's diameters have their maximum. The diameters are calculated with 5 degrees angle increment.

Measurement Type: object

Image Type: binary

Figure 8.27. Orientation

<!-- image -->

Perimeter Perimeter is the total boundary measure. It includes both the outer and inner boundary (if there are holes inside an object). The perimeter is calculated from four projections in the directions 0, 45, 90 and 135 degrees using Crofton's formula

Perimeter = π *(Pr 0 +Pr 45 +Pr 90 +Pr 135 )/4

Measurement Type: object, field, manual

## Image Type: binary

Figure 8.28. Perimeter

<!-- image -->

Red Arithmetic mean of pixel intensities of the Red component.

Measurement Type: manual

Image Type: color

Roughness This feature indicates how much the object is rough. '1' means the object roughness is minimal (the object is circular). The feature may acquire values in range &lt;0;1&gt;.

Roughness = Convex hull perimeter / Perimeter

Measurement Type: object, manual

Image Type:

binary

RoughnessInf This feature indicates how much the object is rough. '1' means the object roughness is minimal (the object is circular). The feature may acquire values in range &lt;1;inf&gt;.

RoughnessInf = 1 / Roughness

Measurement Type: object, manual

Image Type: binary

ShapeFactor This parameter is to define whether the object is rough or not.

Shape factor = 4 π (area)/(Convex hull perimeter) 2

Measurement Type: object, manual

Image Type: binary

Figure 8.29. ShapeFactor

<!-- image -->

StartX StartX is the x co-ordinate of a pixel on the object boundary. When you scan the image from the origin as indicated (left-&gt;right), the first pixel of the object you hit is the one with StartX and StartY coordinates.

Measurement Type: object

Image Type: binary

Figure 8.30. StartX

<!-- image -->

StartY StartY is the y co-ordinate of a pixel on the object boundary.

Measurement Type: object

Image Type: binary

StgPosX StgPosX feature is the x co-ordinate of the absolute position of the measured field. It is available only for systems equipped with a stage.

Measurement Type: object, field

Image Type: binary

Figure 8.31. StgPos

<!-- image -->

StgPosY StgPosY feature is the y co-ordinate of the absolute position of the measured field. It is available only for systems equipped with a stage.

Measurement Type: object, field

Image Type: binary

Straightness Feature which shows overall straightness of the object trajectory calculated by formula: End Points Distance / Trajectory Length. Values range is 0.0 - 1.0.

Measurement Type: object, field

Figure 8.32. VolumeEqCylinder

<!-- image -->

<!-- image -->

Image Type: binary

SumBrightness SumBrightness is defined as the sum of brightness in every pixel of the object.

Measurement Type: object, manual

Image Type: color/gray

SumDensity SumDensity is the sum of individual optical densities (O.D.) of each pixel in the area being measured. This feature describes, for instance, the amount of a substance in biological sections. Optical density is evaluated according to the following formula:

O.D. = -log((PixelIntensityValue+0.5/MaxIntensityValue)

Measurement Type: object, field, manual

Image Type:

color/binary

SumIntensity Sum Intensity is defined as the sum of intensity in every pixel of the object.

Measurement Type: object

Image Type: color/gray

SurfVolumeRatio SurfVolumeRatio is a feature with a strong stereological interpretation: if you measure on fields that are sampled systematically and independently of the content of the sections, then the feature is an unbiased estimator of the surface area of objects (inner structure) per volume of the whole sample.

SurfVolumeRatio = (4/ π )*Perimeter/MeasuredArea

Measurement Type: field

Image Type:

binary

Time Time assigns the time to a field (object) after a measurement has been performed. See the SetReferenceTime function help.

Measurement Type: object, field

Image Type: color/binary

VolumeEqCylinder This parameter is based on the rod model. Length is interpreted as height and Width as the base diameter of a cylinder. Bases are considered to be spherical.

VolumeEqCylinder = ( π d 2 )*(l-d)/4 + π d 3 /6,

where l=max(MaxFeret, Length), d=min(MinFeret, Width).

Measurement Type: object

Image Type: binary

VolumeEqSphere Supposing a profile was created as an intersection of a ball and a section that contains the center of the ball. VolumeEqSphere is the volume of the ball.

VolumeEqSphere = π *Eqdia 3 /6

Measurement Type: object

Image Type: binary

Figure 8.33. VolumeWqSphere

Figure 8.34. Width

<!-- image -->

WaveLen Dominant wavelength. This feature is defined as a wavelength of the pure spectral color that is, together with white, the measured color composed of. The color in the purple must be composed of more than one pure spectral colors therefore they have no dominant wavelength.

Measurement Type: object, field, manual

Image Type: color

Width Width is a derived feature appropriate for elongated or thin structures. It is based on the rod model and is calculated according to the following formula:

Width = Area/Length

Measurement Type: object

Image Type: binary

<!-- image -->

## 8.9. Measurement on Graph

<!-- image -->

The following interactive measurements can be performed within graphs.

- Vertical, Horizontal Pick this tool to measure distances within the graph.
- Angle This tool enables selecting an angle and its both line lengths. The resulting number represents a ratio between the projection of the y arrow on y axis and projection of the x arrow on x axis. The resulting number is a dimensionless value. This tool does not allow adjusting the x line length.
- Free Angle This tool measures the same features as the previous angle tool but allows to adjust all of the angle's anchor points.
- Area of Graph This tool enables you to draw a rectangle in the graph. Area will be measured of intersection of the rectangle with the area below the graph curve.
- FWHM This tool measures the Full Width at Half Maximum value on the given graph range.
- x Clear Mesurement Objects Deletes all the measured objects in the graph.
- Reset Data Clears the table with the measurement results.

## 8.10. Pixel Classifier

A typical task for Pixel Classifier may be counting the area of a cross-section of a blood vessel. Since there are at least three different types of tissue whose area should be calculated while background should not be counted at all.

- 1. Eliminate the background. You can:

- define a region of interest. See 7.6. Regions of Interest - ROIs [112] for more information. ·
- · use the method of accepted region. Run the Edit &gt; Region &gt; Region Settings commandfirst. Choose color of the background in the Region Settings dialog that appears. You can fill in the value 0 , which is easy to threshold. Next run the Edit &gt; Region &gt; Accepted Region command. Draw the boundary around the area to keep.

<!-- image -->

Finish drawing with a right click. The image is cropped according to the boundary. Area of image which remained outside the border is deleted and filled with the set background color.

<!-- image -->

- 2. Run View &gt; Analysis Controls &gt; Pixel Classifier to display the classifier panel. Press the Define button and edit all phases you want to detect separately. Use the and buttons and commands in the contextual menu to Add Rename , or Delete any class.
- If you choose the Manual method of classifying, you can manually choose the intensity ranges of all phases.

<!-- image -->

Alternatively, you can sample areas and train the other algorithms to find phase boundaries.

- 3. Once all phases have been defined properly, the settings can be re-used to classify another images.

## 8.11. Exporting Results

Some image analysis data and measurement results can be transferred out of NIS-Elements D so they could be used further. There is a standard Export pull-down menu in some of the control panels (intensity profile, histogram, measurement, etc...) which enables the export.

<!-- image -->

The set of commands of the menu differs according to the type of data (tables or graphs) which can be exported. Click the arrow button to display the pull-down menu. When you select the destination, the

pull down menu hides and the icon of the selected export type appears on the Export button. The export action is performed after the button is pressed once more.

## Export Destinations

It is possible to export tabular data or a graph:

To MS Excel Tabular data can be exported to MS Excel. A new XLS sheet opens and the table is copied to it automatically.

To File Tabular data can be exported to an MS Excel sheet (xls) or a text file (tab delimited txt).

- To Clipboard Data tables and graph images can be exported (copied) to MS Windows clipboard. Then the data or the image can be inserted into any appropriate application (text editor, spreadsheet processor, graphics editor) typically by the Paste command.

To Report Tabular data and graph images can be exported to NIS-Elements D report. If a report is already opened for editing, the data/graph will be appended to it. Otherwise, a new report will be created and the exported data inserted to it.

To Web Browser, To HTML Clipboard Some tabular data can be exported as a HTML table. It can be displayed in a default Internet browser (the Web Browser option), or the HTML code can be copied to Windows clipboard - ready to be inserted to any HTML/text editor.

To Printer Tabular data can be printed directly. This option opens a standard Print dialog window where it is possible to select a printer and print the data.

## Data Export Options

Run the Options command and switch to the Data export tab or press the Settings button within the export pull-down menu. There are two tabs available:

## Global Settings Options

Export into Microsoft Excel application Select this option if you want to export the data to MS Excel application. You can choose if the data will be exported into currently opened file or a new file will be created. Or you can set to export the data to a specific file. If this file does not exist, it will be created. Choose the path and name of the file to be created/opened.

Set the Start at column values (column and row indexes). These values mark the first cell in the MS Excel application which will hold the exported data.

Export text files into folder Select this item if you prefer to export the data to a text file. Press the ... button and specify the target folder and the file name.

Data delimiter Pick up the type (tabulator, space, semicolon) of data delimiter which will be used when exporting data to MS Excel or clipboard.

Append exported data after previous exports If you check this item the existing data will not be overwritten by the new data.

Export also column headers if not appending Include the titles of columns in the files which are being created or overwritten. If the Append exported data after previous exports is selected, no headers will be included in the export.

Active target application after export If you check this item the exported file is opened in the default application (MS Excel or the default text editor) automatically.

Insert empty lines Check this item to allow insertion of empty lines in the exported data.

## Data export Options

You can modify the amount of data included in each export type.The control panels which contain the Export to file functionality are listed in the top pull-down menu. Select the control panel of which the export shall be modified.

Export Name A control panel such as View &gt; Analysis Controls &gt; Annotations and Measurements stores information about the measurement in multiple tables according to the measurement type (area, length, etc.). In this column, you can select the table you would like to modify.

Sheet name In this column you can define an arbitrary name which will be used to name a sheet or a txt file to which the data will be exported.

Options for: This section of the window enables you to select the items to be included/excluded from the selected table during export.

## 9. Creating Reports

## 9.1. Report Generator

Report Generator allows the user to create a print-ready output containing measured data, images, graphs etc. Once you start it by the File &gt; Report &gt; New Blank Report command, a graphical editor appears.

<!-- image -->

Creating of a report is very similar to creating any document in a common text editor in many ways, so you can insert text fields, simple shapes, images, tables or graphs. As well as in the text editors, you can create report templates containing static objects (which do not change) and dynamic objects to be filled with data upon report creation. This comes especially handy in connection with the 12.2. Database [169] module where database fields are loaded to the report(s) automatically.

## Context Menu Commands

Once you insert an object, its appearance, behavior, and position can be changed via the context menu which appears on right-click:

- · If there are more than one objects selected, the Group command makes them to behave as a single object.
- · The Align or Distribute commands enable moving objects within the page or align them with another object(s).
- · The Resize object commands enables to resize two objects to the same size.
- · The Bring to front command changes the order of overlapping objects and brings the current object to front.
- · The Send to back command moves the object to the bottom layer.
- · The Lock command locks the object disabling any further changes to it until it is unlocked.
- · The Properties command opens a window where object properties such as color, background color, border size and color, object size, font, aspect ratio, alignment, and shape can be adjusted.

## 9.2. Report Objects

Whenyoudouble-click any of the report objects, a window appears where the properties can be adjusted. Some properties are common to all types of objects, and some are special.

## Common Properties

- · The precise position can be determined by defining the XY coordinates of the top-left corner of the object.
- · Line and fill colors can be selected.
- · Line widths can be adjusted within the range of 0,25 to 6 pts.
- · Precise width and height of the objects can be adjusted.
- · Rotation of some objects can be adjusted.

Tip

Vector objects (report objects, annotations, interactive measurement objects, ROIs) can be copied by 'drag and drop' while holding the Shift key down.

- 1. Select the object(s).
- 2. Press Shift and drag the object somewhere.
- 3. A copy of the object is placed to where you release the mouse button.

## Special Object Properties

- Ellipse Minor and major axes lengths can be modified.

- Arrow The arrow tip shape and size can be modified.

## Text Box

- · Format of the text can be adjusted like in a standard text editor.
- · The current date and time can be inserted from a pull-down menu.

## Image

- · A new picture can be loaded to the image frame via the Load Picture button.
- · The current image scale is displayed in the properties window. It shows the current scale/original image dimensions ratio (the image must be calibrated to use this feature).
- · A scale bar can be displayed below the image. The position and width of the scale bar can be defined.

## Table

- · Inner and outer borders can be hidden or displayed.
- · Number of rows/columns can be modified.

## Graph

- · The range of displayed values can be limited by defining the min/max values.
- · Histogram labels can be edited.

Insert bar code (requires:Local Option)

It is possible to insert bar-codes to the report.

## Aligning Objects

## Align Objects

You can align two objects to the same horizontal or vertical level.

- 1. Select more objects (e.g. by holding down CTRL and clicking with the left mouse button).
- 2. Right-click one of the selected objects and select the Align or Distribute &gt; Align ... command from the context menu.
- 3. The objects will be aligned as indicated on the command icon.
- 4. If the Relative to Page ( ) option is turned ON , the objects will be aligned to the edges or the center of the page.

## Distribute Objects

Objects of similar size can be distributed uniformly in the horizontal/vertical direction.

- 1. Select three or more objects.

- 2. Right click one of the objects and select the Align or Distribute &gt; Distribute... command from the context menu.
- 3. Distances between the objects will be adjusted to equal.
- 4. If the Relative to Page option is turned ON , the outer objects will be moved to the edges of the page.

## Match Object Sizes

Sizes of objects can be unified too.

- 1. Select two or more objects.
- 2. Right-click the 'master' object to the size of which you want to resize the other objects.
- 3. Select one of the Resize Objects sub-menu commands.

## Dynamic Data

Results of automatic-interactive measurement, graphs, or the current image can be inserted to reports.

- 1. Insert an object which can contain dynamic data (text, picture, table, or graph).
- 2. Right-click the object and select Insert Dynamic Data/Insert Dynamic Picture from the context menu.
- 3. A window appears.
- 4. Select one of the available sources, and click Next .
- 5. Finish the source definition and click OK . The data appear on the report page.

## List of Available Dynamic Data Sources:

- · Data inserted by user ( available for: image, text, table ) - the system will ask you to type a text or browse for an image to insert during the report creation. When creating a dynamic object of this type, a query text which will be used to prompt you for the data can be defined.
- · System data ( available for: text, table ) - enables you to insert some general data such as date, the name of the user account currently logged in, the page number, or the page count.
- · Macro ( available for: text, table ) - enables you to insert expressions, values, or results of a macro.
- · Measurement available for: text, table, graph ( ) - enables you to insert results of automatic/interactive measurement.
- · Database ( available for: image, text, table ) - this data source is displayed only when creating a database report template (see below). It enables you to insert a link to any of the database records.

The real purpose of the dynamic data turns up when creating reports using report templates.

## 9.3. Report Templates

A report template is a layout defining the appearance of future reports, which is ready to be filled with data. The data can be inserted by the user 'on demand' or automatically (dynamic data).

## To Create a Report Template

- 1. Run the File &gt; Report &gt; New Blank Report command. An empty report appears.
- 2. In the Report Generator, select File &gt; Change to Template .
- 3. Edit the report template in the same way as a common report.
- 4. Insert the dynamic data where it is appropriate - measurement results to text boxes or tables, the current image to the image field, etc.).
- 5. Save the report template (*.rtt) via the File &gt; Save command.

## To Create a Report FROM Template

- 1. If the template is opened inside the Report Generator, run the File &gt; Create Report command. Otherwise, use the File &gt; Report &gt; New Report from Template &gt; Browse command inside the main application window to open a template from harddisk.
- 2. A report opens and the dynamic data is inserted automatically.
- 3. Save the report, print it, or export the page(s) to PDF using the commands from the File menu.

## 9.4. Creating Reports from Database

Pictures of a database together with the associated table data, or common images with the associated Image Info can be exported straight to a report.

- 1. Switch NIS-Elements D to Organizer by the View &gt; Organizer Layout command.
- 2. Select one or more images. These images will be inserted to the report.
- 3. Click the Report button on the main tool bar. The following window appears:

<!-- image -->

- 4. In the Columns section, you can select fields, which will be included in the report. If you are exporting images from a database, the database table fields will be listed. If you are exporting images from a directory, image description items will appear.
- 5. The Template portion of the dialog specifies the layout details. If you select the Standard template, images will be organized in rows and columns. It is possible to set the number of columns and rows. If you select the Custom report template, a user report template (*.rtt) can be opened and used for the report creation. If such report does not exist yet, you can create it using the Create New button.

## If You Pressed the Create New Button

- 1. A wizard appears. Select number of columns and rows of the new report template. Click Next .
- 2. Select the paper size, page orientation, and define margins. Click OK .
- 3. An untitled report template opens containing a grid of images spaced according to the columns/rows settings.
- 4. Edit the top-left cell of the image grid. You can change the text/image boxes position, size, and mapping. During report creation, all the other cells of the grid will be filled automatically according to the settings of the first one.
- 5. A custom header or automatic page numbering can be added to the report.

## 10. Macros

## 10.1. Creating Macros

A macro - an executable sequence of commands - can make the work very effective. NIS-Elements D provides a C-like programming language utilizing its internal set of functions. The sequence of functions can be created either by recording the performed actions, by writing the functions within the macro editor, or by modifying the command history (the history is recorded automatically during the work). The macro can be saved to an external (*.mac) file for later use.

## Recording a Macro

The fastest way to create a macro is to record it.

- · Start the NIS-Elements D macro recorder by selecting the Macro &gt; Record command.
- · Perform the series of actions you would like to record.
- · Finish the recording by the same command again (its name changes to 'Stop Recording')

<!-- image -->

- · It is recommended to check the macro in the macro editor before saving. Run the Macro &gt; Edit command to display it.
- · Save the macro to a file via the Macro &gt; Save As command.

## Creating a Macro from History

You can create a macro using the list of recently performed commands.

- 1) Run the Macro &gt; History command to display the Command History control panel:

<!-- image -->

- 2) Push the Create Macro button.
- 3) Select what portion of the command history will be used in the macro:

<!-- image -->

Selection This option will use only commands which you have previously selected by mouse within the Command History window. Group selection (holding Shift or Ctrl ) is available.

Whole History All commands listed in the Command History window will be used for the new macro.

- 4) After you selected one of the options, the macro editor appears containing the new macro source code. Use the editor to fine-tune it.

Note

The Remove Redundant command is automatically performed before the macro is opened in the editor.

## Writing/Editing a Macro

If you posses programmers skills, a macro can be written by hand in the built-in macro editor. Run the Macro &gt; Edit command to display it.

<!-- image -->

The macro editor provides:

- · Undo/Redo functionality.
- · Command insertion from the list of available commands.
- · Interactive command names list. Press Ctrl+Space to display a simplified list of all commands while typing the macro.
- · Syntax hints (parameter types and names) appear as you type a command name.
- · Bookmarks can be placed to the code so you can easily roll to the important parts of the macro.
- · Breakpoints can be placed to the code. A breakpoint forces the macro to stop the execution at a certain point so you can check the state of variables and therefore inspect the macro functionality thoroughly.
- · Syntax highlighting.
- · Help on commands with detailed description.
- · Use the Save Macro and the Save Macro As commands in the macro editor to save the created macro.

NIS-E automatically remembers the folder from where the macros were run the last time and will open this folder when user clicks on Open/Save command in Macro menu.

## 10.2. Running a Macro

NIS-Elements D provides several ways to run a macro.

- · You can run the current macro loaded to NIS-Elements D by choosing the Macro &gt; Run command or by pressing F4 .
- · A hotkey combination (Ctrl+Alt+1,2,3 ... 9) can be assigned to it in the Macro &gt; Options window.
- · You can run a macro at the beginning of the NIS-Elements D session, by assigning the StartUp flag to the macro in the Macro &gt; Options window.
- · You can run a macro saved to a disk by using the Macro &gt; Run Macro From File command.
- · A tool bar button can be assigned to run a macro. See 3.6. Modifying Tool Bars [31].

## Breaking the Macro

The macro execution can whenever be stopped by pressing the Ctrl+Break key shortcut.

## 10.3. Macro Language Syntax

Specifies the NIS-Elements D Macro Language features.

## Variable types

The following data types are implemented:

char text char8 &lt;-128, 127&gt; byte &lt;0, 255&gt; int &lt;-32768, 32767&gt; word &lt;0, 65535&gt; long &lt;-2 147 483 648, 2 147 483 647&gt; dword &lt;0, 4 294 967 295&gt; double &lt;1.7E +/- 308 (15 digits)&gt;

## Structures and Unions

Structures and unions are not supported.

## Arrays

One and two dimensional arrays are supported.

## Local and Global Variables

You should declare local variables at the beginning of macro or function only. You should declare global variables only at the beginning of macro. You can run two nested macros declaring the same global variables, but they must be of the same type. You can declare global variables by prefixing the declaration global . Eg.:

```
global int Number_Rows; global char buffer[200];
```

The 'global' keyword in front of the variable definition assigns the variable to the global scope. Such variable is then accessible from all function scopes within the macro interpreter.

## Statements Supported

for The for statement lets you repeat a statement a specified number of times.

Syntax

```
for([init-expr]; [cond-expr]; [loop-expr])
```

```
statement
```

First, the initialization (init-expr) is evaluated. Then, while the conditional expression (cond-expr) evaluates to a non zero value, Statement is executed and the loop expression (loop-expr) is evaluated. When condexpr becomes 0, control passes to the statement the following the for loop.

while The while statement lets you repeat a statement until a specified expression becomes false.

Syntax

while(expression) statement

First, the expression is evaluated. If expression is initially false, the body of the while statement is never executed, and control passes from the while statement to the next statement in the program. If expression is true (nonzero), the body of the statement is executed and the process is repeated.

if, else Conditionally executes a statement or group of statements, depending on the value of an expression.

```
Syntax if(expression) statement1 [else statement2]
```

The if keyword executes statement1 if expression is true (nonzero); if else is present and expression is false (zero), it executes statement2. After executing statement1 or statement2, control passes to the next statement.

goto Transfers control of the program execution.

```
Syntax goto name; . . . name: statement
```

You cannot use goto to jump inside the block from outside. E.g. following is not allowed:

```
goto label; if(k>5) { label: DilateBinary(3, 5); FillHoles(); }
```

You cannot use goto to jump out from the block more then 2 block levels down. E.g. the following is not allowed:

```
for(i=0; i<64; i=i+1) { for(j=0; j<64; j=j+1) { if(a[i] > b[i]) { value = i;
```

```
goto end; // crossing 3 right brackets } } } end
```

break Terminates the execution of the nearest enclosing statement.

Syntax

break;

The break keyword terminates the execution of the smallest enclosing for or while statement in which it appears. Control passes to the statement that follows the terminated statement.

continue Passes control to the next iteration of the statement in which it appears.

```
Syntax continue;
```

The continue keyword passes control to the next iteration of the for or while statement in which it appears. Within a while statement, the next iteration starts by reevaluating the expression of the while statement. Within a for statement, the first expression of the for statement is evaluated. Then the compiler reevaluates the conditional expression and, depending on the result, either terminates or iterates the statement body.

## Statements Not Supported

do, switch, case, default, typedef These statements are not supported.

## Directives

Following directives are supported by the system.

define The #define directive assigns a meaningful name to a constant in a program.

```
//Syntax #define identifier token-string
```

The directive substitutes token-string for all subsequent occurrences of the identifier in the source file. Token-string can be a value or a string (only for 32-bit version of NIS-Elements D ).

```
//Example #define ERROR_SPRINTF 0 #define MAINDIR "c:\Images"
```

```
int main() { char buf[256]; int retval; retval = sprintf(buf, "%s", "MAINDIR"); if(retval == ERROR_SPRINTF) Beep(); else WaitText(0., buf); return TRUE; } \
```

include Specifies the name of the file to be included.

```
//Syntax
```

```
#include filename
```

The #include directive includes the contents a file with a specified filename in the source program at the point where the directive appears.

```
Example // if you do not specify the full path, NIS-Elements assumes, that \ it is a relative path to a main directory #include "macros\my_macro.h" #include "c:\NIS-Elements\macros\my_macro1.h"
```

import The #import directive is used to incorporate information from an external library.

```
//Syntax #import("DLLname"); #import function_declaration
```

NIS-Elements can call functions from external DLL's. You should import the DLL, where the functions resides and then make a declaration of the functions. You should not import the following system DLL's: kernel32.dll, user32.dll, gdi32.dll, com32.dll, comdlg32.dll. This feature is available only for 32 bit version of NIS-Elements .

```
//Example #import("luc_13.dll"); #import int RTF_ReplaceVariables(LPSTR destfile, LPSTR sourfile);
```

- #import int RTF\_FindQuestion(LPSTR sourfile, LPSTR question, long \ *length, LPSTR defvar); #import int RTF\_ReplaceQuestion(LPSTR destfile, LPSTR sourfile, LPSTR \ replacement);

## Operators

The following operators are supported by the system. If an expression contains more than one operator, the order of operations is given by the priority of operators. Following operators have higher priority then the others: / * % . You should use brackets to define evaluation order other than implemented in NISElements , which is: from right to the left.

## arithmetic operators

- + Addition
- -Subtraction
- * Multiplication
- / Division

## assignment operators

The assignment operator assigns the value of the right operand to the left operand.

- = Addition

## bitwise operators

The bitwise operators compare each bit of the first operand to the corresponding bit of the second operand. The following bitwise operators are supported.

- &amp; Bitwise AND
- | Bitwise OR
- ~ One's complement

## pointer operators

- &amp; Address of ?
- * Indirection

## relational operators

- &lt; Less than
- &lt;= Less than or equal to
- &gt; Greater than

&gt;= Greater than or equal

==

!=

```
Equal Not equal
```

## logical operators

The logical operators perform logical operations on expressions. The following logical operators are supported:

&amp;&amp; Logical AND

|| Logical OR

! Logical NOT

## Expression evaluator

Expression evaluator support the precedence of operators / * % . It evaluates the expression strictly from right to left, so you need to use brackets.

## C-like functions

The system can interpret your own C - like functions. An entry point to program is the main() function in your macro. If main() is not presented, for backward compatibility, the body of the macro is also considered as "main function". The new macros should use main() as an entry point.

The general C-like functions (also called interpreted functions, as opposed to basic, system functions from NIS-Elements or LUC32\_1.DLL) have the following syntax.

Syntax

```
int MyFunction(int a, LPSTR str, double d) { int retval; . . . return retval;
```

```
}
```

Return Value The return value can be any basic data types (char, int, word, dword, int, double or pointer).

Parameters Parameters can be any basic data types (char int, word, dword, int, double or pointer).

Note

Int and double parameters are automatically converted to string type, when they are assigned to text variable, or are one of the parameters of a function.

```
Example int main() { char buf[256];
```

```
my_function1(buf); WaitText(0., buf); return TRUE; } int my_function1(char *buf) { strcpy(buf, "This function has a pointer to char array as a \ parameter"); return TRUE; }
```

## 10.4. Controlling Cameras by Macro

Every camera can be controlled from within a macro by changing its properties. There is a CameraGet\_* and CameraSet\_* macro function available for each camera property (e.g. CameraGet\_ExposureTime();). The number of functions (beginning with CameraSet\_ and CameraGet\_) and their actual names depend on the type of camera(s) you have currently connected to NIS-Elements D .

CameraGet\_ The CameraGet\_... functions retrieve current values of the properties determined by the function name postfix. So the CameraGet\_Exposure(int Mode, double *Exposure); function retrieves the current value of Exposure of the specified Mode.

CameraSet The CameraSet\_... functions allows you to adjust camera properties. So the CameraSet\_Ex-posure(int Mode, double *Exposure); function sets a new Exposure value for the specified Mode.

## How To Set Camera Properties

Instead of describing each property function, it is better to show you a universal way to handle a camera by macro:

- 1) Display the View &gt; Acquisition Controls &gt; *Camera* Settings control panel and find the property you would like to control.
- 2) Make a change of the property from within the control panel. For example, change the exposure time.
- 3) Display the View &gt; Macro Controls &gt; Command History window and see the last function which has been called and its parameters (e.g. CameraSet\_ExposureTime(1, 500);). This is the function you will control the exposure time with.
- 4) Experiment with the camera control panel in order to determine the right parameter values of the functions to be called within your macro.

## 10.5. Interactive Advanced Macro (API)

(requires:Interactive Advanced Macro (API))

If the API module is installed, it dramatically extends the macro programing capabilities. It adds the following functionality to the main application:

User interaction functions Contains functions, which enable interaction with user like: type value, text, combo boxes, list boxes and many other Windows standard controls with easy and intuitive code handling.

Support of importing functions from external DLLs Functions from external DLLs can be imported at the start of the macro and used during the macro execution.

## Directives (only for 32bit operating systems)

\_\_underC The \_\_underC directive assigns a function to be interpreted by the UnderC engine instead of the standard interpreter.

//Syntax

```
__underC int inter_sharpen(int cols, int rows) { }
```

#importUC The #importUC directive imports an API function to the UnderC engine so that it can be used from within there.

//Syntax

#importUC DisplayCurrentPicture;

## 10.6. Macro Preferences

This window enables you to configure key shortcuts to macros and set a macro to run automatically on startup. Run the Edit &gt; Options command and switch to the Macro tab.

Macros Lists of macros that can be executed using hot keys or automatically at the beginning of the NIS-Elements D session.

Start Up To launch a macro automatically after starting the NIS-Elements D program, select it and press the StartUp button. StartUp field of the selected macro in the list box is filled.

Hot Key To assign a hot key to a macro, select the macro in the macro list box and press the Hotkey button. Select one of the pre-defined key combination and press OK button.

Full Path Shows the full pathname of the selected macro.

Add Adds a macro to the macro list box. Select Macro dialog box appears and you can search the disk for the macro.

Remove Removes a selected macro from the macro list box.

Edit Enables to edits a selected macro from the macro list box.

Filename substitution These lines display the current values of substitution strings available in macro commands.

- # Letter representing a drive e.g. 'C'
- ## A customizable path e.g. 'C:\Images'

### Path to a directory according to the macro function used. It leads to the folder where NIS-Elements EXE file is placed and to a subdirectory - 'Images' for functions concerning image files or 'macros' for functions concerning macros. E.g.:

```
ImageOpen("###\agnor.tif"); //leads to the IMAGES subdir RunMacro("###\macro_001.mac"); //leads to the MACROS subdir
```

####, ##### The current filename including/excluding the path. These substitutions can be used with the Sequences or SequencesEx macro commands.

Information Shown in Caption Optionally, the name of the current macro and an arbitrary user text can be displayed in the NIS-Elements D caption.

Defaults for this Page Restores the default setting for Macro Options.

## 11. Movies

## 11.1. Capturing AVI Movie

- 1. Display the AVI Acquisition control panel by the Acquire &gt; AVI Acquisition command.
- 2. Adjust the advanced settings, especially define the file name and the destination folder.
- 3. Click the Record button. The live image appears and recording starts according to the settings.
- 4. Stop recording by the Stop button, or wait until the time defined in the Duration field passes.
- 5. When stopped, the AVI file remains opened in a new image window.

## 11.2. Save ND2 as AVI

You can easily create an AVI movie from an nd2 file. Run the File &gt; Save As command and select the AVI format in the Save As Type pull-down menu. The Save As window expands as follows:

<!-- image -->

Adjust the AVI file settings and press Save to finish. Please see the File &gt; Save As command description for more details.

## Note

If you have the QuickTime Player installed on your PC, a QuickTime movie (*.mov) can be created as well.

See also 11.3. About Video Compression [167].

## 11.3. About Video Compression

It is common to encode (compress) movies in order to save some disk capacity. This can be done using various types of codecs. A video codec is a software tool which can code (compress) and decode (de-

compress) video files. Remember that the codec you use to save the video will be required for playback as well (when playing the video on other computers).

Look at the list of codecs coming with NIS-Elements D by default. If other codecs are installed on the computer, they become also available to NIS-Elements D .

## Caution

32bit operating systems provide better choice of codecs because a 64bit codec must be used on a 64bit operating system, but there are not many of those in the meantime.

## NIS-Elements D compression options

We performed a test by converting a 1 GB / 4000 frames ND2 file to AVI using different codecs. The results are displayed in the list:

No compression Original quality, file size: 787 MB.

DV Video Encoder This codec produces only videos with 640 x 480 resolution. Videos with other resolutions are stretched to fit, therefore we do not recommend to use this codec.

MJPEG Compressor Very good quality, 240 MB.

Cinepack Codec by Radius Average quality, file size: 70 MB.

Intel IYUV codec Very good quality, file size: 390 MB. Provides the best quality / compression rate.

Microsoft RLE Very poor quality, file size: 90 MB.

Microsoft Video 1 Very poor quality, file size: 6 MB.

## 12. Additional Modules

## 12.1. Automatic Measurement

This module extends the measurement abilities of NIS-Elements D by adding number of automatic processing features. Particularly, it enables users to threshold the image, create a separate binary layer, and process it. See also 8.6. Automated Measurement [127]

## 12.2. Database

If the database module was installed, the system can create and control MS Access databases (*.MDB). A database can help you to efficiently organize your image archives and manage additional information related to the images. The images themselves are stored on hard disk, only links to them and the additional data are stored in the database file.

Please see 6.8. Database [88] and 2.1.9. Installing the Database Module on 64-bit Systems [11].

## 12.3. Extended Depth of Focus

The EDF module allows you to combine an existing Z-stack of images into one focused image by picking the focused regions from each frame and the pieces together.

## 12.4. Filters Particle Analysis

(requires:Local Option)

This module is aimed at analysis of filters according to the ISO 16232 standard.

Please see the electronic help for more details.

## 12.5. HDR

The High Dynamic Range module brings the functionality of creating HDR images within NIS-Elements D .

## 12.6. Industrial GUI

After the Industrial GUI module is installed, the View &gt; SimpleControl command is added to the application. The command activates a simple layout intended to be used in industry imaging applications.

## See 3.10. Simplified User Interface [35]

## 12.7. Interactive Advanced Macro (API)

This module dramatically extends the macro programing capabilities, it:

- · adds a set of user-interaction macro functions
- · allows importing functions from external DLLs

See 10.5. Interactive Advanced Macro (API) [165].

## 12.8. Live Comparisons

This module provides several comparison modes which can help to identify and visualize differences or similarities between two images.

## 12.9. Local Option

Local Option is a pseudo-additional module. When Local Option is installed (see Step 2 [6]), NIS-Elements D will provide some advanced features which did not pass the quality assurance procedure yet. We recommend to wait until they are released officially.

## 12.10. Metalo - Cast Iron Analysis

After the module installation, a new item called Metallography appears in the Applications menu. Select the Cast Iron command to display the cast iron measurement layout.

## 12.11. Metalo - Grain Size Analysis

After the module installation, a new item called Metallography appears in the Applications menu. Select the Grain Size command to display the grain size measurement layout.

## General Index

## A

| A multi-channel image containing 11 channels, 74    |
|-----------------------------------------------------|
| A T/Z/multi-channel image., 74                      |
| About ND Acquisition (Image Acquisition), 59        |
| About Organizer (Displaying Images), 84             |
| About Video Compression (Movies), 167               |
| Adding Buttons to the Left Tool Bar, 32             |
| Additional Module/Device Installation (Installation |
| and Settings), 9                                    |
| Additional Modules, 169                             |
| Adjust the Camera Settings, 40                      |
| Settings), 19                                       |
| Advanced Mode, 85                                   |
| Align Objects, 151                                  |
| Aligning Objects, 151                               |
| Another instance running, 13                        |
| Appearance Options (User Interface), 34             |
| Apply the new policies, 13                          |
| Applying Restrictions (Measurement), 123            |
| Area, 130                                           |
| arithmetic operators, 162                           |
| Arranging User Interface (User Interface), 28       |
| Arrays, 158                                         |
| Assigning Colors to Channels (Displaying Images),   |
| 73                                                  |
| Assigning Objective to a Nosepiece Position (Cam-   |
| eras &amp; Devices), 43                                 |
| assignment operators, 162                           |
| Auto Scale Settings, 81                             |
| Auto-calibration window, 46                         |
| Auto-Detect Tool (Image Analysis), 114              |
| Automated Measurement (Measurement), 127            |
| Automatic Calibration, 45                           |
| Automatic Measurement (Additional Modules), 169     |
| Available Logical Devices, 48                       |
| AWB, 81                                             |

## B

| Basic Mode, 85                          |
|-----------------------------------------|
| Basic Workflows (Cameras &amp; Devices), 39 |
| Behavior (User Interface), 36           |

| Binary Layer (Image Analysis), 108       |
|------------------------------------------|
| Binary Layer Color and Transparency, 108 |
| Binary Operations, 103                   |
| bitwise operators, 162                   |
| BoundsAbs, 131                           |
| Breaking the Macro, 157                  |

## C

| C-like functions, 163                               |
|-----------------------------------------------------|
| Calculation of Hue (H), 134, 135                    |
| Calculation of Intensity (I), 136, 137, 138         |
| Calculation of Saturation (S), 137                  |
| Calibrate Using Objective, 47                       |
| Calibrating an Uncalibrated Image, 117              |
| Calibration (Measurement), 117                      |
| Camera Control Panel (User Interface), 37           |
| Camera ROI (Image Acquisition), 57                  |
| Camera ROI Definition, 58                           |
| CameraSelection on Startup (Cameras &amp; Devices),     |
| 39                                                  |
| Camera Settings (Cameras &amp; Devices), 51             |
| Cameras &amp; Devices, 39                               |
| Changing Appearance of the Threshold Layer, 103     |
| Channel Tabs, 28                                    |
| Chroma (C) definition, 137                          |
| Closing Another Instance of NIS-Elements (Installa- |
| tion and Settings), 13                              |
| Closing Images (Displaying Images), 93              |
| Command Line Installation Options (Installation     |
| and Settings), 9                                    |
| Command Line Startup Options, 1                     |
| Command line switches syntax, 1                     |
| Common ND Experiment Options, 59                    |
| Common Properties, 150                              |
| Connecting a Device to NIS-Elements (Cameras &amp;      |
| Devices), 47                                        |
| Connectivity (Image Analysis), 110                  |
| Context Menu Commands, 149                          |
| Control Bar (Displaying Images), 74                 |
| Controlling Cameras by Macro (Macros), 164          |
| Devices), 54                                        |
| Copying Channels by Drag and Drop (Displaying       |
| Images), 74                                         |

| Creating a Macro from History, 155                 |
|----------------------------------------------------|
| Creating a Shared Layout (Installation and Set-    |
| tings), 12                                         |
| Creating Macros (Macros), 155                      |
| Creating New Optical Configuration, 40             |
| Creating new user, 15                              |
| Creating Reports, 149                              |
| Creating Reports from Database (Creating Reports), |
| 153                                                |

## D

| Data Export Options, 147                           |
|----------------------------------------------------|
| Data export Options, 148                           |
| Database (Additional Modules), 169                 |
| Database (Displaying Images), 88                   |
| Database Backup (Displaying Images), 90            |
| Database Tables (Displaying Images), 89            |
| Database View within Organizer (Displaying Im-     |
| ages), 90                                          |
| Device Updates (Installation and Settings), 10     |
| Dilation, 111                                      |
| Directives, 160                                    |
| Directives (only for 32bit operating systems), 165 |
| Disable layout modification, 13                    |
| Displaying Image Layers (Displaying Images), 72    |
| Displaying Images, 69                              |
| Distribute Objects, 151                            |
| Docking Panes (User Interface), 25                 |
| Drawing Style, 100                                 |
| Drawing tools (Image Analysis), 108                |
| Dynamic Data, 152                                  |

## E

| EqDiameter, 133                               |
|-----------------------------------------------|
| Erasing Single objects, 109                   |
| Erosion, 111                                  |
| Example, 107                                  |
| Example of the warning message, 46            |
| Example Procedure, 121                        |
| Export (Image Analysis), 98                   |
| Export Destinations, 147                      |
| Exporting Results (Measurement), 146          |
| Expression evaluator, 163                     |
| Extended Depth of Focus (Additional Modules), |
| 169                                           |

## F

| Features Available in the Database View, 91         |
|-----------------------------------------------------|
| FillArea, 134                                       |
| Filters Particle Analysis (Additional Modules), 169 |
| Fixed Grabber Startup, 2                            |
| Fixes (Installation and Settings), 11               |
| Functions applied subsequently, 112                 |

## G

| General (Installation and Settings), 20            |
|----------------------------------------------------|
| General Index, 171                                 |
| Global Settings Options, 147                       |
| Graph Memorizing (Image Analysis), 99              |
| Graticules Density, 119                            |
| Grouping of Images, 88                             |
| Groups tab, 17                                     |
| Groups Tab Options (Installation and Settings), 17 |

## H

| Handling Control Panels, 25                                |
|------------------------------------------------------------|
| Hardware key, 10                                           |
| HDR (Additional Modules), 169                              |
| Hiding Toolbar Buttons, 31                                 |
| Histogram (Image Analysis), 97                             |
| Histogram Options (Image Analysis), 100                    |
| Histogram Options Window, 100                              |
| Histogram Scaling (Image Analysis), 99                     |
| Home Position, Range, 67 How to capture a single image, 55 |
| How To Set Camera Properties, 164                          |
| How to setup a shading correction, 57                      |
| How to use the histogram to threshold an image,            |
| 102                                                        |
| How to use the picker tool to threshold an image,          |
| 102                                                        |
| HSI Mode (Image Analysis), 103                             |

## I

| If You Pressed the Create New Button, 154         |
|---------------------------------------------------|
| Image acquired and corrected, 57                  |
| Image acquired without the shading correction, 56 |
| Image Acquisition, 55                             |
| Image Analysis, 97                                |
| Image Filter (Displaying Images), 85              |
| Image Layers (Displaying Images), 71              |
| Image Layers Involved in Measurement, 128         |

| Image Types (Displaying Images), 72                   |
|-------------------------------------------------------|
| Image Window (User Interface), 27                     |
| Industrial GUI (Additional Modules), 169              |
| Inhomogeneous illumination, 56                        |
| Install Local Options, 6                              |
| Installation, 5                                       |
| Installation and Settings, 5                          |
| Installation and Updates (Installation and Settings), |
| 5                                                     |
| (Installation and Settings), 11                       |
| Intensity Mode (Image Analysis), 104                  |
| Interaction with ROIs (Image Analysis), 113           |
| Interactive Advanced Macro (API) (Additional Mod-     |
| ules), 170                                            |
| Interactive Advanced Macro (API) (Macros), 165        |
| Introduction to Image Acquisition (Image Acquisi-     |
| tion), 55                                             |
| Introduction to Image Layers (Displaying Images),     |
| 71                                                    |

## L

| Large Image (Covering) Multi-Point (Image Acquisi-   |    |
|------------------------------------------------------|----|
| tion), 64                                            |    |
| Large Images (Displaying Images), 77                 |    |
| Layout Manager (User Interface), 30                  |    |
| Layout Manager Tools, 30                             |    |
| Layout tabs, 29                                      |    |
| Layouts (User Interface), 29                         |    |
| Legend:, 62, 63                                      |    |
| Length, 135                                          |    |
| Line-length Calibration, 118                         |    |
| List of Available Dynamic Data Sources:, 152         |    |
| List of Layouts, 30                                  |    |
| Live Comparisons (Additional Modules), 170           |    |
| Local and Global Variables, 158                      |    |
| Local Option (Additional Modules), 170               |    |
| Local Options installation, 6                        |    |
| Locating XY Positions Between Images (Displaying     |    |
| Images), 78                                          |    |
| logical operators, 163                               |    |
| Login As, 14                                         |    |
| LUTs (Look-Up Tables) (Displaying Images), 79        |    |
| LUTs on Monochromatic Images (Displaying Im-         |    |
| ages), 82                                            |    |
| 84                                                   | 84 |

| LUTs on RGB Images (Displaying Images), 80   |
|----------------------------------------------|
| LUTs Tools, 80                               |
| LUTs window on two-channel image, 84         |

## M

| Macro Language Syntax (Macros), 157                |                                                   |
|----------------------------------------------------|---------------------------------------------------|
| Macro Preferences (Macros), 165                    |                                                   |
| Macros, 155                                        |                                                   |
| Main Menu (User Interface), 24                     |                                                   |
| Main View, 76                                      |                                                   |
| Main Window Components (User Interface), 24        |                                                   |
| Managing Objectives (Cameras &amp; Devices), 42        |                                                   |
| Managing Optical Configurations, 41                |                                                   |
| Manual Calibration, 44                             |                                                   |
| Manual Measurement (Measurement), 120              |                                                   |
| Match Object Sizes, 152                            |                                                   |
| Mathematical Morphology Basics (Image Analysis),   |                                                   |
| Mathematical Morphology Examples (Image Ana-       |                                                   |
| lysis), 111                                        |                                                   |
| MaxFeret, 136                                      |                                                   |
| MCH Mode (Image Analysis), 104                     |                                                   |
| Measure the Image, 119                             |                                                   |
| Measurement, 117                                   |                                                   |
| Measurement Features (Measurement), 129            |                                                   |
| Measurement on Graph (Measurement), 143            |                                                   |
| Measurement Options (Measurement), 129             |                                                   |
| Metalo - Cast Iron Analysis (Additional Modules),  | Metalo - Cast Iron Analysis (Additional Modules), |
| 170                                                |                                                   |
| Metalo - Grain Size Analysis (Additional Modules), |                                                   |
| Modifying Menus (User Interface), 33               | Modifying Menus (User Interface), 33              |
| Modifying the Layout Settings, 30                  |                                                   |
| Modifying the Main Menu, 33                        | Modifying the Main Menu, 33                       |
| Modifying Tool Bars (User Interface), 31           |                                                   |
| Motorized Stage Initialization, 50                 |                                                   |
| Movies, 167                                        | Movies, 167                                       |
| Multi-channel Images, 72                           |                                                   |
| Multi-point Acquisition (Image Acquisition), 63    |                                                   |
| Multiple Binary Layers, 109                        |                                                   |

## N

| Navigation in ND2 Files (Displaying Images), 74   |
|---------------------------------------------------|
| ND Sequence Options, 60                           |
| ND Views (Displaying Images), 76                  |
| ND2 Information (Displaying Images), 77           |
| New Connection (Displaying Images), 89            |

| New Database (Displaying Images), 88               |
|----------------------------------------------------|
| NIS-Elements authentication (Installation and Set- |
| tings), 12                                         |
| NIS-Elements D compression options, 168            |
| NIS-Elements Installation Steps (Installation and  |
| Settings), 5                                       |
| NIS-Elements Preferences (Installation and Set-    |
| tings), 19                                         |

## O

| Object Count (Measurement), 122                     |
|-----------------------------------------------------|
| Object Count Procedure Example (Measurement),       |
| 126                                                 |
| Object/Field Measurement, 128                       |
| Objective Calibration (Cameras &amp; Devices), 43       |
| Objectives (Cameras &amp; Devices), 42                  |
| Open and Close, 111                                 |
| Opening Files in Progressive Mode (Displaying Im-   |
| ages), 77                                           |
| Opening Image Files (Displaying Images), 69         |
| Operating with Images, 91                           |
| Operations with Images within Organizer (Displaying |
| Images), 86                                         |
| Operations with Optical Configurations, 41          |
| Operators, 162                                      |
| Optical Configurations (Cameras &amp; Devices), 40      |
| Images), 70                                         |
| Organizer (Displaying Images), 84                   |
| Orientation, 138                                    |

## P

| Perimeter, 139                                      |
|-----------------------------------------------------|
| Pixel Classifier (Measurement), 143                 |
| Pixel Size Calibration, 118                         |
| Playing Controls, 74                                |
| Playing options, 75                                 |
| Point by Point (Manual) Multi-Point (Image Acquis-  |
| ition), 63                                          |
| pointer operators, 162                              |
| Predefined Camera ROI, 59                           |
| Preprocessing (Image Analysis), 97                  |
| Preview Control Panel (User Interface), 38          |
| Privileges tab, 18                                  |
| Privileges Tab Options (Installation and Settings), |
| 18                                                  |

| Processing On: Intensity/RGB/Channels (Image   |
|------------------------------------------------|
| Analysis), 97                                  |

## Q

## R

| Random Multi-Point (Image Acquisition), 64        |                                          |
|---------------------------------------------------|------------------------------------------|
| Recording a Macro, 155                            |                                          |
| Regions of Interest - ROIs (Image Analysis), 112  |                                          |
| Renaming of devices, 48                           |                                          |
| Repetition issues, 111                            |                                          |
| Report Generator (Creating Reports), 149          |                                          |
| Report Objects (Creating Reports), 150            |                                          |
| Report Templates (Creating Reports), 153          |                                          |
| Reset of password, 16                             |                                          |
| Resizing the Organizer Panes (Displaying Images), |                                          |
| 88                                                | 88                                       |
| Restricting the Area of Measurement, 128          | Restricting the Area of Measurement, 128 |
| Restrictions, 103                                 | Restrictions, 103                        |
| Restrictions from the Image, 124                  |                                          |
| Results (Measurement), 125                        |                                          |
| RGB Images, 72                                    |                                          |
| RGB Mode (Image Analysis), 100                    |                                          |
| Rough Measurement (Measurement), 119              |                                          |
| Running a Macro (Macros), 157                     |                                          |
| Running a Macro Upon Layout Change (User Inter-   |                                          |
| face), 34                                         |                                          |

## S

| Sample Database Installation (Installation and   |
|--------------------------------------------------|
| Settings), 10                                    |
| Save Control Panel (User Interface), 37          |
| Save ND2 as AVI (Movies), 167                    |
| Save Next Options (Displaying Images), 92        |
| Saving Image Files (Displaying Images), 91       |
| Saving Images with UAC (Displaying Images), 92   |
| Select Camera Driver, 39                         |
| Select Graticule Type, 119                       |
| Selecting a Camera, 39                           |
| Set layout visibility, 13                        |
| Setting Software Limits to Stage Movement, 50    |
| Setting Up the Camera, 39                        |
| Shading Correction (Image Acquisition), 56       |
| ShapeFactor, 139                                 |

| Simple ROI Editor (Image Analysis), 114         | Simple ROI Editor (Image Analysis), 114         |
|-------------------------------------------------|-------------------------------------------------|
| Simple ROI Editor toolbar, 114                  | Simple ROI Editor toolbar, 114                  |
| Simplified User Interface (User Interface), 35  | Simplified User Interface (User Interface), 35  |
| Single function applied to the original, 112    | Single function applied to the original, 112    |
| Slices View (requires:Extended Depth of Focus), | Slices View (requires:Extended Depth of Focus), |
| 77                                              | 77                                              |
| Software Copy Protection (Installation and Set- | Software Copy Protection (Installation and Set- |
| tings), 10                                      | tings), 10                                      |
| Sorting of Images, 87                           | Sorting of Images, 87                           |
| Source Data (Image Analysis), 98                | Source Data (Image Analysis), 98                |
| Special Object Properties, 150                  | Special Object Properties, 150                  |
| Special Options, 61, 67                         | Special Options, 61, 67                         |
| Special Options (Image Acquisition), 65         | Special Options (Image Acquisition), 65         |
| Start menu, 9                                   | Start menu, 9                                   |
| Startup Switches, 1                             | Startup Switches, 1                             |
| StartX, 140                                     | StartX, 140                                     |
| Statements Not Supported, 160                   | Statements Not Supported, 160                   |
| Statements Supported, 158                       | Statements Supported, 158                       |
| Status Bar, 28                                  | Status Bar, 28                                  |
| Status Bar (User Interface), 24                 | Status Bar (User Interface), 24                 |
| Status bar of the image window, 28              | Status bar of the image window, 28              |
| Step by Step, 5, 104                            | Step by Step, 5, 104                            |
| StgPos, 140                                     | StgPos, 140                                     |
| Structures and Unions, 158                      | Structures and Unions, 158                      |
| Structuring Element = Kernel = Matrix (Image    | Structuring Element = Kernel = Matrix (Image    |
| Analysis), 110                                  | Analysis), 110                                  |
| Superresolution Calibration, 47                 |                                                 |
| Supported Image Formats (Displaying Images), 94 | Supported Image Formats (Displaying Images), 94 |
| Images), 69                                     | Images), 69                                     |

## T

| The application status bar, 24                     |
|----------------------------------------------------|
| The Database View, 91                              |
| The Docked Control Panel Caption, 25               |
| The Installation DVD-ROM Content (Installation and |
| Settings), 5                                       |
| The NIS-Elements Main Window, 23                   |
| The organizer layout., 85                          |
| Threshold Adjustments, 102                         |
| Thresholding (Image Analysis), 100                 |
| Thresholding Example (Image Analysis), 104         |
| Thresholding Large Images, 103                     |
| Thresholding the Image (Measurement), 123          |
| Thumbnail Displaying Options, 87                   |

| Time-lapse Acquisition (Image Acquisition), 60   |
|--------------------------------------------------|
| Timing Explanation (Image Acquisition), 62       |
| Tips, 75, 79                                     |
| To Change a Single Z Coordinate: (Image Acquisi- |
| tion), 65 To Create a New Layout, 29             |
| To Create a Report FROM Template, 153            |
| To Create a Report Template, 153                 |
| To Display a Docking Pane, 25                    |
| To Reload Previous Layout Settings, 29           |
| Tool Bar, 126                                    |
| Tool Bar Buttons (User Interface), 36            |
| Tool Bars (User Interface), 24                   |
| Tools for Handling the Live Image, 55            |
| Top and Bottom, Step, 66                         |
| Turn Camera ROI ON/OFF, 58                       |
| Types of ROI (Image Analysis), 113               |

## U

| Units (Measurement), 118                                                                        |
|-------------------------------------------------------------------------------------------------|
| User Interface, 23                                                                              |
| User name and password properties, 15                                                           |
| User Permissions (Displaying Images), 89                                                        |
| User Rights (Installation and Settings), 11 User Rights Options (Installation and Settings), 14 |
| Users Tab Options (Installation and Settings), 14                                               |
| Using ROIs for analysis (Image Analysis), 115                                                   |
| Using two independent Z Drive devices, 50                                                       |

## V

| Variable types, 158 VolumeEqCylinder, 141   |
|---------------------------------------------|
| VolumeWqSphere, 142                         |

## W

| Well Plate (Rectangular) Multi-Point (Image Acquis-   |
|-------------------------------------------------------|
| ition), 63                                            |
| What are Logical Devices? (Cameras &amp; Devices),        |
| 48                                                    |
| Width, 142                                            |
| Working with the Binary Layer, 108                    |
| Working with the Measurement and Annotation           |
| Objects, 121                                          |
| Writing/Editing a Macro, 156                          |

## X

XY Stages and Z Drives Tips (Cameras &amp; Devices),

50

## Z

Z-series Acquisition (Image Acquisition), 66
# SunForge

SunForge is a tool for modding the game Tiberian Sun.

Download [SunForge Beta 4](sunforge-files/SFInstall.exe), released 1999-11-10, by {{highlight |text=King Arthur}} and {{highlight |text=Pendragon}} of {{highlight |text=Camelot Systems}}, and with art by {{highlight |text=Joel Steudler}}.

The readme is included below:

---

## SunForge Beta 4 Readme

### Installing SunForge
To install SunForge Beta 4, simply double-click on the "SFInstall.exe" icon wherever you downloaded the SunForge Installer to. In most cases it was probably your Tiberian Sun directory, although it's up to you where you saved it. Once the Installer is running, follow the steps in the Installation Wizard to install the program. Along with the EXE and Readme, default INI files will be placed in whatever directory you chose to install to. I reccomend editing copies of these files, not the originals, in case something bad happens. Once the installation has completed, you should have a new folder in your Program section in the Start Menu called "Camelot Systems" In there is a subdirectory called "SunForge" where you will find all SunForge related material. I have placed links to SunForge, this Readme, and the INI files there. To start SunForge, simply click on the SunForge icon.

### SunForge Beta 4 Features
- Unit Editor
- Weapon Editor
- AI Editor
- *NEW* Art Editor
- *New* Tileset Editor
- Add/Delete for all the editors

### Using Sunforge
SunForge, I hope, should be easier to use than editing the INI files directly. If it's not, email me what you think should be changed to make it easier to use, and I'll do my best to see that it gets changed accordingly. Assuming that you can get SunForge running, you should be presented with the main screen when it's finished loading. Depending on the speed of your computer this may take a few moments, as there is a lot of graphics to load. The same may be true of some of the editors, especially the Unit and Art Editors which have a lot of options (and therefore graphic resources). The main screen gives you a choice of choosing from any of 7 different editors, and the CamSys logo. You'll notice the mouse cursor change to a hand when you move your mouse over one of the buttons or icons. Due to space constraints, only the AI, Unit, and Weapon editors have icons. That doesn't signify anything except that they were completed first, and therefore had more screen real-estate available when Joel designed the main screen image. The rest (with two exceptions I will explain in a minute) all operate normally - when you click on them, their respective editor (or about box if you click the CamSys icon) will be displayed. When this has happened, the main screen will hide until you're done with the editor you chose. When you close that, the main screen will return. The two exceptions are the Misc. and Terrain Editors - they haven't been completed yet, so when you click on their buttons you just get a message saying so.

If by chance the INI files are not found in the SunForge directory, you will have to load the INI files manually. You may recieve an error message indicating this - this is just to notify you that the file may be invalid, and you can safely ignore the message so long as you open an ini file afterwords. If SunForge can find the INI files in its current directory, it will load them for all editors automatically.

Each editor has a menu bar from which you can open/save the file, add/remove objects, and undo/redo your changes. Each editor also has a listbox on the left hand side filled with names or codes of objects, and to the right of that is a tabsheet of options that you can choose from to save space on screen real-estate, or to provide access to multiple sections in one ini file. To load the data for an object, click on its name/code in the Listbox on the left. The edit boxes and combo boxes should then fill with the appropriate values for that object. You can then make whatever changes you wish to that unit. You will be able to undo/redo any changes that you make in all the editors (except for adding/deleting objects). When you're finished, you should save you changes to either the current file (Save), or to another file (Save As). If you forget to save and try to exit after having made changes, SunForge will let you know and prompt you to do so.

In order to see the changes you made to the INI files take effect, all ini files must be placed in your Tiberian Sun directory, and must be named either AI.ini, Art.ini, Rules.ini, Snow.ini, or Temperat.ini, for each related editor. Note that both Snow and Temperate are the Tileset files, and both are editable via the same Tileset Editor. You don't need to have both files present if you only make changes to one.

One final note: Changes that you make to an ini file will not be present in any saved games that were created prior to using the patched ini files.

### Troubleshooting
For now the most common problem seems to be that people can't get the changes they made to show up in the game. Most of the time this is because either the file isn't named properly, or it's not in the Tiberian Sun directory. Verify that both of these things are correct before contacting me.

Another problem is that the game crashes when it tries to load a game after you made some changes. Typically this is a direct result of chnages that you made to one (or more) of the INI files. The common culprit for this is the lack of a legal image for a unit. If the unit's image name doesn't exist in Art.ini, the game will crash. Almost all units' images are the same name as their codes. You can add images via the Art Editor.

For any further problems, email me via the address specified below. Please do not report problems without first checking to see if it can be solved via one of the above troubleshooting steps.

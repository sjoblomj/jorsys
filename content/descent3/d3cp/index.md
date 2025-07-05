# Descent 3 Control Panel

Descent 3 Control Panel (D3CP) is a tool for modding the game Descent 3.

Download [D3CP 1.02](d3cp-files/d3cp.zip), released 2000-03-10, by {{highlight |text=Dark Knight}} of {{highlight |text=Camelot Systems}}.

The readme is included below:

---

## Descent 3 Control Panel(D3CP) 1.02
made by Dark Knight(dkknight@quebectel.com)

Website: http://www.camsys.org


### First note
This version of D3CP is a full release. Since it's one of the first full release of this project,
it may contain various bugs... If it's the case, please e-mail the author. Thanks!


### What D3CP is used for
D3CP stands for Descent 3 Control Panel, just like the Windows one. It allows you to edit nearly
everything related to data in Descent 3. You can use it to edit Texture, Generic, Weapons, Doors,
Sounds and Ships data. The file containing all this is named a table file, and it is one of the
most important files in Descent 3. You can create your own, to add new values, or you can just
edit the one shipped with Descent 3, named "table.gam".


### Current features
- View the contents of table files
- Support to edit values, as well as adding and deleting pages.
- Support to save the table file.
- Possibility to create a whole new table file.
- Copy/pasting of table pages via CTRL+C(Copy) and CTRL+V(Paste).
- Save of Individual Page Files via CTRL+E(Export) and CTRL+I(Import).

### To be added
- To be able to see immediately the sound/texture/object/gfx by clicking on a button
- *Try* to improve the interface
- Any other good suggestion I get as feedback.
- Any other thing I'm forgetting about :)


### Known bugs
- None. For now :)


### Special note about sub-datas in pages
Many page types have buttons containing sub-data in them. They have their "Apply" button too, but
in order to have these data applied, you have to click on that "Apply" button and ALSO to click
on the main "Apply" button in the main window. If you don't, no changes from the sub-datas will
be applied.


### Another special note
If you're working in a MOD, I STRONGLY suggest you to not edit the main table file itself,
table.gam which is contained in the d3.hog file. It is really big, and would just increase the
downloading time, loading time in D3 as well as saving time in D3CP... Do a new table file for
your new modifications, it will be much more small and efficient. Thanks!


### History

#### D3CP 1.02 - March 10th, 2000
- Fixed various hints problems on some page
- Fixed problems of page redundance in certain situations when the table file was reloaded.
- Fixed crash when loading the D3:Mercenary new table file

#### D3CP 1.01 - November 19th, 1999
- Forgot to branch the "Delete" button in ships page. It's now fixed.
- Forgot to branch the value checker in the ships and doors page. It's now fixed.
- Made the value checker and value writer to use blank values. You can now leave blank spaces
  where a number is needed(it will be replaced by a 0).
- Implemented copy/paste feature for pages.
- Implemented page save feature.
- Replaced the blank text of new pages by a more explicit text.
- Added more hint cleaners, because sometimes the hint text was staying there even if the mouse
  wasn't on the button.
- Fixed a bug in which the array datas(which have #1/8 and etc.) sometimes didn't saved well the
  information in it.
- Fixed a bug in which you couldn't select the page type in the main menu if your mouse was over
  the text.
- Fixed a bug in which D3CP couldn't save properly the table file sometimes, showing "Fichier
  introuvable"(File not found) error.
- Fixed a bug in which D3CP couldn't read any pages after overwriting on the opened table file.
- Included the english strings patch in the executable that I forgot to do last releases.
- Added an "Auto-Update" menu item which link to the Auto-Update CGI at Camsys website(needs
  Internet connection).
- Created and included the "flags.txt" file putting every description to the flags in D3CP(many
  are unknown though).

#### D3CP 1.0 - November 15th, 1999
- Allowed to load the table file after D3CP is launched
- Removed the obligation to have table.gam at start.
- Added support to edit, add and delete pages.
- Added support to save the table file.
- Added support to create a whole new table file.
- Improved code for AI movements.
- Added physics button in ships, which was forgotten.
- Fixed various bugs.

#### D3CP Beta - October 26th, 1999
- First beta release, only allow to view table files.


### Future of D3CP
This project is now at 1.02. I've got some feedback with 1.01, thanks to these users again :)
A pesky bug appeared with D3:Mercenary, which I unfortunately don't have, which made D3CP
instantly crash and nobody warned me about it. I hope you simply forgot to tell me about
this :) Well, I guess this is going to be the last version you'll ever see of D3CP, I have lots
of other projects to work on and I guess I won't have time to finish the features I had in mind...

Please send me feedback, whether you appreciate or dislike it! Thanks in advance!


### Special thanks
- Outrage, for making Descent 3, one of the best 3d games I've seen ;)
- Outrage again, for heavily supporting it and to have released the GAM specs.
- Kuman, for its library of D3 images. I've used a couple of them for some images, they are
  really great. If you want to see them, just go to this URL(http://descent-3.com/models/)
- Metamorphosis, as they promised to use D3CP and made good publicity out of it many times :)
- Deathwinger, of Metamorphosis, to have done a great support on this project.
- Every site who announced this project.
- Everyone who supported this project.
- YOU, for downloading and using D3CP ;)


End of document.

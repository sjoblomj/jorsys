# AxeGraft

{{highlight |text=AxeGraft}} is a modding tool for StarCraft and Warcraft II: Battle.net Edition. It lets you change things that are built into the game executable itself rather than stored in the game's data files, such as what buttons and abilities each unit has, what buildings can do, and what the tech-tree looks like.

It was written by {{highlight |text=Ojan}} (Johan Sjöblom).

{{img |file=axegraft.png |class=centered |title=AxeGraft}}

{{highlight |text=AxeGraft}} consists of two parts:
1. The **{{highlight |text=AxeGraft Editor}}**, where you make your changes and save them as a mod file. It runs directly in your [web browser](https://axegraft.fly.dev/).
2. The **{{highlight |text=AxeGraft Patcher}}**, a plugin for [MPQDraft](mpqdraft.html) that loads your mod into the game when you start it.

Your game files are never overwritten; the mod only exists while the game is running.

## Download
The Editor is hosted [here](https://axegraft.fly.dev/), so you can use it without downloading anything. You can also download [the code](https://github.com/sjoblomj/axegraft) and open `editor/editor.html` in your browser. It needs no server and makes no network requests, so the mods and game files you open stay on your machine.

Download the [AxeGraft Patcher](https://github.com/sjoblomj/axegraft/releases/). You also need [MPQDraft](mpqdraft.html) to use it.

### Source code
The source code is available on [GitHub](https://github.com/sjoblomj/axegraft) under the MIT license.

## Supported games
- StarCraft: Brood War, versions 1.05 to 1.17. More specifically: 1.05, 1.06, 1.07, 1.08, 1.08b, 1.09, 1.09b, 1.10, 1.11, 1.11b, 1.12, 1.12b, 1.13, 1.13b, 1.13c, 1.13d, 1.13e, 1.13f, 1.14, 1.15.0, 1.15.1, 1.15.2, 1.15.3, 1.16, 1.16.1 and 1.17.
- Warcraft II: Battle.net Edition, versions 2.00 and 2.02.
- Warcraft II: Beyond the Dark Portal, versions 1.3, 1.33 and 1.5. **Note**: The Editor supports it, but there is no patcher available for these yet {{dash}} this is yet to be developed!

The Editor runs in any current browser. The Patcher, just like {{highlight |text=MPQDraft}} and the games, needs Windows or Wine.

## What you can change
The Editor has four tabs:

| Tab              | What you can change |
| ---------------- | ------------------- |
| **Units**        | The properties of units and buildings |
| **Button Sets**  | The buttons a unit shows, and what they do |
| **Requirements** | What is needed before something can be built, researched or used. StarCraft only. |
| **Constants**    | Single values for the whole game |

A mod file only holds what differs from the original game. Things you have changed are marked with a small dot, and you can undo with **Ctrl+Z** or revert a single thing to how it was in the original game.

## Making and playing a mod

### In the Editor
1. Open the Editor. Under **New mod**, type a name for your mod, and optionally a version and the authors.
2. Click the logo of the game you want to mod.
3. Make your changes.
4. Choose **File > Save As...** to save your mod as a `.json` file.

### In MPQDraft
1. Start {{highlight |text=MPQDraft}} and click **Load MPQ Patch**, then **Next**.
2. Choose your game and click **Next**.
3. On the **Select MPQ Files** page, you can optionally load any MPQs you may have and click **Next**. An {{highlight |text=AxeGraft}} mod doesn't need any MPQ files.
4. On the **Select Plugins** page, click **Add Plugin...** and choose the AxeGraft Patcher `.qdp` file you downloaded.
5. Select **AxeGraft Patcher** in the list and click **Configure**. Choose your `.json` file. No message is shown when the window closes. That is normal.
6. Click **Launch**. The game starts with your mod.

The plugin remembers which mod you chose, so next time you only need to click **Launch**. If you save your mod under a new name, click **Configure** again and choose the new file.

A full guide is available in the Editor under **Help > How to make a mod**, and on [GitHub](https://github.com/sjoblomj/axegraft/blob/main/docs/making-a-mod.md).

### If something goes wrong
The Patcher checks the whole mod before it changes anything. If it can't use your mod, it shows a message saying what is wrong, and the game closes. It never starts the game with only part of a mod. The Patcher writes a log file called `AxeGraftPatcher.log` in your Windows temporary folder. You can find the folder by typing `%TEMP%` into the address bar of File Explorer.

## History
{{highlight |text=AxeGraft}} is not the first such tool. For the DOS versions of Warcraft II, there was {{highlight |text=WarHack}} by {{highlight |text=Merlin}} (Cameron Burschardt). In 1999, {{highlight |text=King Arthur}} (Andy Bond) released {{highlight |text=StarGraft}}, which became incredibly popular. Later came {{highlight |text=MemGraft}} by {{highlight |text=DarkWizzard}}, and {{highlight |text=FireGraft}} by {{highlight |text=DiscipleOfAdun}}. All of them were closed-source and Windows only.

These tools work by editing specific places in the memory of the game executable. Finding those memory addresses takes careful reverse engineering, and every new patch of the game moves them around. Tool authors then had to start over to support the new patch, and players had to downgrade their games to play mods made for an older version.

The format of {{highlight |text=AxeGraft}} mods doesn't depend on the version of the game. The Patcher looks up where each thing lives in the version that is running, which is why a single mod works on nearly every version of StarCraft up to 1.17.

## Planned improvements
- A converter that turns mods made with older tools into {{highlight |text=AxeGraft}} mods.
- Support for {{highlight |text=GPTP}} and {{highlight |text=DatExtender}}.
- Editing the tech-tree of Warcraft II, the way you can in StarCraft.

# MPQDraft

MPQDraft is a modding tool that allows in-memory patching of game data files, added features through plugins, and creation of self-executing mods.

It was originally written by {{highlight |text=Quantam}} (Justin Olbrantz) and later enhanced by {{highlight |text=milestone-dev}} and {{highlight |text=Ojan}} (Johan Sjöblom).

{{img |file=mpqdraft.svg |class=centered |title=MPQDraft logo}}

## Download
Download [MPQDraft 2026-01-01](mpqdraft-files/MPQDraft-2026-01-01.zip).

### Source code
The source code is available on [GitHub](https://github.com/sjoblomj/MPQDraft) under the CDDL license.

## Modes
MPQDraft supports two modes:
1. Patching games locally: You run the game you choose with the MPQs and plugins that you specify. This mode is for playing mods.
2. SEMPQ (Self-Executing MPQ) creation: You create an executable with your mod that you can distribute to others. All they need to do is to run the executable; they do not need to have MPQDraft installed. This mode is for mod creators, wishing to make it easy for others to run their mods.

## Supported games
There is built in-support for the following games. Other 32-bit games that use MPQs and Storm.dll should theoretically also work.

- Diablo
- Diablo: Hellfire
- Diablo II
- Starcraft
- Starcraft Campaign Editor (StarEdit)
- Warcraft II: Battle.net Edition
- Warcraft III: Reign of Chaos
- Warcraft III: The Frozen Throne
- Warcraft III: World Editor
- Lords of Magic SE


## GUI
MPQDraft comes with a GUI written in Qt. To start it, simply run the MPQDraft executable without passing in any arguments. Passing in arguments will make it run in CLI mode.

## Command Line Usage

### Patch Command
To run a mod on the target you specify, use the `patch` command:

```
MPQDraft.exe patch --target <exePath> --mpq <mpqFile> --plugin <qdpFile>
```

Example:
```
MPQDraft.exe patch --target "C:\Starcraft\StarCraft.exe" --mpq "C:\Mod\my_mod_1.mpq" --mpq "C:\Mod\my_mod_2.mpq" --plugin "C:\Mod\my_plugin_1.qdp" --plugin "C:\Mod\my_plugin_2.qdp"
```

### SEMPQ Command

To create a SEMPQ (Self-Executing MPQ), use the `sempq` command. Three modes are available using the `sempq` command

- **Supported game mode**: Target one of the games that MPQDraft has built-in support for.
- **Custom registry mode**: The SEMPQ uses the Windows Registry to find the path of the game that will be launched on the end-users system. In case you want to target something that is not in the built list of supported games, you can use this mode to specify the target.
- **Custom target mode**: Here, a hard-coded path to an executable can be given. This requires the target application to be present on the end-users system under the exact given path.

#### Supported Game Mode

```
MPQDraft.exe sempq --output <sempqFile> --name <sempqName> --icon <iconFile> --mpq <mpqFile> --plugin <qdpFile> --game <game>
```

Example:
```
MPQDraft.exe sempq --output starwars_tc.exe --name "Star Wars TC" --icon starwars.ico --mpq sctc.mpq --plugin "C:\Mod\my_plugin_1.qdp" --game starcraft
```

For the `game` parameter, use `list-games` to see a list of supported games and their aliases (use any alias at your convenience to specify the game).

#### Custom Registry Mode

```
MPQDraft.exe sempq --output <sempqFile> --name <sempqName> --icon <iconFile> --mpq <mpqFile> --plugin <qdpFile> --reg-key <regKey> --reg-value <regValue> [--exe-file <exeFile>] [--target-file <targetFile>] [--full-path]
```

Example:
```
MPQDraft.exe sempq --output starwars_tc.exe --name "Star Wars TC" --icon starwars.ico --mpq sctc.mpq --plugin "C:\Mod\my_plugin_1.qdp" --reg-key "SOFTWARE\Blizzard Entertainment\SomeGame" --reg-value "InstallPath" --exe-file "SomeGame.exe" --target-file "SomeGame.exe"
```

#### Custom Target Mode

```
MPQDraft.exe sempq --output <sempqFile> --name <sempqName> --icon <iconFile> --mpq <mpqFile> --plugin <qdpFile> --target <targetPath>
```

Example:
```
MPQDraft.exe sempq --output starwars_tc.exe --name "Star Wars TC" --icon starwars.ico --mpq sctc.mpq --plugin "C:\Mod\my_plugin_1.qdp" --target "C:\SomeGame.exe"
```

### Patching Options
Additional options can also be passed on:

- `--params`: Command-line parameters to pass to the target executable. These are passed directly to the game and have no effect on MPQDraft itself.
- `--extended-redir` / `--no-extended-redir`: Enable or disable extended file redirection (default: enabled). Blizzard games use Storm.dll to access MPQ archives. Some Storm functions (like `SFileOpenFileEx`) can bypass the normal MPQ priority chain by accepting a specific archive handle. When enabled, MPQDraft hooks these functions to force them to search through the entire MPQ priority chain (including your custom MPQs), even when the game tries to read from a specific archive. Most Blizzard games including StarCraft and Warcraft III require this for mods to work correctly. Only disable if you experience compatibility issues.
- `--no-spawning`: Do not inject into child processes. By default, MPQDraft injects itself into any child processes created by the game, ensuring that patches work even if the game launches additional executables. Enable this flag if the game launches helper processes (updaters, launchers, crash reporters) that don't need patching and may cause issues.
- `--shunt-count`: The number of times the game restarts itself before MPQDraft activates patching (default: 0). Use 0 for most games to activate immediately. Some games with copy protection (like Diablo) restart themselves after checking the CD, so MPQDraft needs to wait for this restart - use 1 in such cases.


### CLI Plugin Configuration
MPQDraft plugins can optionally have configuration dialogs. The CLI contains no support for configuring plugins, but if one first runs MPQDraft in GUI mode, the plugins can be configured there, and those changes should persist when running in CLI mode.

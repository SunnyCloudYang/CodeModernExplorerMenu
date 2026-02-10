# Cursor Modern Explorer Menu

An MSI package that adds the Windows 11 Modern Explorer menu for Cursor.

> [!NOTE]
> 1. Please restart Windows Explorer after installation.
>
> 2. Installation requires admin rights and accepting UAC prompt to temporarily enable Developer Mode if required and restore its initial status after installation.
>
> 3. If your Cursor is installed in a custom location, you have to add the custom location to the PATH environment variable before installing this extension, otherwise you need to fork this repository and modify the path of Cursor.exe to support your custom location.

> [!CAUTION]
> AV may flag this as a virus due to the lack of a signature and self-elevation.

## Requirements:

- Windows 11+
- Cursor installed (in the default location or added to PATH)
- Admin rights

## Features:

- does not interfere with the classic menu
- works with both system/user installation locations and custom installation location.
- supports the case when Cursor runs as Administrator, thanks to [ArcticLampyrid](https://github.com/microsoft/vscode-explorer-command/pull/17)
- Also works for Devices and drives, thanks to [AndromedaMelody](https://github.com/microsoft/vscode-explorer-command/pull/16)
- Future Cursor updates won't break the menu, thanks to [huutaiii](https://github.com/huutaiii/vscode-explorer-command)
- Support English, French, Spanish, Arabic, Russian and Chinese(Simplified)

## Project changes:

- support more languages
- remove insider support
- replace Azure DevOps with GitHub Actions
- removed C++ dependencies from the repository
- added vcpkg package manager

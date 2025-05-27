[Setup]
AppName=MangaRepacker
AppVersion=0.0.1
DefaultDirName={pf}\MangaRepacker
DefaultGroupName=MangaRepacker
OutputDir=build/windows
OutputBaseFilename=mangarepacker-setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "build/windows/mangarepacker.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MangaRepacker"; Filename: "{app}\mangarepacker.exe"
Name: "{group}\Uninstall MangaRepacker"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\mangarepacker.exe"; Description: "Launch MangaRepacker"; Flags: nowait postinstall skipifsilent

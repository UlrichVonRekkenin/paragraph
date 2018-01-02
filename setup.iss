#define Name "Paragraph adapter"
#define Version "0.1"
#define Author "UlrichVonRekkenin"
#define Site "https://github.com/UlrichVonRekkenin"
#define BuildPath ".\build\exe.win32-3.4\"
#define ExeName "ParagraphAdapter.exe"
#define InitName "init.xls"

[Setup]
AppId={{BEC6990F-2789-4B72-B1ED-056817A74F7A}
AppName={#Name}
AppVersion={#Version}
AppPublisher={#Author}
AppPublisherURL={#Site}
AppUpdatesURL={#Release}
DefaultDirName={userdocs}\Paragraph Adapter
DefaultGroupName={#Name}
OutputDir=setup
OutputBaseFileName=Setup-{#Name}-{#Version}
Compression=lzma2/max
SolidCompression=yes

[Files]
Source: "{#BuildPath}{#ExeName}"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "{#InitName}"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "_readme.md"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "{#BuildPath}cacert.pem"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "{#BuildPath}msvcp100.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}MSVCR100.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}python34.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion


[UninstallDelete]
Type: files; Name: "{app}\{#InitName}"


[Icons]
Name: {group}\{#Name}; Filename: {app}; WorkingDir: {app};

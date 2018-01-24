#define Name "Paragraph Adapter"
#define Version "0.2"
#define Author "UlrichVonRekkenin"
#define Site "https://github.com/UlrichVonRekkenin"
#define Release "https://github.com/UlrichVonRekkenin"
#define BuildPath ".\build\exe.win-amd64-3.6\"
#define ExeName "ParagraphAdapter.exe"
#define PythonVersion 36

[Setup]
AppId={{D6F3D1A3-AFC3-4D76-88EC-574A5B29B203}
AppName={#Name}
AppVersion={#Version}
AppPublisher={#Author}
AppPublisherURL={#Site}
AppUpdatesURL={#Release}
DefaultDirName={userdocs}\{#Name}
DefaultGroupName={#Name}
OutputDir=setup
OutputBaseFileName=Setup-{#Name}-{#Version}
Compression=lzma2/max
SolidCompression=yes

[Files]
Source: "{#BuildPath}{#ExeName}"; DestDir: "{app}"; Flags: ignoreversion touch
Source: "{#BuildPath}python{#PythonVersion}.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#BuildPath}unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion


[UninstallDelete]


[Icons]
Name: {group}\{#Name}; Filename: {app}; WorkingDir: {app};

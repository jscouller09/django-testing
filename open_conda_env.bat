@echo OFF&setlocal

rem set anaconda install location
set root=C:\Anaconda3
echo Anaconda location: %root%

rem set local working directory
set script_dir=%~dp0
echo Script location: %script_dir%

rem get parent directory, assume github repo
for %%i in ("%~dp0.") do set "parent_folder=%%~fi"
echo GitHub repo path: %parent_folder%

rem assume conda environment name is same as github repo, get from parent folder
set env_name=%parent_folder%
:GetFolder
set GetFolderTemp=%env_name:*\=%
If Not %GetFolderTemp%==%env_name% (
    set env_name=%GetFolderTemp%
    Goto :GetFolder
)
echo Environment name: %env_name%

rem set code directory
rem set code_dir=main
rem echo Code location: %script_dir%%code_dir%

rem activate conda
echo Activating conda...
call %root%\Scripts\activate.bat %root%

rem activate right conda environment
echo Activating %env_name% conda environment...
call conda activate %env_name%

cmd /k
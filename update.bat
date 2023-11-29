@echo off
title git update
setlocal enabledelayedexpansion

:::
:::         .__  __                     .___       __          
:::    ____ |__|/  |_   __ ________   __| _/____ _/  |_  ____  
:::   / ___\|  \   __\ |  |  \____ \ / __ |\__  \\   __\/ __ \ 
:::  / /_/  >  ||  |   |  |  /  |_> > /_/ | / __ \|  | \  ___/ 
:::  \___  /|__||__|   |____/|   __/\____ |(____  /__|  \___  >
::: /_____/                  |__|        \/     \/          \/ 
:::

for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

REM cd path\to\your\local\repository

echo Pulling latest changes...
git pull

rem Get changed files
set "changed_files="
for /f %%i in ('git diff --name-only') do (
    set "changed_files=!changed_files! %%i"
)

rem Get untracked files
set "untracked_files="
for /f %%i in ('git ls-files --others --exclude-standard') do (
    set "untracked_files=!untracked_files! %%i"
)

rem Combine changed and untracked files into total_commits
set "total_commits=!changed_files! !untracked_files!"

rem Count the total number of commits
set "total_commits_count=0"
for %%i in (%total_commits%) do (
    set /a "total_commits_count+=1"
)

if %total_commits_count% gtr 0 (
	goto commit
) else (
	echo.
	echo no commits
	ping -n 3 127.0.0.1 > nul
	goto :EOF
)

:commit
	echo.
	echo commits found, please enter a message...
	set /p commit_message=commit message: 
	echo.
	git add --all
	git commit -m "%commit_message%"
	git push
	
echo.
echo.
echo Update complete.
endlocal
ping -n 3 127.0.0.1 > nul
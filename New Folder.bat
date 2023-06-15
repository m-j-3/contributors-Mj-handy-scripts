::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAnk
::fBw5plQjdG8=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSzk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFDZdTwyDAEqqFpEd/OnH3eWGr0QTU94ScYzJ1aeBJvQv3UzqcZk6xUZpncUIOBRkUBe8Lik7pWpHpCqAL8L8
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
set "folderName=New Folder"
set "folderCount=0"

:Loop
set /a folderCount+=1
if exist "%folderName%" (
  set "folderName=New Folder (%folderCount%)"
  goto Loop
)

mkdir "%folderName%"

for %%a in (%*) do (
  if not "%%~a"=="%folderName%" (
    move "%%~a" "%folderName%\"
  )
)

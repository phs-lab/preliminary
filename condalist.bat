:: notepad C:\DS\miniconda3\condabin\condalist.bat, save as ANSI on windows OS (CMD or Windows Terminal)
@echo off
:: @echo off는 명령어 출력 억제, echo는 의도적 출력 → 같이 써도 문제 없음. 예약어 및 Label은 대소문자를 가리지 않음.
setlocal

:: 기본값: 현재 conda 환경 저장, REM도 주석을 의미하지만 REM은 실제로 명령어로 인식되어 실행 시 약간의 오버헤드 발생. REM은 행 중간에 써도 무방하나 안 쓰는 것이 좋음.
set LIST_BAT_ENVNAME=%CONDA_DEFAULT_ENV%

:: 옵션 처리, `:`는 Label을 의미함
:LOOP
if "%~1"=="" goto RUN
if "%~1"=="-n" (
    set LIST_BAT_ENVNAME=%~2
    shift
)
if "%~1"=="-h" (
:: REM goto help, 서브루틴(call로 호출) 종료를 표시하는 `goto :eof`의 경우 항상 Exit Code 0 반환, 반환값은 %ERRORLEVEL% 로 접근/활용 가능. REM은 행 중간에 써도 무방하나 안 쓰는 것이 좋음.
    call :HELP
    goto :eof
)
shift
goto LOOP

:HELP
::echo Usage Help
::echo   (1) condalist                # Current Conda Environment w/o `-n`
::echo   (2) condalist -n ENVIRONMENT # Specified Environment -> Ex: condalist -n base
powershell -Command "Write-Output 'Usage Help'; Write-Output '  (1) condalist                # Current Conda Environment w/o `-n`'; Write-Output '  (2) condalist -n ENVIRONMENT # Specified Environment -> Ex: condalist -n base'"
:: exit = 배치 파일 실행 종료 ; /b = 배치 파일 전체를 종료하지 않고, 현재 실행 중인 배치 파일이나 서브루틴만 종료.
:: 0 = 종료 코드(Exit Code, 0=성공, 다른 값=오류나 특정 상태 표시) ; 반환값은 %ERRORLEVEL% 로 접근/활용 가능.
:: 원래 `exit /b 0` 였으나 batch file  자체가 끝나지 않아서 `goto :eof`로 변경함.
goto :eof

:RUN
:: Python의 `\`와 PowerShell의 `^`는 줄바꿈 이어주기라는 점에서는 같다고 볼 수 있다. 여기서는 파싱 오류 발생하여 한 줄로 수정 작성함.
conda list -n %LIST_BAT_ENVNAME% | powershell -Command "$i=0; foreach($line in [Console]::In.ReadToEnd().Split([Environment]::NewLine)) { if($line -ne '') { $i++; if($i -ge 4) { '{0,5} {1}' -f ($i-3),$line } else { '      ' + $line } } }"
:: conda list -n %LIST_BAT_ENVNAME% | powershell -Command ^
::     "$i=0; foreach($line in [Console]::In.ReadToEnd().Split([Environment]::NewLine)) { ^
::         if($line -ne '') { ^
::             $i++; ^
::             if($i -ge 4) { '{0,5} {1}' -f ($i-3),$line } ^
::             else { '      ' + $line } ^
::         } ^
::     }"

:: setlocal/endlocal → 환경 변수 범위를 제한해 실행 후 원래 상태로 복원.
endlocal

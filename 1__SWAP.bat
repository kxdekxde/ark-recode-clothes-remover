@echo off
echo Running Python Scripts...


REM Run 2___add_bundle_extension.py
python 2___add_bundle_extension.py
if %errorlevel% neq 0 (
    echo 2___add_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 2___add_bundle_extension.py ran successfully



REM Run 3___decompress.py
python 3___decompress.py
if %errorlevel% neq 0 (
    echo 3___decompress.py failed
    pause
    exit /b %errorlevel%
)
echo 3___decompress.py ran successfully




REM Run 4___Swap_bytes_hexedit.py
python 4___Swap_bytes_hexedit.py
if %errorlevel% neq 0 (
    echo 4___Swap_bytes_hexedit.py failed
    pause
    exit /b %errorlevel%
)
echo 4___Swap_bytes_hexedit.py ran successfully





REM Run 5___LZ4_compression.py
python 5___LZ4_compression.py
if %errorlevel% neq 0 (
    echo 5___LZ4_compression.py failed
    pause
    exit /b %errorlevel%
)
echo 5___LZ4_compression.py ran successfully








REM Run 6___remove_repacked_bundle_extension.py
python 6___remove_repacked_bundle_extension.py
if %errorlevel% neq 0 (
    echo 6___remove_repacked_bundle_extension.py failed
    pause
    exit /b %errorlevel%
)
echo 6___remove_repacked_bundle_extension.py ran successfully









echo All scripts ran successfully.
pause

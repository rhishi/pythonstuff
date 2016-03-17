
import subprocess

print 'subprocess.call:'
subprocess.call(r'C:\cygwin\bin\bash.exe --version')
subprocess.call(r'C:\cygwin\bin\bash.exe --help')
subprocess.call(r'C:\cygwin\bin\bash.exe -c "echo Sa and An"')
subprocess.call(r'C:\cygwin\bin\echo.exe Sa and An and Fo')
subprocess.call(r"C:\cygwin\bin\ls.exe '/cygdrive/c/Program Files/'")
print

print 'subprocess.check_output:'
print subprocess.check_output(r'C:\cygwin\bin\bash.exe --version')

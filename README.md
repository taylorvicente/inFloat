# inFloat

Full hardware and firmware suite for the inFloat electronics package (Purdue ME 463).

When the float deploys, the electronics detect it with a Hall-effect switch, power up a 5 V boost rail, flash the survivor lights and send an alert with location data over LTE-M.

## Hardware

| Component | Purpose |
| --- | --- |
| Seeed XIAO ESP32S3 | Main MCU, running MicroPython |
| M5Stack CatM + American LTE-M microSIM | Cellular alert link |
| Survivor Light board | LED beacon, driven with PWM |
| 5 V MiniBoost | Powers the CatM and survivor lights after deployment |
| 400 mAh 3.7 V LiPo | Battery |
| Hall sensor switch | Detects deployment when the magnet moves away |

### Pin map (XIAO ESP32S3)

| GPIO | Signal | Direction |
| --- | --- | --- |
| 1 | Battery voltage (ADC, through a 1:2 divider) | In |
| 2 | Hall sensor | In |
| 3 | Communication / 5 V boost enable | Out |
| 4 | Survivor light PWM | Out |
| D6 / D7 | UART0 TX / RX to the CatM | UART |

## Repository layout

```
esp32.py      Main MicroPython firmware (work in progress)
firmware/     MicroPython image for the ESP32-S3 (v1.29.0, octal SPIRAM)
```

## Getting started

1. Install the tools: `pip install esptool mpremote`
2. Flash MicroPython (replace the port with yours):
   ```sh
   esptool.py --chip esp32s3 --port /dev/cu.usbmodem* erase_flash
   esptool.py --chip esp32s3 --port /dev/cu.usbmodem* write_flash -z 0 \
     firmware/ESP32_GENERIC_S3-SPIRAM_OCT-20260824-v1.29.0.bin
   ```
3. Upload and run the firmware:
   ```sh
   mpremote cp esp32.py :main.py
   mpremote reset
   ```

## Firmware status

- [ ] Battery state of charge
- [ ] Deployment detection (poll the Hall sensor at 5 Hz)
- [ ] 5 V boost / CatM enable on deployment
- [ ] Survivor light flashing at 20% duty cycle
- [ ] LTE-M alert (JSON with location), retried until delivery is confirmed
- [ ] Main loop

## Author

Taylor Vicente

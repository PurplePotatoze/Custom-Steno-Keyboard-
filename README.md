<img width="1476" height="977" alt="Screenshot 2026-09-04 190835" src="https://github.com/user-attachments/assets/94fa3aa8-31e9-47d4-bc1e-c6bb4f468767" />

#  Steno Keyboard
I'm making my very own Steno Keyboard!! (In a nutshell, its a keyboard that you can type over 200 wpm because of the placement of the keys). 42 Keys, USB-C, with a Raspberry Pi Pico. Thank you Hackclub Stardance for funding this!

BOM:
- 1x Raspberry Pi Pico 2
- 10x M3x5mm Screws
- 10x M3 (3mm) Heatset inserts
- 42x Gateron Low Profile Switches
- 42x Gateron Low Profile Keycaps
- 1x 0.91 OLED (Pin order: GND-VCC-SCL-SDA)
- 1x PCB
- 2x 3D Printed Case
- 1x 1.4 M3 Spacers

Features:
- USB-C
- 42 Reprogrammable Keycaps
- Compatibility with Plover
- 0.91 Oled for status

# CAD

<img width="1367" height="773" alt="Screenshot 2026-09-04 190729" src="https://github.com/user-attachments/assets/c09d7251-ed5c-4693-94e5-65ebe6029725" />

Very simple case, just 10 heat set inserts

# Schematics

<img width="1142" height="683" alt="Screenshot 2026-09-04 190550" src="https://github.com/user-attachments/assets/86720971-9385-434c-aaaa-a3f14bbb513a" />

42 SW Push in a matrix (12x4) with a 4 pin connector for the oled.

# PCB

<img width="1527" height="758" alt="Screenshot 2026-09-04 185040" src="https://github.com/user-attachments/assets/2b528cbc-d8ea-4cb6-b6d3-e7fbc4705f88" />

Designed in Kicad, gets yours at JLCPCB or PCBway with my Gerber files.

# Firmware

<img width="1916" height="1141" alt="Screenshot 2026-09-04 190635" src="https://github.com/user-attachments/assets/7a04b581-6829-4d56-8e94-1be0c1d039a0" />

KMK, very simple python based code. Firmware in "Production" file, flash onto Pico. Very modifiable. 

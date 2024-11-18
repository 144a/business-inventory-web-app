import enum

class DisplayTypeEnum(str, enum.Enum):
  crt_color = 'Color CRT'
  crt_bw = 'B&W CRT'
  plasma = 'Plasma'
  lcd = 'LCD'
  oled = 'OLED'
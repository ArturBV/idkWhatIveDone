from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x111111)

Black=0x000000
White=0xffffff
BaseColor=0x111111
ScrW = 135
ScrH = 240
ScrCenter = (ScrW // 2, ScrH // 2)
TextH = 30

def vanish_bottom():
  lcd.rect(0, TextH - 5, ScrW, ScrH - TextH, fillcolor=BaseColor)

def get_ready():
  lcd.print('ready!', 30, 0, White)
  for i in range(3, 0, -1):
    vanish_bottom()
    lcd.print(str(i), ScrCenter[0], ScrCenter[1], White)
    wait(1)

  
def game_cycle():
  result = 0
  lcd.fill(BaseColor)
  
  get_ready() # 3 seconds
  lcd.fill(BaseColor)

  result = 0
  res_max = 1000000
  timer = 0.0
  imu0 = imu.IMU()
  
  prev = time.ticks_ms()
  while timer // 1000 < 15:
    
    # for i in range(1, 3):
      # result += abs(int(imu0.acceleration[i] * 10))
    result += abs(int(imu0.acceleration[1])) * 10
    lcd.fill(BaseColor)
    lcd.print(result % res_max, 0, ScrCenter[1], White)
    
    cur = time.ticks_ms()
    timer += (cur - prev) 
    
    lcd.print(15 - int(timer // 1000), ScrCenter[0] - 10, 0, White)
    prev = cur
    wait_ms(200)
  
  return result % res_max


while True:
  
  lcd.print('welcome', 10, 0, 0xffffff)
  lcd.print('\/press\/', 13, 200, 0xffffff)
  res = 0
  if btnA.isPressed():
    res = game_cycle()
    lcd.fill(BaseColor)
    lcd.print('Result is', 10, 0, 0xffffff)
    lcd.print(res, ScrCenter[0] - 20, 30, 0xffffff)
    while btnA.isReleased():
      pass
    lcd.fill(BaseColor)
  
  wait_ms(300)
  
import Adafruit_DHT

# 设置传感器类型：可选项有DHT11、DHT22或AM2302。
sensor=Adafruit_DHT.DHT11

# 设置传感器数据引脚连接到的GPIO口。
gpio=17

# 使用读取重试方法。这将重试最多15次
# 获取传感器读数（每次重试之间等待2秒）。
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

# 读取DHT11的数据需要非常高的时间灵敏度，有时
# PI可能无法获得有效的读数。所以检查读数是否有效。
if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
  print('Failed to get reading. Try again!')

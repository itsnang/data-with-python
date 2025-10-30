def temperature_conversion(temperature, unit):
  result = 0
  if(unit == '1'):
    result = (temperature * 9/5) + 32
  elif(unit == '2'):
    result = 5/9 * (temperature - 32)
  return result

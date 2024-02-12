import moonrakerpy as moonpy

printer = moonpy.MoonrakerPrinter('http://rotationsensor.local')
printer.send_gcode('G28 X')
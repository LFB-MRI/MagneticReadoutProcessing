
mkdir /home/pi/linear
mkdir /home/pi/linear_results
MRPCli --basepath /home/pi/linear config setup linear
MRPCli --basepath /home/pi/linear config setupsensor linear

wget http://192.168.178.88/printer/gcode/script?script=G90
wget http://192.168.178.88/printer/gcode/script?script=G0%20Z60
wget http://192.168.178.88/printer/gcode/script?script=G91




i=0

until [ $i -gt 120 ]
do
  echo i: $i
  ((i=i+1))

    rm /home/pi/linear/*.mag.json

    wget http://192.168.178.88/printer/gcode/script?script=G1%20Z+1
    sleep 1
    MRPCli --basepath /home/pi/linear measure run linear

    cp /home/pi/linear/*.mag.json /home/pi/linear_results/DISTANCE=$i.mag.json
done

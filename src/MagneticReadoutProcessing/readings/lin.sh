mkdir /tmp/linear
mkdir /tmp/linear_results
MRPCli --basepath /tmp/linear config setup linear
MRPCli --basepath /tmp/linear config setupsensor linear

wget http://192.168.178.88/printer/gcode/script?script=G90
wget http://192.168.178.88/printer/gcode/script?script=G0%20Z51
wget http://192.168.178.88/printer/gcode/script?script=G91




i=0

until [ $i -gt 120 ]
do
  echo i: $i
  ((i=i+1))

    rm /tmp/linear/*.mag.json

    wget http://192.168.178.88/printer/gcode/script?script=G1%20Z+1
    sleep 1
    MRPCli --basepath /tmp/linear measure run linear

    #cp /tmp/linear/*SID0*.mag.json /home/pi/linear_results/DISTANCE=$i.mag.json
    cp /tmp/linear/*.mag.json /tmp/linear_results/DISTANCE=$i.mag.json
done

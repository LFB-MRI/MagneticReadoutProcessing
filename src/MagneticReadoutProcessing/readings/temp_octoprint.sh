mkdir /tmp/temp
mkdir /tmp/temp_results
MRPCli --basepath /tmp/temp config setup temp
MRPCli --basepath /tmp/temp config setupsensor temp
MRPCli --basepath /tmp/temp sensor info temp
MRPCli --basepath /tmp/temp sensor query temp

wget --quiet http://192.168.178.88/printer/gcode/script?script=SET_HEATER_TEMPERATURE%20HEATER=heater_bed%20TARGET=0
TOKEN="9CC218A47F2A4375957D4CE880C8AE3C"
curl -X POST -H "Content-Type: application/json" -H "X-Api-Key":"$TOKEN" -d '{"command":"M140 S0"}' http://octopi.local/api/printer/command

for i in {20..50}
do
  echo i: $i


    rm /tmp/temp/*.mag.json

    curl -X POST -H "Content-Type: application/json" -H "X-Api-Key":"$TOKEN" -d "{\"command\":\"M140 S$i\"}" http://octopi.local/api/printer/command
    sleep 10
    #curl -X POST -H "Content-Type: application/json" -H "X-Api-Key":"$TOKEN" -d '{"command":"M140 S0"}' http://octopi.local/api/printer/command
    #sleep 10
    MRPCli --basepath /tmp/temp measure run temp

    #cp /tmp/linear/*SID0*.mag.json /home/pi/linear_results/DISTANCE=$i.mag.json
    cp /tmp/temp/*.mag.json /tmp/temp_results/TEMPERATURE=$i.mag.json
done

curl -X POST -H "Content-Type: application/json" -H "X-Api-Key":"$TOKEN" -d '{"command":"M140 S0"}' http://octopi.local/api/printer/command
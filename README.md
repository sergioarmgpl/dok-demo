LB=YOUR_IP

curl -X POST -H "Accept: application/json" \
-H "Content-Type: application/json" \
--data '{"lat":1.633518,"lng": -90.591706}' \
http://$LB:3000/position/1

curl HTTP://$LB:3000/position/2

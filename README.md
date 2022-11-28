LB=YOUR_IP

curl -X POST -H "Accept: application/json" \
-H "Content-Type: application/json" \
--data '{"lat":1.633518,"lng": -90.591706}' \
http://$LB:3000/position/1

curl HTTP://$LB:3000/position/2

kubectl port-forward --address 0.0.0.0 svc/longhorn-frontend 5555:80 -n longhorn-system

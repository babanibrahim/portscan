#pewysta python3 bakar benin.
#  socket module bakar det bo mamala krdn lagall API.
import socket
# pewista am pacejy [ regular ] add bkain bo away data ba shewayaki drwst input bkret la data type gwnjaw da.
import re

# lerada waman krdwa ka IP versiony 4 bnasetawa.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# lera da aw portana  dyari dakai ka datawe scannian bkai  <zhmarai_nzmtrin_port>-<zhmarai_barztrin_port> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# dyari krdni portakan la varablakani xwarawa anjam drawa.
port_min = 0
port_max = 65535

# am scripta socket api bakar dahene bo awai bzane daxwa datwane paywandi bkat ba IP dyari kraw yan na.
# katek twani paywandi bkat awa aw PORT a krawaya.

# rwkar
print("\n****************************************************************")
print("\n*              Academy Under Ocean                             *")
print("\n*              Baban Ibrahim, 2022                             *")
print("\n*       https://www.facebook.com/Babanpasha01/                 *")
print("\n*           https://twitter.com/Baban_pasha                    *")
print("\n****************************************************************")

open_ports = []
# dawa la bakar henaran dakat bo daxl krdni aw ip ka dayawe scani bka.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print({ip_add_entered}," is a valid ip address")
        break

while True:
    # datwani 65535 port scann bkai balam hamwyan bayakwa nakret ba 1 jar chwnka multithred nia w [ sadaya ] am toola
    # boya waman krdwa aw newanai mabastta dyari bkai bo xerabwni karakat.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

#  sockety port scann krdn [ sadaya ]
for port in range(port_min, port_max + 1):
    # lera socketa ka hawl dada paiwandi ba IP yakwa bkat .
    try:
        # ba socket.AF_INET datwani  domain yan  ip scann bkait.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # lera da pewista katek dyari bkai bo paiwandi krdn ba server
            #  hata kataka zyatr be krdaraka anjami bashtr dabe balam hewashtr dabe
            #  gwnjaw trin mawa [ 0.1s ] bo awai ham xera be ham anjameki bashi habet
            s.settimeout(0.5)
            # lera aw OBJ ektai drwstman krdwa bakarde bo paywandi krdn baw
            #  IP address ay ka daxlman krdwa la gall zhmarai portakan .
            s.connect((ip_add_entered, port))
            # agar hamw code akani sarawa  run bwn awa ba sar kawtwana paiwandi ba port a kawa krawa .
            open_ports.append(port)

    except:
        # lera pewist naka hich dabnein , katek pewist bw ka bman wistba porta daxrawakan bbinin.
        pass

# tanha grngi ba porta krawakan dadain .
for port in open_ports:
    print("Port", {port}," is open on", {ip_add_entered})

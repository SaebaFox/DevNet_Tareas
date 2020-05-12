from ncclient import manager
import xmltodict
import xml.dom.minidom

Conec = manager.connect(
   host= "192.164.1.58",
   port= 830,
   username = "cisco",
   password = "cisco123!",
   hostkey_verify = False
)

def get_info_device():

   netconf_reply = Conec.get_config(source="running")
   print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


def create_interface():
   netconf_data = """
   <config>
        <interface xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <Loopback>
                <name>7</name>
                <description>prueba</description>
                <ip>
                    <address>
                        <primary>
                            <address>192.168.60.60</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
   </config>
   """
   netconf_reply = Conec.edit_config(target="running",config=netconf_data)
   print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def delete_interface():
   netconf_data= """
     <config>
         <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
             <interface operation="delete">
                 <name>7</name>
             </interface>
         </interfaces>
     </config>"""
   netconf_reply = Conec.edit_config(target="running",config=netconf_data)
   print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



def get_table_routing():
   filtro = """
        <filter>
             <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
                <routing-instance>
                    <name>default</name>
                    <ribs>
                        <rib>
                            <name>ipv4-default</name>
                        </rib>
                    </ribs>
                </routing-instance>
            </routing-state>
        </filter>
        """
   Datos = Conec.get(filtro)
   diccionario = xmltodict.parse(Datos.xml)

   for item in diccionario:
       pass


def menu():
   print("**********************")
   print("Introduce la operacion")
   print("1 get_info_device ")
   print("2 create_interface")
   print("3 delete_interface")
   print("4 get_table_routing")
   print("**********************")
   return input("")

def opcion(opcion):
   if (opcion == "1"):
      get_info_device()
   elif(opcion == "2"):
      create_interface()
   elif(opcion == "3"):
      delete_interface()
   elif(opcion == "4"):
      get_table_routing()
   else:
      print("opcion no valida")

if __name__ == "__main__":
   opcion(menu())
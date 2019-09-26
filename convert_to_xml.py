from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

# Instantiate the codec service
codec = CodecService()

# Instantiate codec providers with json and xml options
json_provider = CodecServiceProvider(type='json')
xml_provider = CodecServiceProvider(type='xml')

# Declare the JSON configuration
vlan_json = ''' {
    "openconfig-network-instance:network-instances": {
        "network-instance": [
            {
                "name": "default",
                "config": {
                    "name": "default"
                },
                "vlans": {
                    "vlan": [
                        {
                            "vlan-id": 1,
                            "config": {
                                "vlan-id": 1,
                                "name": "default",
                                "status": "ACTIVE"
                            }
                        },
                        {
                            "vlan-id": 1000,
                            "config": {
                                "vlan-id": 1000,
                                "name": "prod1",
                                "status": "ACTIVE"
                            }
                        },
                        {
                            "vlan-id": 100,
                            "config": {
                                "vlan-id": 100,
                                "name": "vlan100",
                                "status": "ACTIVE"
                            }
                        },
                        {
                            "vlan-id": 1020,
                            "config": {
                                "vlan-id": 1020,
                                "name": "vlan1020",
                                "status": "ACTIVE"
                            }
                        }
                    ]
                }
            }
        ]
    }
}
'''

interface_configurations = codec.decode(json_provider, vlan_json)

if_xml = codec.encode(xml_provider, interface_configurations)
print(if_xml)

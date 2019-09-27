#!./venv/bin/python -i

from ydk.providers import CodecServiceProvider
from ydk.services import CodecService
from copy import deepcopy
import argparse
import json

parser = argparse.ArgumentParser(description='convert yang json to xml')
parser.add_argument('-j','--json_file', help='json_file', required=True)

args = vars(parser.parse_args())

codec = CodecService()

json_provider = CodecServiceProvider(type='json')
xml_provider = CodecServiceProvider(type='xml')

def yang_json_to_xml(json_file):
    config_json_yang = json.dumps(json.load(open(json_file)))
    
    decoded_json_yang = codec.decode(json_provider, config_json_yang)
    
    yang_xml = codec.encode(xml_provider, decoded_json_yang)
    return yang_xml

print(yang_json_to_xml(args['json_file']))


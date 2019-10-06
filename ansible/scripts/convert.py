#!./venv/bin/python -i

from ydk.providers import CodecServiceProvider
from ydk.services import CodecService
from copy import deepcopy
import argparse
import json
import yaml
import sys

parser = argparse.ArgumentParser(description='convert yang json to xml')
parser.add_argument('-j','--json_file', help='json_file')
parser.add_argument('-y','--yaml_file', help='yaml_file')

args = vars(parser.parse_args())

codec = CodecService()

json_provider = CodecServiceProvider(type='json')
xml_provider = CodecServiceProvider(type='xml')

def yang_yaml_to_xml(yaml_file):
    with open(yaml_file, 'r') as yaml_in:
        yaml_object = yaml.safe_load(yaml_in) 
    
    config_json_yang = json.dumps(yaml_object)
    decoded_json_yang = codec.decode(json_provider, config_json_yang)

    yang_xml = codec.encode(xml_provider, decoded_json_yang)
    return yang_xml

def yang_json_to_xml(json_file):
    config_json_yang = json.dumps(json.load(open(json_file)))
    
    decoded_json_yang = codec.decode(json_provider, config_json_yang)
    
    yang_xml = codec.encode(xml_provider, decoded_json_yang)
    return yang_xml


if args['json_file']:
    print(yang_json_to_xml(args['json_file']))
elif args['yaml_file']:
    print(yang_yaml_to_xml(args['yaml_file']))

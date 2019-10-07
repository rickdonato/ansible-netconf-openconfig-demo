#!./venv/bin/python -i
"""
Author: Rick Donato <admin@packetflow.co.uk>

Script to convert JSON/YAML to XML structures.
"""

import argparse
import json

import yaml
from ydk.providers import CodecServiceProvider
from ydk.services import CodecService

PARSER = argparse.ArgumentParser(description='convert yang json to xml')
PARSER.add_argument('-j', '--json_file', help='json_file')
PARSER.add_argument('-y', '--yaml_file', help='yaml_file')

ARGS = vars(PARSER.parse_args())

CODEC = CodecService()

JSON_PROVIDER = CodecServiceProvider(type='json')
XML_PROVIDER = CodecServiceProvider(type='xml')


def yang_yaml_to_xml(yaml_file):
    """
    Convert YAML to XML
    """
    with open(yaml_file, 'r') as yaml_in:
        yaml_object = yaml.safe_load(yaml_in)

    config_json_yang = json.dumps(yaml_object)
    decoded_json_yang = CODEC.decode(JSON_PROVIDER, config_json_yang)

    yang_xml = CODEC.encode(XML_PROVIDER, decoded_json_yang)
    return yang_xml


def yang_json_to_xml(json_file):
    """
    Convert JSON to XML.
    """
    config_json_yang = json.dumps(json.load(open(json_file)))
    decoded_json_yang = CODEC.decode(JSON_PROVIDER, config_json_yang)

    yang_xml = CODEC.encode(XML_PROVIDER, decoded_json_yang)
    return yang_xml

if ARGS['json_file']:
    print(yang_json_to_xml(ARGS['json_file']))
elif ARGS['yaml_file']:
    print(yang_yaml_to_xml(ARGS['yaml_file']))

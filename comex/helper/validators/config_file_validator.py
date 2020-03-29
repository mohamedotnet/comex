from jsonschema import Draft7Validator
import json


def validate_network_config_file(config_file):
    """
        :param config_file:json
        :return:
    """
    schema = json.load(open('/comex/schema/draft_schema.json',
                            "r+")
                       )
    network_config = json.load(config_file)
    return Draft7Validator(schema).is_valid(network_config)



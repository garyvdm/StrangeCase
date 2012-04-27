import os
import yaml


def folder_config_file(source_file, config):
    if config['type'] == 'folder' and config.get('config_file'):
        # the config is read *before* its processor is invoked (so no matter what processor you
        # use, it is guaranteed that its config is complete)
        config_path = os.path.join(source_file, config['config_file'])
        if os.path.isfile(config_path):
            with open(config_path, 'r') as config_file:
                yaml_config = yaml.load(config_file)

            if yaml_config:
                config.update(yaml_config)
        # if { ignore: true }, the entire directory is ignored
        if config.get('ignore') is True:
            return
    return config

folder_config_file.defaults = {
    'config_file': 'config.yaml',
}

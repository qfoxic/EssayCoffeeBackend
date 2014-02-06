import lib.yaml as yaml
import os.path
import constants as co

def merge(d1, d2):
  """Function merge two dictionary into one and retun merged dictionary.
  NOTE!!! It doesn't overload existing data but just extend them.

  d1 - dictinary that will be populated with d2.
  """
  keys1 = set(d1)
  common_keys = keys1.intersection(set(d2))
  for key in common_keys:
    d2_tmp = d2.pop(key)
    if isinstance(d1[key], list):
      d1[key].extend(d2_tmp)
    elif isinstance(d1[key], dict):
      merge(d1[key], d2_tmp)

  d1.update(d2)
  return d1


def load(module_name):
  """Looks for YAML settings for specific module.

  Args:
     module_name: the name of the module that was requested.
  """
  config_path = os.path.join(co.CONFIG_PATH, module_name+co.CONFIG_FILE_ENDING)
  config_settings = {}
  try:
    config_file = open(config_path, 'r').read()
  except IOError, e:
    print 'Could not read config file: %s' % (str(e),)
    return {}

  try:
    config_settings = yaml.load(config_file)
  except yaml.YAMLError, e:
    print 'Yaml parse error: %s' % (str(e),)
    return {}
  return config_settings and config_settings or {}
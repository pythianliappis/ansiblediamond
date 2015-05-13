#!/usr/bin/python
# -*- coding: utf-8 -*-

DEFAULT_COLLECTOR_DIR="/etc/diamond/collectors"

def main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True),
            collector_dir = dict(),
            config = dict(type='dict'),
        )
    )

    params = module.params

    if params['collector_dir']:
        collector_dir = params['collector_dir']
    else:
        collector_dir = DEFAULT_COLLECTOR_DIR

    config_file = "%s/%s.conf" % (collector_dir, params['name'])

    config = ""

    for (k, v) in params['config'].iteritems():
        config += "%s=%s\n" % (k, v)

    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            if file.read() == config:
                module.exit_json(changed=False)

    with open(config_file, "w") as file:
        file.write(config)

    module.exit_json(changed=True)

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

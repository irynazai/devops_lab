import yaml
from jinja2 import Template

with open('data.yml') as data_file:
    config_data = yaml.safe_load(data_file)

with open('vhosts.j2') as template_file:
    template_html = template_file.read()

template = Template(template_html)
vhosts_conf = template.render(config_data)

# Please add the full path to the "vhosts.conf" file if you need.
# For examlple: '/etc/httpd/conf.d/vhosts.conf'
with open('vhosts.conf', 'w') as vhosts_file:
    vhosts_file.write(vhosts_conf)

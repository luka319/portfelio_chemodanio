from jinja2 import Template

template = Template('''

{% for s in spisok %}
   {{ s }}
{% endfor %}


''')

liverpool = {'spisok': ['kk','bb','zz'] }

print(template.render(liverpool))

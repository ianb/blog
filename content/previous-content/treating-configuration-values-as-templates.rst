Treating configuration values as templates
##########################################
:date: 2009-04-20 00:11
:author: Ian Bicking
:tags: Programming

A while back I `described fassembler <http://blog.ianbicking.org/2008/06/19/my-experience-writing-a-build-system />`_ and one of the things I liked in it is how the configuration works.  It uses a conventional declarative INI-style but also allows arbitrary code, so that defaults can be based on each other.

Here's a basic example of a default configuration::

    [some_app]
    port_offset = 10
    port = {{int(section.DEFAULT['base_port'])+int(port_offset)}}

Then if another configuration file defines ``base_port`` then this will all resolve.  You can do this in Python, but you don't get sections, and you have to define everything in just the right order.  So while ``base_port`` will probably be defined in a deployment-specific configuration, it has to be defined before these other derivative settings are defined.  On the other hand, you want deployment-specific configuration to take precedence... so there's really no good ordering.

Anyway, the implementation really isn't that hard.  I use `Tempita <http://pythonpaste.org/tempita />`_ as the templating language because, well, I wrote it, and because it's simple and appropriate for small strings.  For the configuration parsing, `ConfigParser <http://docs.python.org/library/configparser.html>`_ will do.

Here's what the basic code looks like in ConfigParser::

    from ConfigParser import ConfigParser
    from tempita import Template

    class TempitaConfigParser(ConfigParser):

        def _interpolate(self, section, option, rawval, vars):
            ns = _Namespace(self, section, vars)
            tmpl = Template(rawval, name='%s.%s' % (section, option))
            value = tmpl.substitute(ns)
            return value

Actually instead of using ``tempita.Template``, we could just do ``eval(rawval, {}, ns)``, it would just require a lot more quoting (every value would have to be a valid Python expression).  Either with that or Tempita the implementation of ``_Namespace`` will look the same.

Here's a simple implementation::

    from UserDict import DictMixin

    class _Namespace(DictMixin):
        def __init__(self, config, section, vars):
            self.config = config
            self.section = section
            self.vars = vars

        def __getitem__(self, key):
            if key == 'section':
                return _Section(self)
            if self.config.has_option(self.section, key):
                return self.config.get(self.section, key)
            if vars and key in self.vars:
                return self.vars[key]
            raise KeyError(key)

       def __setitem__(self, key, value):
           if self.vars is None:
               self.vars = {key: value}
           else:
               self.vars[key] = value

We've introduced a magic variable ``section``, which is used to refer to other sections.  It looks like this::

    class _Section(object):
        def __init__(self, namespace):
            self._namespace = namespace

        def __getattr__(self, attr):
            if attr.startswith('_'):
                raise AttributeError(attr)
            return _Namespace(self._namespace.config, attr,     self._namespace.vars)

With these I think you get many of the benefits of using Python code as your configuration format, while still having the benefits of a more declarative approach to configuration, one that allows for forward and backward references.

A full implementation has several more things than I show here, but you can see the full example `in my recipes <http://svn.colorstudy.com/home/ianb/recipes/evalconfig.py>`_.  It also has an example of using `INITools <http://pythonpaste.org/initools />`_ instead of ConfigParser to give more accurate filenames and line numbers when there is an exception, while otherwise using the same interface.

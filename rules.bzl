load('//scripts/pyproject:pyproject.bzl', 'pyproject_package')

def load_rules(lib_name, internal_dependencies, extra_info):
    pyproject_package(
        name = 'package',
        package = lib_name
            .replace('-', '.')
            .replace('salto.', 'saltoapis.')
            .replace('third_party.', ''),
        deps = ["{}:package".format(dep) for dep in internal_dependencies],
    )

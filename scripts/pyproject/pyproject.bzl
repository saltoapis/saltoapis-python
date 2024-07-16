load('//:python_metadata.bzl', 'GRPC_VERSION', 'PROTOBUF_VERSION')

"""
This file contains rules used to generate the `pyproject.toml` file.
"""
PythonPackageInfo = provider(
    fields = {
        "target_package": """
        The package name
        """,
        "target_deps_packages": """
        The package names of the dependencies from the same package
        """,
        "target_external_deps": """
        external dependencies
        """,
    },
)

def _pyproject_deps_impl(_target, ctx):
    package_name = getattr(ctx.rule.attr, "package", [])
    deps = getattr(ctx.rule.attr, "deps", [])
    external_deps = getattr(ctx.rule.attr, "external_deps", {})

    dep_packages = []
    for dep in deps:
        dep_packages.append(dep[PythonPackageInfo].target_package)

    return [
        PythonPackageInfo(
            target_package = package_name,
            target_deps_packages = depset(dep_packages),
            target_external_deps = external_deps,
        )
    ]

_pyproject_deps = aspect(
    attr_aspects = [
        "deps",
    ],
    doc = """
    Collects the dependencies of a pyproject.
    """,
    implementation = _pyproject_deps_impl,
    provides = [PythonPackageInfo]
)

def _pyproject_package(ctx):
    content = '# packages need a __init__.py file\n'
    f = ctx.actions.declare_file('__init__.py')
    ctx.actions.write(f, content)
    return [DefaultInfo(
        files = depset([f]),
    )]


pyproject_package = rule(
    implementation = _pyproject_package,
    attrs = {
        "package": attr.string(
            mandatory = True,
        ),
        "deps": attr.label_list(
            default = [],
            aspects = [
                _pyproject_deps,
            ],
        ),
        "external_deps": attr.string_list_dict(
            default = {},
        ),
    },
)

def _get_package_name(info):
    return """
    '%s',""" % info.target_package

def _pyproject_impl(ctx):
    name = ctx.attr.project
    packages = ctx.attr.packages
    dependencies = ctx.attr.external_deps

    pkgs = ""
    for package in packages:
        info = package[PythonPackageInfo]
        if info:
            pkgs += _get_package_name(info)

    out = ctx.actions.declare_file('pyproject.toml')
    ctx.actions.expand_template(
        template = ctx.file._template,
        output = out,
        substitutions = {
            '$(project_name)': name,
            '$(packages)': pkgs,
            '$(GRPC_VERSION)': GRPC_VERSION,
            '$(PROTOBUF_VERSION)': PROTOBUF_VERSION,
        }
    )

    return [DefaultInfo(
        files = depset([out])
    )]



pyproject = rule(
    implementation = _pyproject_impl,
    attrs = {
        "project": attr.string(
            mandatory = True,
        ),
        "packages": attr.label_list(
            default = [],
            aspects = [
                _pyproject_deps,
            ],
        ),
        "external_deps": attr.string_dict(
            default = {},
        ),
        "_template": attr.label(
            allow_single_file = True,
            default = ':pyproject.tmpl.toml',
        )
    },
)

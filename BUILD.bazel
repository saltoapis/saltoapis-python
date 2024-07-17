load('//scripts/pyproject:pyproject.bzl', 'pyproject')
load(':python_metadata.bzl', 'python_projects')

pyproject(
    name = "pyproject",
    project = "saltoapis-python",
    packages = ["{}:package".format(project) for project in python_projects],
)

filegroup(
    name = "packages",
    srcs = ["{}:package".format(project) for project in python_projects],
)

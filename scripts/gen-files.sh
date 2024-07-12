#!/bin/bash

set +x

# generate pyproject.toml
if ! bazel_out=$(bazel build //:pyproject 2>&1); then
    echo "Error creating pyproject.toml:" >&2
    echo "$bazel_out" >&2
fi

# generate __init__.py files
if ! bazel_out=$(bazel build //:packages 2>&1); then
    echo "Error creating __init__.py files:" >&2
    echo "$bazel_out" >&2
fi

# copy generated files to the repository
cp -rf bazel-bin/* ./
echo "Successfuly generated pyproject.toml and __init__.py files"

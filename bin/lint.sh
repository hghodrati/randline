#!/usr/bin/env bash

set -xeuo pipefail

docker run -v $(pwd):/usr/app randline:latest bash -c "pylint randline"

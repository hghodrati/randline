#!/usr/bin/env bash

set -xeuo pipefail

docker run -it -v $(pwd):/usr/app randline:latest bash

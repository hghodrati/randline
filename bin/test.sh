#!/usr/bin/env bash

set -xeuo pipefail

cmd="python -m pytest tests/${1:-}"
docker run -v $(pwd):/usr/app randline:latest bash -c "${cmd}"

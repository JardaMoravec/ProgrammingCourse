#!/bin/bash
export PYTHONIOENCODING=utf-8
if command -v python3 >/dev/null 2>&1; then
  python3 vpl_evaluate.py
else
  python vpl_evaluate.py
fi

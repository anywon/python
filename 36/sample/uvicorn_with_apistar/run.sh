#!/bin/bash

# new
uvicorn app_server:app --host=0.0.0.0 --port=18080 --log-level=debug

# old
# python3.6 uvicorn app_server:app --workers=3 --bind=[0.0.0.0]:18080 --pid=pid --log-level=DEBUG --keep-alive=100

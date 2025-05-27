#!/usr/bin/env python3

import subprocess

# Runs 'top' in batch mode for a single iteration
output = subprocess.check_output(['top', '-b', '-n', '1'])
print(output.decode())

import os, platform
print(" Loading ")
bit = platform.architecture()[0]
if "64bit" in bit:
  import ankit64
else:
  print(" Not Supported ")

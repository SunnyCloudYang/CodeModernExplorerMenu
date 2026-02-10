#!/usr/bin/env python3
from __future__ import print_function
from shutil import copy
import os
import sys

code_clsid_map = {
  'x86': '978573D8-4037-4F64-A055-0C6BDC64D71F',
  'x64': 'E4E4C322-3388-45AF-8D39-BE19BFC78A18',
  'arm64': '12483301-B459-40BE-A434-DF8010E8958F'
}

root = os.path.dirname(os.path.dirname(__file__))
out_dir = os.path.join(root, 'out')
pkg_type = sys.argv[1]
arch = sys.argv[2]
pkg_dir = os.path.join(out_dir, pkg_type + '_explorer_pkg_' + arch)

# Create output directory.
if not os.path.exists(pkg_dir):
    os.mkdir(pkg_dir)

# Update AppxManifest.
manifest = os.path.join(root, 'template', 'AppxManifest.xml')
with open(manifest, 'r') as f:
  content = f.read()
  content = content.replace('@@PublisherDisplayName@@', 'Cursor Modern Explorer Menu')
  if pkg_type != 'stable':
    print("Only 'stable' package type is supported now.", file=sys.stderr)
    sys.exit(1)
  content = content.replace('@@Publisher@@', 'Cursor.Modern.Explorer.Menu')
  content = content.replace('@@PackageDescription@@', 'Cursor Modern Explorer Menu')
  content = content.replace('@@PackageName@@', 'Cursor.Modern.Explorer.Menu')
  content = content.replace('@@PackageDisplayName@@', 'Cursor Modern Explorer Menu')
  content = content.replace('@@Application@@', 'Cursor.exe')
  content = content.replace('@@ApplicationIdShort@@', 'Cursor')
  content = content.replace('@@MenuID@@', 'OpenWithCursor')
  content = content.replace('@@CLSID@@', code_clsid_map[arch])
  content = content.replace('@@PackageDLL@@', 'Cursor Modern Explorer Menu.dll')

# Copy AppxManifest file to the package directory.
manifest_output = os.path.join(pkg_dir, 'AppxManifest.xml')
with open(manifest_output, 'w+') as f:
  f.write(content)
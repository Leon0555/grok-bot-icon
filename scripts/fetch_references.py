#!/usr/bin/env python3
"""Download the pinned public visual references; never upload user images."""
import hashlib
import json
from pathlib import Path
import sys
import urllib.request


def main():
    root = Path(__file__).resolve().parent.parent
    manifest = json.loads((root / 'references/images.json').read_text())
    for item in manifest['images']:
        name = item['name']
        if Path(name).name != name or not name.endswith('.png'):
            raise ValueError(f'Invalid reference filename: {name}')
        url = item['url']
        if not url.startswith('https://raw.githubusercontent.com/Leon0555/grok-bot-icon/'):
            raise ValueError(f'Unexpected reference URL: {name}')
        dest = root / 'references' / name
        if dest.exists():
            if hashlib.sha256(dest.read_bytes()).hexdigest() != item['sha256']:
                raise ValueError(f'Existing reference differs: {dest}; preserve it and resolve manually')
            print(f'OK {dest}')
            continue
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read(5 * 1024 * 1024 + 1)
        if len(data) > 5 * 1024 * 1024 or not data.startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError(f'Invalid PNG response: {name}')
        if hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError(f'Reference checksum mismatch: {name}')
        # Validate before creating the file; never replace a pre-existing image.
        with dest.open('xb') as file:
            file.write(data)
        print(f'Downloaded {dest}')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as exc:
        print(f'Reference images unavailable: {exc}', file=sys.stderr)
        sys.exit(1)

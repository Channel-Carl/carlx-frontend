"""Audit the canonical Markdown palette tables; no third-party packages needed."""
from pathlib import Path
import re
import sys


def luminance(hex_color):
    values = [int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in values]
    return sum(v * weight for v, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(first, second):
    high, low = sorted((luminance(first), luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def main():
    library = Path(__file__).resolve().parents[1] / 'references' / 'style-library.md'
    content = library.read_text(encoding='utf-8')
    seen = set()
    failures = []
    for row in content.splitlines():
        if not row.startswith('|') or '#' not in row:
            continue
        cells = [cell.strip() for cell in row.strip('|').split('|')]
        if len(cells) != 8:
            failures.append(f'Malformed palette row: {row}')
            continue
        palette_id = cells[0].split('/')[0].strip()
        if palette_id in seen:
            failures.append(f'Duplicate palette: {palette_id}')
        seen.add(palette_id)
        if not all(re.fullmatch(r'#[0-9a-fA-F]{6}', cell) for cell in cells[1:]):
            failures.append(f'Invalid color: {palette_id}')
            continue
        bg, surface, body, muted, accent, on_accent, _line = cells[1:]
        pairs = [('text/bg', body, bg), ('text/surface', body, surface),
                 ('muted/bg', muted, bg), ('muted/surface', muted, surface),
                 ('on-accent/accent', on_accent, accent)]
        for label, foreground, background in pairs:
            ratio = contrast(foreground, background)
            if ratio < 4.5:
                failures.append(f'{palette_id} {label}: {ratio:.3f}:1 < 4.5:1')
    if not seen:
        failures.append('No palettes found')
    style_ids = re.findall(r'^## ([a-z][a-z0-9-]+) ·', content, re.MULTILINE)
    if len(style_ids) != len(set(style_ids)):
        failures.append('Duplicate style ID')
    if failures:
        print('\n'.join(failures))
        return 1
    print(f'PASS: {len(style_ids)} styles, {len(seen)} palettes, {len(seen) * 5} opaque text pairs >= 4.5:1.')
    print('Rendered opacity, imagery, data marks and control boundaries require separate checks.')
    return 0


if __name__ == '__main__':
    sys.exit(main())

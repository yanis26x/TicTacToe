# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['tictac.py'],
    pathex=[],
    binaries=[],
    datas=[('OST/musicCool.wav', 'OST'), ('OST/yay.wav', 'OST'), ('OST/BASKETpELE.wav', 'OST'), ('IMG/sang.png', 'IMG'), ('IMG/xRed.png', 'IMG'), ('IMG/circleWater.png', 'IMG')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TicTacToe26x',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='TicTacToe26x.app',
    icon=None,
    bundle_identifier=None,
)

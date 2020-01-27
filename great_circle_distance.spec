# -*- mode: python -*-

block_cipher = None


a = Analysis(['great_circle_distance.py'],
             pathex=['C:\\dev\\great_circle_calculator'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='great_circle_distance',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

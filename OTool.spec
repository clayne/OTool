# -*- mode: python -*-

block_cipher = None


a = Analysis(['OTool.py'],
             pathex=['C:\\Users\\Hyperenor\\PycharmProjects\\OTool'],
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
          name='OSelector',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='C:\\Users\\Hyperenor\\PycharmProjects\\OTool\\Resources\\icon.ico')
# -*- mode: python -*-
a = Analysis(['..\\..\\bin\\eyegrade'],
             pathex=['.'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
a.datas += Tree('eyegrade\\data', prefix='data')
#a.datas += [('qt.conf', 'installers\\windows\\qt.conf', 'DATA')]
a.datas = list({tuple(map(str.upper, t)) for t in a.datas})
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='eyegrade.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon='eyegrade\\data\\eyegrade.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='eyegrade')

# app.spec
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['C:\\Users\\iuri.santos\\Desktop\\Projetos\\Curso\\projetos-webscrapy\\extrair leilao\\extrair_leilao'],
    binaries=[],
    datas=[
        ('settings.py', 'extrair_leilao'),
        ('spiders', 'extrair_leilao/spiders'),
    ],
    hiddenimports=['scrapy', 'scrapy.utils.project', 'scrapy.crawler'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Remova ou comente a linha abaixo
# pyz = PYZ(a.pure, a.zipped, cipher=block_cipher)
pyz = PYZ(a.pure, [], cipher=block_cipher)  # Atualizado para usar uma lista vazia

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)  # Altere para console=True para ver mensagens no terminal

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')

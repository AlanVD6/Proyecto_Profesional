# build_grammar.ps1
# -------------------
# Regenera el lexer y el parser de PyLite a partir de los archivos
# .g4 usando tu instalacion local de ANTLR4 (la misma que ya usas en
# tu proyecto individual: D:\Automatas ll\ANTLR\antlr-4.13.2-complete.jar).
#
# Uso (desde la raiz del proyecto, en PowerShell):
#   .\build_grammar.ps1
#
# Si tu jar esta en otra ruta, cambia la variable $AntlrJar de abajo.

$AntlrJar = "D:\Automatas ll\ANTLR\antlr-4.13.2-complete.jar"

if (-not (Test-Path $AntlrJar)) {
    Write-Host "No se encontro el jar de ANTLR en: $AntlrJar" -ForegroundColor Red
    Write-Host "Edita la variable `$AntlrJar en este script con la ruta correcta." -ForegroundColor Yellow
    exit 1
}

$ErrorActionPreference = "Stop"

# Limpia y recrea la carpeta generated/
if (Test-Path "generated") {
    Remove-Item "generated" -Recurse -Force
}
New-Item -ItemType Directory -Path "generated" | Out-Null

# Copia la clase base del lexer (no la genera ANTLR, es codigo propio)
Copy-Item "grammar\PyLiteLexerBase.py" "generated\PyLiteLexerBase.py"

Push-Location grammar

Write-Host "Generando lexer..." -ForegroundColor Cyan
java -jar $AntlrJar -Dlanguage=Python3 -visitor -no-listener -o ..\generated PyLiteLexer.g4
if ($LASTEXITCODE -ne 0) { Pop-Location; exit 1 }

Write-Host "Generando parser..." -ForegroundColor Cyan
java -jar $AntlrJar -Dlanguage=Python3 -visitor -no-listener -o ..\generated -lib ..\generated PyLiteParser.g4
if ($LASTEXITCODE -ne 0) { Pop-Location; exit 1 }

Pop-Location

Write-Host "Listo. Archivos generados en .\generated\" -ForegroundColor Green
Get-ChildItem "generated" | Select-Object Name

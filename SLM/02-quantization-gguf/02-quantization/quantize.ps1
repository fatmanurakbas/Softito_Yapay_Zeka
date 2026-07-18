param(
    [Parameter(Mandatory = $true)][string]$Source,
    [Parameter(Mandatory = $true)][string]$Output,
    [Parameter(Mandatory = $true)][string]$Type,
    [string]$LlamaQuantizePath = "llama-quantize"
)

$sourcePath = Resolve-Path -LiteralPath $Source -ErrorAction Stop
$outputParent = Split-Path -Parent $Output
if ($outputParent -and -not (Test-Path -LiteralPath $outputParent)) {
    New-Item -ItemType Directory -Path $outputParent -Force | Out-Null
}
if (Test-Path -LiteralPath $Output) {
    throw "Hedef dosya zaten var: $Output"
}

Write-Host "Quantization başlıyor: $($sourcePath.Path) -> $Output ($Type)"
& $LlamaQuantizePath $sourcePath.Path $Output $Type
if ($LASTEXITCODE -ne 0) { throw "llama-quantize başarısız oldu (çıkış kodu: $LASTEXITCODE)." }
Write-Host "Tamamlandı: $Output"

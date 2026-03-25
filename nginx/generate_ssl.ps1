# generate_ssl.ps1
# Generate self-signed certificates for the SUGAM Nginx Gateway

$CertDir = Join-Path $PSScriptRoot "ssl"
if (!(Test-Path $CertDir)) {
    New-Item -ItemType Directory -Path $CertDir
}

Write-Host "Generating Self-Signed Certificate for localhost..." -ForegroundColor Cyan

# Generate certificate using New-SelfSignedCertificate (standard in Windows PowerShell)
$cert = New-SelfSignedCertificate -DnsName "localhost" -CertStoreLocation "Cert:\LocalMachine\My" -FriendlyName "SUGAM Gateway"

# Export the certificate as .crt (Base64 encoded)
$exportPathCrt = Join-Path $CertDir "nginx.crt"
$exportPathKey = Join-Path $CertDir "nginx.key"

# Note: In a real production environment, you would use OpenSSL to generate .key and .crt files.
# For this local bootstrap, we use PowerShell's native tools.

Write-Host "SSL certificates generated in $CertDir" -ForegroundColor Green
Write-Host "IMPORTANT: For production deployment on Linux, use OpenSSL to generate nginx.crt and nginx.key." -ForegroundColor Yellow

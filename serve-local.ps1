param(
    [switch]$Stop,
    [int]$Port = 8080
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$pidFile = Join-Path $root ".serve-local.pid"

if ($Stop) {
    if (Test-Path -LiteralPath $pidFile) {
        $serverPid = [int](Get-Content -Raw -LiteralPath $pidFile)
        $serverProcess = Get-Process -Id $serverPid -ErrorAction SilentlyContinue

        if ($serverProcess) {
            Stop-Process -Id $serverPid -Force
            Write-Host "Stopped local server process $serverPid."
        } else {
            Write-Host "No running local server was found."
        }

        Remove-Item -LiteralPath $pidFile -Force
    } else {
        Write-Host "No running local server was found."
    }

    exit
}

if (Test-Path -LiteralPath $pidFile) {
    $serverPid = [int](Get-Content -Raw -LiteralPath $pidFile)
    $serverProcess = Get-Process -Id $serverPid -ErrorAction SilentlyContinue

    if ($serverProcess) {
        Write-Host "Local server is already running at http://localhost:$Port/"
        Write-Host "Run .\serve-local.ps1 -Stop to stop it."
        exit
    }

    Remove-Item -LiteralPath $pidFile -Force
}

$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add("http://localhost:$Port/")

try {
    $listener.Start()
} catch {
    Write-Host "Could not start http://localhost:$Port/ because that address is already in use."
    Write-Host "Close the app using port $Port, or run: .\serve-local.ps1 -Stop"
    Write-Host "If the page opens in your browser, the server is already running."
    exit 1
}

Write-Host "Serving $root at http://localhost:$Port/"
Write-Host "Press Ctrl+C to stop."
Set-Content -LiteralPath $pidFile -Value $PID

$contentTypes = @{
    ".html" = "text/html; charset=utf-8"
    ".css" = "text/css; charset=utf-8"
    ".js" = "application/javascript; charset=utf-8"
    ".png" = "image/png"
    ".jpg" = "image/jpeg"
    ".jpeg" = "image/jpeg"
    ".svg" = "image/svg+xml"
}

try {
    while ($listener.IsListening) {
        $context = $listener.GetContext()
        $requestPath = [Uri]::UnescapeDataString($context.Request.Url.AbsolutePath.TrimStart("/"))

        if ([string]::IsNullOrWhiteSpace($requestPath)) {
            $requestPath = "index.html"
        }

        $filePath = Join-Path $root $requestPath

        if (-not (Test-Path -LiteralPath $filePath -PathType Leaf)) {
            $filePath = Join-Path $root "index.html"
        }

        $extension = [System.IO.Path]::GetExtension($filePath).ToLowerInvariant()
        $context.Response.ContentType = if ($contentTypes.ContainsKey($extension)) {
            $contentTypes[$extension]
        } else {
            "application/octet-stream"
        }

        $bytes = [System.IO.File]::ReadAllBytes($filePath)
        $context.Response.ContentLength64 = $bytes.Length
        $context.Response.OutputStream.Write($bytes, 0, $bytes.Length)
        $context.Response.OutputStream.Close()
    }
} finally {
    if ($listener.IsListening) {
        $listener.Stop()
    }

    if (Test-Path -LiteralPath $pidFile) {
        $serverPid = [int](Get-Content -Raw -LiteralPath $pidFile)
        if ($serverPid -eq $PID) {
            Remove-Item -LiteralPath $pidFile -Force
        }
    }
}

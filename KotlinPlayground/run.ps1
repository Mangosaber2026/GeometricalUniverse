
$ProjectRoot = $PSScriptRoot

Push-Location $ProjectRoot

try {
    & .\gradlew.bat jsNodeDevelopmentRun

    if ($LASTEXITCODE -ne 0) {
        throw "Kotlin/JS execution failed."
    }
}
finally {
    Pop-Location
}

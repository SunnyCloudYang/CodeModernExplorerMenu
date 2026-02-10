# If not running as Administrator, re-launch the script with elevated privileges
if (-not ([Security.Principal.WindowsPrincipal]::new([Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator))) {
    Start-Process powershell.exe -ArgumentList "-NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File `"$($script:MyInvocation.MyCommand.Path)`"" -Verb RunAs -Wait -WindowStyle Minimized
    exit
}

$ScriptRoot = if ( $PSScriptRoot ) { $PSScriptRoot } else { ($(try { $script:psEditor.GetEditorContext().CurrentFile.Path } catch {}), $script:MyInvocation.MyCommand.Path, $script:PSCommandPath, $(try { $script:psISE.CurrentFile.Fullpath.ToString() } catch {}) | % { if ($_ ) { $_.ToLower() } } | Split-Path -EA 0 | Get-Unique ) | Get-Unique }

$ProductName = 'Cursor Modern Explorer Menu'
$PackageName = $ProductName -replace '\s+', '.'
$RegKeyPath = 'HKCU\SOFTWARE\Classes\' + ($ProductName -replace '\s+')

# Remove shell extension registration for both registry views
REG DELETE "$RegKeyPath" /reg:64 /f
REG DELETE "$RegKeyPath" /reg:32 /f

Get-AppxPackage -Name $PackageName | Remove-AppxPackage 

# Clean up the external install directory created on install
$InstallRoot = Join-Path $Env:LOCALAPPDATA "Programs\$ProductName"
if (Test-Path $InstallRoot) {
    Remove-Item -Path $InstallRoot -Recurse -Force
}

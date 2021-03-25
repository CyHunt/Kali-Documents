# Requirements: Need to be signed-in to the system using a domain account example "corp.com\offsec"

# Construct the LDAP Provider Path. Example: "LDAP://DC01.corp.com/DC=corp,DC=com"
# This is the full LDAP Provider Path needed to perform LDAP queries against the domain controller
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = ($domainObj.PdcRoleOwner).Name
$SearchString = "LDAP://"
$SearchString += $PDC + "/"
$DistinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$SearchString += $DistinguishedName

# Instantiate the DirectorySearcher class with the LDAP provider path. Allowing us to perform a search against the Active Directory results.
$Searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI]$SearchString)
$objDomain = New-Object System.DirectoryServices.DirectoryEntry
$Searcher.SearchRoot = $objDomain

# Creates a search filter that will List members of nested groups
# If the group is a member of another nested group, update the filter to keep drilling down, repeat this process, its that simple
$Searcher.filter="name=Secret_group"

$Result = $Searcher.FindAll()

# This last bit cleans up the results a bit making them cleaner and easier to view
Foreach($obj in $Result)
{
	$obj.Properties.member
}
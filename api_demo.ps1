# Define the URL and token
$token = "ACCESS_TOKEN_HERE"
$serialNumber = "FP-XX-XXXXXXX"
$url = "https://fernportal.xtherma.de/api/device/$serialNumber"

# Make the API call
$response = Invoke-RestMethod -Uri $url -Headers @{Authorization = "Bearer $token"}

# Display the response
$response | Format-List

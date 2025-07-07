Xtherma-Rest-API v0.1 documentation
__

## Changelog

07.07.2025: Die Änderungen kamen mit der der Einführung von TCP dazu:
- Wir hatten pk 2x in der API, sind jetzt pk (PK ein/aus) und pkl (PK Leistung in %).
- Error (Wärmepumpe ungestört) indiziert Berücksichtigt falls der Wert von 1 auf 0 geht die folgende Meldungen: P16, F20, S14, S13, S05, S08, F01, F02, F03, F04, F05, F06, F07, F08, F10, F11, F12, P11, E01, E02, E03, E04, E05, E06, E07, E08
- Controller_v ist die aktuelle Regler-Version (240 = V2.40).
- h1_target, h2_target, c1_target und c2_target sind die Zielwerte der Kreise 1 und 2 jeweils im Heizen und Kühlen.
- h2_target ist angepasst, war versehentlich falsch eingetragen

__

## Xtherma-Rest-API is a restful API. 
It is read-only for now.
The endpoints accessible are temporary and prone to change. Currently, the limit is 1500 requests per day.
If you would like a specific setting exposed in the API please tell us via info [at] xtherma.de.


## Authentification
Authentification is currently done via bearer token. 
Authentification via oAuth2 is under development and will be available shortly.
A Fernportal-User with an assigned heat pump is needed to access data. 

## Getting your access token
Go to your user profile by clicking the grey user icon in the top right of the fernportal and scroll to the bottom to retrieve your access token. 

## Getting data
Individual heat pumps are identified by their Fernportal-S/N. 
You can find your Fernportal-S/N on fernportal.xtherma.de
on the overview tab under "Gerät" -> "SN-Fernportal-Modul".

There are many ways to fetch data from the API. Here is an example using curl:
```
curl -H "Authorization: Bearer YOUR_TOKEN_HERE" https://fernportal.xtherma.de/api/device/FP-YOUR_FP_NUM
```
The response will look like this:

```
{
    "serial_number": "FP-YOUR_FP_NUM",
    "settings": [
		{
	    "key" : "002"	
            "name": "002 - Betriebsmodus",
            "value": 1,
            "min": "",
            "max": "",
            "mapping": "Standby,Heizbetrieb, Kühlbetrieb,Warmwasser,Automatik",
            "unit": "",
            "output_factor": "",
            "input_factor": ""
        }
    ]
}
```
### key
This is a unique identifier for a given settings. 

### name
This is the name of the settin. It is the same as on Fernportal.

```diff
- This key/value pair will soon be deprecated.
```
### value
This is the value of the setting. These values are always standard 16-bit unsigned INT. 
If you expect a signed value, e.g., for a temperature, you must sign them yourself.

### min
This is the minimal value of "value". If it is empty it defaults to 0.

### max 
This is the max value of "value". If it is empty it defaults to 65335.

### mapping
This is a comma-separated list of strings that further describe "value".
In this example "Betriebsmodus" can be 0 = Standby, 1 = Heizbetrieb, 2 = Kühlbetrieb ...

### unit
If "value" is a numerical value, the unit contains the unit as a string e.g. "°C", "K" and so on. 

### output_factor
not used right now.

### input_factor
this field contains a mathematical instruction for value as a string. "/10" means you have to divide by 10 to get the real value. 





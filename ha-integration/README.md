<h2 align="center">
   <a href="https://www.xtherma.de/">Xtherma</a> and<a href="https://www.home-assistant.io"> Home Assistant</a> Integration
   </br></br>
</h2>

## Installation

Kopiere den Ordner `custom_components/xtherma_fp` in die HA installation, so dass er dort unter `/config/custom_components/xtherma_fp` gefunden wird.
Anschließend Home Assistant neu starten.

## Konfiguration

In **Einstellungen > Geräte & Dienste** auf **Integration hinzufügen** klicken. Der Konfigurationsdialog fragt nach dem REST-API Token und der Seriennummer.

Beides kann aus dem Fernportal herauskopiert werden (Start Seite, Mein Account.)

## Funktion

Aktuell ist das REST-API read-only. Es werden nur die Sensorwerte des Datenbereichs `db_data` angezeigt.

## Logging

Debug logs können folgendermaßen eingeschaltet werden:

```yaml
logger:
  default: info
  logs:
    custom_components.xtherma_fp: debug
```

# Lineare elektrische Netzwerke - Workshop A

Dieses Repository enthält sämtliche Materialien, Skripte und Ergebnisse für die Bearbeitung des **Lineare elektrische Netzwerke - Workshop A**. Der Fokus des Projekts liegt auf der Untersuchung der Eigenschaften von Solarzellen und der Analyse von Energiespeichern.

## Inhalt

Das Repository umfasst:

- **LaTeX-Projekt:**
    - Code und Dokumentation der schriftlichen Ausarbeitung.
- **Python/Matlab-Skripte:**
    - Analyse- und Visualisierungsskripte für Messdaten.
- **Messwerte der Versuche:**
    - Alle experimentellen Messwerte (CSV-Dateien).
- **Plots und Diagramme:**
    - Grafische Darstellung der Messresultate.
- **PDF-Dokumente:**
    - Lösungen der Aufgaben sowie Zusammenfassungen.
- **Craft-Dokument:**
    - Übersicht über den Projektaufbau und -fortschritt ([Craft-Link](https://s.craft.me/mhUFPI9u8bNAJS)).

## Ziele der Arbeit

1. **Vermessung von Solarzellen:**
    - Bestimmung der Strom-Spannungs-Kennlinie unter verschiedenen Bestrahlungsbedingungen.
    - Berechnung des Maximum-Power-Points (MPP).
2. **Langzeitmessung unter realen Bedingungen:**
    - Untersuchung des Energiegewinns in Abhängigkeit der Sonneneinstrahlung.
3. **Energiespeicherung:**
    - Analyse eines Speicherkondensators als Energiespeicher.
    - Untersuchung von Lade- und Entladeverhalten sowie Wirkungsgrad.
4. **Vergleich von Photovoltaikanlagen mit und ohne Energiespeicher.**


## Nutzung der Skripte

### Voraussetzungen

- **Python 3.10+** mit den folgenden Bibliotheken:
    - `numpy`
    - `pandas`
    - `matplotlib`
- Alternativ Matlab (falls MATLAB-Skripte verwendet werden).

### Beispiel: Ausführung eines Python-Skripts

```bash
# Navigiere ins Skript-Verzeichnis
cd scripts/

# Führe ein Skript aus
python plot_u_t.py
```

Autoren

- **Bryan Jonas** (Messdurchführung der Versuche)
- **Henri Schulz** (Python-Skripte zur Datenanalyse)
- **Simon Hagenlocher** (Analyse der elektrischen Netze & Ergebnisse)

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

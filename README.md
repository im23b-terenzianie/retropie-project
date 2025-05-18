# 🎮 Raspberry Pi RetroPie ROM Organizer

Dieses Projekt beinhaltet ein Python-Script, das ROM-Dateien automatisch in die richtigen RetroPie-Ordner verschiebt – komplett hands-free. Ideal für jeden, der sein Setup sauber, automatisiert und cool halten will 😎

---

## 🧱 Projektstruktur

```
retropie-project/
├── scripts/
│   └── sort_roms.py        # Haupt-Skript zur ROM-Verwaltung
├── roms_inbox/             # Eingangsordner für neue ROM-Dateien
├── README.md               # Diese Datei
└── .gitignore              # Optional: für Pyc-Files etc.
```

---

## ⚙️ Voraussetzungen

* Raspberry Pi mit installiertem **RetroPie**
* Python 3 (ist bei RetroPie OS schon dabei)
* Zugriff via SSH oder direkt am Pi
* Git (für GitHub-Integration)

---

## 📅 Setup-Anleitung

### 1. Projekt klonen

```bash
git clone git@github.com:DEIN-BENUTZERNAME/retropie-project.git
cd retropie-project
```

### 2. Ordner für neue ROMs anlegen

```bash
mkdir ~/roms_inbox
```

Hier landen alle neuen ROMs, bevor sie automatisch einsortiert werden.

### 3. Python-Script ausführen

```bash
python3 scripts/sort_roms.py
```

Das Script prüft die Dateiendung, erkennt das System (z. B. SNES, GBA, NES etc.) und verschiebt die Datei in den passenden `RetroPie/roms/<system>`-Ordner.

---

## 🚀 Automatisierung (optional)

Wenn du willst, dass das Script **automatisch alle 5 Minuten läuft**:

```bash
crontab -e
```

Dann ganz unten einfügen:

```cron
*/5 * * * * /usr/bin/python3 /home/pi/retropie-project/scripts/sort_roms.py
```

(Verpflichte dich vorher, dass dein Pfad zum Script korrekt ist!)

---

## 🗂️ Unterstützte ROM-Endungen

Beispiel:

* `.nes`, `.smc`, `.gba`, `.gb`, `.gbc`, `.n64`, `.bin`, `.cue`, `.zip`, `.gen`, `.md`, `.sms`, `.gg`, `.sg` usw.

Die genaue Zuordnung steht im Python-Script `sort_roms.py` → dort kannst du einfach neue Systeme ergänzen.

---

## 👾 ROMs beschaffen (Legal!)

> Bitte lade nur ROMs herunter, die du legal besitzen darfst!

## 🧠 Idee & Motivation

Ich wollte mir das Leben einfach machen: ROMs dumpen → Script regelt den Rest.
Wenn du auch faul-effizient bist, ist das hier dein Ding 💡

---

## ✨ Autor

**@im23b-terenzianie**
💬 GitHub, 🎩 Raspberry Pi Fan, 🧪 Bastler mit Plan


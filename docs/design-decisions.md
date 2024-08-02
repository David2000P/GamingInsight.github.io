---
title: Design Decisions
nav_order: 3
---



{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


## 01: Entwicklungsumgebung und Sprache
Meta
Status: Decided
Updated: 01-Aug-2024

**Problemstellung**
Welche Entwicklungsumgebung und Programmiersprache bieten die optimale Unterstützung für die schnelle Entwicklung und Wartung unserer Webanwendung?

**Entscheidung**
Wir entschieden uns für Visual Studio als Entwicklungsumgebung und Python als Programmiersprache, da beide Tools umfangreiche Unterstützung für schnelle Entwicklung und effiziente Fehlerbehebung bieten. Außerdem war es im Kurs auch vorgegeben.

**Mögliche Optionen**
JavaScript mit Node.js: Schnelle Ausführung und gut für Echtzeit-Anwendungen.
Ruby on Rails: Schnelle Entwicklung mit vielen eingebauten Funktionen.

**Pro/Kontra:**
JavaScript mit Node.js: Pro: große Community, Kontra: asynchroner Programmierstil kann komplex sein.
Ruby on Rails: Pro: "Convention over configuration" vereinfacht viele Aufgaben, Kontra: weniger Flexibilität im Vergleich zu Python.


## 02: Web-Framework
Meta
Status: Decided
Updated: 26-Jul-2024

**Problemstellung**
Welches Web-Framework unterstützt am besten unsere Anforderungen an Flexibilität und einfache Skalierbarkeit?

**Entscheidung**
Wir haben uns für das Flask-Framework entschieden, da es leichtgewichtig ist und uns die benötigte Flexibilität bietet, um spezifische Lösungen für unsere Anforderungen zu entwickeln.

**Betrachtete Optionen**
Django: Bietet ein umfangreicheres Framework.
Express.js: Leichtgewichtig und flexibel in der JavaScript-Umgebung.

**Pro/Kontra:**
Django: Pro: viele eingebaute Features, Kontra: zu schwerfällig für unsere Bedürfnisse.
Express.js: Pro: hohe Flexibilität, Kontra: erfordert tiefere JavaScript-Kenntnisse.


## 03: Datenmanagement
Meta
Status: Decided
Updated: 20-Jul-2024

**Problemstellung**
Wie sollen CRUD-Operationen (Create, Read, Update, Delete) in unserer Datenbank gehandhabt werden?

**Entscheidung**
Wir haben uns entschieden, SQLite mit einfachem SQL zu verwenden, um die Datenverwaltung direkt und ohne zusätzliche Abstraktionsschichten zu handhaben.

**Betrachtete Optionen**
Verwendung von SQLAlchemy: Bietet eine ORM-Schicht für Python-Anwendungen.
Direkte Verwendung von SQL-Befehlen: Einfacher Zugang und Kontrolle über die Datenbank.

**Pro/Kontra:**
Verwendung von SQLAlchemy: Pro: abstrahiert Datenbankzugriffe und vereinfacht Code, Kontra: erfordert zusätzlichen Lernaufwand und Setup.
Direkte Verwendung von SQL-Befehlen: Pro: vollständige Kontrolle und einfaches Setup, Kontra: kann bei komplexeren Datenstrukturen unübersichtlich werden.

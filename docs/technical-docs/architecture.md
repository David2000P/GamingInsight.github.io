---
title: Architecture
parent: Technical Docs
nav_order: 1
---

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

# Backend-Architektur

## Flask:

Wir haben uns für Flask entschieden, weil es ein leichtgewichtiges und flexibles Webanwendungs-Framework ist, das uns die notwendige Agilität für schnelle Entwicklungszyklen bietet. Flask ermöglicht es uns, robuste Backend-Logiken und APIs effizient zu implementieren, was für die Unterstützung unserer dynamischen Frontend-Anwendungen unerlässlich ist. Die Wahl fiel auf Flask, da es besonders gut für kleinere bis mittelgroße Projekte geeignet ist, bei denen eine schnelle Markteinführung und einfache Skalierbarkeit im Vordergrund stehen.

## SQLite:

SQLite wurde als unser Datenbankverwaltungssystem ausgewählt, weil es leichtgewichtig ist und keine separate Server-Installation benötigt. Dies macht es ideal für unsere Entwicklungs- und Testumgebungen, wo Einfachheit und Schnelligkeit gefordert sind. SQLite unterstützt uns bei der schnellen Prototypentwicklung und ist durch seine einfache Konfigurierbarkeit besonders benutzerfreundlich.

## Flask-SQLAlchemy:

Die Integration von Flask-SQLAlchemy in unser Projekt vereinfacht den Umgang mit der Datenbank erheblich. Als ORM-Tool abstrahiert es Datenbankzugriffe, was die Entwicklung und Wartung der Datenbanklogik vereinfacht. Wir haben Flask-SQLAlchemy gewählt, weil es uns eine konsistente und effiziente Interaktion mit der Datenbank ermöglicht und dabei hilft, die Komplexität der direkten Datenbankmanipulation zu reduzieren.

## Flask-Login:

Für die Benutzerverwaltung innerhalb unserer Anwendung nutzen wir Flask-Login. Diese Wahl wurde getroffen, weil es eine einfache Implementierung von Authentifizierungsmechanismen bietet, die für die Sicherheit unserer Plattform entscheidend ist. Flask-Login unterstützt das Management von Benutzersitzungen und erleichtert so die Erstellung einer sicheren und benutzerfreundlichen Anwendung.
Frontend-Architektur

## Jinja2:

Im Frontend verwenden wir Jinja2 als Template-Engine, die eine klare Trennung zwischen Design und Logik ermöglicht. Jinja2 unterstützt leistungsstarke Funktionen zur dynamischen HTML-Generierung, was uns große Flexibilität bei der Anpassung der Benutzeroberfläche bietet. Diese Wahl trägt erheblich zur Wartbarkeit und Erweiterbarkeit unseres Frontends bei.

## CSS:

CSS ist unerlässlich für die Gestaltung des visuellen Designs unserer Webseiten. Wir haben CSS gewählt, um benutzerfreundliche und ästhetisch ansprechende Interfaces zu schaffen, die das Benutzererlebnis verbessern. Durch CSS können wir präzise Layouts erstellen, die die Zugänglichkeit und die Usability unserer Plattform fördern.

## HTML:

HTML ist die Grundlage für das Erstellen unserer Webseiten und ist entscheidend für die Strukturierung des Inhalts. Die Entscheidung für HTML fiel, weil es das Rückgrat jeder Webseite bildet und essentiell für die Erstellung einer funktionsfähigen Benutzeroberfläche ist.

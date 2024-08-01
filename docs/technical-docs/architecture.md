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
# Backend


Flask Verwendung: Flask ist ein leichtgewichtiges WSGI-Webanwendung-Framework. Es wird verwendet, um die Backend-Logik und APIs zu implementieren, die die Frontend-Anwendungen bedienen. Grund der Wahl: Flask bietet Flexibilität und ist einfach zu verwenden, was schnelle Entwicklungszyklen ermöglicht. Es eignet sich besonders gut für kleinere bis mittelgroße Projekte mit Bedarf an einer soliden Webanwendungsstruktur ohne den Overhead größerer Frameworks wie Django.

SQLite Verwendung: SQLite ist eine relationale Datenbankverwaltungssystem, das in einer C-Bibliothek enthalten ist. In Flask-Projekten dient es dazu, Daten effizient zu speichern und zu verwalten. Grund der Wahl: SQLite ist leichtgewichtig und benötigt keine separate Server-Installation, was es ideal für Entwicklungsumgebungen und kleinere Anwendungen macht. Es unterstützt schnelle Prototypentwicklung und ist einfach zu konfigurieren.

Flask-SQLAlchemy Verwendung: SQLAlchemy ist ein SQL-Toolkit und ORM (Object Relational Mapper) für Python. Flask-SQLAlchemy ist eine Erweiterung für Flask, die mehr Komfort bei der Verwendung von SQLAlchemy bietet. Grund der Wahl: Es abstrahiert Datenbankzugriffe und verbessert die Datenbankinteraktionen durch eine höhere Abstraktionsebene, was die Wartung und Erweiterung der Datenbanklogik erleichtert.

Flask-Login Verwendung: Flask-Login bietet Benutzerverwaltung für Flask-Anwendungen und unterstützt das Management von Benutzersitzungen. Grund der Wahl: Es erleichtert die Implementierung von Authentifizierungsmechanismen, was die Entwicklung von sicheren Anwendungen vereinfacht und verbessert.

# Frontend

Jinja2 Verwendung: Jinja2 ist eine Template-Engine für Python, die in Flask-Anwendungen für die Erstellung von HTML-Templates verwendet wird. Grund der Wahl: Sie ermöglicht eine klare Trennung zwischen Design und Logik, bietet leistungsstarke Funktionen zur dynamischen Generierung von HTML-Inhalten und erhöht die Flexibilität und Wartbarkeit des Frontends.

CSS Verwendung: CSS (Cascading Style Sheets) wird verwendet, um das Layout und das visuelle Design der Webseiten zu gestalten. Grund der Wahl: CSS ist essentiell für die Erstellung benutzerfreundlicher Interfaces und ermöglicht die kreative und präzise Gestaltung der Benutzeroberfläche.

HTML Verwendung: HTML (Hypertext Markup Language) ist die Standard-Auszeichnungssprache für das Erstellen von Webseiten und Webanwendungen. Grund der Wahl: HTML bildet das Grundgerüst jeder Webseite und ist grundlegend für die Strukturierung und den Inhalt der Benutzeroberfläche.



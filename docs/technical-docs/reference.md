---
title: Reference
parent: Technical Docs
nav_order: 3
---
<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

{: .no_toc }
# Reference Documentation

## Inhaltsverzeichnis
- [Benutzerregistrierung](#benutzerregistrierung)
- [Bewertungen verwalten](#bewertungen-verwalten)
- [Benachrichtigungen](#benachrichtigungen)

### Benutzerregistrierung
`register_user()`
**Route:** /register/

**Methods:** POST

**Purpose:** Registriert einen neuen Benutzer auf der Plattform. Sammelt Benutzerdaten wie E-Mail, Benutzername und Passwort und speichert sie sicher in der Datenbank.

**Sample Output:**

Wenn erfolgreich: `{"status": "success", "message": "User registered successfully."}`

Wenn fehlerhaft: `{"status": "error", "message": "Registration failed. Please try again."}`

### Bewertungen verwalten
`post_review()`
**Route:** /reviews/

**Methods:** POST

**Purpose:** Ermöglicht es Benutzern, eine Bewertung für ein Unternehmen abzugeben. Nimmt Benutzer-Feedback und Bewertungsdetails entgegen und speichert diese in der Datenbank.

**Sample Output:**

Wenn erfolgreich: `{"status": "success", "message": "Review posted successfully."}`

Wenn fehlerhaft: `{"status": "error", "message": "Failed to post review. Please try again."}`

`get_reviews(company_id)`
**Route:** /reviews/<int:company_id>

**Methods:** GET

**Purpose:** Ruft alle Bewertungen für ein spezifisches Unternehmen ab. Nützlich für Nutzer, die Bewertungen zu einem bestimmten Unternehmen sehen möchten.

**Sample Output:**

Liste von Bewertungen: `{"reviews": [{"rating": 4, "comment": "Great work environment."}, {"rating": 5, "comment": "Excellent management."}]}`

### Benachrichtigungen
`send_notification()`
**Route:** /notify/

**Methods:** POST

**Purpose:** Sendet Benachrichtigungen an Benutzer, z.B. wenn eine neue Bewertung gepostet wird oder wenn eine wichtige Information verfügbar ist.

**Sample Output:**

Wenn erfolgreich: `{"status": "success", "message": "Notification sent."}`

Wenn fehlerhaft: `{"status": "error", "message": "Failed to send notification."}`

---
title: User Evaluation
nav_order: 4
---


{: .no_toc }
#  User Evaluation 


<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

### Meta

Status: Work in progress- **Done** - Obsolete

Updated: 31-Jul-2024


## 01: Registrierungsprozess

**Goals**

Unser Hauptziel bei der Gestaltung des Registrierungsprozesses war es, eine einfache und sichere Methode zu entwickeln, mit der neue Benutzer effizient und ohne unnötige Komplikationen ein Konto erstellen können. Angesichts der Bedeutung des ersten Eindrucks wollten wir sicherstellen, dass dieser Prozess nicht nur technisch einwandfrei funktioniert, sondern auch die Nutzer durch seine Benutzerfreundlichkeit überzeugt. Der Prozess sollte schnell und reibungslos verlaufen, um eine hohe Konversionsrate von Besuchern zu registrierten Nutzern zu gewährleisten und gleichzeitig hohe Sicherheitsstandards zu erfüllen, um die Vertrauenswürdigkeit der Plattform zu stärken. Allerdings brauchen wir mehr Zeit um die Sicherheitsstandards gut zu implementieren.

**Method**

Die Methode umfasste die Entwicklung mehrerer Prototypen des Registrierungsprozesses, die in einer kontrollierten Testumgebung evaluiert wurden. Wir setzten auf die Methodik des iterativen Designs, bei dem Feedbackschleifen integriert sind, um den Prozess kontinuierlich zu verbessern. Dazu gehörten sowohl technische Tests zur Überprüfung der Sicherheitsaspekte als auch Usability-Tests, um die Benutzerfreundlichkeit zu evaluieren. Diese Tests wurden durch simulierte Nutzungsszenarien unterstützt, in denen verschiedene Altersgruppen und Nutzertypen durch den Prozess geführt wurden, um ein breites Spektrum an Benutzererfahrungen zu sammeln.

**Results**

Die Ergebnisse aus den internen Tests zeigten, dass ein mehrstufiger Registrierungsprozess mit klaren Anweisungen und Feedback am effektivsten ist. Nutzer bevorzugten eindeutige, kurze Formulare mit visuellen Indikatoren für den Fortschritt. Ebenso wurde deutlich, dass eine zu hohe Anzahl an Pflichtfeldern die Abbruchrate erhöht. Die Integration von Sicherheitsfeatures wie Captcha und Zwei-Faktor-Authentifizierung wurde positiv aufgenommen, sofern diese nicht als aufdringlich empfunden wurden.

**Implications**

Basierend auf diesen Ergebnissen haben wir entschieden, den Registrierungsprozess mit einer minimalen Anzahl an Pflichtfeldern und optionalen Zusatzinformationen zu implementieren, um den Prozess schneller und benutzerfreundlicher zu gestalten. Weiterhin werden wir regelmäßige Updates und Sicherheitsüberprüfungen einplanen, um die Integrität der Plattform zu gewährleisten. Zukünftige Überarbeitungen werden auch adaptive Sicherheitsmaßnahmen berücksichtigen, die basierend auf dem Nutzerverhalten und externen Bedrohungen angepasst werden können.

## 02: Nutzung der Bewertungsfunktion

**Goals**

Das Ziel der Bewertungsfunktion war es, eine benutzerfreundliche und ansprechende Schnittstelle zu entwickeln, die es den Nutzern ermöglicht, schnell und unkompliziert Feedback zu geben. Wir wollten sicherstellen, dass diese Funktion reichhaltiges, nuanciertes Feedback fördert, das sowohl für andere Nutzer als auch für Entwickler von Wert ist.

**Method**

Für die Evaluation der Bewertungsfunktion setzten wir auf Prototypen-Tests, bei denen verschiedene Bewertungssysteme ausprobiert wurden, darunter Sternebewertungen, numerische Skalen und textbasierte Bewertungen. Zusätzlich führten wir Fokusgruppeninterviews mit typischen Nutzern durch, um zu verstehen, welche Arten von Feedback sie am nützlichsten finden und welche Anreize sie motivieren würden, Bewertungen abzugeben.

**Results**

Die Testergebnisse zeigten eine klare Präferenz für eine Kombination aus Sternebewertungen und textbasierten Bewertungen, da diese den Nutzern die Flexibilität bieten, präzise und detaillierte Rückmeldungen zu geben.

Unser Bewertungssystem wurde in verschiedene Kategorien unterteilt, sodass eine Bewertung immer auf eine spezifische Kategorie bezogen ist. Zu den Bewertungskategorien gehören beispielsweise Work-Life-Balance, Bezahlung, Teamarbeit und Arbeitsumgebung. Nutzer haben die Möglichkeit, Bewertungen für jede Kategorie separat abzugeben, was ein differenziertes Feedback ermöglicht.

Die Bewertungen können in einer übersichtlichen Tabellenform angezeigt werden, die es den Nutzern ermöglicht, die Bewertungen der verschiedenen Kategorien separat zu betrachten. Diese Struktur erleichtert es, spezifische Aspekte der Nutzererfahrung zu identifizieren und gezielt darauf einzugehen. Nutzer schätzten auch die Möglichkeit, Feedback anonym oder unter einem Pseudonym zu veröffentlichen, was die Beteiligungsrate deutlich erhöhte.

**Implications**

Aufgrund dieser Erkenntnisse haben wir beschlossen, ein hybrides Bewertungssystem zu implementieren, das sowohl quantitative als auch qualitative Feedbackelemente enthält. Weiterhin planen wir, regelmäßige Anpassungen und Verbesserungen basierend auf weiterem Nutzerfeedback und technologischen Entwicklungen durchzuführen, um die Nutzererfahrung kontinuierlich zu verbessern und das Engagement zu steigern.

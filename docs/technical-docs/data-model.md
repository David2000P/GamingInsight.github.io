---
title: Data Model
parent: Technical Docs
nav_order: 2
---


<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


# Data model



![image](https://github.com/user-attachments/assets/5a5b11ad-32da-4799-8f02-e8dd842f8aba)



Wie Sie aus der Abbildung entnehmen können haben wir 3 Tabellen Company,Review und User in der Datenbank mit Ihren jeweiligen Attributen. Die Beziehungen sehen folgendermaßen aus ein Unternehmen kann 0 oder mehrere Bewerungen haben aber eine Bewertung gehört immer zu einem Unternehmen. Ein User kann 0 oder mehrere Reviews abgeben aber eine Review ist immer von einem User geschrieben. Aufgrund dieser Beziehungen bekommt Review die schlüssel Attribute von Company und User.

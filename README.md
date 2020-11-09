# Python - NeedWine

[TOC]

## Objectif

Projet de démonstration Python

Stack :

- Python 3.8
- Flask-RESTPlus
- SqlAchemy/SQLite



## Tutorial

L'objectif est de créer une API REST permettant à des utilisateurs de donner leur avis sur différents vins.

Il y a 2 types d'utilisateurs : 

- Les modérateurs
- Les utilisateurs classiques



### Backlog

| US index | US Description                                               |
| -------- | ------------------------------------------------------------ |
| 1        | En tant qu'utilisateur, je souhaite pouvoir me connecter et me déconnecter à l'application. |
| 2        | En tant qu'utilisateur, je souhaite avoir accès à la liste des vins. |
| 3        | En tant qu'utilisateur, je souhaite avoir accès aux détails d'un vin. |
| 4        | En tant qu'utilisateur, je souhaite pouvoir ajouter un nouveau vin. |
| 5        | En tant qu'utilisateur, je souhaite avoir accès à la liste des avis. |
| 6        | En tant qu'utilisateur, je souhaite pouvoir ajouter un avis. |
| 7        | En tant que modérateur, je souhaite pouvoir ajouter un utilisateur |
| 8        | En tant que modérateur, je souhaite pouvoir supprimer un utilisateur |
| 9        | En tant que modérateur, je souhaite pouvoir supprimer un vin |
| 10       | En tant que modérateur, je souhaite pouvoir supprimer un avis |

#### US 1 -   En tant qu'utilisateur, je souhaite pouvoir me connecter et me déconnecter à l'application.

Ajouter les Endpoints de connexion et de déconnexion à l'application. L'authentification doit être gérée avec un token JWT.

#### US 2 - En tant qu'utilisateur, je souhaite avoir accès à la liste des vins.

Ajout d'un Endpoint permettant à un utilisateur **connecté** d'avoir accès à la liste des vins. Il faut prévoir une pagination côté serveur.

#### US 3 -   En tant qu'utilisateur, je souhaite avoir accès aux détails d'un vin.

Ajout d'un Endpoint permettant à un utilisateur **connecté** d'avoir accès aux détails d'un vin.

Pour un vin donné, il faut remonter les informations suivantes : 

- Le nom du vin
- Le type de vin (blanc, rosé ou rouge)
- Le millésime du vin

#### US 4 - En tant qu'utilisateur, je souhaite pouvoir ajouter un nouveau vin.

Ajout d'un Endpoint permettant à un utilisateur **connecté** d'ajouter un nouveau vin.

Pour ajouter un vin l'utilisateur doit renseigner : 

- Le nom du vin
- Le type de vin (blanc, rosé, rouge)
- Le millésime du vin (idéalement il faut contrôler le format AAAAMMYY)

Une contrainte d'unicité sur le nom et le millésime du vin doit exister. Pour un millésime donné, un utilisateur ne peut pas créer un vin avec un nom déjà existant.

#### US 5 -   En tant qu'utilisateur, je souhaite avoir accès à la liste des avis.

Ajout d'un Endpoint permettant à un utilisateur **connecté** d'avoir accès à la liste des avis. Il faut prévoir une pagination côté serveur, ainsi qu'un filtre par vin et par utilisateur pour les besoins de l'ihm.

Pour un avis, il faut remonter les informations suivantes:

- Nom de l'utilisateur ayant créé l'avis
- La description de l'avis
- La date de création de l'avis
- Le nom du vin et le millésime correspondant

#### US 6 - En tant qu'utilisateur, je souhaite pouvoir ajouter un avis.

Ajout d'un Endpoint permettant à un utilisateur **connecté** d'ajouter un avis pour un vin donné.

Pour ajouter un avis, l'utilisateur doit renseigner :

- La description
- Le vin correspondant (ID du vin en BDD, un champ de recherche sera disponible dans l'IHM)

#### US 7 - En tant que modérateur, je souhaite pouvoir supprimer un vin

Ajout d'un Endpoint permettant à un modérateur **connecté** de supprimer un vin

#### US 8 -   En tant que modérateur, je souhaite pouvoir supprimer un avis

Ajout d'un Endpoint permettant à un modérateur **connecté** de supprimer un avis



### Déroulement du projet

3 phases sont identifiées : 

- Phase 1 :  Rédaction du contrat d'interface de L'API (Open API) et du modèle de données (UML)
- Phase 2 : Implémentation de la solution
- Phase 3 : Industrialisation de la solution

Pour valider chacune de ses phases, il faudra prévoir une démo afin d'obtenir la validation du responsable d'application.
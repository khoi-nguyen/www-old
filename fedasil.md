---
title: ORM + React Hook + Form/List view
output: revealjs
institute: Fedasil
split: true
...

# Motivations

- Gros problèmes de qualité de code et maintenabilité

- Tout est afficher/éditer/supprimer un record dans la base de données

- Manque de coordination

- Separation des préoccupations (design >< base de données)

- Éviter la répétition

- Exploiter la puissance du stack choisi

<hr />

::: question
- Est-ce que je pourrais avoir de l'aide?
:::

# Modèle / Vue

::::: {.col}

### Modèle

~~~ javascript
class Resident extends Model {

    _table = "Residents.RESIDENTS"

    @field({ label: "First name", required: True })
    firstName: string;

    @field({ label: "Last name", required: True })
    lastName: string;

    @email
    @field({ label: "Email adress", required: True })
    email: string;

}
~~~

:::::

::::: {.col}

### Vue

~~~ typescript
const Form = ({ Button, Field }) => (
    <>
        <Field name="firstName" />
        <Field name="lastName" />
        <Field name="email" />
        // Probablement pas nécéssaire
        <Button action="save" />
    </>
);
~~~

~~~ {.typescript .fragment}
const List = ({ Button, Field }) => (
    <>
        // Va peut-être changer...
        <Field name="firstName" />
        <Field name="lastName" />
        <Field name="email" />
    </>
)
~~~

:::::

# Fonctionnement

- D'une URL comme `resident/1`:
    - **Modèle**: `Resident` de `models/Resident.tsx`

    - **Action**: view

    - **Vue**: `Form` de `templates/Resident.tsx`


- D'une URL comme `resident/1`:
    - **Modèle**: `Resident` de `models/Resident.tsx`

    - **Action**: view

    - **Vue**: `Form` de `templates/Resident.tsx`

- D'une URL comme `resident/`:

    - **Modèle**: `Resident` de `models/Resident.tsx`

    - **Action**: lister les records

    - **Vue**: `List` de `templates/Resident.tsx`

# Avancement

- [X] \ Générer les requêtes simples
- [ ] \ Requêtes "JOIN" (facile avec Hasura)
- [X] \ CRUD
- [X] \ Intégration avec React
- [X] \ Routing automatique
- [ ] \ Validation automatique des formulaires
- [ ] \ Gestion d'erreur
- [ ] \ Design
- [ ] \ Tests, tests, tests

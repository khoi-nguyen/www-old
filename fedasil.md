---
title: ORM + React Hook
output: revealjs
institute: Fedasil
...

# ORM

::::: {.col}
~~~ typescript
class Resident extends Model {

    _table: string = "Residents";

    @primary
    id: number;

    @field({ label: "First Name", required: true })
    firstName: string;

    @field({ label: "FA Number" })
    faNumber: string;

    @date({ label: "Date of birth" })
    dob: string;

    @computed
    @field({ label: "Badge number" })
    get badgeNumber() {
        return this.faNumber.substring(2);
    }

    @computed
    @title
    get title() {
        return `${this.lastName}, ${this.firstName}`
    }
}
~~~
:::::

::::: {.col}

::: {.question name="Motivation"}
Everything should in theory be generated from the model,
and we should avoid code repetition.
:::

::: {.info name="Features"}
- Automatic generation of CRUD GraphQL queries
- Automatic validation (`@date`, `required`, etc.)
- Computed fields (e.g. `badgeNumber`)
- Error handling and notifications
:::

:::::

# CRUD

::::: {.col}
~~~ typescript
resident = new Resident();

// Read
resident.load({ faNumber: "FA11111" });

// Create + Update
resident.firstName = "Khoi";
resident.update({ dob: "24/01/1991", lastName: "Nguyen" });
resident.save();

// Delete
resident.delete();
~~~
:::::

::::: {.col}
- All models **inherit** CRUD operations.
- No need to write queries

::: question
How are we going to connect our models to react components?
:::
:::::

# React Hook

::::: {.col}
~~~ typescript
const Component = () => {
    // Gives you access to load, delete, save, etc.
    const model = useModel(Resident, "read", {id: 1});

    // Change current record
    model.load({id: 2});

    // Access the state of the current record
    model.payload

    // Delete current record
    model.delete();
};
~~~
:::::

::::: {.col}
- `useModel` accesses all the data on the model
- `model.payload`: reactive state with the values of the form
- `model.fields` contains all information on the field,
  including `onchange` methods to update the payload.
:::::

# Form and List Views

- Read views are just read-only versions of form views
- Automatic routing can be done to choose the view type

~~~ typescript
const FormView = () => {
    model = useModel(props.Model, props.action, props.query);
    if (props.children) {
        return (
            <>
                {props.children}
            </>
        )
    }
    return (
        <>
            {model.fields.map((field, i) =>
                <Field data={field} key={i}/>
            )}
        </>
    )
}
~~~


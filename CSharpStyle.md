# DIKU — Software Development — C# Coding Style

Coding style is a social construct: When joining a new software development
project, it is forced upon you. In return, when new peers join your project,
you can force it upon them. You must gather clout before you get to change
things. Keeping consistency in code layout makes it easier to collaborate with
other people, especially when the project stretches over thousands of lines of
code.

Let us now make a social contract: We aim to keep our code consistent in style
to make it easy for you to drop into new code handouts. In return, you stick to
our style in your extensions, to make it easy for us to drop in and give you
(more valuable) feedback.

We also try to give the reasons for our choices. If you disagree, you *can*
take it up with your TA, but your time is better spent _programming_.

## Indentation

4 spaces

Using spaces (rather than tabs) ensures to always retain the hierarchical
presentation of the code, as intended by the author, regardless of the reader's
system settings.

4 is not too many (e.g., 8), and not too little (e.g., 2). This is not a
reason, but a _compromise_.

## Braces

All braces are to be placed on a _line of their own_. For instance,
```csharp
class MyClass : BaseClass
{
    public int myVariable
    {
        // all rules have exceptions
        get { return myVariable; }
    }
    
    public void MyFunc (int a, int b)
    {
        for (int i = 0; i < 15; i++)
        {
            ...
        }
    }
}
```

This includes loops, `if`-statements, and declarative scopes.

Braces are _always_ required. Even around one-line blocks. This way, if you
ever want to add a line to what originally was a one-liner, you still retain the
control flow.

## Whitespace

* Use a line break between using and namespace declarations.
* Use blank lines between class members.
* Use a space between parameters.
* Use spaces around the `:` operator.

## Comments

A well-named member, with well-named parameters, in a well-named class, and a
well-named namespace, needs little comment: Comment only on the parts you can't
express with member signatures.

In general, you can use either multi-line (`/* */`) or single-line (`//`)
comments. We recommend single-line comments for everything.

For commenting out code, always use `//`. This is a great chance for you to get
acquainted with your text-editor.  Please also _consider removing commented out
code completely_, or add a comment as to why the code is commented out, if you
want someone else to sort it out.

Another useful option is to mark code with the `[System.Obsolete("This is
obsolete. Use that instead.")]` attribute. Make sure that the comment you give
as to what the user should use instead is sensible.

When writing comments for something (e.g. a member function), describe what it
does, but refrain from commenting on how it is doing it - that should be obvious
from just reading the code.

## Naming

In general, we follow the [Microsoft Naming
Guidelines](https://msdn.microsoft.com/en-us/library/ms229002.aspx). We agree
with their stated reasons.

In particular, you should take a look at the [Capitalization
Conventions](https://msdn.microsoft.com/en-us/library/ms229043.aspx). We also
use `PascalCase` for solution and project names.

Furthermore, akin to the [corefx C# Coding
Style](https://github.com/dotnet/corefx/blob/master/Documentation/coding-guidelines/coding-style.md),
we use `_camelCase` for internal and private instance fields, and `s_camelCase`
for internal and private _static_ fields. We mark fields as `readonly` where
possible. When used on static fields, `readonly` must come after `static`
(i.e., `static readonly`, not `readonly static`).

## Files

There should be one class per file. This is to keep source files small. An
exception is made for partial classes, where a part of the class is written by
an automated tool (e.g., a GUI designer).

## MonoDevelop / Xamarin Studio

Our IDE has the option to help you follow this style guide. To get started, you
will need to download [our policy](DIKU.mdpolicy), and add it to MonoDevelop /
Xamarin Studio:

* Select Edit, Custom Policies...
* Select Add Policy, From File...
* Select the file you just downloaded and press Open.

You can now selectively apply this policy on a per-solution basis, however, it
is best to apply the policy system-wide:

* Select Edit, Preferences...
* Go to Source Code, Code Formatting, C# source code.
* Under the Policy drop-down select DIKU.
* Go to Source Code, Name Conventions.
* Under the Policy drop-down select DIKU.
* Press OK to apply.

To do this for a given solution:

* Right-click on the solution
* Select Options.
* Go to Source Code, Code Formatting, C# source code.
* Under the Policy drop-down select DIKU.
* Go to Source Code, Name Conventions.
* Under the Policy drop-down select DIKU.
* Press OK to apply.

NB! This doesn't reformat everything. You'll have to do that manually, on a
per-file basis:

To format a given file according to the policy:

* Select Edit, Format, Format Document.

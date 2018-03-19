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

## Origins

This style guide makes a sacrifice between the style of the code found
in [C# precisely, 2nd ed., by Peter Sestoft and Henrik I.
Hansen](http://www.itu.dk/~sestoft/csharpprecisely/), and what you
might see in a large-scale C# development project. Here's why: The
style of the code in the textbook intends to conserve space, whereas,
in practice, software developers reach for a compromise between
utility and maintainability.

## Indentation

**4 spaces.**

Using spaces (rather than tabs) ensures to always retain the hierarchical
presentation of the code, as intended by the author, regardless of the reader's
system settings (e.g., tab width).

4 is not too many (e.g., 8), and not too little (e.g., 2). This is not a
reason, but a _compromise_.

## Line width

**100 characters.**

Code is like prose, and as with prose, shorter lines [make for a
faster
read](https://web.archive.org/web/20171025201838/http://www.humanfactors.com/newsletters/optimal_line_length.asp).
In short, you avoid forcing your readers to shift eye-focus along
multiple dimensions, and avoid the risk that they will have to scroll
left/right, in addition to up/down, to get an overview of your code.

## Braces

Opening braces are to be placed on the same line as the declaration
opening (K&R style). Closing braces are to be placed on a _line of
their own_, except when both the opening and closing brace fit on a
line, or when both the _closing and opening_ brace fit on a line, and
are part of the same statement.

Braces are _always_ required. Even around one-line blocks. This way, if you
ever want to add a line to what originally was a one-liner, you still retain the
control flow.

For instance,
```csharp
class MyClass : BaseClass {
    public int myVariable {
        // all rules have exceptions
        get { return myVariable; }
    }
    
    public void MyFunc (int a, int b) {
        for (int i = 0; i < 15; i++) {
            if (i < 5) {
              // ...
            } else if (i < 10) {
              // ...
            } else {
              // ...
            }
        }
    }
}
```

## Line breaks

In general, you should use line breaks to group code vertically. In
particular, you should, at least:

* Use a line break between using and namespace declarations.
* Use blank lines between class members.

## Spacing out

Use spaces to space out the syntactical elements along a line. In
particular, you should:

* Use a space before any opening parentheses that is part of a
  statement (e.g., argument list, `for`- or `if`- statement
  condition).
* Use a space before an opening brace.
* Use a space after each parameter in a parameter list.
* Have a space on each side of an infix operator.

For instance,
```csharp
(-b+Math.Sqrt(d))/(2*a)
```
is regarded as less readable than
```csharp
(-b + Math.Sqrt(d)) / (2 * a)
```

## Comments

Well-placed, well-named, and well-typed things need no comments:
Comment on your code only if there is no way to refactor it to make
its operation clearer. Here's why: Code doesn't lie, but comments
might.

If you have to comment, you can use either multi-line (`/* */`) or
single-line (`//`) comments. We recommend single-line comments for
everything.

For commenting out code, always use `//`. This is a great chance for you to get
acquainted with your text-editor.  Please also _consider removing commented out
code completely_, or add a comment as to why the code is commented out, if you
want someone else to sort it out.

Another useful option is to mark code with the following attribute:

```csharp
[System.Obsolete("This is obsolete. Use that instead.")]
```

Make sure that the comment you give as to what the user should use
instead is sensible.

When writing comments for something (e.g., a member method), describe
what it does, but refrain from commenting on how it is doing it — that
should be obvious from just reading the code.

## Naming

In general, we follow the naming conventions mentioned in C#
Precisely, Section 3, on page 4. In addition, constants and static
read-only fields are written in `ALL_CAPS`.

## Accessibility and Modifiability

It is the public and protected members of a class the determine its
responsibility. Hence, you should mark your members as `private`,
unless it is intensional that they are exposed as part of your
inheritance or public interface.

Also, mark fields as `const` or `readonly` when possible. When used on
static fields, let `readonly` come after `static` (i.e., `static
readonly`, not `readonly static`).

## Files

There should be one class per file. This is to keep source files small. An
exception is made for partial classes, where a part of the class is written by
an automated tool (e.g., a GUI designer).

## JetBrains Rider Settings

Our IDE has the option to help you follow this style guide.

To get started, you will need to download [Rider
Settings](https://github.com/diku-dk/su18-guides/raw/v1.1/files/RiderSettings.jar),
and import them in your JetBrains Rider instance:

* Select File, Import Settings...
* Select the downloaded settings file, and press OK.
* Select all the components of the settings file, and press OK.
* Press OK to restart Rider.

NB! This doesn't reformat everything. You'll have to do that manually, on a
per-file basis:

To format a given file according to the policy:

* Press Ctrl + E, followed by C.
* Select either the given file or your entire solution.
* Select Full Cleanup, and press OK.

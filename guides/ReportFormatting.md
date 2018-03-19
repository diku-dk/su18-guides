# Report Formatting

This guide will provide some advide on how to format and structure your technical reports.

The [su18](https://github.com/diku-dk/su18-guides/raw/v1.4/files/su18.sty)
LaTeX package provides a template for your LaTeX reports in Software Development.

To use it, you will have to install [Python 3](https://www.python.org/download/releases/3.0/),
the Python package manager [pip](https://pip.pypa.io/en/stable/installing/),
as well as the [Pygments](http://pygments.org/) package for Python:

```
$ pip install Pygments
```

Then, you can start with a `master.tex` as follows:

```
\documentclass[a4paper]{article}

\usepackage{su18}

\header{%
  assignment={Exercise 1: Introduction to C#},%
  authors={Donald E. Knuth <\texttt{knuth@stanford.edu}>},%
  shortAuthors={\texttt{knuth}},%
  date={Friday, February 10, 15:00}
}

\begin{document}

\maketitle

\end{document}
```

If you are writing in Danish, you should instead write:

```
\usepackage[danish]{su18}
```

When including code snippets we recommend using the `minted` package. It is a
very nice environment for viewing code, as it allows for a lot of customization.

For your convenience we provide a configuration for `minted` in
`su18.sty` This configuration is not mandatory, but we expect that all included
code snippets are included through LaTeX code-packages and not as images.
Furthermore we expect both syntax highlighting and line numbers. If you chose to
use our configuration, including code is as easy as the following example:

```
\documentclass[a4paper]{article}

\usepackage{su18}

\begin{document}

\maketitle

\inputminted{csharp}{src/code.cs}

\end{document}
```

This example includes an external code file `src/code.cs`. The benefit is that
you get syntax highlighting, and this could be your solution to the programming
exercise in question. Here is some sample code to put into `src/code.cs`:

```
class MyClass : BaseClass {
    // Properties are always capitalized
    public int MyProperty { get; private set; }

    public void MyFunc(int a, int b) {
        for (int i = 0; i < 15; i++) {
            ...
        }
    }
}

```

## Compilation

The technical report can be compiled in a number of different ways:

#### Using `pdflatex`

```
$ pdflatex -shell-escape master.tex
```

That is, provided you've placed `su18.sty` either in the same
directory, or in your `~/texmf/tex/latex/` directory.

#### Using `latexrun`

Latexrun is a tool that is designed to make it really nice to compile latex
documents. Instead of +50 lines of random messages you only get errors or
warnings printed in your terminal.
```
$ ./latexrun --latex-args='-shell-escape' master.tex
```

P.S. `latexrun` can be downloaded here:
[latexrun](https://github.com/diku-dk/su18-guides/raw/v1.3/files/latexrun) or at
the original [repository](https://github.com/aclements/latexrun).

Remember to make sure that `latexrun` is an executable (`sudo chmod +x latexrun`)!

#### Using Makefile

We have created a package containing a Makefile an a default folder structure to make it
really nice and easy to compile your technical report, cleaning up latex compile files
(.aux, .log, etc.).

P.S This setup can be downloaded as a .zipped folder here:
[su18TechReportSample](https://github.com/diku-dk/su18-guides/raw/v1.3/files/testSU18sty.zip)

### Final notes

We expect to update [su18.sty](su18.sty) during
the course.  We will announce changes on Absalon and our GitLab. You can always
check the version of su18.sty you are using by looking at its line 24. We will
insure backwards compatibility, so using a new version will not brake your
existing LaTeX-files.

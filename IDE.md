# DIKU — Software Development — Integrated Development Environmnet

You will need [Mono](http://www.mono-project.com/),
[MonoDevelop](http://www.monodevelop.com/), and
[Gtk#](http://www.mono-project.com/docs/gui/gtksharp/).


# Common pitfalls with MonoDevelop

## Problems on linux when running a console application
There where some issues that some of you using MonoDevelop on linux could not run the console project. But there is a quick fix to that.
1. Right click on the project
2. Click on options
3. Under Run->Configurations->Default, find the checkbox "Run on external console"
4. Uncheck the checkbox "Run on external console"

Now you should be able to run the console project directly from MonoDevelop

## See Also

* [Mono Documentation](http://docs.go-mono.com/)

On Windows you furthermore need to install [Microsoft Build Tools 2013](https://www.microsoft.com/en-us/download/details.aspx?id=40760).

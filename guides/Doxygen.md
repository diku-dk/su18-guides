# Running Doxygen Locally

To build the `DIKUArcade` documentation, you will need
[Doxygen](http://www.stack.nl/~dimitri/doxygen/) and
[graphviz](http://www.graphviz.org/) installed.

## Installation

### Linux

Use your favourite package manager to install the most recent versions of
`doxygen` and `graphviz`.

### macOS

Similar to Linux. We recommend using [Homebrew](https://brew.sh/):

```
$ brew update
$ brew install doxygen graphviz
```

### Windows

Download the following binaries from the web:

* [doxygen-1.8.13-setup.exe](http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.13-setup.exe)
* [graphviz-2.38.msi](http://www.graphviz.org/pub/graphviz/stable/windows/graphviz-2.38.msi)

OBS! It is important to check the checksum of the files you download over an
insecure protocol (e.g., `http`), or from an otherwise untrusted service (e.g.,
`ftp.stack.nl`). This gives you more confidence that the files you got are the
files you were after.

On Windows, you can use the `certUtil` command-line utility. For instance,

```
> certUtil -hashfile doxygen-1.8.13-setup.exe SHA256
```

(On Linux and macOS you can use the `sha256sum` command-line utility, but this
is not relevant in the context of package managers, that _can_ do this sort of
thing for you.)

We can assert that the SHA256 checksums are:

```
graphviz-2.38.msi
  c794ea03bc2631fff468f4d97fa6726c536fc98ee579529779aa6f45e94e4f6d
doxygen-1.8.13-setup.exe
  bd9e233fd648662eff6ad9cdd1a944a0b40b032e82fee02b1eab5ef4afc763cf
```

Having verified the files, run the installers.

Modify your `PATH` environment variable to include the path to where
`graphviz.exe` is installed. **The installer does not do this for you.**

## Running Doxygen

Just go to the directory containing `DIKUArcade` and run `doxygen` from the
command-line. This will create the directory `Docs`, with a subdirectory
`html`, containing an `index.html`. Open the `index.html` in your browser to
see the documentation.

## Doxygen Documentation

We recommend jumping directly to the [special
commands](https://www.stack.nl/~dimitri/doxygen/manual/commands.html) section,
but your might also find [this
section](http://www.stack.nl/~dimitri/doxygen/manual/docblocks.html) useful.

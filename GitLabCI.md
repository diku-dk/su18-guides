# GitLab Continuous Integration

GitLab Continuous Integration (CI) can help you keep your git repositories
well-formed. The following details how you can make your projects work with our
GitLab CI.

## Reports

For your reports, we require that you write in LaTeX, and that your entry-point
document is called `master.tex`. Our GitLab CI can help you meet these
requirements, and produce a PDF "artifact" along the way:

Create a file `.gitlab-ci.yml` in the root of your repository. Assuming your
`master.tex` and `latexrun` are located in the same directory, you can just
paste the following CI configuration:

```
report:
  stage: build
  script:
  - ./latexrun --latex-args "\-shell-escape" -o report.pdf master.tex
  - ./latexrun --latex-args "\-shell-escape" -o report.pdf master.tex
  - ./latexrun --latex-args "\-shell-escape" -o report.pdf master.tex
  artifacts:
    paths:
    - report.pdf
  tags:
  - latex
  only:
  - master
```
We run `pdflatex` three times to obtian the refrences in the document, i.e building
table of contents etc. 
 

If you are not using `latexrun`, you can instead use the following command
under `script` above:

```
  - pdflatex -jobname report master.tex
```

**That's it!** Commit and push.

This will start a "pipeline" on GitLab, a part of which will be a "job" to
build your report. If all goes well, you get a nice green "passed" icon on the
home page of your repository.

If you then, from your project page, click "Pipelines", and then "Jobs", you
can get an overview of all your past and present jobs (aka. builds). For
instance, [here](https://git.dikunix.dk/su17/LaTeXTemplate/builds) is the list
of jobs for our [LaTeXTemplate](https://git.dikunix.dk/su17/LaTeXTemplate). If
you then click in on a job that passed, you can _browse_ the artifacts that the
job created. For instance,
[here](https://git.dikunix.dk/su17/LaTeXTemplate/builds/153/artifacts/browse)
is the list of artifacts created by a successful
[LaTeXTemplate](https://git.dikunix.dk/su17/LaTeXTemplate) job at commit ID
[3292044b22c9ff375e7449974dc65b0d43eb6a2e](https://git.dikunix.dk/su17/LaTeXTemplate/commit/3292044b22c9ff375e7449974dc65b0d43eb6a2e).

## Doxygen

Similarly, you can use our GitLab CI to build your Doxygen documentation.
Proceed as above, and let your `.gitlab-ci.yml` contain the following:

```
doxygen:
  stage: deploy
  script:
  - doxygen
  artifacts:
    paths:
    - Docs
  tags:
  - doxygen
  only:
  - master
```

It is not recommended to _browse_ the Doxygen artifact. Instead, just download
the artifact ZIP archive, unzip, and open `Docs/html/index.html` in your
favourite browser. For privacy reasons, we do not yet host this HTML directly
on our GitLab CI.

## NUnit

Coming soon..

## Tips

Our CI will pick up your code every time you push. This might be too often for
your needs. End your commit header with `[ci skip]` to tell CI to skip the
commit.

For more on the GitLab CI configuration file format, see the [official
documentation](https://docs.gitlab.com/ce/ci/yaml/).

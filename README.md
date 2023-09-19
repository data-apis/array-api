# Array API standard
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-64-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This repository contains documents, tooling and other content related to the
API standard for arrays (or tensors).

These are relevant documents related to the content in this repository:

- [Rendered html docs for latest version](https://data-apis.github.io/array-api/latest)
- [Consortium announcement blog post](https://data-apis.org/blog/announcing_the_consortium/)
- [Blog post on first release of draft array API standard](https://data-apis.org/blog/array_api_standard_release/)

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to go about contributing to
this array API standard.


## Building docs locally

### Quickstart

To install the local stubs and additional dependencies of the Sphinx docs, you
can use `pip install -r doc-requirements.txt`. Then just running `make` at the
root of the repository should build the whole spec website.

```sh
$ pip install -r doc-requirements.txt
$ make
$ ls _site/
2021.12/  draft/  index.html  latest/  versions.json
```

### The nitty-gritty

The spec website is comprised of multiple Sphinx docs (one for each spec version),
all of which exist in `spec/` and rely on the modules found in `src/` (most
notably `array_api_stubs`). For purposes of building the docs, these `src/`
modules do not need to be installed as they are added to the `sys.path` at
runtime.

To build specific versions of the spec, run `sphinx-build` on the respective
folder in `spec/`, e.g.

```sh
$ sphinx-build spec/2012.12/ _site/2012.12/
```

Additionally, `make draft` aliases

```sh
$ sphinx-build spec/draft/ _site/draft/
```

To build the whole website, which includes every version of the spec, you can
utilize `make spec`.


## Making a spec release

The Sphinx doc at `spec/draft/` should be where the in-development spec resides,
with `src/array_api_stubs/_draft/` containing its respective stubs. A spec
release should involve:

* Renaming `src/array_api_stubs/_draft/` to `src/array_api_stubs/_YYYY_MM`
* Renaming `spec/draft/` to `spec/YYYY.MM`
* Updating `spec/YYYY.MM/conf.py`

  ```diff
  ...
  - from array_api_stubs import _draft as stubs_mod
  + from array_api_stubs import _YYYY_MM as stubs_mod
  ...
  - release = "DRAFT"
  + release = "YYYY.MM"
  ...
  ```

* Updating `spec/_ghpages/versions.json`

  ```diff
  {
  +     "YYYY.MM": "YYYY.MM",
  ...
  ```

* Updating `Makefile`

  ```diff
  ...
  	-sphinx-build "$(SOURCEDIR)/PREVIOUS.VER" "$(BUILDDIR)/PREVIOUS.VER" $(SPHINXOPTS)
  + 	-sphinx-build "$(SOURCEDIR)/YYYY.MM" "$(BUILDDIR)/YYYY.MM" $(SPHINXOPTS)
  - 	-cp -r "$(BUILDDIR)/PREVIOUS.VER" "$(BUILDDIR)/latest"
  + 	-cp -r "$(BUILDDIR)/YYYY.MM" "$(BUILDDIR)/latest"
  ...
  ```

These changes should be committed and tagged. The next draft should then be
created. To preserve git history for both the new release and the next draft:

1. Create and checkout to a new temporary branch.

  ```sh
  $ git checkout -b tmp
  ```

2. Make an empty commit. <sup>This is required so merging the temporary branch
   (4.) is not automatic.</sup>

  ```sh
  $ git commit --allow-empty -m "Empty commit for draft at YYYY.MM "
  ```

3. Checkout back to the branch you are making a spec release in.

  ```sh
  $ git checkout YYYY.MM-release
  ```

4. Merge the temporary branch, specifying no commit and no fast-forwarding.

  ```sh
  $ git merge --no-commit --no-ff tmp
  Automatic merge went well; stopped before committing as requested
  ```

5. Checkout the `spec/draft/` files from the temporary branch.

  ```sh
  $ git checkout tmp -- spec/draft/
  ```

6. Commit your changes.

  ```sh
  $ git commit -m "Copy YYYY.MM as draft with preserved git history"
  ```

You can run `git blame` on both `spec/YYYY.MM` and `spec/draft` files to verify
we've preserved history. See this [StackOverflow question](https://stackoverflow.com/q/74365771/5193926)
for more background on the approach we use.

<!-- TODO: write a script to automate/standardise spec releases -->


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://saulshanabrook.github.io/"><img src="https://avatars.githubusercontent.com/u/1186124?v=4?s=100" width="100px;" alt="Saul Shanabrook"/><br /><sub><b>Saul Shanabrook</b></sub></a><br /><a href="#tool-saulshanabrook" title="Tools">🔧</a> <a href="#ideas-saulshanabrook" title="Ideas, Planning, & Feedback">🤔</a> <a href="#research-saulshanabrook" title="Research">🔬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/stdlib-js/stdlib"><img src="https://avatars.githubusercontent.com/u/2643044?v=4?s=100" width="100px;" alt="Athan"/><br /><sub><b>Athan</b></sub></a><br /><a href="#content-kgryte" title="Content">🖋</a> <a href="#data-kgryte" title="Data">🔣</a> <a href="#tool-kgryte" title="Tools">🔧</a> <a href="#research-kgryte" title="Research">🔬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/steff456"><img src="https://avatars.githubusercontent.com/u/20992645?v=4?s=100" width="100px;" alt="Stephannie Jimenez Gacha"/><br /><sub><b>Stephannie Jimenez Gacha</b></sub></a><br /><a href="#data-steff456" title="Data">🔣</a> <a href="#content-steff456" title="Content">🖋</a> <a href="#research-steff456" title="Research">🔬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/asmeurer"><img src="https://avatars.githubusercontent.com/u/71486?v=4?s=100" width="100px;" alt="Aaron Meurer"/><br /><sub><b>Aaron Meurer</b></sub></a><br /><a href="#content-asmeurer" title="Content">🖋</a> <a href="https://github.com/data-apis/array-api/commits?author=asmeurer" title="Tests">⚠️</a> <a href="#tool-asmeurer" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://deathbeds.github.io/"><img src="https://avatars.githubusercontent.com/u/4236275?v=4?s=100" width="100px;" alt="Tony Fast"/><br /><sub><b>Tony Fast</b></sub></a><br /><a href="#maintenance-tonyfast" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rgommers"><img src="https://avatars.githubusercontent.com/u/98330?v=4?s=100" width="100px;" alt="Ralf Gommers"/><br /><sub><b>Ralf Gommers</b></sub></a><br /><a href="#blog-rgommers" title="Blogposts">📝</a> <a href="#business-rgommers" title="Business development">💼</a> <a href="https://github.com/data-apis/array-api/commits?author=rgommers" title="Code">💻</a> <a href="#content-rgommers" title="Content">🖋</a> <a href="https://github.com/data-apis/array-api/commits?author=rgommers" title="Documentation">📖</a> <a href="#fundingFinding-rgommers" title="Funding Finding">🔍</a> <a href="#maintenance-rgommers" title="Maintenance">🚧</a> <a href="#ideas-rgommers" title="Ideas, Planning, & Feedback">🤔</a> <a href="#projectManagement-rgommers" title="Project Management">📆</a> <a href="#talk-rgommers" title="Talks">📢</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/teoliphant"><img src="https://avatars.githubusercontent.com/u/254880?v=4?s=100" width="100px;" alt="Travis E. Oliphant"/><br /><sub><b>Travis E. Oliphant</b></sub></a><br /><a href="#business-teoliphant" title="Business development">💼</a> <a href="#fundingFinding-teoliphant" title="Funding Finding">🔍</a> <a href="#ideas-teoliphant" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://leofang.github.io/"><img src="https://avatars.githubusercontent.com/u/5534781?v=4?s=100" width="100px;" alt="Leo Fang"/><br /><sub><b>Leo Fang</b></sub></a><br /><a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aleofang" title="Reviewed Pull Requests">👀</a> <a href="#ideas-leofang" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-leofang" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://tqchen.com/"><img src="https://avatars.githubusercontent.com/u/2577440?v=4?s=100" width="100px;" alt="Tianqi Chen"/><br /><sub><b>Tianqi Chen</b></sub></a><br /><a href="#ideas-tqchen" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Atqchen" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://stephanhoyer.com/"><img src="https://avatars.githubusercontent.com/u/1217238?v=4?s=100" width="100px;" alt="Stephan Hoyer"/><br /><sub><b>Stephan Hoyer</b></sub></a><br /><a href="#ideas-shoyer" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Ashoyer" title="Reviewed Pull Requests">👀</a> <a href="#question-shoyer" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.ic.unicamp.br/~tachard/"><img src="https://avatars.githubusercontent.com/u/5061?v=4?s=100" width="100px;" alt="Alexandre Passos"/><br /><sub><b>Alexandre Passos</b></sub></a><br /><a href="#ideas-alextp" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aalextp" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://paigevie.ws/"><img src="https://avatars.githubusercontent.com/u/3712347?v=4?s=100" width="100px;" alt="Paige Bailey"/><br /><sub><b>Paige Bailey</b></sub></a><br /><a href="#fundingFinding-dynamicwebpaige" title="Funding Finding">🔍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/apaszke"><img src="https://avatars.githubusercontent.com/u/4583066?v=4?s=100" width="100px;" alt="Adam Paszke"/><br /><sub><b>Adam Paszke</b></sub></a><br /><a href="#ideas-apaszke" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aapaszke" title="Reviewed Pull Requests">👀</a> <a href="#talk-apaszke" title="Talks">📢</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://amueller.github.io/"><img src="https://avatars.githubusercontent.com/u/449558?v=4?s=100" width="100px;" alt="Andreas Mueller"/><br /><sub><b>Andreas Mueller</b></sub></a><br /><a href="#ideas-amueller" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aamueller" title="Reviewed Pull Requests">👀</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/shengzha/"><img src="https://avatars.githubusercontent.com/u/2626883?v=4?s=100" width="100px;" alt="Sheng Zha"/><br /><sub><b>Sheng Zha</b></sub></a><br /><a href="#ideas-szha" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kkraus"><img src="https://avatars.githubusercontent.com/u/1324560?v=4?s=100" width="100px;" alt="kkraus"/><br /><sub><b>kkraus</b></sub></a><br /><a href="#ideas-kkraus" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Akkraus" title="Reviewed Pull Requests">👀</a> <a href="#talk-kkraus" title="Talks">📢</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://tomaugspurger.github.io/"><img src="https://avatars.githubusercontent.com/u/1312546?v=4?s=100" width="100px;" alt="Tom Augspurger"/><br /><sub><b>Tom Augspurger</b></sub></a><br /><a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3ATomAugspurger" title="Reviewed Pull Requests">👀</a> <a href="#question-TomAugspurger" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/edloper"><img src="https://avatars.githubusercontent.com/u/5790348?v=4?s=100" width="100px;" alt="edloper"/><br /><sub><b>edloper</b></sub></a><br /><a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aedloper" title="Reviewed Pull Requests">👀</a> <a href="#question-edloper" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/aregm"><img src="https://avatars.githubusercontent.com/u/1798344?v=4?s=100" width="100px;" alt="Areg Melik-Adamyan"/><br /><sub><b>Areg Melik-Adamyan</b></sub></a><br /><a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aaregm" title="Reviewed Pull Requests">👀</a> <a href="#fundingFinding-aregm" title="Funding Finding">🔍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://math.stackexchange.com/users/11069/sasha"><img src="https://avatars.githubusercontent.com/u/21087696?v=4?s=100" width="100px;" alt="Oleksandr Pavlyk"/><br /><sub><b>Oleksandr Pavlyk</b></sub></a><br /><a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aoleksandr-pavlyk" title="Reviewed Pull Requests">👀</a> <a href="#question-oleksandr-pavlyk" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tdimitri"><img src="https://avatars.githubusercontent.com/u/62962217?v=4?s=100" width="100px;" alt="tdimitri"/><br /><sub><b>tdimitri</b></sub></a><br /><a href="#ideas-tdimitri" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jack-pappas"><img src="https://avatars.githubusercontent.com/u/477287?v=4?s=100" width="100px;" alt="Jack Pappas"/><br /><sub><b>Jack Pappas</b></sub></a><br /><a href="#ideas-jack-pappas" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/agarwalashish"><img src="https://avatars.githubusercontent.com/u/3207727?v=4?s=100" width="100px;" alt="Ashish Agarwal"/><br /><sub><b>Ashish Agarwal</b></sub></a><br /><a href="https://github.com/data-apis/array-api/pulls?q=is%3Apr+reviewed-by%3Aagarwalashish" title="Reviewed Pull Requests">👀</a> <a href="#question-agarwalashish" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ezyang.com/"><img src="https://avatars.githubusercontent.com/u/13564?v=4?s=100" width="100px;" alt="Edward Z. Yang"/><br /><sub><b>Edward Z. Yang</b></sub></a><br /><a href="#ideas-ezyang" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mruberry"><img src="https://avatars.githubusercontent.com/u/38511765?v=4?s=100" width="100px;" alt="Mike Ruberry"/><br /><sub><b>Mike Ruberry</b></sub></a><br /><a href="#ideas-mruberry" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ericwieser.me/"><img src="https://avatars.githubusercontent.com/u/425260?v=4?s=100" width="100px;" alt="Eric Wieser"/><br /><sub><b>Eric Wieser</b></sub></a><br /><a href="#ideas-eric-wieser" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.willingconsulting.com/"><img src="https://avatars.githubusercontent.com/u/2680980?v=4?s=100" width="100px;" alt="Carol Willing"/><br /><sub><b>Carol Willing</b></sub></a><br /><a href="#ideas-willingc" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://arogozhnikov.github.io/"><img src="https://avatars.githubusercontent.com/u/6318811?v=4?s=100" width="100px;" alt="Alex Rogozhnikov"/><br /><sub><b>Alex Rogozhnikov</b></sub></a><br /><a href="#ideas-arogozhnikov" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://explosion.ai/"><img src="https://avatars.githubusercontent.com/u/8059750?v=4?s=100" width="100px;" alt="Matthew Honnibal"/><br /><sub><b>Matthew Honnibal</b></sub></a><br /><a href="#ideas-honnibal" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lezcano"><img src="https://avatars.githubusercontent.com/u/3291265?v=4?s=100" width="100px;" alt="Mario Lezcano Casado"/><br /><sub><b>Mario Lezcano Casado</b></sub></a><br /><a href="#ideas-lezcano" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/BvB93"><img src="https://avatars.githubusercontent.com/u/43369155?v=4?s=100" width="100px;" alt="Bas van Beek"/><br /><sub><b>Bas van Beek</b></sub></a><br /><a href="#ideas-BvB93" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/seberg"><img src="https://avatars.githubusercontent.com/u/61977?v=4?s=100" width="100px;" alt="Sebastian Berg"/><br /><sub><b>Sebastian Berg</b></sub></a><br /><a href="#ideas-seberg" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/IsaacBreen"><img src="https://avatars.githubusercontent.com/u/57783927?v=4?s=100" width="100px;" alt="Isaac Breen"/><br /><sub><b>Isaac Breen</b></sub></a><br /><a href="#ideas-IsaacBreen" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kmaehashi"><img src="https://avatars.githubusercontent.com/u/939877?v=4?s=100" width="100px;" alt="Kenichi Maehashi"/><br /><sub><b>Kenichi Maehashi</b></sub></a><br /><a href="#ideas-kmaehashi" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cnpryer"><img src="https://avatars.githubusercontent.com/u/14341145?v=4?s=100" width="100px;" alt="Chris Pryer"/><br /><sub><b>Chris Pryer</b></sub></a><br /><a href="#ideas-cnpryer" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tirthasheshpatel"><img src="https://avatars.githubusercontent.com/u/43181252?v=4?s=100" width="100px;" alt="Tirth Patel"/><br /><sub><b>Tirth Patel</b></sub></a><br /><a href="#ideas-tirthasheshpatel" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kshitij12345"><img src="https://avatars.githubusercontent.com/u/19503980?v=4?s=100" width="100px;" alt="Kshiteej K"/><br /><sub><b>Kshiteej K</b></sub></a><br /><a href="#ideas-kshitij12345" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://anirudhdagar.ml/"><img src="https://avatars.githubusercontent.com/u/23621655?v=4?s=100" width="100px;" alt="Anirudh Dagar"/><br /><sub><b>Anirudh Dagar</b></sub></a><br /><a href="#ideas-AnirudhDagar" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://tom-e-white.com/"><img src="https://avatars.githubusercontent.com/u/85085?v=4?s=100" width="100px;" alt="Tom White"/><br /><sub><b>Tom White</b></sub></a><br /><a href="#ideas-tomwhite" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/honno"><img src="https://avatars.githubusercontent.com/u/8246949?v=4?s=100" width="100px;" alt="Matthew Barber"/><br /><sub><b>Matthew Barber</b></sub></a><br /><a href="#ideas-honno" title="Ideas, Planning, & Feedback">🤔</a> <a href="#content-honno" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/pmeier"><img src="https://avatars.githubusercontent.com/u/6849766?v=4?s=100" width="100px;" alt="Philip Meier"/><br /><sub><b>Philip Meier</b></sub></a><br /><a href="#research-pmeier" title="Research">🔬</a> <a href="https://github.com/data-apis/array-api/commits?author=pmeier" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Zac-HD"><img src="https://avatars.githubusercontent.com/u/12229877?v=4?s=100" width="100px;" alt="Zac Hatfield-Dodds"/><br /><sub><b>Zac Hatfield-Dodds</b></sub></a><br /><a href="#ideas-Zac-HD" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/data-apis/array-api/commits?author=Zac-HD" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/djl11"><img src="https://avatars.githubusercontent.com/u/22750088?v=4?s=100" width="100px;" alt="Daniel Lenton"/><br /><sub><b>Daniel Lenton</b></sub></a><br /><a href="https://github.com/data-apis/array-api/commits?author=djl11" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/simonetgordon"><img src="https://avatars.githubusercontent.com/u/74716948?v=4?s=100" width="100px;" alt="Simone G"/><br /><sub><b>Simone G</b></sub></a><br /><a href="https://github.com/data-apis/array-api/commits?author=simonetgordon" title="Code">💻</a> <a href="#ideas-simonetgordon" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tylerjereddy"><img src="https://avatars.githubusercontent.com/u/7903078?v=4?s=100" width="100px;" alt="Tyler Reddy"/><br /><sub><b>Tyler Reddy</b></sub></a><br /><a href="#ideas-tylerjereddy" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mattbarrett98"><img src="https://avatars.githubusercontent.com/u/83289589?v=4?s=100" width="100px;" alt="Matt Barrett"/><br /><sub><b>Matt Barrett</b></sub></a><br /><a href="#ideas-mattbarrett98" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bicycleman15"><img src="https://avatars.githubusercontent.com/u/47978882?v=4?s=100" width="100px;" alt="Jatin Prakash"/><br /><sub><b>Jatin Prakash</b></sub></a><br /><a href="#ideas-bicycleman15" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Ishticode"><img src="https://avatars.githubusercontent.com/u/53497039?v=4?s=100" width="100px;" alt="Ishtiaq Hussain"/><br /><sub><b>Ishtiaq Hussain</b></sub></a><br /><a href="#ideas-Ishticode" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sherry30"><img src="https://avatars.githubusercontent.com/u/65318415?v=4?s=100" width="100px;" alt="sherry30"/><br /><sub><b>sherry30</b></sub></a><br /><a href="#ideas-sherry30" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/juaolobo"><img src="https://avatars.githubusercontent.com/u/49628984?v=4?s=100" width="100px;" alt="João Lobo"/><br /><sub><b>João Lobo</b></sub></a><br /><a href="#ideas-juaolobo" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/NeilGirdhar"><img src="https://avatars.githubusercontent.com/u/730137?v=4?s=100" width="100px;" alt="Neil Girdhar"/><br /><sub><b>Neil Girdhar</b></sub></a><br /><a href="#ideas-NeilGirdhar" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/nstarman"><img src="https://avatars.githubusercontent.com/u/8949649?v=4?s=100" width="100px;" alt="Nathaniel Starkman"/><br /><sub><b>Nathaniel Starkman</b></sub></a><br /><a href="#ideas-nstarman" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jakirkham"><img src="https://avatars.githubusercontent.com/u/3019665?v=4?s=100" width="100px;" alt="jakirkham"/><br /><sub><b>jakirkham</b></sub></a><br /><a href="#ideas-jakirkham" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RickSanchezStoic"><img src="https://avatars.githubusercontent.com/u/57310695?v=4?s=100" width="100px;" alt="RickSanchezStoic"/><br /><sub><b>RickSanchezStoic</b></sub></a><br /><a href="#ideas-RickSanchezStoic" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tlambert03"><img src="https://avatars.githubusercontent.com/u/1609449?v=4?s=100" width="100px;" alt="Talley Lambert"/><br /><sub><b>Talley Lambert</b></sub></a><br /><a href="#ideas-tlambert03" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://ilovesymposia.com/"><img src="https://avatars.githubusercontent.com/u/492549?v=4?s=100" width="100px;" alt="Juan Nunez-Iglesias"/><br /><sub><b>Juan Nunez-Iglesias</b></sub></a><br /><a href="#ideas-jni" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/chkothe"><img src="https://avatars.githubusercontent.com/u/5318120?v=4?s=100" width="100px;" alt="Christian Kothe"/><br /><sub><b>Christian Kothe</b></sub></a><br /><a href="#ideas-chkothe" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vnmabus"><img src="https://avatars.githubusercontent.com/u/2364173?v=4?s=100" width="100px;" alt="Carlos Ramos Carreño"/><br /><sub><b>Carlos Ramos Carreño</b></sub></a><br /><a href="#ideas-vnmabus" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/gilfree"><img src="https://avatars.githubusercontent.com/u/88031955?v=4?s=100" width="100px;" alt="Gilad"/><br /><sub><b>Gilad</b></sub></a><br /><a href="#ideas-gilfree" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/thomasjpfan"><img src="https://avatars.githubusercontent.com/u/5402633?v=4?s=100" width="100px;" alt="Thomas J. Fan"/><br /><sub><b>Thomas J. Fan</b></sub></a><br /><a href="#ideas-thomasjpfan" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://e-pot.xyz/"><img src="https://avatars.githubusercontent.com/u/9047355?v=4?s=100" width="100px;" alt="Conchylicultor"/><br /><sub><b>Conchylicultor</b></sub></a><br /><a href="#ideas-Conchylicultor" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/fcharras"><img src="https://avatars.githubusercontent.com/u/29153872?v=4?s=100" width="100px;" alt="Franck Charras"/><br /><sub><b>Franck Charras</b></sub></a><br /><a href="#ideas-fcharras" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kkraus14"><img src="https://avatars.githubusercontent.com/u/3665167?v=4?s=100" width="100px;" alt="Keith Kraus"/><br /><sub><b>Keith Kraus</b></sub></a><br /><a href="#ideas-kkraus14" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lucascolley"><img src="https://avatars.githubusercontent.com/u/51488791?v=4?s=100" width="100px;" alt="Lucas Colley"/><br /><sub><b>Lucas Colley</b></sub></a><br /><a href="#maintenance-lucascolley" title="Maintenance">🚧</a> <a href="https://github.com/data-apis/array-api/issues?q=author%3Alucascolley" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

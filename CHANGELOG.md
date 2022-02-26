# Changelog

<!--next-version-placeholder-->

## v0.10.4 (2022-02-26)
### Fix
* Renaming run parameters to configuration to avoid conflict ([`407e185`](https://github.com/Sciance-Inc/statisfactory/commit/407e185f4cb333be96a42f259bf53a0507f3dcb6))

## v0.10.3 (2022-02-22)
### Fix
* Odbc connector is now initiaed before accessing atributes ([`b7d92ca`](https://github.com/Sciance-Inc/statisfactory/commit/b7d92ca08ab7b3c60350a953e6aac09d1589adf8))

## v0.10.2 (2022-02-22)
### Fix
* Updating odbc query ([`0683b3d`](https://github.com/Sciance-Inc/statisfactory/commit/0683b3d82ba178602359b119630ee53324d762ea))

## v0.10.1 (2022-02-22)
### Fix
* Fixing missing CLI path for import ([`3a2d8ed`](https://github.com/Sciance-Inc/statisfactory/commit/3a2d8ed68956c2aea979b03e45d04dbf318b2192))

## v0.10.0 (2022-02-22)
### Feature
* Adding cli ([`09ba7c2`](https://github.com/Sciance-Inc/statisfactory/commit/09ba7c246f35b1c0d0aa764ecff7701fb84958ed))
* Adding install systemwide ([`213d136`](https://github.com/Sciance-Inc/statisfactory/commit/213d136c6ada9cce4b6871995629634129f90c70))
* Adding run method to the cli ([`dc68b35`](https://github.com/Sciance-Inc/statisfactory/commit/dc68b352a0b1b332af8e0fd71ded9e838f37fc6b))

### Fix
* Bumping version ([`a13854b`](https://github.com/Sciance-Inc/statisfactory/commit/a13854b268947e58215760fff788ece86837685b))

## v0.9.0 (2022-02-20)
### Feature
* Setting trigger on push ([`cac8e56`](https://github.com/Sciance-Inc/statisfactory/commit/cac8e5649fb4168a7232eef5ae75dbb7de5f07a3))

## v0.8.0 (2022-02-20)
### Feature
* Adding custom session ([`4c3e9a3`](https://github.com/Sciance-Inc/statisfactory/commit/4c3e9a3d32b54455000bc66007e31464a08ec2e2))
* Adding custom session injection ([`7bbaccc`](https://github.com/Sciance-Inc/statisfactory/commit/7bbaccca4646a2e3340000d76b655a2fa29963a6))
* Adding validation to the parsed pyproject.toml ([`85f907d`](https://github.com/Sciance-Inc/statisfactory/commit/85f907d25c39ae8be035fa1e62061c113d7c0b27))
* Replaceing pipelines_definitions with parameters ([`d483c84`](https://github.com/Sciance-Inc/statisfactory/commit/d483c84321d7accfb105235882c4e8f970ae6016))
* Adding an error message to the validation ([`f396b00`](https://github.com/Sciance-Inc/statisfactory/commit/f396b00dcfa135dd7f0313ecd8663df3f5a93885))
* Adding support fort custom checks on artifact ([`14154f4`](https://github.com/Sciance-Inc/statisfactory/commit/14154f41a8c04cba699e31d7ecb2858db9343bea))
* Streamlining the artefact creation ([`7bc7102`](https://github.com/Sciance-Inc/statisfactory/commit/7bc71025d3ec741db0fba5f8b5d2b14efeaf0d7f))
* Allowing arbitrary keys in artifacts ([`2e986bc`](https://github.com/Sciance-Inc/statisfactory/commit/2e986bcf1a7d872aa7bdd3538a1193df894d8c73))
* Configurations now supports jinja2 ([`45e0c40`](https://github.com/Sciance-Inc/statisfactory/commit/45e0c403a45512d83d9f83dc3c0d196cfef898c7))

### Fix
* Fixing double trigger in the package release workflow ([`3f3fd9b`](https://github.com/Sciance-Inc/statisfactory/commit/3f3fd9bed720a9f765cd92befff287fb479ba183))
* Removing push from on ([`1fcf470`](https://github.com/Sciance-Inc/statisfactory/commit/1fcf470c0aea5bde00c15513fbea689a0245ac2a))
* Removing marhsmalklow since yaml parsing is now done with pydantic ([`d726a25`](https://github.com/Sciance-Inc/statisfactory/commit/d726a25970d4da7a5d3ce8c80288ed0a34c6b75a))

### Documentation
* Updating catalog exemple ([`421b9b0`](https://github.com/Sciance-Inc/statisfactory/commit/421b9b0290d70e0a3d72faa0cadb12172eee88f8))
* Updating documentation ([`becb728`](https://github.com/Sciance-Inc/statisfactory/commit/becb728875832e0b9fed6c65136a95a55ce32de2))

## v0.7.0 (2022-02-18)


## v0.6.0 (2022-02-18)
### Feature
* Switching to a more flexible artifact handling ([#9](https://github.com/Sciance-Inc/statisfactory/issues/9)) ([`42e6ef7`](https://github.com/Sciance-Inc/statisfactory/commit/42e6ef706cf4aa0ebaaf1642c7be8e854e824c77))

## v0.5.0 (2022-02-18)


## v0.4.0 (2022-02-16)
### Feature
* Statisfactory config is now read from pyproject.toml ([`fa8402a`](https://github.com/Sciance-Inc/statisfactory/commit/fa8402a56d567bc09c3390b3726e5c6d785ff884))

### Fix
* Cleaning olds errors and typo ([`14e31f4`](https://github.com/Sciance-Inc/statisfactory/commit/14e31f4a47880513833236be910b8f1a7bc1104c))
* Ignoring dp cache ([`7573a73`](https://github.com/Sciance-Inc/statisfactory/commit/7573a73b68151cf077c64cdc45f3def7f432b7d6))
* Removing useless code ([`0fae3b5`](https://github.com/Sciance-Inc/statisfactory/commit/0fae3b520ccc8f2a3e3039bc1e63e26b66c32765))
* Adding missing pull_request event ([`303c622`](https://github.com/Sciance-Inc/statisfactory/commit/303c6228365a2d88aea2b1bfec2e1a211bbe97fd))
* Switching to semantic-release ([`fb84139`](https://github.com/Sciance-Inc/statisfactory/commit/fb841392f226d142ce6c7a476ca2e5a63b3d283b))
* Adding missing branches ref ([`0b45b18`](https://github.com/Sciance-Inc/statisfactory/commit/0b45b18d4dfa5a924a621de8c6c02919ec8db727))

## v0.3.1 (2022-02-15)
### Fix
* Lowcasing ([`bc47526`](https://github.com/Sciance-Inc/statisfactory/commit/bc47526449e64456bf3344d452ada0768ce54fab))
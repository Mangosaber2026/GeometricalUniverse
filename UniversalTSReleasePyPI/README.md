# UniversalTSReleasePyPI

A reusable TypeScript CLI for managing independent PyPI releases
of Python packages within GeometricalUniverse.

## Supported packages

- GeometricalDomination (`gd`)
- UniversalFunctions (`uf`)
- TurtleExtension (`tx`)

## Release architecture

The CLI validates package metadata and Git state, creates
package-specific Git tags, and pushes them to GitHub.

GitHub Actions handles distribution builds and PyPI publication
through Trusted Publishing.

## Development

Run the CLI with:

    npm run release -- gd

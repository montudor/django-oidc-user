workflow "Deploy" {
  on = "release"
  resolves = ["Deploy to PyPi"]
}

action "Deploy to PyPi" {
  uses = "mariamrf/py-package-publish-action@0.0.2"
  secrets = ["TWINE_PASSWORD", "TWINE_USERNAME"]
  env = {
    PYTHON_VERSION = "3.6.0"
  }
}

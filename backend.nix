{ buildPythonPackage, poetry-core }:

buildPythonPackage {
  pname = "backend";
  version = "0.1.0";
  format = "pyproject";

  src = ./.;

  nativeBuildInputs = [
    poetry-core
  ];
}

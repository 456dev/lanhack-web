{ buildPythonApplication, fastapi, poetry-core, uvicorn }:

buildPythonApplication {
  pname = "backend";
  version = "0.1.0";
  format = "pyproject";

  src = ./.;

  propagatedBuildInputs = [
    fastapi
    uvicorn
  ];

  nativeBuildInputs = [
    poetry-core
  ];
}
